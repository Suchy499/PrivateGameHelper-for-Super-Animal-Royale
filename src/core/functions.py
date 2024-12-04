from core.qt_core import *
from core.classes import *
import core.globals as global_vars
import json
import os
import time
import keyboard
import pyperclip
import pywinctl
import pyautogui
import random
import winreg
from pynput.mouse import Button
from functools import partial
from typing import Literal, Callable, Any
    
# Presets
def read_presets() -> list[dict]:
    with open(os.path.join(os.path.dirname(__file__), "presets.json")) as f:
        return json.load(f)

def save_presets(data: list[dict]) -> None:
    with open(os.path.join(os.path.dirname(__file__), "presets.json"), "w") as f:
        json.dump(data, f, indent=4)

def edit_preset() -> None:
    presets_data: list[dict] = read_presets()
    preset_index: int = find_dict_index(presets_data, "preset_id", global_vars.PREGAME_SETTINGS["preset_id"])
    global_vars.PREGAME_SETTINGS["last_edited"] = time.time()
    if global_vars.PREGAME_SETTINGS["name"] is None or global_vars.PREGAME_SETTINGS["name"] == "":
        global_vars.PREGAME_SETTINGS["name"] = "Untitled"
    presets_data[preset_index] = global_vars.PREGAME_SETTINGS
    save_presets(presets_data)
    global_vars.SIGNAL_MANAGER.presetsChanged.emit()

def save_preset() -> None:
    presets_data: list[dict] = read_presets()
    if len(presets_data) >= 1:
        global_vars.PREGAME_SETTINGS["preset_id"] = presets_data[-1]["preset_id"] + 1
    else:
        global_vars.PREGAME_SETTINGS["preset_id"] = 0
    global_vars.PREGAME_SETTINGS["last_edited"] = time.time()
    if global_vars.PREGAME_SETTINGS["name"] is None or global_vars.PREGAME_SETTINGS["name"] == "":
        global_vars.PREGAME_SETTINGS["name"] = "Untitled"
    presets_data.append(global_vars.PREGAME_SETTINGS)
    save_presets(presets_data)
    global_vars.SIGNAL_MANAGER.presetsChanged.emit()

def delete_preset() -> None:
    presets_data: list[dict] = read_presets()
    preset_index: int = find_dict_index(presets_data, "preset_id", global_vars.PREGAME_SETTINGS["preset_id"])
    presets_data.pop(preset_index)
    save_presets(presets_data)
    global_vars.SIGNAL_MANAGER.presetsChanged.emit()
    global_vars.ACTIVE_PRESET = None

# SAR Keybinds
def read_registry_key(key: str) -> Any:
    a_reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    a_key = winreg.OpenKey(a_reg, r"SOFTWARE\Pixile Inc\Super Animal Royale")
    for i in range(1024):
        try:
            value_name, value_data, data_type = winreg.EnumValue(a_key, i)
            if value_name == key:
                if data_type == 3:
                    return str(value_data)[2:-5]
                return value_data
        except WindowsError:
            break
    return None

def parse_hotkey(hotkey: str | None) -> int | str | None:
    if hotkey is None:
        return None
    if "Minus" == hotkey:
        return 12
    if "Equals" == hotkey:
        return 13
    if "Backspace" == hotkey:
        return 14
    if "Tab" == hotkey:
        return 15
    if "LeftBracket" == hotkey:
        return 26
    if "RightBracket" == hotkey:
        return 27
    if "Return" == hotkey:
        return 28
    if "LeftControl" == hotkey:
        return 29
    if "Semicolon" == hotkey:
        return 39
    if "Quote" == hotkey:
        return 40
    if "BackQuote" == hotkey:
        return 41
    if "LeftShift" == hotkey:
        return 42
    if "Backslash" == hotkey:
        return 43
    if "Comma" == hotkey:
        return 51
    if "Period" == hotkey:
        return 52
    if "Slash" == hotkey:
        return 53
    if "RightShift" == hotkey:
        return 54
    if "KeypadMultiply" == hotkey:
        return 55
    if "LeftAlt" == hotkey:
        return 56
    if "Space" == hotkey:
        return 57
    if "CapsLock" == hotkey:
        return 58
    if "Numlock" == hotkey:
        return 69
    if "ScrollLock" == hotkey:
        return 70
    if "Keypad7" == hotkey:
        return 71
    if "Keypad8" == hotkey:
        return 72
    if "Keypad9" == hotkey:
        return 73
    if "KeypadMinus" == hotkey:
        return 74
    if "Keypad4" == hotkey:
        return 75
    if "Keypad5" == hotkey:
        return 76
    if "Keypad6" == hotkey:
        return 77
    if "KeypadPlus" == hotkey:
        return 78
    if "Keypad1" == hotkey:
        return 79
    if "Keypad2" == hotkey:
        return 80
    if "Keypad3" == hotkey:
        return 81
    if "Keypad0" == hotkey:
        return 82
    if "KeypadPeriod" == hotkey:
        return 83
    if "KeypadEnter" == hotkey:
        return 156
    if "RightControl" == hotkey:
        return 157
    if "KeypadDivide" == hotkey:
        return 181
    if "Home" == hotkey:
        return 199
    if "UpArrow" == hotkey:
        return 200
    if "PageUp" == hotkey:
        return 201
    if "LeftArrow" == hotkey:
        return 203
    if "RightArrow" == hotkey:
        return 205
    if "End" == hotkey:
        return 207
    if "DownArrow" == hotkey:
        return 208
    if "PageDown" == hotkey:
        return 209
    if "Insert" == hotkey:
        return 210
    if "Delete" == hotkey:
        return 211
    if "Alpha" in hotkey:
        return hotkey[-1]
    return hotkey.lower()

def press_hotkey(hotkey: str | int) -> None:
    match hotkey:
        case "mouse0":
            global_vars.MOUSE_CTL.click(Button.left)
        case "mouse1":
            global_vars.MOUSE_CTL.click(Button.right)
        case "mouse2":
            global_vars.MOUSE_CTL.click(Button.middle)
        case "mouse3":
            global_vars.MOUSE_CTL.click(Button.x1)
        case "mouse4":
            global_vars.MOUSE_CTL.click(Button.x2)
        case _:
            keyboard.send(hotkey)

