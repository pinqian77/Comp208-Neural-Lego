import json
import os

def FC(input_size, output_size, init, forward, pointer):

    string = "self.fc"+str(-1*pointer)+" = nn.Linear("+str(input_size)+", "+str(output_size)+")"
    string = "\t\t"+string + "\n"
    init += string
    string = "x = self.fc" + str(-1*pointer) + "(x)"
    string = "\t\t" + string + "\n"
    forward += string
    return init, forward
def ReLU(forward):
    forward += "\t\tx = F.relu(x)\n"
    return forward

with open(os.path.join('.','example.json'), 'r') as f:
    List = json.load(f)

nodeList = List['nodeDataArray']
linkList = List['linkDataArray']

nodedict = {}
linkdict = {}
start = 0
end = 0
for node in nodeList:
    nodedict[node['key']] = {'category':node['category'], 'para':node['reasonsList']}
    if node['category'] == "Data":
        start = node['key']
    if node['category'] == "End":
        end = node['key']

for link in linkList:
    linkdict[link['from']] =  link['to']

#if start == 0 or end == 0:
#    raise 

################################################## model date
pointer = linkdict[start]
with open('model.py', 'w') as f:
    head = '''import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as Data
import torch.optim as optim
import torchvision
import csv
import pandas as pd
from torchvision import transforms
import time
import json

with open("hyper.json", 'r') as f:
    args = json.load(f)
#use_cuda = not args.no_cuda and torch.cuda.is_available()
#device = torch.device("cuda" if use_cuda else "cpu")
device = torch.device("cpu")

torch.manual_seed(args['seed'])
#kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}
kwargs = {}

def readcsv(files):
    csvfile = pd.read_csv(files)
    columns = csvfile.columns
    label = csvfile[columns[-1]].unique()
    map = {}
    for index, item in enumerate(label):
        map[item] = index
    csvfile[columns[-1]] = csvfile[columns[-1]].map(map)
    x = csvfile.drop(columns[-1], axis=1).values
    y = csvfile[columns[-1]].values
    return x, y

X, y = readcsv("%s"+args['dataset'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = args['seed'])
X_train, y_train = torch.stack([torch.Tensor(i) for i in X_train]), torch.stack([torch.Tensor([i]) for i in y_train])
X_test, y_test = torch.stack([torch.Tensor(i) for i in X_test]), torch.stack([torch.Tensor([i]) for i in y_test])
y_train, y_test = y_train.squeeze().type(torch.LongTensor), y_test.squeeze().type(torch.LongTensor)
train_set = Data.TensorDataset(X_train, y_train)
test_set = Data.TensorDataset(X_test, y_test)
train_loader = Data.DataLoader(train_set, batch_size=args['batch_size'], shuffle=True)
test_loader = Data.DataLoader(test_set, batch_size=args['test_batch_size'], shuffle=True)

class Net(nn.Module):
'''%("./")
    f.write(head+"\n")
    init, forward = "\tdef __init__(self):\n\t\tsuper(Net, self).__init__()\n", "\tdef forward(self, x):\n"
    while pointer != end:
        if nodedict[pointer]['category'] == 'FC':
            init, forward = FC(nodedict[pointer]['para'][0]['text1'], nodedict[pointer]['para'][0]['text3'], init, forward, pointer)
        elif nodedict[pointer]['category'] == 'ReLU':
            forward = ReLU(forward)
        pointer = linkdict[pointer]
    forward += "\t\treturn x\n"
    f.write(init+"\n")
    f.write(forward+"\n")
    end = '''
def train(args, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
#        target = target.squeeze().type(torch.LongTensor)
        
        optimizer.zero_grad()
        
        loss = nn.CrossEntropyLoss()(model(data), target)
        
        loss.backward()
        optimizer.step()
        


def eval_test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
#            target = target.squeeze().type(torch.LongTensor)
            output = model(data)
            test_loss += nn.CrossEntropyLoss()(output, target).item()
            pred = output.max(1, keepdim=True)[1]
            correct += pred.eq(target.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)
    test_accuracy = correct / len(test_loader.dataset)
    return test_loss, test_accuracy

def train_model():
    model = Net().to(device)
    
    optimizer = optim.SGD(model.parameters(), lr=args['lr'])
    for epoch in range(1, args['epoch'] + 1):
        start_time = time.time()
        
        train(args, model, device, train_loader, optimizer, epoch)
        
        trnloss, trnacc = eval_test(model, device, train_loader)
        
        print('Epoch '+str(epoch)+': '+str(int(time.time()-start_time))+'s', end=', ')
        print('trn_loss: {:.4f}, trn_acc: {:.2f}%'.format(trnloss, 100. * trnacc), end=', ')
        
    return model
    '''
    f.write(end)
