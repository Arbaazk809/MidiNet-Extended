import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from dataset import MidiDataset
from models.generator import Generator
from models.discriminator import Discriminator
from models.conditioner import Conditioner

from config import (
    BATCH_SIZE,
    LEARNING_RATE,
    NOISE_DIM,
    EPOCHS
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using device:", device)

# -------------------------------------------------------
# Dataset
# -------------------------------------------------------

dataset = MidiDataset(
    "data/processed/bars.npy",
    "data/processed/chords.npy"
)

dataloader = DataLoader(
    dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

# -------------------------------------------------------
# Models
# -------------------------------------------------------

generator = Generator().to(device)
discriminator = Discriminator().to(device)
conditioner = Conditioner().to(device)

# -------------------------------------------------------
# Optimizers
# -------------------------------------------------------

optimizer_G = optim.Adam(
    generator.parameters(),
    lr=LEARNING_RATE,
    betas=(0.5, 0.999)
)

optimizer_D = optim.Adam(
    discriminator.parameters(),
    lr=LEARNING_RATE,
    betas=(0.5, 0.999)
)

criterion = nn.BCELoss()

print("Dataset size:", len(dataset))
print("Generator ready.")
print("Discriminator ready.")
print("Conditioner ready.")

# -------------------------------------------------------
# Training
# -------------------------------------------------------

for epoch in range(EPOCHS):

    generator.train()
    discriminator.train()
    conditioner.train()

    d_loss_epoch = 0
    g_loss_epoch = 0

    for previous_bar, chord, current_bar in dataloader:

        previous_bar = previous_bar.to(device)
        current_bar = current_bar.unsqueeze(1).to(device)
        chord = chord.to(device)

        batch_size = current_bar.size(0)

        real = torch.ones(batch_size, 1).to(device)
        fake = torch.zeros(batch_size, 1).to(device)

        # -----------------------------------
        # Conditioner
        # -----------------------------------

        condition = conditioner(previous_bar)

        # -----------------------------------
        # Train Discriminator
        # -----------------------------------

        optimizer_D.zero_grad()

        noise = torch.randn(batch_size, NOISE_DIM).to(device)

        fake_bar = generator(
            noise,
            chord,
            condition
        )

        real_output = discriminator(current_bar)
        fake_output = discriminator(fake_bar.detach())

        d_real_loss = criterion(real_output, real)
        d_fake_loss = criterion(fake_output, fake)

        d_loss = d_real_loss + d_fake_loss

        d_loss.backward()

        optimizer_D.step()

        # -----------------------------------
        # Train Generator
        # -----------------------------------

        optimizer_G.zero_grad()

        condition = conditioner(previous_bar)

        noise = torch.randn(batch_size, NOISE_DIM).to(device)

        fake_bar = generator(
            noise,
            chord,
            condition
        )

        output = discriminator(fake_bar)

        g_loss = criterion(output, real)

        g_loss.backward()

        optimizer_G.step()

        d_loss_epoch += d_loss.item()
        g_loss_epoch += g_loss.item()

    print(
        f"Epoch {epoch+1}/{EPOCHS} | "
        f"D Loss = {d_loss_epoch/len(dataloader):.4f} | "
        f"G Loss = {g_loss_epoch/len(dataloader):.4f}"
    )

# -------------------------------------------------------
# Save Models
# -------------------------------------------------------

torch.save(generator.state_dict(), "generator_baseline.pth")
torch.save(conditioner.state_dict(), "conditioner_baseline.pth")

print("\nTraining Finished!")
print("Generator saved.")
print("Conditioner saved.")