def refresh_hotkeys() -> None:
    global_vars.OPEN_CHAT_BIND = parse_hotkey(read_registry_key("Open Chat_h2580809935")) or "enter"
    global_vars.MELEE_BIND = parse_hotkey(read_registry_key("Melee Weapon_h3432856419")) or "3"
    global_vars.THROWABLE_BIND = parse_hotkey(read_registry_key("Grenade_h3300402683")) or "4"
    global_vars.USE_BIND = parse_hotkey(read_registry_key("Use / Pickup_h1560228861")) or "e"

refresh_hotkeys()

# Queue
def send_commands(*commands: str, delay: int = 1):
    for command in commands:
        time.sleep(global_vars.KEY_DELAY*delay)
        pyperclip.copy(f"/{command}")
        press_hotkey(global_vars.OPEN_CHAT_BIND)
        time.sleep(global_vars.KEY_DELAY*delay)
        keyboard.send("ctrl+v")
        time.sleep(global_vars.KEY_DELAY*delay)
        keyboard.send("enter")
        
def add_commands(*commands: str, delay: int = 1) -> None:
    global_vars.WORK_THREAD.QUEUE.append(lambda: send_commands(*commands, delay))

def queue_append(command: Callable):
    global_vars.WORK_THREAD.QUEUE.append(command)
    
def execute_queue() -> None:
    global_vars.WORK_THREAD.start()

def clear_queue() -> None:
    global_vars.WORK_THREAD.QUEUE = []

# Buttons
def get_match_id() -> None:
    if not open_window("Super Animal Royale"):
        return
    global_vars.WORK_THREAD.QUEUE = []
    add_commands("matchid")
    execute_queue()

def start_game() -> None:
    if not open_window("Super Animal Royale"):
        return
    global_vars.WORK_THREAD.QUEUE = []
    if global_vars.PREGAME_SETTINGS["settings"]["bots"]:
        add_commands("start")
    else:
        add_commands("startp")
    execute_queue()
    
def apply_settings() -> None:
    if not open_window("Super Animal Royale"):
        return
    global_vars.WORK_THREAD.QUEUE = []
    settings: dict = global_vars.PREGAME_SETTINGS["settings"]
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
        global_vars.PLAYER_LIST = []
        send_commands("getplayers")
        time.sleep(0.5)
        clipboard: list[str] = pyperclip.paste().split("\n")
        clipboard.remove("")
        clipboard.pop(0)
        for player in clipboard:
            player_id = int(player.split("\t")[0])
            name = player.split("\t")[1]
            global_vars.PLAYER_LIST.append(PlayerItem(player_id, name))
        global_vars.SIGNAL_MANAGER.playersRefreshed.emit()
    return global_vars.PLAYER_LIST

def send_player_command(command: str) -> None:
    if not global_vars.SELECTED_PLAYER:
        return
    if not open_window("Super Animal Royale"):
        return
    add_commands(f"{command} {global_vars.SELECTED_PLAYER.player_id}")
    execute_queue()

# Teleport
def teleport_player(x: int, y: int) -> None:
    if not global_vars.SELECTED_PLAYER_TELE:
        return
    if not open_window("Super Animal Royale"):
        return
    if global_vars.SELECTED_PLAYER_TELE == "ALL":
        add_commands(f"tele all {x} {y}")
    else:
        add_commands(f"tele {global_vars.SELECTED_PLAYER_TELE.player_id} {x} {y}")
    execute_queue()

def select_all_players() -> None:
    global_vars.SELECTED_PLAYER_TELE = "ALL"
    global_vars.SIGNAL_MANAGER.playerSelected.emit()

# Items
def spawn_weapon(weapon_id: int) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_commands(f"gun{weapon_id} {global_vars.SELECTED_RARITY}")

def spawn_ammo(amount: int, ammo_id: int) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_commands(f"ammo{ammo_id} {amount}")

def spawn_healing(amount: int, healing_type: Literal["juice", "tape"]) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_commands(f"{healing_type} {amount}")

def spawn_throwable(amount: int, throwable_type: Literal["banana", "nade", "zip"]) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_commands(f"{throwable_type} {amount}")

def spawn_equipment(command: str) -> None:
    if not open_window("Super Animal Royale"):
        return
    send_commands(command)

# Commands
send_other_command = spawn_equipment

# Duels
def get_teams() -> tuple[list, list, list]:
    a = []
    b = []
    spec = []
    for player in global_vars.PLAYER_LIST:
        match player.team:
            case 0:
                a.append(player.player_id)
            case 1:
                spec.append(player.player_id)
            case 2:
                b.append(player.player_id)
    return a, b, spec

def spawn_ammo(x: int, y: int, players: int) -> None:
    send_commands(f"tele {global_vars.HOST_ID} {x} {y}")
    time.sleep(0.5)
    for _ in range(players):
        for i in range(6):
            send_commands(f"ammo{i} 500")
        send_commands("juice 200", "tape 5")
    time.sleep(0.5)

def spawn_powerups(x: int, y: int, players: int) -> None:
    send_commands(f"tele {global_vars.HOST_ID} {x} {y}")
    time.sleep(0.5)
    for _ in range(players):
        send_commands("util2", "util4")
    time.sleep(0.5)

def spawn_throwables(x: int, y: int, players: int) -> None:
    send_commands(f"tele {global_vars.HOST_ID} {x} {y}")
    time.sleep(0.5)
    for _ in range(players):
       send_commands("banana 10", "nade 4")
    time.sleep(0.5)

def spawn_armor(x: int, y: int, players: int) -> None:
    send_commands(f"tele {global_vars.HOST_ID} {x} {y}")
    time.sleep(0.5)
    for _ in range(players):
       send_commands("armor3")
    time.sleep(0.5)

