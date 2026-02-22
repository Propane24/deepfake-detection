import torch
import cv2
from model import DeepfakeModel
from frequency import extract_frequency
from torchvision import transforms

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = DeepfakeModel().to(device)
model.load_state_dict(torch.load("weights/model.pth", map_location=device))
model.eval()

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

def predict(image_path):
    img = cv2.imread(image_path)
    freq = extract_frequency(img)

    img_t = transform(img).unsqueeze(0).to(device)
    freq_t = torch.tensor(freq).unsqueeze(0).float().to(device)

    with torch.no_grad():
        prob = model(img_t, freq_t)

    return prob.item()
