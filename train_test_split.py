import os
import random
import shutil

input_folder = 'raw_data'
output_folder = 'datasets'
test_size = 0.2

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(output_folder + "/images/train", exist_ok=True)
os.makedirs(output_folder + "/images/val", exist_ok=True)
os.makedirs(output_folder + "/labels/train", exist_ok=True)
os.makedirs(output_folder + "/labels/val", exist_ok=True)

# Read the data
labels_list = os.listdir(input_folder + "/labels/")
images_list = os.listdir(input_folder + "/images/")
assert len(labels_list) == len(images_list)

test_length = int(len(labels_list) * test_size)
train_length = len(labels_list) - test_length

test_index = random.sample(range(0, len(labels_list)), test_length)
train_index = [i for i in range(0, len(labels_list)) if i not in test_index]

# Copy the files
for i in train_index:
    shutil.copy(input_folder + "/labels/" + labels_list[i], output_folder + "/labels/train")
    shutil.copy(input_folder + "/images/" + images_list[i], output_folder + "/images/train")

for i in test_index:
    shutil.copy(input_folder + "/labels/" + labels_list[i], output_folder + "/labels/val")
    shutil.copy(input_folder + "/images/" + images_list[i], output_folder + "/images/val")

print("Train and test split was successful.")