def spawn_weapon_duel(x: int, y: int, weapon_id: int, players: int) -> None:
    send_commands(f"tele {global_vars.HOST_ID} {x} {y}")
    time.sleep(0.5)
    for _ in range(players):
       send_commands(f"gun{weapon_id} 3")
    time.sleep(0.5)

def append_weapons(weapons_list: list[int], players: int, team: Literal["a", "b"]) -> None:
    match team:
        case "a":  
            x_a: int = 735
            y_a: int = 1305
            for i, weapon_id in enumerate(weapons_list):
                call = partial(spawn_weapon_duel, x_a, y_a, weapon_id, players)
                queue_append(call)
                x_a += 10
                if i == 9:
                    x_a = 735
                    y_a -= 20
        case "b":
            x_b: int = 3875
            y_b: int = 1515
            for i, weapon_id in enumerate(weapons_list):
                call = partial(spawn_weapon_duel, x_b, y_b, weapon_id, players)
                queue_append(call)
                x_b += 10
                if i in (6, 13):
                    x_b = 3875
                    y_b -= 20

def ghost_spectators(spec_list: list[int]) -> None:
    for player in spec_list:
        if player != global_vars.HOST_ID:
            send_commands(f"ghost {player}")

def teleport_players(x: int, y: int, team: list[int]) -> None:
    for player in team:
        send_commands(f"tele {player} {x} {y}")

def wait_time() -> None:
    add_commands("yell 30 Seconds")
    queue_append(lambda: time.sleep(20))
    queue_append(lambda: open_window("Super Animal Royale"))
    add_commands("yell 10")
    queue_append(lambda: time.sleep(7))
    queue_append(lambda: open_window("Super Animal Royale"))
    add_commands("yell 3")
    queue_append(lambda: time.sleep(1))
    add_commands("yell 2")
    queue_append(lambda: time.sleep(1))
    add_commands("yell 1")
    queue_append(lambda: time.sleep(1))

def spawn_bananas(amount: int) -> None:
    time.sleep(global_vars.KEY_DELAY*40)
    send_commands(f"banana {amount}")
    time.sleep(global_vars.KEY_DELAY*80)
    press_hotkey(global_vars.THROWABLE_BIND)
    global_vars.BANANA_COUNT = 10
    send_commands("tele all 511 391")
    time.sleep(global_vars.KEY_DELAY*10)

def lay_banana(sar_handle, host_id: int, x_player: int, y_player: int, direction: Literal["N", "S", "E", "W"] = "N") -> None:
    sar_window_rect = sar_handle.getClientFrame()
    window_top_left_x, window_top_left_y = sar_window_rect[0], sar_window_rect[1]
    window_width: int = sar_window_rect[2] - window_top_left_x
    x_position, y_position = sar_handle.center
    player_offset: int = 9
    offset: int = 50
    
    size_ratio: float = window_width / 1920
    if size_ratio != 1:
        offset: int = int(offset * size_ratio)
    
    match direction:
        case "N":
            y_position -= offset
            y_player -= player_offset
        case "S":
            y_position += offset
            y_player += player_offset
        case "E":
            x_position += offset
            x_player -= player_offset
        case "W":
            x_position -= offset
            x_player += player_offset
    
    send_commands(f"tele {host_id} {x_player} {y_player}")
    time.sleep(global_vars.KEY_DELAY*8)
    if global_vars.BANANA_COUNT <= 0:
        spawn_bananas(10)
        send_commands(f"tele {host_id} {x_player} {y_player}")
    mouse_click(x_position, y_position)
    global_vars.BANANA_COUNT -= 1
    
