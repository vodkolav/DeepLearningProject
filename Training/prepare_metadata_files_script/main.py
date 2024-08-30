
"""
!!!!!!!!! NOTES !!!!!!!!!

1. Download Dataset from this link:
https://zenodo.org/records/1117372/files/musdb18.zip?download=1

2. Fill the paths for the dataset and all the name of the dataset

3. The file : class_labels_indices.csv, was not created, if it makes errors, copy the file to the right place like ldm repository.

"""

from json_metadata_utils import *

# Change the paths if necessary!! The paths should adjust according to the OS on your computer
audio_train_dir = Path('MUSDB18/MUSDB18-7/train')  # Set this to your actual audio directory
audio_test_dir = Path('MUSDB18/MUSDB18-7/test')
name_of_dataset = "MUSDB18"
alL_audio_dataset_dir = Path('MUSDB18/MUSDB18-7')

generate_metadata_for_ldm_wrapper(audio_train_dir, audio_test_dir, name_of_dataset, alL_audio_dataset_dir)
