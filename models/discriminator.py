import torch
import torch.nn as nn

from config import BAR_HEIGHT, BAR_WIDTH


class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()

        self.model = nn.Sequential(

            nn.Conv2d(
                1,
                32,
                kernel_size=(4, 4),
                stride=(2, 2),
                padding=1
            ),
            nn.LeakyReLU(0.2),

            nn.Conv2d(
                32,
                64,
                kernel_size=(4, 4),
                stride=(2, 2),
                padding=1
            ),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2),

            nn.Flatten(),

            nn.Linear(64 * 32 * 4, 1),

            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)