#!/bin/bash

source_folder="/path/to/source/folder"
destination_folder="/path/to/destination/folder"
num_samples=100000

# Create the destination folder if it doesn't exist
mkdir -p "$destination_folder"

# Get a list of all image files in the source folder
image_files=("$source_folder"/*.jpg)  # Replace *.jpg with the appropriate file extension

# Randomly sample from the image files and copy them to the destination folder
for ((i=0; i<num_samples; i++)); do
    # Choose a random image file
    random_file="${image_files[RANDOM % ${#image_files[@]}]}"

    # Generate a new name for the image
    new_name="$(date +%s%N).jpg"  # You can modify the new name generation logic as per your requirement

    # Copy the image file to the destination folder with the new name
    cp "$random_file" "$destination_folder/$new_name"
done
