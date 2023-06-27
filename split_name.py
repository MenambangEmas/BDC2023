import os
import shutil
import tqdm

input_folder = 'raw_data/stage_1'
output_folder = 'raw_data/stage_1_split'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

images_list = os.listdir(input_folder)

for i in tqdm.tqdm(images_list):
    prefix, name = i.split('-')
    basedir = os.getcwd()
    
    # copy and rename the image
    shutil.copy(input_folder + "/" + i, output_folder + "/" + name)