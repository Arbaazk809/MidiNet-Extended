import torch
import torch.nn as nn
from config import HISTORY


class Conditioner(nn.Module):
    def __init__(self):
        super().__init__()

        self.model = nn.Sequential(

            nn.Conv2d(
                in_channels=HISTORY,
                out_channels=32,
                kernel_size=3,
                stride=2,
                padding=1
            ),
            nn.ReLU(inplace=True),

            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                stride=2,
                padding=1
            ),
            nn.ReLU(inplace=True),

            nn.Conv2d(
                in_channels=64,
                out_channels=128,
                kernel_size=3,
                stride=2,
                padding=1
            ),
            nn.ReLU(inplace=True),

            nn.Conv2d(
                in_channels=128,
                out_channels=256,
                kernel_size=2,
                stride=2
            ),
            nn.ReLU(inplace=True)
        )

    def forward(self, previous_bar):
        return self.model(previous_bar)