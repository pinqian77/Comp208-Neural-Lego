import torch.nn.functional as F
import torch.nn as nn

class Net(nn.Module):
    
	def __init__(self):
		super(Net, self).__init__()
		self.fc3 = nn.Linear(4, 12)
		self.fc6 = nn.Linear(12, 3)

	def forward(self, x):
		x = self.fc3(x)
		x = F.relu(x)
		x = self.fc6(x)
		return x

