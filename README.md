🇬🇧 English | [🇩🇪 Deutsch](README_DE.md)

# 🎵 MidiNet-Extended: Conditional Symbolic Music Generation using GANs

<p align="center">
  <img src="assets/banner.png" width="100%">
</p>

## 📖 Overview

This project presents an extended implementation of **MidiNet**, a Conditional Generative Adversarial Network (cGAN) for symbolic music generation.

Unlike the original MidiNet architecture, this implementation investigates how different lengths of musical history influence melody generation. Three conditioning settings were implemented and compared:

- 🎼 Baseline (1 previous bar)
- 🎼 2-Bar History
- 🎼 4-Bar History

The project was developed as part of an MSc research module to explore sequential conditioning in symbolic music generation using deep learning.

---

# 🚀 Features

- Conditional GAN (MidiNet)
- PyTorch implementation
- Chord-conditioned melody generation
- Multiple history conditioning
- Automatic MIDI generation
- Preprocessing pipeline
- Training and evaluation scripts

---

# 🧠 Model Variants

| Model | Previous Musical Context |
|--------|--------------------------|
| Baseline | 1 Previous Bar |
| Extended Model 1 | 2 Previous Bars |
| Extended Model 2 | 4 Previous Bars |

---

# 📊 Results

| Model | Generated Notes |
|--------|-----------------|
| Baseline | 880 |
| 2-Bar History | 797 |
| 4-Bar History | 785 |

The experiments demonstrate that increasing historical conditioning changes the generated musical structure while maintaining chord consistency.

---

# 🏗️ Architecture

<p align="center">
<img src="assets/architecture.png" width="90%">
</p>

---

# 📈 Model Comparison

<p align="center">
<img src="assets/comparison.png" width="85%">
</p>

---

# 📁 Project Structure

```text
MidiNet-Extended/
│
├── assets/
│   ├── banner.png
│   ├── architecture.png
│   └── comparison.png
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── models/
│   ├── generator.py
│   ├── discriminator.py
│   └── conditioner.py
│
├── outputs/
│   ├── baseline.mid
│   ├── 2bar.mid
│   └── 4bar.mid
│
├── saved_models/
│   ├── generator_baseline.pth
│   ├── generator_2bar.pth
│   ├── generator_4bar.pth
│   ├── conditioner_baseline.pth
│   ├── conditioner_2bar.pth
│   └── conditioner_4bar.pth
│
├── preprocess.py
├── dataset.py
├── train.py
├── generate.py
├── evaluate.py
├── pt_to_midi.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/MidiNet-Extended.git
cd MidiNet-Extended
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📂 Dataset

The original dataset is **not included** due to licensing and repository size limitations.

To reproduce the experiments:

1. Place the raw MIDI files inside

```
data/raw/
```

2. Run preprocessing

```bash
python preprocess.py
```

---

# 🏋️ Training

Train the model

```bash
python train.py
```

Three experiments were performed by modifying

```python
HISTORY = 1
HISTORY = 2
HISTORY = 4
```

inside

```
config.py
```

---

# 🎹 Generate Music

Generate a piano-roll

```bash
python generate.py
```

Convert to MIDI

```bash
python pt_to_midi.py
```

Generated files are stored inside

```
outputs/
```

---

# 🛠 Technologies

- Python
- PyTorch
- NumPy
- pretty_midi
- MIDI Toolkit
- GAN
- Conditional GAN
- Deep Learning

---

## 🚀 Future Work

- Train on larger symbolic music datasets
- Explore Transformer-based music generation models
- Improve long-term musical coherence
- Add objective evaluation metrics (e.g., pitch diversity, tonal consistency)
- Develop a web interface for real-time music generation

---

# 📚 Reference

Original paper:

Yang, L.-C., Chou, S.-Y., & Yang, Y.-H.

**MidiNet: A Convolutional Generative Adversarial Network for Symbolic-domain Music Generation**

ISMIR 2017.

---

# 👨‍💻 Author

**Arbaz Khan**

MSc Artificial Intelligence

BTU Cottbus, Germany

Interested in

- Data Science
- Machine Learning
- Deep Learning
- Generative AI
- NLP

---

## ⭐ If you found this project useful, consider giving it a star!