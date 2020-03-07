#! /usr/bin/env python3
# image_add_boarder.py - Automatically grabs all images in folder and adds a border around it

import os
import sys
from PIL import Image, ImageOps

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue  # skip non-image files
    img = Image.open(filename)
    print('Adding border to %s...' % (filename))
    im = ImageOps.expand(img, border=2, fill='black')
    im.size(os.path.join('withBorder', filename))
