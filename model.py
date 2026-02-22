import torch
import torch.nn as nn
import torchvision.models as models

class DeepfakeModel(nn.Module):
    def __init__(self):
        super().__init__()

        # spatial CNN
        self.cnn = models.resnet18(weights=None)
        self.cnn.fc = nn.Linear(512, 128)

        # frequency branch
        self.freq_branch = nn.Sequential(
            nn.Linear(1024, 256),
            nn.ReLU(),
            nn.Linear(256, 128)
        )

        # fusion layer
        self.classifier = nn.Sequential(
            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )

    def forward(self, img, freq):
        spatial = self.cnn(img)
        freq_feat = self.freq_branch(freq)

        fused = torch.cat([spatial, freq_feat], dim=1)
        return self.classifier(fused)
