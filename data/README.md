# Dataset

The original dataset is **not included** in this repository due to its size and redistribution/licensing considerations.

## Directory Structure

```
data/
├── raw/
└── processed/
```

## Preparing the Dataset

1. Place the raw MIDI files inside the `data/raw/` directory.
2. Run the preprocessing script:

```bash
python preprocess.py
```

3. This will generate the processed piano-roll and chord files required for training.

## Notes

- `raw/` contains the original MIDI files.
- `processed/` contains the generated NumPy files used for model training.
- These files are not included in this repository.