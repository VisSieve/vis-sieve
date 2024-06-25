# Preprocess the Data

Tools: We use Python for this process, please make sure python is installed and all libraries are installed.

- if encountered pip3 install related issue:

```
    python3 -m venv ~/venv
    source ~/venv/bin/activate
    pip install [Lib Name you want to install]
```

1. abstract images from the folder and make them in one folder and name it properly - (moveImg.py)

```python
import os
import shutil
import json

# path to the folder containing the PDFs
# input
source_dir = '2022_pdfs_subset100' #the directory containing the source files
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

```
- image_data.json data file example:

```json

[
    {
        "id": 1,
        "path": "/total_imgs/img-1.jpg"
    },

    ...

    {
        "id": 13000,
        "path": "/total_imgs/img-13000.jpg"
    }
]

```

---------

2. make giant montage images for preview
    - downsize the image to 32*32 pixels;
    - split resized images into smaller folders(3600 images in each folder)
    Below is the struture of the folders
```
    src
    ├── data
    │   ├── downsize.py
    │   ├── total_imgs
    │   ├── image_data.json
    │   └── batches
            

```
# !!!!!make sure before downsizeing, the images are ordered in 00001 --> 10000. otherwises the order will be different
# !!!!!make sure before downsizeing, the images are ordered in 00001 --> 10000. otherwises the order will be different
# !!!!!make sure before downsizeing, the images are ordered in 00001 --> 10000. otherwises the order will be different

Here is the python code to do the sorting work:
- downsize.py
```python
import os
from PIL import Image

# Directory containing images
source_dir = 'total_imgs/'
# Directory to save resized images
target_root_dir = 'batches'
# Base name for the output files
base_filename = 'figures'

# Ensure the source directory exists
if not os.path.exists(source_dir):
    print(f"Source directory {source_dir} does not exist.")
    exit()

# Ensure the target directory exists
if not os.path.exists(target_root_dir):
    os.makedirs(target_root_dir)

def count_images(directory):
    """Count the number of image files in the specified directory."""
    return len([name for name in os.listdir(directory) 
                if name.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))])

# Get the number of images to determine the global_image_count format
image_count = count_images(source_dir)
global_image_count_digits = len(str(image_count))

# Image size and batch size settings
new_size = (32, 32)
batch_size = 3600
batch_number = 1
image_count_in_batch = 0  # Counter for images in the current batch
global_image_count = 1  # Global counter for all images

# Start processing images
for filename in sorted(os.listdir(source_dir)):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(source_dir, filename)
        img = Image.open(img_path)
        original_size = img.size  # Get original size before resizing
        img = img.resize(new_size, Image.Resampling.LANCZOS)

        # Create a new batch folder if necessary
        batch_dir = os.path.join(target_root_dir, f'batch-{batch_number}')
        if not os.path.exists(batch_dir):
            os.makedirs(batch_dir)

        # Format new filename using the base_filename variable
        new_filename = f"{base_filename}-{global_image_count:0{global_image_count_digits}}.jpg"
        img.save(os.path.join(batch_dir, new_filename))

        # Increment the image count in the current batch and the global count
        image_count_in_batch += 1
        global_image_count += 1

        if image_count_in_batch == batch_size:
            print(f"Batch {batch_number} completed with {image_count_in_batch} images.")
            batch_number += 1  # Start a new batch
            image_count_in_batch = 0  # Reset the count for the new batch
            print(f"Starting new batch: batch-{batch_number}")

# Output the number of images in the last batch and the how many lines for the last folder
if image_count_in_batch > 0:
    print(f"Last batch {batch_number} has {image_count_in_batch} images. The height should be: {(image_count_in_batch // 60) + (1 if image_count_in_batch % 60 != 0 else 0)}")

print("Image resizing and batching completed.")

```
Once you run the code, you are expected the images will be placed into the batches directory and here is the layout of the path:
```
    src
    ├── data
    │   ├── downsize.py
    │   ├── total_imgs
    │   ├── image_data.json
    │   └── batches
    │       ├── batch-1 --> 3600 images inside 
    │       ├── batch-2 --> 3600 images inside 
    │       ├── batch-3 --> 3600 images inside
    │       └── batch-4 --> rest images inside
```
----------------------------------------------------------------
  - Create a file that lists all files to be include in the montage
  - run the code in terminal

