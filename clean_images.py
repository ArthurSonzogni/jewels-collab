#!/usr/bin/env python3
import re
import os

content_path = 'content'
images_path = 'public/images'

# Part 1: Remove unused images
referenced_images = set()
for root, _, files in os.walk(content_path):
    for file in files:
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
                found_images = re.findall(r':\s*/images/(.*)', content)
                referenced_images.update(image.strip() for image in found_images)

all_images = set(os.listdir(images_path))
all_images = all_images - {'.gitkeep'}

unused_images = all_images - referenced_images

for image in unused_images:
    full_path = os.path.join(images_path, image)
    print(f'Removing unused image: {full_path}')
    os.remove(full_path)

# Part 2: Remove references to non-existing images.
all_images = set(os.listdir(images_path))
print(f'All images in {images_path}: {all_images}')

for root, _, files in os.walk(content_path):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                lines = f.readlines()

            new_lines = []
            modified = False
            for line in lines:
                match = re.search(r':\s*/images/(.*)', line)
                if match:
                    image_name = match.group(1).strip()
                    print(f'Checking image reference: {image_name}')
                    if image_name not in all_images:
                        print(f'Removing reference to non-existing image {image_name} in {filepath}')
                        modified = True
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)

            if modified:
                with open(filepath, 'w') as f:
                    f.writelines(new_lines)
