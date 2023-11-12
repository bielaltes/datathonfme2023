#!/bin/bash

# Set the paths
images_folder="data/images"
csv_file="src/data_preprocessed/items_data.csv"

# Check if the CSV file exists
if [ ! -f "$csv_file" ]; then
    echo "CSV file not found: $csv_file"
    exit 1
fi

# Create an array to store the valid image names from the CSV
valid_images=()

# Read the CSV file and populate the array
while IFS=',' read -r model _; do
    if [ -n "$model" ]; then
        valid_images+=("${model}.jpg")
    fi
done < "$csv_file"

# Remove images that are not in the CSV file
for image_path in "$images_folder"/*.jpg; do
    image_name=$(basename "$image_path")
    
    if ! [[ " ${valid_images[@]} " =~ " $image_name " ]]; then
        echo "Removing $image_name"
        rm "$image_path"
    fi
done
