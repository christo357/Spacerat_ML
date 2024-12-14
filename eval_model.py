from sklearn.model_selection import ParameterGrid
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, random_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from glob import glob
from ml_model import SpaceRatNetwork

params = {
    'LR' : 1e-3,
    'kernel_size' : 3,
    'filters' : 16,
    'batch' : 16,
    'strides' : 1,
    'dropout_rate' : 0.3
}

class getSimulResults():
    def __init__(self,  dataPath):
        self.device = torch.device("mps" if torch.backends.mps.is_built() else "cpu")
        self.model = SpaceRatNetwork(params['filters'], params['kernel_size'],params['strides'] ,params['dropout_rate']).to(self.device)
        self.model.load_state_dict(torch.load('model.pth'))
        self.loss_function =  nn.L1Loss()
        self.dataPath = dataPath
        self.dataset = BeliefShipDataset(self.dataPath)
        
        self.dataloader = DataLoader(self.dataset, shuffle=False)
        self.losses = []
        
        self.findLoss()
        self.plotLossCurve()
        
    def findLoss(self):
        test_loss, total = 0, 0
        self.model.eval()
        with torch.no_grad():
            for images, labels in self.dataloader:
                images, labels = images.to(self.device), labels.to(self.device)
                
                outputs = self.model(images)
                loss = self.loss_function(outputs.squeeze(), labels)
                test_loss += loss.item()
                self.losses.append(loss.item())
                # print(f"output: {outputs}, true: {labels}, loss = {loss.item()}")
                
            
    def plotLossCurve(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.losses, label="Loss", marker='o')
        plt.title("Loss Curve")
        plt.xlabel("No. of steps bot taken in Phase II")
        plt.ylabel("Loss")
        plt.legend()
        plt.grid(True)
        plt.savefig("loss_curve.png")  
        print("Loss curve saved as 'loss_curve.png'.")
        
class BeliefShipDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        belief = np.array(eval(self.data.loc[idx, 'belief']), dtype=np.float32)
        ship = np.array(eval(self.data.loc[idx, 'ship']), dtype=np.float32)

        input_tensor = torch.stack((torch.tensor(belief), torch.tensor(ship)), dim=0)  
        target = torch.tensor(self.data.loc[idx, 'remain'], dtype=torch.float32)

        return input_tensor, target
        
        
        
