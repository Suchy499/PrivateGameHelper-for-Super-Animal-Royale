import os

path = os.path.dirname(__file__)
IMAGES = {}

for dirpath, dirnames, filenames in os.walk(rf"{path}\images"):
    for f in filenames:
        IMAGES[os.path.splitext(f)[0]] = os.path.join(dirpath, f)