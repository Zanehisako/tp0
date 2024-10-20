import torch
import torch.nn as nn

class MaxMinNN(nn.Module):
    def __init__(self):
        super(MaxMinNN, self).__init__()
        self.hidden1= nn.Linear(1, 64)
        self.hidden2= nn.Linear(64, 32)
        self.output= nn.Linear(32, 1)
        self.ReLU= nn.ReLU()

    def forward(self, x):
        x = self.ReLU(self.hidden1(x))
        x = self.ReLU(self.hidden2(x))
        x = self.output(x)
        return x
loaded_model = MaxMinNN()
loaded_model.load_state_dict(torch.load('surface_model.pth'))
loaded_model.eval()
print('enter a number de cubes:')
N = input()
with torch.no_grad():
    result = loaded_model(torch.tensor([[float(N)]]))
    print(f'{torch.round(result[0,0])}')
