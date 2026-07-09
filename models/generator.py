import torch
import torch.nn as nn

print("Generator.py loaded successfully.")

from config import (
    NOISE_DIM,
    BAR_HEIGHT,
    BAR_WIDTH
)


class Generator(nn.Module):
    """
    MidiNet Generator
    Uses:
    - Noise (1D)
    - Chord Vector (1D)
    - Previous Bar Feature Map (2D)
    """

    def __init__(self):
        super().__init__()

        # ----------------------------
        # Noise + Chord
        # ----------------------------

        self.fc = nn.Sequential(

            nn.Linear(NOISE_DIM + 12, 1024),
            nn.ReLU(True),

            nn.Linear(1024, 256 * 8 * 1),
            nn.ReLU(True)

        )

        # ----------------------------
        # Decoder
        # ----------------------------

        self.deconv = nn.Sequential(

            nn.ConvTranspose2d(
                512,
                128,
                kernel_size=(2, 2),
                stride=(2, 2)
            ),

            nn.BatchNorm2d(128),
            nn.ReLU(True),

            nn.ConvTranspose2d(
                128,
                64,
                kernel_size=(2, 2),
                stride=(2, 2)
            ),

            nn.BatchNorm2d(64),
            nn.ReLU(True),

            nn.ConvTranspose2d(
                64,
                32,
                kernel_size=(2, 2),
                stride=(2, 2)
            ),

            nn.BatchNorm2d(32),
            nn.ReLU(True),

            nn.ConvTranspose2d(
                32,
                1,
                kernel_size=(2, 2),
                stride=(2, 2)
            ),

            nn.Tanh()

        )

    def forward(self, noise, chord, condition):

        # ----------------------------
        # Concatenate Noise + Chord
        # ----------------------------

        x = torch.cat((noise, chord), dim=1)

        x = self.fc(x)

        x = x.view(-1, 256, 8, 1)

        # ----------------------------
        # Concatenate 2D Conditioner
        # ----------------------------

        x = torch.cat((x, condition), dim=1)

        x = self.deconv(x)

        return x