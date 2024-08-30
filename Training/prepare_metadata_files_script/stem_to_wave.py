from pydub import AudioSegment
import os

# Load the stem file
stem_file = "A Classic Education - NightOwl.stem.mp4"

# Extract the audio segment
audio = AudioSegment.from_file(stem_file, format="m4a")

# Get the number of channels
num_channels = audio.channels

# Split the audio into individual mono tracks
mono_tracks = audio.split_to_mono()

# Initialize the mixed track with the first track
if num_channels > 0:
    mixed = mono_tracks[0]

    # Overlay each additional track
    for i in range(1, num_channels):
        mixed = mixed.overlay(mono_tracks[i])

    # Export the mixed track to a single WAV file
    mixed.export("output.wav", format="wav")

    print(f"Successfully mixed {num_channels} channels into output.wav")
else:
    print("No channels found in the stem file.")
