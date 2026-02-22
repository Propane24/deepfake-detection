import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from model import DeepfakeModel
from dataset import DeepfakeDataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

dataset = DeepfakeDataset("data/")
loader = DataLoader(dataset, batch_size=16, shuffle=True)

model = DeepfakeModel().to(device)
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

for epoch in range(10):
    total = 0
    for img, freq, label in loader:
        img = img.to(device)
        freq = freq.to(device)
        label = label.float().unsqueeze(1).to(device)

        pred = model(img, freq)
        loss = criterion(pred, label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total += loss.item()

    print("epoch", epoch, "loss", total)

torch.save(model.state_dict(), "weights/model.pth")
