import os

with open(rf"{os.path.dirname(__file__)}\default_style.qss", "r") as f:
    default_style: str = f.read()