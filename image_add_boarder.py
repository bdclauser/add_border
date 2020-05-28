#!/usr/bin/env python3
# image_add_boarder.py - Automatically grabs all images in folder and adds a border around it

import os
import sys
from PIL import Image, ImageOps

os.makedirs('withBorder', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue  # skip non-image files
    img = Image.open(filename)
    print('Adding border to %s...' % (filename))
    im = ImageOps.expand(img, border=3, fill='black')
    im = im.convert("RGB")
    im.save(os.path.join('withBorder', filename.replace("png", "jpg")))
