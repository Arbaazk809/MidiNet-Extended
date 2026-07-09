import torch
import numpy as np

from dataset import MidiDataset
from models.generator import Generator
from models.conditioner import Conditioner
from config import NOISE_DIM

# ==========================================
# Device
# ==========================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# ==========================================
# CHANGE THESE FOR EACH MODEL
# ==========================================

GENERATOR_MODEL = "generator_4bar.pth"
CONDITIONER_MODEL = "conditioner_4bar.pth"



# GENERATOR_MODEL = "generator_2bar.pth"
# CONDITIONER_MODEL = "conditioner_2bar.pth"

# GENERATOR_MODEL = "generator_4bar.pth"
# CONDITIONER_MODEL = "conditioner_4bar.pth"

# ==========================================
# Load Dataset
# ==========================================

dataset = MidiDataset(
    "data/processed/bars.npy",
    "data/processed/chords.npy"
)

previous_bar, chord, current_bar = dataset[0]

# Add batch dimension only
previous_bar = previous_bar.unsqueeze(0).to(device)
chord = chord.unsqueeze(0).to(device)

# ==========================================
# Load Models
# ==========================================

generator = Generator().to(device)
conditioner = Conditioner().to(device)

generator.load_state_dict(
    torch.load(GENERATOR_MODEL, map_location=device)
)

conditioner.load_state_dict(
    torch.load(CONDITIONER_MODEL, map_location=device)
)

generator.eval()
conditioner.eval()

print("Models loaded successfully.")

# ==========================================
# Generate Music
# ==========================================

noise = torch.randn(1, NOISE_DIM).to(device)

with torch.no_grad():

    condition = conditioner(previous_bar)

    generated_bar = generator(
        noise,
        chord,
        condition
    )

print("Generated Shape:", generated_bar.shape)

# ==========================================
# Save Piano Roll
# ==========================================

generated_bar = generated_bar.squeeze().cpu().numpy()

np.save(
    "generated_bar.npy",
    generated_bar
)

print("generated_bar.npy saved successfully.")