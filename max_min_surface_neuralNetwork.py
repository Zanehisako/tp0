import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data 
import pandas as pd
import matplotlib.pyplot as plt



def init_weights(m):
    if isinstance(m, nn.Linear):
        nn.init.xavier_uniform_(m.weight)
        nn.init.zeros_(m.bias)

class MaxMinNN(nn.Module):
    def __init__(self):
        super(MaxMinNN, self).__init__()
        self.hidden1= nn.Linear(1, 64)
        self.hidden2= nn.Linear(64, 32)
        self.output= nn.Linear(32, 1)
        self.relu= nn.ReLU()

    def forward(self, x):
        x = self.relu(self.hidden1(x))
        x = self.relu(self.hidden2(x))
        x = self.output(x)
        return x


#setting up the data
df = pd.read_csv('min_max_surface_trainingData.csv')
input = df['NumberOfCubes'].to_numpy()
output1= df['MinSurface'].to_numpy()
output2= df['MaxSurface'].to_numpy()
#print(output2[:100])
#plt.plot(input[:100],output1[:100])
#plt.show()



#input = (input - input.min()) / (input.max() - input.min())
#output1= (output1 - output1.min()) / (output1.max() - output1.min())
#output2 = (output2 - output2.min()) / (output2.max() - output2.min())

# Convert numpy arrays to torch tensors
input = torch.tensor(input, dtype=torch.float32).unsqueeze(1)  # Add a dimension for batch size
output1 = torch.tensor(output1, dtype=torch.float32).unsqueeze(1)  # Add a dimension for batch size
output2 = torch.tensor(output2, dtype=torch.float32).unsqueeze(1)



# Create a dataset and dataloader
#dataset = TensorDataset(input,torch.cat([output1,output2],dim=1))
#dataloader = DataLoader(dataset, batch_size=100, shuffle=True)

# Set up the network
model = MaxMinNN()

#model.apply(init_weights)

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Example training loop
num_epochs = 100000
for epoch in range(num_epochs):
        optimizer.zero_grad()
        # Forward pass
        outputs = model(input)

        target = torch.cat((output1, output2), dim=1)
        loss = criterion(outputs,output2)
        
        # Backward pass and optimize
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

#save the module
torch.save(model.state_dict(), 'surface_model.pth')

# Test the model
with torch.no_grad():
   test_input = torch.tensor([[144.0]],dtype = torch.float32) 
   prediction = model(test_input)
   print(f"Prediction: {prediction}")
