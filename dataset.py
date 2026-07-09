import numpy as np
import torch
from torch.utils.data import Dataset
from config import HISTORY


class MidiDataset(Dataset):

    def __init__(self, bars_path, chords_path):

        self.bars = np.load(bars_path)
        self.chords = np.load(chords_path)

        assert len(self.bars) == len(self.chords)

    def __len__(self):
        return len(self.bars)

    def __getitem__(self, idx):
        previous_bar = []

        for i in range(HISTORY):

            previous_idx = idx - HISTORY + i

            if previous_idx < 0:
                previous_idx = 0

            previous_bar.append(self.bars[previous_idx])

        previous_bar = np.stack(previous_bar)

        current_bar = self.bars[idx]

        chord = self.chords[idx]

        return (

            torch.tensor(previous_bar, dtype=torch.float32),
            torch.tensor(chord, dtype=torch.float32),
            torch.tensor(current_bar, dtype=torch.float32)   
        )    



if __name__ == "__main__":

    dataset = MidiDataset(
        "data/processed/bars.npy",
        "data/processed/chords.npy"
    )

    print("Dataset Size:", len(dataset))

    previous_bar, chord, current_bar = dataset[0]

    print("Previous Bar:", previous_bar.shape)
    print("Chord:", chord.shape)
    print("Current Bar:", current_bar.shape)