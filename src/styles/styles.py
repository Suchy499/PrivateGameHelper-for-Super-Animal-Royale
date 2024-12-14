from styles.qss_parser import dumps, load, dump
import os
from enum import StrEnum
from copy import deepcopy

STYLESHEETS: dict[str, dict] = {}

for dirpath, dirnames, filenames in os.walk(os.path.join(os.path.dirname(__file__), "styles")):
    for name in filenames:
        STYLESHEETS[os.path.splitext(name)[0]] = load(os.path.join(dirpath, name))

def merge_styles() -> str:
    stylesheets_copy = deepcopy(STYLESHEETS)
    base_template = stylesheets_copy["base"]
    stylesheets_copy.pop("base")
    for name, stylesheet in stylesheets_copy.items():
        STYLESHEETS[name] = deepcopy(base_template)
        for rule, properties in stylesheet.items():
            STYLESHEETS[name][rule] = properties

merge_styles()

class Style(StrEnum):
    PURPLE = dumps(STYLESHEETS["purple"])
    DARK = dumps(STYLESHEETS["dark"])
    BLUE = dumps(STYLESHEETS["blue"])
    PURPLE_SKY = dumps(STYLESHEETS["purple_sky"])
    COTTON_CANDY = dumps(STYLESHEETS["cotton_candy"])
    AQUA = dumps(STYLESHEETS["aqua"])
    NEBULA = dumps(STYLESHEETS["nebula"])
    VOID = dumps(STYLESHEETS["void"])
    SUNRISE = dumps(STYLESHEETS["sunrise"])
    VAPORWAVE = dumps(STYLESHEETS["vaporwave"])
    BLACK_AND_WHITE = dumps(STYLESHEETS["black_and_white"])
    
    @staticmethod
    def getValue(index):
        return list(Style)[index].value