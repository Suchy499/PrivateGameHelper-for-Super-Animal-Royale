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
from functools import partial
from typing import Literal, Callable
    
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

# Queue
def send_commands(*commands: str, delay: int = 1):
    for command in commands:
        time.sleep(global_vars.KEY_DELAY*delay)
        pyperclip.copy(f"/{command}")
        keyboard.send("enter")
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

def spawn_weapon(x: int, y: int, weapon_id: int, players: int) -> None:
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
                call = partial(spawn_weapon, x_a, y_a, weapon_id, players)
                queue_append(call)
                x_a += 10
                if i == 9:
                    x_a = 735
                    y_a -= 20
        case "b":
            x_b: int = 3875
            y_b: int = 1515
            for i, weapon_id in enumerate(weapons_list):
                call = partial(spawn_weapon, x_b, y_b, weapon_id, players)
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
    send_commands("yell 30 Seconds")
    time.sleep(20)
    open_window("Super Animal Royale")
    send_commands("yell 10")
    time.sleep(7)
    open_window("Super Animal Royale")
    send_commands("yell 3")
    time.sleep(1)
    send_commands("yell 2")
    time.sleep(1)
    send_commands("yell 1")
    time.sleep(1)
    
def start_duel() -> None:
    if not open_window("Super Animal Royale"):
        return
    
    team_a, team_b, team_spec = get_teams()
    team_a_len, team_b_len = len(team_a), len(team_b)
    if team_a_len > 4:
        team_a_len = 4

    if team_b_len > 4:
        team_b_len = 4
    
    add_commands("allitems", "emus", "hamballs", "gasoff")
    
    if global_vars.DUELS_SETTINGS["no_pets"]:
        add_commands("pets")
    
    if global_vars.DUELS_SETTINGS["onehits"]:
        add_commands("onehits")
    
    if global_vars.DUELS_SETTINGS["noroll"]:
        add_commands("noroll")
        
    add_commands("startp", "god all")
    add_commands(
        "yell Welcome to duels!",
        "yell Please jump out of the eagle as soon as possible",
        "yell So you can be teleported to weapon selection",
        f"yell Selected map: {global_vars.SELECTED_MAP_DUELS}"
    )
    queue_append(lambda: ghost_spectators(team_spec))
    
    queue_append(lambda: time.sleep(25))
    queue_append(lambda: open_window("Super Animal Royale"))
    queue_append(lambda: keyboard.send("e"))
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
    
    if global_vars.HOST_ID in team_spec:
        add_commands(f"kill {global_vars.HOST_ID}", f"ghost {global_vars.HOST_ID}")
    
    queue_append(lambda: teleport_players(715, 1310, team_a))
    queue_append(lambda: teleport_players(3855, 1535, team_b))
    
    queue_append(wait_time)
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
        
# Keybinds
keyboard.add_hotkey("ctrl+alt+q", clear_queue)