def start_duel() -> None:
    sar_handle = open_window("Super Animal Royale")
    place_banana = partial(lay_banana, sar_handle, global_vars.HOST_ID)
    if not sar_handle:
        return
    
    team_a, team_b, team_spec = get_teams()
    team_a_len, team_b_len = len(team_a), len(team_b)
    if team_a_len > 4:
        team_a_len = 4
    elif team_a_len == 0:
        team_a_len = 1

    if team_b_len > 4:
        team_b_len = 4
    elif team_b_len == 0:
        team_b_len = 1
    
    queue_append(lambda: time.sleep(0.2))
    add_commands("allitems", "emus", "hamballs", "gasoff")
    
    if global_vars.DUELS_SETTINGS["no_pets"]:
        add_commands("pets")
    
    if global_vars.DUELS_SETTINGS["onehits"]:
        add_commands("onehits")
    
    if global_vars.DUELS_SETTINGS["noroll"]:
        add_commands("noroll")
        
    add_commands(
        "startp", "god all",
        "yell Welcome to duels!",
        "yell Please jump out of the eagle as soon as possible",
        "yell So you can be teleported to weapon selection",
        f"yell Selected map: {global_vars.SELECTED_MAP_DUELS}"
    )
    queue_append(lambda: ghost_spectators(team_spec))
    
    queue_append(lambda: time.sleep(25))
    queue_append(lambda: open_window("Super Animal Royale"))
    queue_append(lambda: press_hotkey(global_vars.USE_BIND))
    queue_append(lambda: spawn_ammo(705, 1335, team_a_len))
    queue_append(lambda: spawn_ammo(3845, 1535, team_b_len))
    
    if global_vars.DUELS_SETTINGS["throwables"]:
        queue_append(lambda: spawn_throwables(735, 1335, team_a_len))
        queue_append(lambda: spawn_throwables(3875, 1545, team_b_len))
    
    if global_vars.DUELS_SETTINGS["armor"]:
        queue_append(lambda: spawn_armor(755, 1335, team_a_len))
        queue_append(lambda: spawn_armor(3895, 1545, team_b_len))
        
    if global_vars.DUELS_SETTINGS["powerups"]:
        queue_append(lambda: spawn_powerups(775, 1335, team_a_len))
        queue_append(lambda: spawn_powerups(3915, 1545, team_b_len))
        
    if global_vars.DUELS_SETTINGS["weapons"]:
        team_a_weapons = []
        team_b_weapons = []

        for weapon_id, state in global_vars.DUELS_A_WEAPONS.items():
            if state:
                team_a_weapons.append(weapon_id)

        for weapon_id, state in global_vars.DUELS_B_WEAPONS.items():
            if state:
                team_b_weapons.append(weapon_id)
        
        append_weapons(team_a_weapons, team_a_len, "a")
        append_weapons(team_b_weapons, team_b_len, "b")
    
    if global_vars.DUELS_SETTINGS["boundaries"]:
        global_vars.BANANA_COUNT = 0
        match global_vars.SELECTED_MAP_DUELS:
            case "Bamboo Resort":
                for x in range(2530, 2630, 30):
                    queue_append(partial(place_banana, x, 1760, "N"))
                
                for x in range(2556, 2606, 20):
                    queue_append(partial(place_banana, x, 1985, "S"))
                    
                for y in range(1817, 1857, 10):
                    queue_append(partial(place_banana, 2380, y, "E"))
                    queue_append(partial(place_banana, 2770, y, "W"))
                    
            case "SAW Security":
                for x in range(3460, 3530, 20):
                    queue_append(partial(place_banana, x, 1695, "N"))
                    
                for x in range(3600, 3630, 20):
                    queue_append(partial(place_banana, x, 1695, "N"))
                    
                for y in range(1810, 1865, 15):
                    queue_append(partial(place_banana, 3675, y, "W"))
                    
                for x in range(3545, 3575, 10):
                    queue_append(partial(place_banana, x, 2065, "S"))
                    
                for y in range(2037, 2057, 10):
                    queue_append(partial(place_banana, 3190, y, "E"))
                    
                for y in range(1795, 1835, 10):
                    queue_append(partial(place_banana, 3187, y, "E"))
                
            case "SAW Research Labs":
                for x in range(2710, 2740, 10):
                    queue_append(partial(place_banana, x, 2835, "N"))
                    
                for x in range(2784, 2814, 10):
                    queue_append(partial(place_banana, x, 2835, "N"))
                    
                for y in range(2847, 2867, 10):
                    queue_append(partial(place_banana, 2958, y, "E"))
                    queue_append(partial(place_banana, 2553, y, "E"))
                    
                for y in range(2920, 2950, 10):
                    queue_append(partial(place_banana, 2556, y, "W"))
                    queue_append(partial(place_banana, 2957, y, "E"))
                    
                for y in range(3028, 3058, 10):
                    queue_append(partial(place_banana, 2556, y, "W"))
                    queue_append(partial(place_banana, 2957, y, "E"))
                
                for offset in range(0, 40, 10):
                    queue_append(partial(place_banana, 2561 + offset, 3103 + offset, "W"))
                    queue_append(partial(place_banana, 2956 - offset, 3110 + offset, "W"))
                
                queue_append(partial(place_banana, 2766, 3126, "N"))
                queue_append(partial(place_banana, 2748, 3126, "N"))
                queue_append(partial(place_banana, 2644, 3136, "N"))
                    
            case "Welcome Center":
                for x in range(660, 740, 20):
                    queue_append(partial(place_banana, x, 660, "S"))
                    
                for x in range(835, 865, 15):
                    queue_append(partial(place_banana, x, 650, "S"))
                    
                queue_append(partial(place_banana, 1023, 678, "E"))
                queue_append(partial(place_banana, 1023, 745, "E"))
                queue_append(partial(place_banana, 1023, 806, "E"))
                
                for x in range(990, 1010, 10):
                    queue_append(partial(place_banana, x, 830, "N"))
                
                queue_append(partial(place_banana, 828, 815, "N"))
                
                for x in range(740, 770, 15):
                    queue_append(partial(place_banana, x, 815, "N"))
                    
                for x in range(785, 815, 15):
                    queue_append(partial(place_banana, x, 815, "N"))
                    
                for x in range(660, 720, 20):
                    queue_append(partial(place_banana, x, 815, "N"))
                    
                for x in range(580, 645, 15):
                    queue_append(partial(place_banana, x, 815, "N"))
                    
                queue_append(partial(place_banana, 550, 815, "N"))
                queue_append(partial(place_banana, 450, 815, "N"))
                queue_append(partial(place_banana, 354, 796, "W"))
                queue_append(partial(place_banana, 354, 765, "W"))
                queue_append(partial(place_banana, 354, 694, "W"))
                
                for x in range(365, 430, 15):
                    queue_append(partial(place_banana, x, 649, "N"))
                    
            case "Penguin Palace":
                for x in range(2160, 2195, 15):
                    queue_append(partial(place_banana, x, 3766, "S"))
                    
                queue_append(partial(place_banana, 2314, 3865, "E"))
                queue_append(partial(place_banana, 2284, 3964, "N"))
                queue_append(partial(place_banana, 2118, 3955, "N"))
                queue_append(partial(place_banana, 2052, 3954, "N"))
                queue_append(partial(place_banana, 2033, 3865, "W"))
            
    if global_vars.HOST_ID in team_spec:
        add_commands(f"kill {global_vars.HOST_ID}", f"ghost {global_vars.HOST_ID}")
    
    queue_append(lambda: teleport_players(715, 1310, team_a))
    queue_append(lambda: teleport_players(3855, 1535, team_b))
    
    wait_time()
    add_commands("god all")

    match global_vars.SELECTED_MAP_DUELS:
        case "Bamboo Resort":   
            queue_append(lambda: teleport_players(2430, 1830, team_a))
            queue_append(lambda: teleport_players(2725, 1830, team_b))
        case "SAW Security":
            queue_append(lambda: teleport_players(3335, 1910, team_a))
            queue_append(lambda: teleport_players(3520, 1910, team_b))
        case "SAW Research Labs":
            queue_append(lambda: teleport_players(2600, 2985, team_a))
            queue_append(lambda: teleport_players(2900, 2985, team_b))
        case "Welcome Center":
            queue_append(lambda: teleport_players(510, 735, team_a))
            queue_append(lambda: teleport_players(865, 735, team_b))
        case "Penguin Palace":
            queue_append(lambda: teleport_players(2052, 3886, team_a))
            queue_append(lambda: teleport_players(2295, 3886, team_b))
            
    add_commands("yell Fight!")
    
    execute_queue()
    
