import pandas as pd
import torch
import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self, input_dim=5, h_RNN_layers=2, h_RNN=256, drop_p=0.2, num_classes=1):
        super(LSTMModel, self).__init__()
        self.input_dim = input_dim
        self.h_RNN_layers = h_RNN_layers   # RNN hidden layers
        self.h_RNN = h_RNN                 # RNN hidden nodes
        self.drop_p = drop_p
        if h_RNN_layers < 2:
            drop_p = 0
        self.num_classes = num_classes
        self.LSTM = nn.LSTM(
            input_size=self.input_dim,
            hidden_size=self.h_RNN,
            num_layers=h_RNN_layers,
            dropout=drop_p,
            batch_first=True,       # input & output will has batch size as 1s dimension. e.g. (batch, time_step, input_size)
        )
        self.fc1 = nn.Linear(self.h_RNN, self.num_classes)

    def forward(self, x, h_s=None):
        # print('forward started')
        self.LSTM.flatten_parameters()
        RNN_out, h_s = self.LSTM(x, h_s)
        """ h_n shape (n_layers, batch, hidden_size), h_c shape (n_layers, batch, hidden_size) """
        """ None represents zero initial hidden state. RNN_out has shape=(batch, time_step, output_size) """

        # FC layers
        out = self.fc1(RNN_out[:, -1, :])   # choose RNN_out at the last time step
        return out, h_s