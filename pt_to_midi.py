import pretty_midi
import numpy as np

# --------------------------------------------------
# Load generated piano roll
# --------------------------------------------------

bar = np.load("generated_bar.npy")

print("Shape:", bar.shape)

# --------------------------------------------------
# Create MIDI object
# --------------------------------------------------

midi = pretty_midi.PrettyMIDI()

instrument = pretty_midi.Instrument(program=0)

time_step = 0.25
note_length = 0.25

threshold = 0.5

# --------------------------------------------------
# Convert piano roll to notes
# --------------------------------------------------

for pitch in range(128):

    for t in range(16):

        if bar[pitch, t] > threshold:

            note = pretty_midi.Note(

                velocity=100,

                pitch=pitch,

                start=t * time_step,

                end=t * time_step + note_length

            )

            instrument.notes.append(note)

midi.instruments.append(instrument)

# --------------------------------------------------
# Save MIDI
# --------------------------------------------------

midi.write("generated.mid")

print("MIDI saved successfully!")
print("Total notes:", len(instrument.notes))