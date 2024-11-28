from .qt_core import *
import json
import os
import time
import keyboard
import pyperclip
import pywinctl
import pyautogui
from dataclasses import dataclass
from typing import Literal

# Classes
class SignalManager(QObject):
    presetOpened = Signal(dict)
    presetsChanged = Signal()
    presetRestored = Signal(dict)
    playersRefreshed = Signal()
    playerSelected = Signal()
    raritySelected = Signal()

@dataclass
class PlayerItem:
    player_id: int
    name: str

class Globals:
    SIGNAL_MANAGER: SignalManager = SignalManager()
    QUEUE: list = []
    TIMER: QTimer = QTimer()
    ACTIVE_PRESET: int | None = None
    SELECTED_PLAYER: PlayerItem | None = None
    SELECTED_PLAYER_TELE: PlayerItem | Literal["ALL"] | None = None
    SELECTED_RARITY: int = 0
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
    PLAYER_LIST: list[PlayerItem] = []
    
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
    Globals.ACTIVE_PRESET = None

# Queue
def send_command(command):
    pyautogui.press("enter")
    pyautogui.write(f"/{command}")
    pyautogui.press("enter")
        
def add_commands(commands: str) -> None:
    Globals.QUEUE.append(lambda: send_command(commands))
    
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
    if not open_window("Super Animal Royale"):
        return
    Globals.QUEUE = []
    add_commands("matchid")
    execute_queue()

def start_game() -> None:
    if not open_window("Super Animal Royale"):
        return
    Globals.QUEUE = []
    if Globals.PREGAME_SETTINGS["settings"]["bots"]:
        add_commands("start")
    else:
        add_commands("startp")
    execute_queue()
    
def apply_settings() -> None:
    if not open_window("Super Animal Royale"):
        return
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

# Players
def read_players() -> list:
    if open_window("Super Animal Royale"):
        Globals.PLAYER_LIST = []
        send_command("getplayers")
        time.sleep(0.5)
        clipboard: list[str] = pyperclip.paste().split("\n")
        clipboard.remove("")
        clipboard.pop(0)
        for player in clipboard:
            player_id = int(player.split("\t")[0])
            name = player.split("\t")[1]
            Globals.PLAYER_LIST.append(PlayerItem(player_id, name))
        Globals.SIGNAL_MANAGER.playersRefreshed.emit()
    return Globals.PLAYER_LIST

def send_player_command(command: str) -> None:
    if not Globals.SELECTED_PLAYER:
        return
    if not open_window("Super Animal Royale"):
        return
    send_command(f"{command} {Globals.SELECTED_PLAYER.player_id}")

# Teleport
def teleport_player(x: int, y: int) -> None:
    if not Globals.SELECTED_PLAYER_TELE:
        return
    if not open_window("Super Animal Royale"):
        return
    if Globals.SELECTED_PLAYER_TELE == "ALL":
        send_command(f"tele all {x} {y}")
    else:
        send_command(f"tele {Globals.SELECTED_PLAYER_TELE.player_id} {x} {y}")

def select_all_players() -> None:
    Globals.SELECTED_PLAYER_TELE = "ALL"
    Globals.SIGNAL_MANAGER.playerSelected.emit()

# Items
def spawn_weapon(weapon_id: int) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_command(f"gun{weapon_id} {Globals.SELECTED_RARITY}")

def spawn_ammo(amount: int, ammo_id: int) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_command(f"ammo{ammo_id} {amount}")

def spawn_healing(amount: int, healing_type: Literal["juice", "tape"]) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_command(f"{healing_type} {amount}")

def spawn_throwable(amount: int, throwable_type: Literal["banana", "nade", "zip"]) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_command(f"{throwable_type} {amount}")

def spawn_equipment(command: str) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_command(command)

# Commands
send_other_command = spawn_equipment

# Keybinds
keyboard.add_hotkey("ctrl+alt+q", clear_queue)