import os
from PIL import Image
import shutil
import imghdr

source_folder = "Data Test for BDC 2023 - Penyisihan/"
destination_folder = "low-res-test/"
threshold_width = 100


def copy_large_images(source_folder, destination_folder, threshold_width):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Check if the file is an image
        if not os.path.isfile(file_path) or not imghdr.what(file_path):
            continue

        # Open the image using PIL
        image = Image.open(file_path)

        # Get the image resolution
        width, height = image.size

        # Check if the image is large based on the specified thresholds
        if width <= threshold_width:
            # Copy the image to the destination folder
            shutil.copy(file_path, destination_folder)

    print("Small images copied successfully.")

copy_large_images(source_folder, destination_folder, threshold_width)