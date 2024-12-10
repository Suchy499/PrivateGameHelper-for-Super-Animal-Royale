import os
from enum import StrEnum

with open(rf"{os.path.dirname(__file__)}\purple.qss", "r") as f:
    purple: str = f.read()

with open(rf"{os.path.dirname(__file__)}\blue.qss", "r") as f:
    blue: str = f.read()
    
with open(rf"{os.path.dirname(__file__)}\overlay_dark.qss", "r") as f:
    overlay_dark: str = f.read()
    
with open(rf"{os.path.dirname(__file__)}\overlay_purple.qss", "r") as f:
    overlay_purple: str = f.read()

class AppStyle(StrEnum):
    PURPLE = purple
    BLUE = blue
    
    @staticmethod
    def getValue(index):
        return list(AppStyle)[index].value

class OverlayStyle(StrEnum):
    PURPLE = overlay_purple
    DARK = overlay_dark
    
    @staticmethod
    def getValue(index):
        return list(OverlayStyle)[index].value