# Dodgeball
def mouse_click(x: int, y: int) -> None:
    pyautogui.moveTo(x, y)
    time.sleep(global_vars.KEY_DELAY*8)
    pyautogui.click()
    time.sleep(global_vars.KEY_DELAY*4)

def spawn_nade(x: int, y: int) -> None:
    add_commands(f"tele {global_vars.HOST_ID} {x} {y}")
    queue_append(lambda: time.sleep(0.2))
    add_commands("nade")

def spawn_zips(x: int, y: int, amount: int) -> None:
    add_commands(f"tele {global_vars.HOST_ID} {x} {y}")
    queue_append(lambda: press_hotkey(global_vars.USE_BIND))
    queue_append(lambda: time.sleep(8))
    add_commands(f"zip {amount}")
    queue_append(lambda: time.sleep(2))
    queue_append(lambda: press_hotkey(global_vars.THROWABLE_BIND))

def lay_zip(sar_handle, x_player: int, y_player: int, x_mouse: int, y_mouse: int) -> None:
        sar_window_rect = sar_handle.getClientFrame()
        window_top_left_x, window_top_left_y = sar_window_rect[0], sar_window_rect[1]
        window_width: int = sar_window_rect[2] - window_top_left_x
        
        size_ratio: float = window_width / 1920
        if size_ratio != 1:
            x_mouse = int(x_mouse * size_ratio)
            y_mouse = int(y_mouse * size_ratio)
        
        click_x: int = window_top_left_x + x_mouse
        click_y: int = window_top_left_y + y_mouse
        
        sar_handle.activate()
        time.sleep(global_vars.KEY_DELAY*16)
        send_commands(f"tele {global_vars.HOST_ID} {x_player} {y_player}")
        press_hotkey(global_vars.THROWABLE_BIND)
        mouse_click(click_x, click_y)

def break_boxes(sar_handle, x_player: int, y_player: int, x_mouse: int, y_mouse: int) -> None:
        sar_window_rect = sar_handle.getClientFrame()
        window_top_left_x, window_top_left_y = sar_window_rect[0], sar_window_rect[1]
        window_width: int = sar_window_rect[2] - window_top_left_x
        
        size_ratio: float = window_width / 1920
        if size_ratio != 1:
            x_mouse = int(x_mouse * size_ratio)
            y_mouse = int(y_mouse * size_ratio)
        
        click_x: int = window_top_left_x + x_mouse
        click_y: int = window_top_left_y + y_mouse
        
        sar_handle.activate()
        time.sleep(global_vars.KEY_DELAY*16)
        send_commands(f"tele {global_vars.HOST_ID} {x_player} {y_player}")
        press_hotkey(global_vars.MELEE_BIND)
        mouse_click(click_x, click_y)

def teleport_host(x: int, y: int, zip_amount: int = 0) -> None:
    send_commands(f"tele {global_vars.HOST_ID} {x} {y}")
    time.sleep(1)
    send_commands("gun13 2")
    if zip_amount != 0:
        send_commands(f"zip {zip_amount}")

