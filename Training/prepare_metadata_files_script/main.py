
"""
!!!!!!!!! NOTES !!!!!!!!!

1. Download Dataset from this link:
https://zenodo.org/records/1117372/files/musdb18.zip?download=1

2. Fill the paths for the dataset and all the name of the dataset

3. The file : class_labels_indices.csv, was not created, if it makes errors, copy the file to the right place like ldm repository.

"""

from json_metadata_utils import *
# Change the root if necessary!! The paths should adjust according to the OS on your computer
# root_path = Path('MUSDB18/MUSDB18-7')
#root_path = Path('C:/Users/97254/Desktop/MUSDB18/MUSDB18-7')
root_path = Path("./data/dataset/MUSDB18")

audio_train_dir = root_path / Path('train')
audio_test_dir = root_path / Path('test')
name_of_dataset_dir = "MUSDB18"


generate_metadata_for_ldm_wrapper(audio_train_dir, audio_test_dir, name_of_dataset_dir, root_path)
