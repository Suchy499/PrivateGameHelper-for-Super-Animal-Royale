from .qt_core import *
import json
import os
import time
import keyboard
import pywinctl
import pyautogui

# Keybinds
keyboard.add_hotkey("ctrl+alt+q", lambda: clear_queue())

# Classes
class SignalManager(QObject):
    presetOpened = Signal(dict)
    presetsChanged = Signal()
    presetRestored = Signal(dict)

class Globals:
    SIGNAL_MANAGER: SignalManager = SignalManager()
    QUEUE: list = []
    TIMER: QTimer = QTimer()
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
    
# Presets
def read_presets() -> list[dict]:
    with open(os.path.join(os.path.dirname(__file__), "presets.json")) as f:
        return json.load(f)

def save_presets(data: list[dict]) -> None:
    with open(os.path.join(os.path.dirname(__file__), "presets.json"), "w") as f:
        json.dump(data, f, indent=4)

def edit_preset() -> None:
    presets_data: list[dict] = read_presets()
    preset_index: int = find_dict_index(presets_data, "preset_id", Globals.PREGAME_SETTINGS["preset_id"])
    Globals.PREGAME_SETTINGS["last_edited"] = time.time()
    if Globals.PREGAME_SETTINGS["name"] is None or Globals.PREGAME_SETTINGS["name"] == "":
        Globals.PREGAME_SETTINGS["name"] = "Untitled"
    presets_data[preset_index] = Globals.PREGAME_SETTINGS
    save_presets(presets_data)
    Globals.SIGNAL_MANAGER.presetsChanged.emit()

def save_preset() -> None:
    presets_data: list[dict] = read_presets()
    if len(presets_data) >= 1:
        Globals.PREGAME_SETTINGS["preset_id"] = presets_data[-1]["preset_id"] + 1
    else:
        Globals.PREGAME_SETTINGS["preset_id"] = 0
    Globals.PREGAME_SETTINGS["last_edited"] = time.time()
    if Globals.PREGAME_SETTINGS["name"] is None or Globals.PREGAME_SETTINGS["name"] == "":
        Globals.PREGAME_SETTINGS["name"] = "Untitled"
    presets_data.append(Globals.PREGAME_SETTINGS)
    save_presets(presets_data)
    Globals.SIGNAL_MANAGER.presetsChanged.emit()

def delete_preset() -> None:
    presets_data: list[dict] = read_presets()
    preset_index: int = find_dict_index(presets_data, "preset_id", Globals.PREGAME_SETTINGS["preset_id"])
    presets_data.pop(preset_index)
    save_presets(presets_data)
    Globals.SIGNAL_MANAGER.presetsChanged.emit()

# Queue
def add_commands(*commands: str) -> None:
    for command in commands:
        Globals.QUEUE.append(lambda: pyautogui.press("enter"))
        Globals.QUEUE.append(lambda: pyautogui.write(f"/{command}"))
        Globals.QUEUE.append(lambda: pyautogui.press("enter"))
    
def execute_queue(timeout_msc: int = 0) -> None:
    Globals.TIMER.timeout.connect(execute_command)
    Globals.TIMER.start(timeout_msc)

def execute_command() -> None:
    try:
        command = Globals.QUEUE[0]
        Globals.QUEUE.pop(0)
        command()
    except IndexError:
        Globals.TIMER.stop()

def clear_queue() -> None:
    Globals.QUEUE = []

# Buttons
def get_match_id() -> None:
    open_window("Super Animal Royale")
    Globals.QUEUE = []
    add_commands("matchid")
    execute_queue()

def start_game() -> None:
    open_window("Super Animal Royale")
    Globals.QUEUE = []
    if Globals.PREGAME_SETTINGS["settings"]["bots"]:
        add_commands("start")
    else:
        add_commands("startp")
    execute_queue()
    
def apply_settings() -> None:
    open_window("Super Animal Royale")
    Globals.QUEUE = []
    settings: dict = Globals.PREGAME_SETTINGS["settings"]
    weights: dict = settings["gun_weights"]
    for key, value in settings.items():
        match key:
            case "gun_weights":
                continue
            case "onehits" | "noroll":
                if value:
                    add_commands(key)
            case "gasspeed" | "gasdmg" | "bulletspeed" | "dmg":
                if value != 1.0:
                    add_commands(f"{key} {value}")
            case "highping":
                if value != 250:
                    add_commands(f"{key} {value}")
            case _:
                if not value:
                    add_commands(key)
    
    for key, value in weights.items():
        if value != 1.0:
            add_commands(f"weight {key} {value}")
    
    execute_queue()

# Misc
def find_dict_index(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def open_window(window_title: str) -> None | object:
    if len(pywinctl.getWindowsWithTitle(window_title, flags="IS")) == 0:
        return None
    window = pywinctl.getWindowsWithTitle(window_title, flags="IS")[0]
    window.activate()
    return window