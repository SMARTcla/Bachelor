import torch
import torch.optim as optim
from model import EyeColorNet
from data_loader import train_loader, val_loader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = EyeColorNet().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10): 
    model.train()
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    model.eval()

torch.save(model.state_dict(), 'eye_color_model.pth')
