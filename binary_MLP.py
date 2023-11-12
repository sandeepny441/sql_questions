import torch
import torch.nn as nn
import torch.optim as optim

# Define the MLP model
class BinaryClassificationMLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(BinaryClassificationMLP, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.sigmoid(x)
        return x

# Parameters for the model
input_size = 2  # Number of input features
hidden_size = 5  # Number of hidden nodes
output_size = 1  # Number of output features (1 for binary classification)

# Create the model
model = BinaryClassificationMLP(input_size, hidden_size, output_size)

# Loss function and optimizer
criterion = nn.BCELoss()  # Binary Cross-Entropy Loss for binary classification
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent

# Example dummy data: 12 samples, 2 features each, binary labels
features = torch.randn(12, 2)
labels = torch.randint(0, 2, (12, 1)).type(torch.FloatTensor)

# Training loop
for epoch in range(100):  # 100 epochs
    optimizer.zero_grad()  # Clear gradients
    outputs = model(features)  # Forward pass
    loss = criterion(outputs, labels)  # Compute loss
    loss.backward()  # Backward pass
    optimizer.step()  # Update weights
    
    if (epoch+1) % 10 == 0:  # Print every 10 epochs
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

# Predictions (example)
with torch.no_grad():
    test_samples = torch.tensor([[0.5, -0.2], [0.3, 0.4]])
    predictions = model(test_samples)
    predicted_classes = (predictions >= 0.5).type(torch.int)
    print(f"Predictions: {predictions.flatten()}")
    print(f"Predicted classes: {predicted_classes.flatten()}")