def start_dodgeball() -> None:
    sar_handle = open_window("Super Animal Royale")
    lay_zip_prep = partial(lay_zip, sar_handle)
    break_boxes_prep = partial(break_boxes, sar_handle)
    if not sar_handle:
        return
    
    team_a, team_b, team_spec = get_teams()
    
    try:
        team_a.remove(global_vars.HOST_ID)
    except ValueError:
        pass
    
    try:
        team_b.remove(global_vars.HOST_ID)
    except ValueError:
        pass
    
    queue_append(lambda: time.sleep(0.2))
    add_commands(
        "allitems", "emus", "hamballs", "gasoff", "ziplines",
        f"dmg {global_vars.DODGEBALL_SETTINGS["damage"]}", "startp", "god all",
        "yell Welcome to dodgeball!",
        "yell Remember to stay in the arena and don't hit players with",
        "yell anything other than grenades or you will be disqualified",
        "yell Please jump out of the eagle as soon as possible",
        "yell And of course good luck have fun gamers!",
        f"yell Selected map: {global_vars.SELECTED_MAP_DODGEBALL}"
    )
    
    queue_append(lambda: ghost_spectators(team_spec))
    queue_append(lambda: time.sleep(20))
    queue_append(lambda: open_window("Super Animal Royale"))
    queue_append(lambda: time.sleep(1))
    queue_append(lambda: press_hotkey(global_vars.USE_BIND))
    queue_append(lambda: time.sleep(1))
    
    match global_vars.SELECTED_MAP_DODGEBALL:
        case "Bamboo Resort":
            spawn_zips(2575, 2047, 4)
            spawn_nade(2575, 2138)
            spawn_nade(2575, 2130)
            spawn_nade(2575, 2122)
            spawn_nade(2575, 2114)
            spawn_nade(2575, 2210)
            spawn_nade(2575, 2218)
            spawn_nade(2575, 2224)
            spawn_nade(2575, 2228)
            queue_append(lambda: lay_zip_prep(2575, 2235, 960, 750))
            queue_append(lambda: lay_zip_prep(2575, 2090, 960, 220))
            queue_append(lambda: lay_zip_prep(2512, 2149, 950, 320))
            queue_append(lambda: lay_zip_prep(2639, 2149, 950, 320))
            queue_append(lambda: teleport_host(2574, 2037, 4))
            queue_append(lambda: teleport_players(2513, 2165, team_a))
            queue_append(lambda: teleport_players(2637, 2165, team_b))
        case "SAW Security":
            spawn_zips(3430, 1815, 3)
            
            add_commands(f"tele {global_vars.HOST_ID} 3350 1816")
            queue_append(lambda: time.sleep(2))
            queue_append(lambda: press_hotkey(global_vars.USE_BIND))
            queue_append(lambda: time.sleep(2))
            
            spawn_nade(3430, 1877)
            spawn_nade(3430, 1885)
            spawn_nade(3430, 1951)
            spawn_nade(3430, 1892)
            spawn_nade(3430, 1899)
            spawn_nade(3430, 1906)
            spawn_nade(3430, 1913)
            spawn_nade(3430, 1920)
            queue_append(lambda: lay_zip_prep(3430, 1865, 960, 150))
            queue_append(lambda: lay_zip_prep(3430, 1965, 960, 670))
            queue_append(lambda: teleport_host(3430, 1839))
            queue_append(lambda: teleport_players(3358, 1910, team_a))
            queue_append(lambda: teleport_players(3500, 1910, team_b))
        case "SAW Research Labs":
            spawn_zips(2757, 3200, 4)
            spawn_nade(2757, 2951)
            spawn_nade(2757, 2974)
            spawn_nade(2757, 2982)
            spawn_nade(2757, 2990)
            spawn_nade(2757, 2998)
            spawn_nade(2757, 3020)
            spawn_nade(2757, 3025)
            queue_append(lambda: lay_zip_prep(2757, 3038, 1400, 534))
            queue_append(lambda: lay_zip_prep(2757, 3038, 500, 534))
            queue_append(lambda: lay_zip_prep(2757, 2937, 500, 534))
            queue_append(lambda: lay_zip_prep(2757, 2937, 1400, 534))
            queue_append(lambda: teleport_host(2757, 2890))
            queue_append(lambda: teleport_players(2695, 2989, team_a))
            queue_append(lambda: teleport_players(2816, 2989, team_b))
        case "Welcome Center":
            spawn_zips(512, 404, 4)
            spawn_nade(555, 541)
            spawn_nade(555, 549)
            spawn_nade(555, 557)
            spawn_nade(555, 564)
            spawn_nade(555, 583)
            spawn_nade(555, 591)
            spawn_nade(555, 599)
            spawn_nade(555, 622)
            spawn_nade(555, 628)
            queue_append(lambda: lay_zip_prep(555, 538, 954, 360))
            queue_append(lambda: lay_zip_prep(555, 580, 954, 360))
            queue_append(lambda: lay_zip_prep(549, 619, 1034, 460))
            queue_append(lambda: lay_zip_prep(515, 527, 1197, 544))
            queue_append(lambda: teleport_host(512, 404, 2))
            queue_append(lambda: teleport_players(489, 588, team_a))
            queue_append(lambda: teleport_players(617, 588, team_b))
        case "Penguin Palace":
            spawn_zips(2174, 3690, 4)
            spawn_nade(2175, 3822)
            spawn_nade(2175, 3848)
            spawn_nade(2175, 3856)
            spawn_nade(2175, 3864)
            spawn_nade(2175, 3870)
            spawn_nade(2175, 3905)
            spawn_nade(2175, 3913)
            spawn_nade(2175, 3921)
            queue_append(lambda: lay_zip_prep(2166, 3818, 1060, 480))
            queue_append(lambda: lay_zip_prep(2174, 3846, 965, 380))
            queue_append(lambda: lay_zip_prep(2174, 3904, 961, 420))
            queue_append(lambda: teleport_host(2174, 3690))
            queue_append(lambda: teleport_players(2096, 3883, team_a))
            queue_append(lambda: teleport_players(2250, 3883, team_b))
        case "Pyramid":
            spawn_zips(1405, 2692, 2)
            spawn_nade(1405, 2792)
            spawn_nade(1405, 2798)
            spawn_nade(1405, 2802)
            spawn_nade(1405, 2810)
            spawn_nade(1405, 2816)
            spawn_nade(1405, 2822)
            spawn_nade(1405, 2827)
            queue_append(lambda: lay_zip_prep(1403, 2791, 963, 290))
            queue_append(lambda: lay_zip_prep(1479, 2806, 967, 410))
            queue_append(lambda: teleport_host(1403, 2692))
            queue_append(lambda: teleport_players(1343, 2819, team_a))
            queue_append(lambda: teleport_players(1471, 2819, team_b))
        case "Emu Ranch":
            spawn_zips(1900, 2530, 4)
            spawn_nade(1893, 2557)
            spawn_nade(1893, 2561)
            spawn_nade(1893, 2564)
            spawn_nade(1893, 2571)
            spawn_nade(1893, 2590)
            spawn_nade(1893, 2596)
            queue_append(lambda: break_boxes_prep(1891, 2574, 1050, 343))
            queue_append(lambda: lay_zip_prep(1893, 2552, 957, 220))
            queue_append(lambda: lay_zip_prep(1881, 2546, 1340, 535))
            queue_append(lambda: lay_zip_prep(1825, 2570, 954, 430))
            queue_append(lambda: lay_zip_prep(1960, 2566, 952, 390))
            queue_append(lambda: teleport_host(1900, 2530))
            queue_append(lambda: teleport_players(1838, 2580, team_a))
            queue_append(lambda: teleport_players(1952, 2580, team_b))
        case "Shooting Range":
            spawn_zips(930, 1016, 4)
            spawn_nade(930, 1073)
            spawn_nade(930, 1081)
            spawn_nade(930, 1089)
            spawn_nade(930, 1096)
            spawn_nade(930, 1124)
            spawn_nade(930, 1128)
            queue_append(lambda: lay_zip_prep(930, 1064, 954, 330))
            queue_append(lambda: lay_zip_prep(848, 1064, 954, 330))
            queue_append(lambda: lay_zip_prep(1009, 1064, 954, 330))
            queue_append(lambda: lay_zip_prep(938, 1119, 827, 480))
            queue_append(lambda: teleport_host(930, 1016))
            queue_append(lambda: teleport_players(859, 1090, team_a))
            queue_append(lambda: teleport_players(1002, 1090, team_b))
        case "Juice Factory":
            spawn_zips(3433, 2655, 4)
            queue_append(lambda: break_boxes_prep(3428, 2744, 1050, 343))
            queue_append(lambda: break_boxes_prep(3450, 2740, 1050, 343))
            queue_append(lambda: break_boxes_prep(3427, 2723, 1050, 343))
            spawn_nade(3412, 2751)
            spawn_nade(3428, 2751)
            spawn_nade(3436, 2751)
            spawn_nade(3454, 2751)
            queue_append(lambda: lay_zip_prep(3372, 2711, 965, 100))
            queue_append(lambda: lay_zip_prep(3369, 2751, 1145, 539))
            queue_append(lambda: lay_zip_prep(3413, 2751, 1255, 539))
            queue_append(lambda: lay_zip_prep(3472, 2751, 1145   , 539))
            queue_append(lambda: teleport_host(3433, 2665))
            queue_append(lambda: teleport_players(3433, 2701, team_a))
            queue_append(lambda: teleport_players(3433, 2799, team_b))
        case "Super Sea Land":
            spawn_zips(4028, 606, 4)
            spawn_nade(4140, 570)
            spawn_nade(4140, 588)
            spawn_nade(4140, 596)
            spawn_nade(4140, 618)
            spawn_nade(4140, 626)
            spawn_nade(4140, 634)
            queue_append(lambda: break_boxes_prep(4130, 573, 1050, 343))
            queue_append(lambda: lay_zip_prep(4142, 556, 948, 270))
            queue_append(lambda: lay_zip_prep(4142, 616, 948, 140))
            queue_append(lambda: lay_zip_prep(4090, 596, 950, 400))
            queue_append(lambda: lay_zip_prep(4193, 596, 950, 400))
            queue_append(lambda: teleport_host(4028, 606))
            queue_append(lambda: teleport_players(4090, 607, team_a))
            queue_append(lambda: teleport_players(4193, 607, team_b))
    
    add_commands("god all")
    
    execute_queue()
    update_hotkeys()
    
