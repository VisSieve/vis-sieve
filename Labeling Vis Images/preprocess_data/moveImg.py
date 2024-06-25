import os
import shutil
import json

# path to the folder containing the PDFs
# input
source_dir = '2022_pdfs_subset100'
# output
target_dir = 'total_imgs'

# make sure the output folder exist
os.makedirs(target_dir, exist_ok=True)

# make sure include all possible files type
extensions = ('.png', '.jpg', '.jpeg', '.svg')
image_files = []
image_id = 1

# traverse the folder
for folder in os.listdir(source_dir):
    figures_path = os.path.join(source_dir, folder, 'figures')
    if os.path.exists(figures_path):
        for file in os.listdir(figures_path):
            if file.lower().endswith(extensions):
                # image file full path
                file_path = os.path.join(figures_path, file)
                # new image name and path
                new_filename = f'img-{image_id}.jpg'
                new_file_path = os.path.join(target_dir, new_filename)
                # copy and rename the new image
                shutil.copy(file_path, new_file_path)
                # put the new image into the list
                image_files.append({'id': image_id, 'path': f'/{target_dir}/{new_filename}'})
                image_id += 1

# generate the json file 
json_path = 'image_data.json'
with open(json_path, 'w') as json_file:
    json.dump(image_files, json_file, indent=4)

print('image are saved to new path and json file is generated')
