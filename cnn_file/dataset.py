import os
import cv2
import torch
from torch.utils.data import Dataset
from torchvision import transforms
from frequency import extract_frequency

class DeepfakeDataset(Dataset):
    def __init__(self, root):
        self.paths = []
        self.labels = []

        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((224,224)),
            transforms.ToTensor()
        ])

        for label in ["real", "fake"]:
            folder = os.path.join(root, label)
            for f in os.listdir(folder):
                self.paths.append(os.path.join(folder,f))
                self.labels.append(0 if label=="real" else 1)

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        img = cv2.imread(self.paths[idx])
        freq = extract_frequency(img)

        img = self.transform(img)

        return img, torch.tensor(freq, dtype=torch.float32), self.labels[idx]
