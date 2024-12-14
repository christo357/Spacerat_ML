
import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn


class SpaceRatNetwork(nn.Module):    
    def __init__(self, filters, kernel_size, strides, dropout_rate):
        super(SpaceRatNetwork, self).__init__()
        self.conv1 = nn.Conv2d(2, filters, kernel_size, stride=strides, padding = 1)
        self.pool = nn.MaxPool2d(2)
        self.relu = nn.ReLU()
        
        conv_out_size = ((30 - kernel_size + 2) // strides) + 1  
        pool_out_size = ((conv_out_size - 2) // 2) + 1  
        fc1_input_size = filters * (pool_out_size ** 2)
        self.fc1 = nn.Linear(fc1_input_size, 256)  
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128,1)
        self.dropout = nn.Dropout(dropout_rate)
        self.flatten = nn.Flatten()
    
    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.flatten(x)
        x = self.dropout(self.relu(self.fc1(x)))
        x = self.dropout(self.relu(self.fc2(x)))
        x = self.fc3(x)
        return x