# Keybinds
def spawn_nade_setup(x: int, y: int) -> None:
    if not global_vars.DODGEBALL_SETTINGS["hotkeys"]:
        return
    
    if pywinctl.getActiveWindowTitle() == "Super Animal Royale":
        send_commands(f"tele {global_vars.HOST_ID} {x} {y}")
        time.sleep(0.5)
        send_commands("nade")
        
def hr_and_zip_hotkey() -> None:
    if not global_vars.DODGEBALL_SETTINGS["hotkeys"]:
        return
    
    if pywinctl.getActiveWindowTitle() == "Super Animal Royale":
        time.sleep(0.5)
        send_commands("gun13 2", "zip 4")
    
def ghost_host_hotkey() -> None:
    if not global_vars.DODGEBALL_SETTINGS["hotkeys"]:
        return
    
    if pywinctl.getActiveWindowTitle() == "Super Animal Royale":
        time.sleep(0.5)
        send_commands(f"kill {global_vars.HOST_ID}", f"ghost {global_vars.HOST_ID}")

def spawn_grenade_hotkey() -> None:
    if not global_vars.DODGEBALL_SETTINGS["hotkeys"]:
        return
    
    if pywinctl.getActiveWindowTitle() == "Super Animal Royale":
        send_commands("nade")

def spawn_grenades_random(x_start: int, x_end: int, y_start: int, y_end: int, amount: int) -> None:
    for _ in range(amount):
        x: int = random.randint(x_start, x_end)
        y: int = random.randint(y_start, y_end)
        spawn_nade_setup(x, y)

def spawn_grenades_preset(x: int, y: int, offset: int, offset_direction: Literal["x", "y"], amount: int) -> None:
    for _ in range(amount):
        spawn_nade_setup(x, y)
        if offset_direction == "x":
            x += offset
        elif offset_direction == "y":
            y += offset
        else:
            raise ValueError("Invalid offset_direction, use 'x' or 'y'")

def spawn_grenades_from_left_hotkey(amount: int) -> None:
    if not global_vars.DODGEBALL_SETTINGS["hotkeys"]:
        return
    
    if pywinctl.getActiveWindowTitle() != "Super Animal Royale":
        return
    
    time.sleep(0.5)
    match global_vars.SELECTED_MAP_DODGEBALL:
        case "Bamboo Resort":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(2519, 2560, 2126, 2207, amount)
                spawn_grenades_random(2590, 2622, 2126, 2207, amount)
            else:
                spawn_grenades_preset(2539, 2147, 20, "y", amount)
                spawn_grenades_preset(2618, 2147, 20, "y", amount)
        case "SAW Security":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(3358, 3397, 1872, 1951, amount)
                spawn_grenades_random(3461, 3500, 1872, 1951, amount)
            else:
                spawn_grenades_preset(3380, 1893, 20, "y", amount)
                spawn_grenades_preset(3479, 1893, 20, "y", amount)
        case "SAW Research Labs":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(2697, 2752, 2944, 3028, amount)
                spawn_grenades_random(2762, 2817, 2944, 3028, amount)
            else:
                spawn_grenades_preset(2719, 2965, 25, "y", amount)
                spawn_grenades_preset(2793, 2965, 25, "y", amount)
        case "Welcome Center":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(488, 548, 540, 630, amount)
                spawn_grenades_random(563, 609, 540, 630, amount)
            else:
                spawn_grenades_preset(523, 549, 40, "y", amount)
                spawn_grenades_preset(592, 549, 40, "y", amount)
        case "Penguin Palace":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(2111, 2167, 3848, 3923, amount)
                spawn_grenades_random(2179, 2239, 3848, 3923, amount)
            else:
                spawn_grenades_preset(2133, 3860, 24, "y", amount)
                spawn_grenades_preset(2216, 3860, 24, "y", amount)
        case "Pyramid":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(1339, 1396, 2792, 2828, amount)
                spawn_grenades_random(1410, 1471, 2792, 2828, amount)
            else:
                spawn_grenades_preset(1365, 2796, 18, "y", amount)
                spawn_grenades_preset(1441, 2796, 18, "y", amount)
        case "Emu Ranch":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(1835, 1887, 2572, 2599, amount)
                spawn_grenades_random(1898, 1953, 2572, 2599, amount)
            else:
                spawn_grenades_preset(1862, 2568, 15, "y", amount)
                spawn_grenades_preset(1930, 2568, 15, "y", amount)
        case "Shooting Range":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(862, 918, 1071, 1123, amount)
                spawn_grenades_random(944, 999, 1071, 1123, amount)
            else:
                spawn_grenades_preset(890, 1080, 12, "y", amount)
                spawn_grenades_preset(972, 1080, 12, "y", amount)
        case "Juice Factory":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(3376, 3497, 2707, 2746, amount)
                spawn_grenades_random(3376, 3497, 2762, 2800, amount)
            else:
                spawn_grenades_preset(3411, 2711, 22, "x", amount)
                spawn_grenades_preset(3411, 2797, 22, "x", amount)
        case "Super Sea Land":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(4100, 4136, 570, 636, amount)
                spawn_grenades_random(4148, 4182, 570, 636, amount)
            else:
                spawn_grenades_preset(4114, 591, 15, "y", amount)
                spawn_grenades_preset(4161, 591, 15, "y", amount)
    
