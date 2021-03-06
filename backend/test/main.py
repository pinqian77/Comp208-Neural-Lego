import torch.nn as nn
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
from model import Net

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

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

X, y = readcsv("./"+args['dataset'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = args['seed'])
X_train, y_train = torch.stack([torch.Tensor(i) for i in X_train]), torch.stack([torch.Tensor([i]) for i in y_train])
X_test, y_test = torch.stack([torch.Tensor(i) for i in X_test]), torch.stack([torch.Tensor([i]) for i in y_test])
y_train, y_test = y_train.squeeze().type(torch.LongTensor), y_test.squeeze().type(torch.LongTensor)
train_set = Data.TensorDataset(X_train, y_train)
test_set = Data.TensorDataset(X_test, y_test)
train_loader = Data.DataLoader(train_set, batch_size=args['batch_size'], shuffle=True)
test_loader = Data.DataLoader(test_set, batch_size=args['test_batch_size'], shuffle=True)



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

    target_list = []
    pred_list = []
    with torch.no_grad():
        for data, target in test_loader:
#            target = target.squeeze().type(torch.LongTensor)
            output = model(data)
            test_loss += nn.CrossEntropyLoss()(output, target).item()
            pred = output.max(1, keepdim=True)[1]
            correct += pred.eq(target.view_as(pred)).sum().item()
            # AUC
            # Compute ROC curve and ROC area for each class
            target = nn.functional.one_hot(target, num_classes = 3)
            pred = nn.functional.one_hot(pred, num_classes=3).squeeze()
            target_list.append(target)
            pred_list.append(pred)

    # AUC
    writeAuc(target_list, pred_list)

    test_loss /= len(test_loader.dataset)
    test_accuracy = correct / len(test_loader.dataset)
    return test_loss, test_accuracy
def writeAuc(target_list, pred_list):
    for i in pred_list:
        print(i.shape)
    pred_all, target_all = torch.cat([i for i in pred_list], dim=0), torch.cat([i for i in target_list], dim=0)
    print(pred_all.shape)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(3):
        fpr[i], tpr[i], _ = roc_curve(pred_all[:, i], target_all[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Compute micro-average ROC curve and ROC area
    fpr["micro"], tpr["micro"], _ = roc_curve(pred.ravel(), target.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    
    plt.figure()
    lw = 2
    plt.plot(fpr[2], tpr[2], color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()

def writeLossAcc(loss, acc):
    plt.subplot(1, 2, 1)
    plt.plot(acc, label = "Training Accuracy")
    plt.title("Accuracy")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(loss, label = "Training Loss")
    plt.title("Loss")
    plt.legend()
    plt.show()
def train_model():
    model = Net().to(device)
    
    optimizer = optim.SGD(model.parameters(), lr=args['lr'])
    for epoch in range(1, args['epoch'] + 1):
        start_time = time.time()
        
        train(args, model, device, train_loader, optimizer, epoch)
        
        trnloss, trnacc = eval_test(model, device, train_loader)
        
        with open("out", "w") as f:
            f.write('Epoch '+str(epoch)+': '+str(int(time.time()-start_time))+'s'+"\n")
            f.write('trn_loss: {:.4f}, trn_acc: {:.2f}%'.format(trnloss, 100. * trnacc)+"\n")
        
    return model

model = train_model()
    
