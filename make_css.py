#!/usr/bin/env python

import os
import sys
from PIL import Image

if len(sys.argv) > 4:
    css = sys.argv[1]
    sprite = sys.argv[2]
    img_folder = sys.argv[3]
    layout = sys.argv[4]
else:
    print "Usage: python make_css.py <css_filename> <sprite_filename> <image_folder> <sprite_layout>"
    print "Example: python make_css.py example.css example.png ../images vertical"

file = open(css, 'w')

file.write("/** sprite: " + sprite[0:-4] + "; sprite-image: url('" + sprite + "'); sprite-layout: " + layout + " */\n")

for image in os.listdir(img_folder):
    try:
        im = Image.open(img_folder + '/' + image)
    except:
        print "failed to identify", image
    else:
        file.write("#" + image[0:-4] + "\n")
        file.write("{\n")
        file.write("  width: " + `im.size[0]` + "\n")
        file.write("  height: " + `im.size[1]` + "\n")
        file.write("  background-image: url(" + img_folder + "/" + image + "); /** sprite-ref: " + sprite[0:-4] + "; */\n")
        file.write("}\n\n")
