from pathlib import Path
import pretty_midi
import numpy as np

DATASET_PATH = Path(r"data/raw/nottingham/MIDI")

BAR_LENGTH = 16
FS = 4


def split_into_bars(piano_roll, bar_length=BAR_LENGTH):
    bars = []

    total_columns = piano_roll.shape[1]

    for start in range(0, total_columns - bar_length + 1, bar_length):

        bars.append(
            piano_roll[:, start:start + bar_length]
        )

    return bars


def extract_chroma(bar):
    """
    Create a 12-dimensional pitch-class vector.
    """

    chroma = np.zeros(12, dtype=np.float32)

    active_notes = np.where(bar > 0)[0]

    for note in active_notes:
        chroma[note % 12] = 1.0

    return chroma


midi_files = sorted(DATASET_PATH.glob("*.mid"))

print(f"Found {len(midi_files)} MIDI files")

all_bars = []
all_chords = []

for midi_file in midi_files:

    try:

        midi = pretty_midi.PrettyMIDI(str(midi_file))

        if len(midi.instruments) == 0:
            continue

        melody = midi.instruments[0]

        piano_roll = melody.get_piano_roll(fs=FS)

        bars = split_into_bars(piano_roll)

        for bar in bars:

            all_bars.append(bar.astype(np.float32))

            chord = extract_chroma(bar)

            all_chords.append(chord)

    except Exception as e:

        print(midi_file.name, e)

bars = np.array(all_bars, dtype=np.float32)
chords = np.array(all_chords, dtype=np.float32)

print("Bars:", bars.shape)
print("Chords:", chords.shape)

Path("data/processed").mkdir(parents=True, exist_ok=True)

np.save("data/processed/bars.npy", bars)
np.save("data/processed/chords.npy", chords)

print("bars.npy saved")
print("chords.npy saved")