def spawn_grenades_from_right_hotkey(amount: int) -> None:
    if not global_vars.DODGEBALL_SETTINGS["hotkeys"]:
        return
    
    if pywinctl.getActiveWindowTitle() != "Super Animal Royale":
        return
    
    time.sleep(0.5)
    match global_vars.SELECTED_MAP_DODGEBALL:
        case "Bamboo Resort":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(2590, 2622, 2126, 2207, amount)
                spawn_grenades_random(2519, 2560, 2126, 2207, amount)
            else:
                spawn_grenades_preset(2618, 2147, 20, "y", amount)
                spawn_grenades_preset(2539, 2147, 20, "y", amount)
        case "SAW Security":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(3461, 3500, 1872, 1951, amount)
                spawn_grenades_random(3358, 3397, 1872, 1951, amount)
            else:
                spawn_grenades_preset(3479, 1893, 20, "y", amount)
                spawn_grenades_preset(3380, 1893, 20, "y", amount)
        case "SAW Research Labs":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(2762, 2817, 2944, 3028, amount)
                spawn_grenades_random(2697, 2752, 2944, 3028, amount)
            else:
                spawn_grenades_preset(2793, 2965, 25, "y", amount)
                spawn_grenades_preset(2719, 2965, 25, "y", amount)
        case "Welcome Center":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(563, 609, 540, 630, amount)
                spawn_grenades_random(488, 548, 540, 630, amount)
            else:
                spawn_grenades_preset(592, 549, 40, "y", amount)
                spawn_grenades_preset(523, 549, 40, "y", amount)
        case "Penguin Palace":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(2179, 2239, 3848, 3923, amount)
                spawn_grenades_random(2111, 2167, 3848, 3923, amount)
            else:
                spawn_grenades_preset(2216, 3860, 24, "y", amount)
                spawn_grenades_preset(2133, 3860, 24, "y", amount)
        case "Pyramid":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(1410, 1471, 2792, 2828, amount)
                spawn_grenades_random(1339, 1396, 2792, 2828, amount)
            else:
                spawn_grenades_preset(1441, 2796, 18, "y", amount)
                spawn_grenades_preset(1365, 2796, 18, "y", amount)
        case "Emu Ranch":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(1898, 1953, 2572, 2599, amount)
                spawn_grenades_random(1835, 1887, 2572, 2599, amount)
            else:
                spawn_grenades_preset(1930, 2568, 15, "y", amount)
                spawn_grenades_preset(1862, 2568, 15, "y", amount)
        case "Shooting Range":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(944, 999, 1071, 1123, amount)
                spawn_grenades_random(862, 918, 1071, 1123, amount)
            else:
                spawn_grenades_preset(972, 1080, 12, "y", amount)
                spawn_grenades_preset(890, 1080, 12, "y", amount)
        case "Juice Factory":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(3376, 3497, 2762, 2800, amount)
                spawn_grenades_random(3376, 3497, 2707, 2746, amount)
            else:
                spawn_grenades_preset(3411, 2797, 22, "x", amount)
                spawn_grenades_preset(3411, 2711, 22, "x", amount)
        case "Super Sea Land":
            if global_vars.DODGEBALL_SETTINGS["random_nades"]:
                spawn_grenades_random(4148, 4182, 570, 636, amount)
                spawn_grenades_random(4100, 4136, 570, 636, amount)
            else:
                spawn_grenades_preset(4161, 591, 15, "y", amount)
                spawn_grenades_preset(4114, 591, 15, "y", amount)

keyboard.add_hotkey("ctrl+alt+q", clear_queue)

def update_hotkeys() -> None:
    keyboard.unhook_all_hotkeys()
    keyboard.add_hotkey(global_vars.SETTINGS.value("Keybinds/SpawnHrAndZiplines", "Ctrl+Shift+S"), hr_and_zip_hotkey)
    keyboard.add_hotkey(global_vars.SETTINGS.value("Keybinds/GhostHost", "Ctrl+Shift+K"), ghost_host_hotkey)
    keyboard.add_hotkey(global_vars.SETTINGS.value("Keybinds/SpawnSingleNade", "Ctrl+Y"), spawn_grenade_hotkey)
    keyboard.add_hotkey(global_vars.SETTINGS.value("Keybinds/SpawnOneNadeLeft", "Ctrl+1"), spawn_grenades_from_left_hotkey, args=(1,))
    keyboard.add_hotkey(global_vars.SETTINGS.value("Keybinds/SpawnTwoNadesLeft", "Ctrl+2"), spawn_grenades_from_left_hotkey, args=(2,))
    keyboard.add_hotkey(global_vars.SETTINGS.value("Keybinds/SpawnThreeNadesLeft", "Ctrl+3"), spawn_grenades_from_left_hotkey, args=(3,))
    keyboard.add_hotkey(global_vars.SETTINGS.value("Keybinds/SpawnOneNadeRight", "Alt+1"), spawn_grenades_from_right_hotkey, args=(1,))
    keyboard.add_hotkey(global_vars.SETTINGS.value("Keybinds/SpawnTwoNadesRight", "Alt+2"), spawn_grenades_from_right_hotkey, args=(2,))
    keyboard.add_hotkey(global_vars.SETTINGS.value("Keybinds/SpawnThreeNadesRight", "Alt+3"), spawn_grenades_from_right_hotkey, args=(3,))
    keyboard.add_hotkey("ctrl+alt+q", clear_queue)
    