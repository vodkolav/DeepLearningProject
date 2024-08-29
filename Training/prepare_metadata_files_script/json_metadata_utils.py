
from pathlib import Path
import json
import platform
import random

def generate_metadata_entries(audio_files, metadata_files_dir, json_file_name):
    metadata_entries = []
    for audio_file in audio_files:
        entry = {
            "wav": str(audio_file),
            "seg_label": "",  # Placeholder, adjust as necessary
            "labels": "",  # Placeholder, adjust as necessary
            "caption": ""  # Placeholder, adjust as necessary
        }
        metadata_entries.append(entry)

    # Store metadata in the JSON file
    metadata = {"data": metadata_entries}
    with open(metadata_files_dir / json_file_name, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"Metadata for {json_file_name} created successfully in {metadata_files_dir / json_file_name}")


def generate_metadata(audio_dir: Path, metadata_files_dir: Path, json_file_name: str, train_or_test: str):
    # Use Pathlib for cross-platform compatibility
    audio_extensions = ('.wav', '.stem', '.mp4', '.mp3')

    # List all audio files in the directory
    audio_files_in_dir = [f for f in audio_dir.iterdir() if f.suffix in audio_extensions]

    # Shuffle the list to ensure randomness
    random.shuffle(audio_files_in_dir)

    # Split files if generating train/val sets
    if train_or_test == "train_val":
        num_validation_files = int(len(audio_files_in_dir) * 0.05)
        validation_files = audio_files_in_dir[:num_validation_files]
        train_files = audio_files_in_dir[num_validation_files:]

        # Generate and store validation metadata
        validation_json_name = json_file_name
        validation_json_name = validation_json_name.replace("train", "validation")
        generate_metadata_entries(validation_files, metadata_files_dir, validation_json_name)

        # Generate and store train metadata
        generate_metadata_entries(train_files, metadata_files_dir, json_file_name)

    elif train_or_test == "test":
        # Generate and store test metadata
        generate_metadata_entries(audio_files_in_dir, metadata_files_dir, json_file_name)

    else:
        print(f"Invalid value for train_or_test: {train_or_test}")

def adjust_path_for_os(path):
    return str(Path(path))

def generate_root_metadata(audio_data_path, name_of_data_set, train_json_path, validation_json_path,  test_json_path, class_label_path, output_path):
    # Adjust paths using Pathlib and convert them to strings for JSON serialization
    train_json_path = adjust_path_for_os(train_json_path)
    validation_json_path = adjust_path_for_os(validation_json_path)
    test_json_path = adjust_path_for_os(test_json_path)
    class_label_path = adjust_path_for_os(class_label_path)
    output_path = adjust_path_for_os(output_path)

    # Create the dictionary with the desired structure
    root_metadata = {
        name_of_data_set: str(audio_data_path),
        "comments": {},  # Empty comments section
        "metadata": {
            "path": {
                name_of_data_set: {
                    "train": train_json_path,
                    "test": test_json_path,
                    "val": validation_json_path,
                    "class_label_indices": class_label_path
                }
            }
        }
    }

    # Write the dictionary to a JSON file
    with open(output_path, 'w') as f:
        json.dump(root_metadata, f, indent=2)

    print(f"Root metadata file created successfully at {output_path}")



def generate_metadata_for_ldm_wrapper(audio_train_dir, audio_test_dir, name_of_dataset, alL_audio_dataset_dir):
    # Detect operating system
    system = platform.system()

    print(f"Operating system is {system}")

    # Define paths using Pathlib

    base_dir = Path('./data/dataset')
    metadata_dir = base_dir / 'metadata'
    name_of_dataset_dir = metadata_dir / name_of_dataset
    metadata_json_files_dir = name_of_dataset_dir / 'datafiles'
    testset_subset_dir = name_of_dataset_dir / 'testset_subset'

    # print(metadata_dir)
    # print(name_of_dataset_dir)
    # print(metadata_json_files_dir)
    # print(testset_subset_dir)

    # Create directories
    audio_train_dir.mkdir(parents=True, exist_ok=True)
    metadata_json_files_dir.mkdir(parents=True, exist_ok=True)
    testset_subset_dir.mkdir(parents=True, exist_ok=True)

    # Generate metadata files
    generate_metadata(audio_train_dir, metadata_json_files_dir, f'{name_of_dataset}_train_label.json', "train_val")
    generate_metadata(audio_test_dir, metadata_json_files_dir, f'{name_of_dataset}_test_label.json', "test")

    # Adjust paths using Pathlib for cross-platform compatibility
    train_json_path = Path(metadata_json_files_dir / f'{name_of_dataset}_train_label.json')
    validation_json_path = Path(metadata_json_files_dir / f'{name_of_dataset}_validation_label.json')
    test_json_path = Path(metadata_json_files_dir / f'{name_of_dataset}_test_label.json')
    class_label_path = Path(name_of_dataset_dir / 'class_labels_indices.csv')
    output_path = Path(metadata_dir / 'dataset_root.json')

    # Generate the root metadata
    generate_root_metadata(alL_audio_dataset_dir,name_of_dataset, train_json_path,validation_json_path, test_json_path, class_label_path, output_path)

    print("Metadata for all audio files created successfully.")