```
ls batch-1/* > images_to_montage-1.txt
ls batch-2/* > images_to_montage-2.txt
ls batch-3/* > images_to_montage-3.txt
ls batch-4/* > images_to_montage-4.txt
```

Once you finsihed the code, you should be able to see 
```
    src
    ├── data
    │   ├── downsize.py
    │   ├── total_imgs
    │   ├── image_data.json
    │   └── batches
    │   │   ├── batch-1 --> 3600 images inside 
    │   │   ├── batch-2 --> 3600 images inside 
    │   │   ├── batch-3 --> 3600 images inside
    │   │   ├── batch-4 --> rest images inside
    │   │   ├── images_to_montage-1.txt
    │   │   ├── images_to_montage-2.txt
    │   │   ├── images_to_montage-3.txt
    │   │   └── images_to_montage-4.txt
    
```

Here is a simple images_to_montage-1.txt

```
batch-1/figures-00001.jpg
batch-1/figures-00001.jpg
batch-1/figures-00002.jpg
.....
batch-1/figures-03600.jpg
```

----------------------------------------------------------------
- Once we get the txt file, we can create a montage
```
montage `cat images_to_montage-1.txt` -geometry +0+0 -background none -tile 60x60 atlas-1.jpg
montage `cat images_to_montage-2.txt` -geometry +0+0 -background none -tile 60x60 atlas-2.jpg
montage `cat images_to_montage-3.txt` -geometry +0+0 -background none -tile 60x60 atlas-3.jpg
montage `cat images_to_montage-4.txt` -geometry +0+0 -background none -tile 60x60 atlas-4.jpg
```
Explaination:
- montage: Command to create a composite image.
- `cat images_to_montage-1.txt`: Outputs the list of image filenames from images_to_montage-1.txt.
- -geometry +0+0: Places images starting from the top-left corner of the composite image.
- -background none: Sets the background of the composite image to transparent.
- -tile 60x60: Arranges images in a grid layout where each cell is 60x60 pixels.
- atlas-1.jpg: Output filename for the composite image.

- Output:
```
    src
    ├── data
    │   ├── downsize.py
    │   ├── total_imgs
    │   ├── image_data.json
    │   └── batches
    │   │   ├── batch-1 --> 3600 images inside 
    │   │   ├── batch-2 --> 3600 images inside 
    │   │   ├── batch-3 --> 3600 images inside
    │   │   ├── batch-4 --> rest images inside
    │   │   ├── images_to_montage-1.txt
    │   │   ├── images_to_montage-2.txt
    │   │   ├── images_to_montage-3.txt
    │   │   ├── images_to_montage-4.txt
    │   │   ├── atlas-1.jpg
    │   │   ├── atlas-2.jpg
    │   │   ├── atlas-3.jpg
    │   │   └── atlas-4.jpg  
    
```

----------------------------------------------------------------

Once we have all the data we need to put all those images with the same directory into the server

```
    src
    ├── data
    │   ├── downsize.py
    │   ├── total_imgs
    │   ├── image_data.json
    │   └── batches
    │   │   ├── batch-1 --> 3600 images inside 
    │   │   ├── batch-2 --> 3600 images inside 
    │   │   ├── batch-3 --> 3600 images inside
    │   │   ├── batch-4 --> rest images inside
    │   │   ├── images_to_montage-1.txt
    │   │   ├── images_to_montage-2.txt
    │   │   ├── images_to_montage-3.txt
    │   │   ├── images_to_montage-4.txt
    │   │   ├── atlas-1.jpg
    │   │   ├── atlas-2.jpg
    │   │   ├── atlas-3.jpg
    │   │   └── atlas-4.jpg  
    
```

example, I am hosting those data at my server <em>https://zhiyangwang.site</em>
```
# here is the sturcture of my server
    public
    ├── Giant-image-data
    │   ├── total_imgs
    │   ├── image_data.json
    │   └── batches
    │   │   ├── batch-1 --> 3600 images inside 
    │   │   ├── batch-2 --> 3600 images inside 
    │   │   ├── batch-3 --> 3600 images inside
    │   │   ├── batch-4 --> rest images inside
    │   │   ├── atlas-1.jpg
    │   │   ├── atlas-2.jpg
    │   │   ├── atlas-3.jpg
    │   │   └── atlas-4.jpg  
    
```