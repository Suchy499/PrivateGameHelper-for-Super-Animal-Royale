import os
from . import rc_images

IMAGES = {}

with open(os.path.join(os.path.dirname(__file__), "rc_images.qrc"), "r") as f:
    file_lines = f.readlines()
    for line in file_lines[2:-2]:
        line = line.strip()
        line = line.replace("<file>", "")
        line = line.replace("</file>", "")
        line_data = line.split("/")
        IMAGES[os.path.splitext(line_data[1])[0]] = f":/{line}"