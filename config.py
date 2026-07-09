"""
Configuration file for MidiNet.
"""

# ==========================
# Dataset
# ==========================

DATA_PATH = "data/processed/bars.npy"

# ==========================
# Training
# ==========================

BATCH_SIZE = 32
EPOCHS = 30
LEARNING_RATE = 0.0002

# ==========================
# Model
# ==========================

NOISE_DIM = 100

BAR_HEIGHT = 128
BAR_WIDTH = 16

HISTORY = 4     # Change to 2 or 4 for your research experiments

# ==========================
# Output
# ==========================

MODEL_DIR = "saved_models"
GENERATED_DIR = "data/generated"

