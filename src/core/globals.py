from core.qt_core import *
from core.classes import *
from typing import Literal

KEY_DELAY: float = 0.025
SIGNAL_MANAGER: SignalManager = SignalManager()
WORK_THREAD: QThread = WorkThread()
ACTIVE_PRESET: int | None = None
SELECTED_PLAYER: PlayerItem | None = None
SELECTED_PLAYER_TELE: PlayerItem | Literal["ALL"] | None = None
SELECTED_RARITY: int = 0
HOST_ID: int = 1
SELECTED_MAP_DUELS: str = "Bamboo Resort"
PREGAME_SETTINGS: dict = {
    "preset_id": None,
    "name": None,
    "last_edited": None,
    "settings": {
        "allitems": True,
        "guns": True,
        "armors": True,
        "throwables": True,
        "powerups": True,
        "onehits": False,
        "emus": True,
        "hamballs": True,
        "ziplines": True,
        "moles": True,
        "pets": True,
        "gasoff": True,
        "noroll": False,
        "bots": False,
        "gasspeed": 1.0,
        "gasdmg": 1.0,
        "bulletspeed": 1.0,
        "dmg": 1.0,
        "highping": 250,
        "gun_weights": {
            "gunpistol": 1.0,
            "gunmagnum": 1.0,
            "gundeagle": 1.0,
            "gunsilencedpistol": 1.0,
            "gunshotgun": 1.0,
            "gunjag7": 1.0,
            "gunsmg": 1.0,
            "gunthomas": 1.0,
            "gunak": 1.0,
            "gunm16": 1.0,
            "gundart": 1.0,
            "gundartepic": 1.0,
            "gunhuntingrifle": 1.0,
            "gunsniper": 1.0,
            "gunlaser": 1.0,
            "gunminigun": 1.0,
            "gunbow": 1.0,
            "guncrossbow": 1.0,
            "gunegglauncher": 1.0,
            "grenadefrag": 1.0,
            "grenadebanana": 1.0,
            "grenadeskunk": 1.0,
            "grenadecatmine": 1.0,
            "grenadezipline": 1.0
        }
    }
}
PREGAME_DEFAULT_SETTINGS: dict = {
    "preset_id": None,
    "name": None,
    "last_edited": None,
    "settings": {
        "allitems": True,
        "guns": True,
        "armors": True,
        "throwables": True,
        "powerups": True,
        "onehits": False,
        "emus": True,
        "hamballs": True,
        "ziplines": True,
        "moles": True,
        "pets": True,
        "gasoff": True,
        "noroll": False,
        "bots": False,
        "gasspeed": 1.0,
        "gasdmg": 1.0,
        "bulletspeed": 1.0,
        "dmg": 1.0,
        "highping": 250,
        "gun_weights": {
            "gunpistol": 1.0,
            "gunmagnum": 1.0,
            "gundeagle": 1.0,
            "gunsilencedpistol": 1.0,
            "gunshotgun": 1.0,
            "gunjag7": 1.0,
            "gunsmg": 1.0,
            "gunthomas": 1.0,
            "gunak": 1.0,
            "gunm16": 1.0,
            "gundart": 1.0,
            "gundartepic": 1.0,
            "gunhuntingrifle": 1.0,
            "gunsniper": 1.0,
            "gunlaser": 1.0,
            "gunminigun": 1.0,
            "gunbow": 1.0,
            "guncrossbow": 1.0,
            "gunegglauncher": 1.0,
            "grenadefrag": 1.0,
            "grenadebanana": 1.0,
            "grenadeskunk": 1.0,
            "grenadecatmine": 1.0,
            "grenadezipline": 1.0
        }
    }
}
DUELS_SETTINGS: dict = {
    "weapons": True,
    "armor": True,
    "throwables": True,
    "powerups": True,
    "no_pets": False,
    "onehits": False,
    "noroll": False,
    "boundaries": False
}
DUELS_A_WEAPONS: dict = {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: True,
    8: True,
    9: True,
    10: True,
    11: True,
    12: True,
    13: True,
    14: True,
    15: True,
    16: True,
    17: True,
    18: True,
    19: True,
}
DUELS_B_WEAPONS: dict = {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: True,
    8: True,
    9: True,
    10: True,
    11: True,
    12: True,
    13: True,
    14: True,
    15: True,
    16: True,
    17: True,
    18: True,
    19: True,
}
PLAYER_LIST: list[PlayerItem] = []