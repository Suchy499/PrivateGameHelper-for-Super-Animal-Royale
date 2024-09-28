import customtkinter
import keyboard
import re
import time
import pywinctl
import random
import pyperclip
from typing import Literal
from CTkMessagebox import CTkMessagebox
from functions import *
from widgets import *

class Dodgeball(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("600x630")
        self.title("Private Game Helper - Dodgeball")
        self.resizable(False, False)
        
        Text(self, text="Dodgeball", font="title", place=(20, 20))
        
        # Settings
        Text(self, text="Map:", place=(20, 60))
        self.map_select = OptionMenu(self, width=175, values=["Bamboo Resort", "SAW Security Grass", "SAW Research Labs", "Super Welcome Center", "Penguin Palace", "Pyramid", "Emu Ranch", "Shooting Range", "Juice Factory", "Super Sea Land"], place=(20, 90))
        Text(self, text="Host ID:", place=(20, 140))
        self.host_id_entry = Entry(self, width=175, placeholder_text="e.g. 1", place=(20, 170))
        Text(self, text="Team A IDs (separated by spaces):", place=(300, 60))
        self.team_a_entry = Entry(self, width=175, placeholder_text="e.g. 2 4 5 8", place=(300, 90))
        Text(self, text="Team B IDs (separated by spaces):", place=(300, 140))
        self.team_b_entry = Entry(self, width=175, placeholder_text="e.g. 3 6 7 9", place=(300, 170))
        self.random_nades_switch = Switch(self, text="Random Nades", place=(20, 220))
        self.disable_hotkeys_switch = Switch(self, text="Disable Hotkeys", command=self.disable_hotkeys, place=(300, 220))
        self.damage_slider = SliderFrame(self, element="damage", place=(20, 270))
        self.random_teams_switch = Switch(self, text="Random Teams", command=self.enable_random_teams, place=(300, 270))
        
        # Hotkeys
        Text(self, text="Hotkeys", font="title", place=(20, 340))
        Text(self, text="(Ctrl + Shift + S)", font="italic", place=(20, 390))
        Text(self, text="Spawn hunting rifle and ziplines", place=(300, 390))
        keyboard.add_hotkey("ctrl+shift+s", self.hr_and_zip_hotkey)
        Text(self, text="(Ctrl + Shift + K)", font="italic", place=(20,420))
        Text(self, text="Kill and ghost host", place=(300, 420))
        keyboard.add_hotkey("ctrl+shift+k", self.kill_host_hotkey)
        Text(self, text="(Alt + Y)", font="italic", place=(20, 450))
        Text(self, text="Spawn a grenade", place=(300, 450))
        keyboard.add_hotkey("alt+y", self.spawn_grenade_hotkey)
        Text(self, text="(Left + [1-3])", font="italic", place=(20, 480))
        Text(self, text="Spawn [1-3] grenades\nstarting from the left", place=(300, 480))
        keyboard.add_hotkey("left+1", self.spawn_grenades_from_left_hotkey, args=(1,))
        keyboard.add_hotkey("left+2", self.spawn_grenades_from_left_hotkey, args=(2,))
        keyboard.add_hotkey("left+3", self.spawn_grenades_from_left_hotkey, args=(3,))
        Text(self, text="(Right + [1-3])", font="italic", place=(20, 530))
        Text(self, text="Spawn [1-3] grenades\nstarting from the right", place=(300, 530))
        keyboard.add_hotkey("right+1", self.spawn_grenades_from_right_hotkey, args=(1,))
        keyboard.add_hotkey("right+2", self.spawn_grenades_from_right_hotkey, args=(2,))
        keyboard.add_hotkey("right+3", self.spawn_grenades_from_right_hotkey, args=(3,))
        
        # Start
        Button(self, text="Start Match", command=self.start_match, place=(20, 585))
        
        Settings.update(self=Settings)
    
    def enable_random_teams(self) -> None:
        if self.random_teams_switch.get() == 1:
            self.team_a_entry.configure(state="disable")
            self.team_b_entry.configure(state="disable")
        else:
            self.team_a_entry.configure(state="normal")
            self.team_b_entry.configure(state="normal")
    
    def get_teams(self) -> tuple[list[str], list[str]] | None:
        if self.random_teams_switch.get() == 1:
            if open_window("Super Animal Royale") is False:
                return

            send_commands("getplayers")
            time.sleep(KEY_DELAY*16)
            clipboard: list[str] = pyperclip.paste().split("\n")
            clipboard.remove("")
            player_list: list[str] = []
            team_a: list[str] = []
            team_b: list[str] = []
            for player in clipboard:
                player_id = player.split("\t")[0]
                if player_id not in("pID", self.host_id_entry.get()):
                    player_list.append(player_id)
            random.shuffle(player_list)
            for index, player in enumerate(player_list):
                if index % 2 == 0:
                    team_a.append(player)
                else:
                    team_b.append(player)
        else:
            team_a: list[str] = self.team_a_entry.get().strip().split(sep=" ")
            team_b: list[str] = self.team_b_entry.get().strip().split(sep=" ")
        return team_a, team_b
    
    # Hotkeys
    def hr_and_zip_hotkey(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands("gun13 2", "zip 4")
    
    def kill_host_hotkey(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"kill {self.host_id_entry.get()}", f"ghost {self.host_id_entry.get()}")
    
    def spawn_grenade_hotkey(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands("nade")
    
    def spawn_grenades_random(self, x_start: int, x_end: int, y_start: int, y_end: int, amount: int) -> None:
        for _ in range(amount):
            x: int = random.randint(x_start, x_end)
            y: int = random.randint(y_start, y_end)
            self.spawn_nade(x, y)
    
    def spawn_grenades_preset(self, x: int, y: int, offset: int, offset_direction: Literal["x", "y"], amount: int) -> None:
        for _ in range(amount):
            self.spawn_nade(x, y)
            if offset_direction == "x":
                x += offset
            elif offset_direction == "y":
                y += offset
            else:
                raise ValueError("Invalid offset_direction, use 'x' or 'y'")
    
    def spawn_grenades_from_left_hotkey(self, amount: int) -> None:
        match self.map_select.get():
            case "Bamboo Resort":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(2519, 2560, 2126, 2207, amount)
                    self.spawn_grenades_random(2590, 2622, 2126, 2207, amount)
                else:
                    self.spawn_grenades_preset(2539, 2147, 20, "y", amount)
                    self.spawn_grenades_preset(2618, 2147, 20, "y", amount)
            case "SAW Security Grass":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(3358, 3397, 1872, 1951, amount)
                    self.spawn_grenades_random(3461, 3500, 1872, 1951, amount)
                else:
                    self.spawn_grenades_preset(3380, 1893, 20, "y", amount)
                    self.spawn_grenades_preset(3479, 1893, 20, "y", amount)
            case "SAW Research Labs":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(2697, 2752, 2944, 3028, amount)
                    self.spawn_grenades_random(2762, 2817, 2944, 3028, amount)
                else:
                    self.spawn_grenades_preset(2719, 2965, 25, "y", amount)
                    self.spawn_grenades_preset(2793, 2965, 25, "y", amount)
            case "Super Welcome Center":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(488, 548, 540, 630, amount)
                    self.spawn_grenades_random(563, 609, 540, 630, amount)
                else:
                    self.spawn_grenades_preset(523, 549, 40, "y", amount)
                    self.spawn_grenades_preset(592, 549, 40, "y", amount)
            case "Penguin Palace":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(2111, 2167, 3848, 3923, amount)
                    self.spawn_grenades_random(2179, 2239, 3848, 3923, amount)
                else:
                    self.spawn_grenades_preset(2133, 3860, 24, "y", amount)
                    self.spawn_grenades_preset(2216, 3860, 24, "y", amount)
            case "Pyramid":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(1339, 1396, 2792, 2828, amount)
                    self.spawn_grenades_random(1410, 1471, 2792, 2828, amount)
                else:
                    self.spawn_grenades_preset(1365, 2796, 18, "y", amount)
                    self.spawn_grenades_preset(1441, 2796, 18, "y", amount)
            case "Emu Ranch":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(1835, 1887, 2572, 2599, amount)
                    self.spawn_grenades_random(1898, 1953, 2572, 2599, amount)
                else:
                    self.spawn_grenades_preset(1862, 2568, 15, "y", amount)
                    self.spawn_grenades_preset(1930, 2568, 15, "y", amount)
            case "Shooting Range":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(862, 918, 1071, 1123, amount)
                    self.spawn_grenades_random(944, 999, 1071, 1123, amount)
                else:
                    self.spawn_grenades_preset(890, 1080, 12, "y", amount)
                    self.spawn_grenades_preset(972, 1080, 12, "y", amount)
            case "Juice Factory":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(3376, 3497, 2707, 2746, amount)
                    self.spawn_grenades_random(3376, 3497, 2762, 2800, amount)
                else:
                    self.spawn_grenades_preset(3411, 2711, 22, "x", amount)
                    self.spawn_grenades_preset(3411, 2797, 22, "x", amount)
            case "Super Sea Land":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(4100, 4136, 570, 636, amount)
                    self.spawn_grenades_random(4148, 4182, 570, 636, amount)
                else:
                    self.spawn_grenades_preset(4114, 591, 15, "y", amount)
                    self.spawn_grenades_preset(4161, 591, 15, "y", amount)
        
    def spawn_grenades_from_right_hotkey(self, amount: int) -> None:
        match self.map_select.get():
            case "Bamboo Resort":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(2590, 2622, 2126, 2207, amount)
                    self.spawn_grenades_random(2519, 2560, 2126, 2207, amount)
                else:
                    self.spawn_grenades_preset(2618, 2147, 20, "y", amount)
                    self.spawn_grenades_preset(2539, 2147, 20, "y", amount)
            case "SAW Security Grass":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(3461, 3500, 1872, 1951, amount)
                    self.spawn_grenades_random(3358, 3397, 1872, 1951, amount)
                else:
                    self.spawn_grenades_preset(3479, 1893, 20, "y", amount)
                    self.spawn_grenades_preset(3380, 1893, 20, "y", amount)
            case "SAW Research Labs":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(2762, 2817, 2944, 3028, amount)
                    self.spawn_grenades_random(2697, 2752, 2944, 3028, amount)
                else:
                    self.spawn_grenades_preset(2793, 2965, 25, "y", amount)
                    self.spawn_grenades_preset(2719, 2965, 25, "y", amount)
            case "Super Welcome Center":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(563, 609, 540, 630, amount)
                    self.spawn_grenades_random(488, 548, 540, 630, amount)
                else:
                    self.spawn_grenades_preset(592, 549, 40, "y", amount)
                    self.spawn_grenades_preset(523, 549, 40, "y", amount)
            case "Penguin Palace":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(2179, 2239, 3848, 3923, amount)
                    self.spawn_grenades_random(2111, 2167, 3848, 3923, amount)
                else:
                    self.spawn_grenades_preset(2216, 3860, 24, "y", amount)
                    self.spawn_grenades_preset(2133, 3860, 24, "y", amount)
            case "Pyramid":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(1410, 1471, 2792, 2828, amount)
                    self.spawn_grenades_random(1339, 1396, 2792, 2828, amount)
                else:
                    self.spawn_grenades_preset(1441, 2796, 18, "y", amount)
                    self.spawn_grenades_preset(1365, 2796, 18, "y", amount)
            case "Emu Ranch":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(1898, 1953, 2572, 2599, amount)
                    self.spawn_grenades_random(1835, 1887, 2572, 2599, amount)
                else:
                    self.spawn_grenades_preset(1930, 2568, 15, "y", amount)
                    self.spawn_grenades_preset(1862, 2568, 15, "y", amount)
            case "Shooting Range":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(944, 999, 1071, 1123, amount)
                    self.spawn_grenades_random(862, 918, 1071, 1123, amount)
                else:
                    self.spawn_grenades_preset(972, 1080, 12, "y", amount)
                    self.spawn_grenades_preset(890, 1080, 12, "y", amount)
            case "Juice Factory":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(3376, 3497, 2762, 2800, amount)
                    self.spawn_grenades_random(3376, 3497, 2707, 2746, amount)
                else:
                    self.spawn_grenades_preset(3411, 2797, 22, "x", amount)
                    self.spawn_grenades_preset(3411, 2711, 22, "x", amount)
            case "Super Sea Land":
                if self.random_nades_switch.get() == 1:
                    self.spawn_grenades_random(4148, 4182, 570, 636, amount)
                    self.spawn_grenades_random(4100, 4136, 570, 636, amount)
                else:
                    self.spawn_grenades_preset(4161, 591, 15, "y", amount)
                    self.spawn_grenades_preset(4114, 591, 15, "y", amount)
    
    def disable_hotkeys(self) -> None:
        if self.disable_hotkeys_switch.get() == 1:
            keyboard.unhook_all_hotkeys()
        else:
            keyboard.add_hotkey("ctrl+shift+s", self.hr_and_zip_hotkey)
            keyboard.add_hotkey("ctrl+shift+k", self.kill_host_hotkey)
            keyboard.add_hotkey("alt+y", self.spawn_grenade_hotkey)
            keyboard.add_hotkey("left+1", self.spawn_grenades_from_left_hotkey, args=(1,))
            keyboard.add_hotkey("left+2", self.spawn_grenades_from_left_hotkey, args=(2,))
            keyboard.add_hotkey("left+3", self.spawn_grenades_from_left_hotkey, args=(3,))
            keyboard.add_hotkey("right+1", self.spawn_grenades_from_right_hotkey, args=(1,))
            keyboard.add_hotkey("right+2", self.spawn_grenades_from_right_hotkey, args=(2,))
            keyboard.add_hotkey("right+3", self.spawn_grenades_from_right_hotkey, args=(3,))
    
    def validate_host(self, value: str) -> bool:
        pattern = r"\d{1,2}"
        return re.fullmatch(pattern, value) is not None
    
    def validate_teams(self, value: str) -> bool:
        pattern = r"[\d\s]+"
        return re.fullmatch(pattern, value) is not None
    
    def spawn_nade(self, x: int, y: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tele {self.host_id_entry.get()} {x} {y}", "nade")
    
    def spawn_zips(self, x: int, y: int, amount: int) -> None:
        if open_window("Super Animal Royale") is False:
            return
        
        send_commands(f"tele {self.host_id_entry.get()} {x} {y}")
        press_use()
        time.sleep(5)
        send_commands(f"zip {amount}")
        time.sleep(2)
        press_throwable()
    
    def lay_zip(self, x_player: int, y_player: int, x_mouse: int, y_mouse: int) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window_rect = sar_window.getClientFrame()
        window_top_left_x, window_top_left_y = sar_window_rect[0], sar_window_rect[1]
        window_width: int = sar_window_rect[2] - window_top_left_x
        
        size_ratio: float = window_width / 1920
        if size_ratio != 1:
            x_mouse = int(x_mouse * size_ratio)
            y_mouse = int(y_mouse * size_ratio)
        
        click_x: int = window_top_left_x + x_mouse
        click_y: int = window_top_left_y + y_mouse
        
        sar_window.activate()
        time.sleep(KEY_DELAY*16)
        send_commands(f"tele {self.host_id_entry.get()} {x_player} {y_player}")
        press_throwable()
        mouse_click(click_x, click_y)
    
    def break_boxes(self, x_player: int, y_player: int, x_mouse: int, y_mouse: int) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window_rect = sar_window.getClientFrame()
        window_top_left_x, window_top_left_y = sar_window_rect[0], sar_window_rect[1]
        window_width: int = sar_window_rect[2] - window_top_left_x
        
        size_ratio: float = window_width / 1920
        if size_ratio != 1:
            x_mouse = int(x_mouse * size_ratio)
            y_mouse = int(y_mouse * size_ratio)
        
        click_x: int = window_top_left_x + x_mouse
        click_y: int = window_top_left_y + y_mouse
        
        sar_window.activate()
        time.sleep(KEY_DELAY*16)
        send_commands(f"tele {self.host_id_entry.get()} {x_player} {y_player}")
        press_melee()
        mouse_click(click_x, click_y)
    
    def teleport_host(self, x: int, y: int, zip_amount: int = 0) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tele {self.host_id_entry.get()} {x} {y}", "gun13 2")
            if zip_amount != 0:
                send_commands(f"zip {zip_amount}")
    
    def teleport_players(self, team: list[str], x: int, y: int) -> None:
        if open_window("Super Animal Royale"):
            for player in team:
                send_commands(f"tele {player} {x} {y}")
    
    def start_match(self) -> None:
        # Guard clauses
        if self.validate_host(self.host_id_entry.get()) is False:
            CTkMessagebox(self, message="Invalid host ID")
            return
        
        if self.random_teams_switch.get() == 0:
            if self.validate_teams(self.team_a_entry.get()) is False:
                CTkMessagebox(self, message="Invalid team A IDs")
                return
            
            if self.validate_teams(self.team_b_entry.get()) is False:
                CTkMessagebox(self, message="Invalid team B IDs")
                return
        
        if open_window("Super Animal Royale") is False:
            return
        
        team_a, team_b = self.get_teams()
        
        # Disable items, emus, hamballs and gas
        send_commands("allitems", "emus", "hamballs", "gasoff")
        
        # Start game and instructions
        send_commands(f"dmg {round(self.damage_slider.get(), 1)}", "startp", "god all", "ziplines")
        send_commands("yell Welcome to dodgeball!")
        send_commands("yell Remember to stay in the arena and don't hit players with")
        send_commands("yell anything other than grenades or you will be disqualified")
        send_commands("yell Please jump out of the eagle as soon as possible")
        send_commands("yell And of course good luck have fun gamers!")
        
        # Wait for eagle and jump out
        time.sleep(16)
        open_window("Super Animal Royale")
        press_use()
        
        # Map selection
        match self.map_select.get():
            case "Bamboo Resort":
                self.spawn_nade(2575, 2138)
                self.spawn_nade(2575, 2130)
                self.spawn_nade(2575, 2122)
                self.spawn_nade(2575, 2114)
                self.spawn_nade(2575, 2210)
                self.spawn_nade(2575, 2218)
                self.spawn_nade(2575, 2224)
                self.spawn_nade(2575, 2228)
                self.spawn_zips(2575, 2047, 4)
                self.lay_zip(2575, 2235, 960, 750)
                self.lay_zip(2575, 2090, 960, 220)
                self.lay_zip(2512, 2149, 950, 320)
                self.lay_zip(2639, 2149, 950, 320)
                self.teleport_host(2574, 2037, 4)
                self.teleport_players(team_a, 2513, 2165)
                self.teleport_players(team_b, 2637, 2165)
            case "SAW Security Grass":
                self.spawn_nade(3430, 1877)
                self.spawn_nade(3430, 1885)
                self.spawn_nade(3430, 1951)
                self.spawn_zips(3430, 1815, 3)
                
                # Opening the door
                send_commands(f"tele {self.host_id_entry.get()} 3350 1816")
                time.sleep(1)
                press_use()
                time.sleep(1)
                
                self.lay_zip(3430, 1865, 960, 150)
                self.lay_zip(3430, 1965, 960, 670)
                self.spawn_nade(3430, 1892)
                self.spawn_nade(3430, 1899)
                self.spawn_nade(3430, 1906)
                self.spawn_nade(3430, 1913)
                self.spawn_nade(3430, 1920)
                self.teleport_host(3430, 1839)
                self.teleport_players(team_a, 3358, 1910)
                self.teleport_players(team_b, 3500, 1910)
            case "SAW Research Labs":
                self.spawn_nade(2757, 2951)
                self.spawn_nade(2757, 2974)
                self.spawn_nade(2757, 2982)
                self.spawn_nade(2757, 2990)
                self.spawn_nade(2757, 2998)
                self.spawn_nade(2757, 3020)
                self.spawn_nade(2757, 3025)
                self.spawn_zips(2757, 3200, 4)
                self.lay_zip(2757, 3038, 1400, 534)
                self.lay_zip(2757, 3038, 500, 534)
                self.lay_zip(2757, 2937, 500, 534)
                self.lay_zip(2757, 2937, 1400, 534)
                self.teleport_host(2757, 2890)
                self.teleport_players(team_a, 2695, 2989)
                self.teleport_players(team_b, 2816, 2989)
            case "Super Welcome Center":
                self.spawn_nade(555, 541)
                self.spawn_nade(555, 549)
                self.spawn_nade(555, 557)
                self.spawn_nade(555, 564)
                self.spawn_nade(555, 583)
                self.spawn_nade(555, 591)
                self.spawn_nade(555, 599)
                self.spawn_nade(555, 622)
                self.spawn_nade(555, 628)
                self.spawn_zips(512, 404, 4)
                self.lay_zip(555, 538, 954, 360)
                self.lay_zip(555, 580, 954, 360)
                self.lay_zip(549, 619, 1034, 460)
                self.lay_zip(515, 527, 1197, 544)
                self.teleport_host(512, 404, 2)
                self.teleport_players(team_a, 489, 588)
                self.teleport_players(team_b, 617, 588)
            case "Penguin Palace":
                self.spawn_nade(2175, 3822)
                self.spawn_nade(2175, 3848)
                self.spawn_nade(2175, 3856)
                self.spawn_nade(2175, 3864)
                self.spawn_nade(2175, 3870)
                self.spawn_nade(2175, 3905)
                self.spawn_nade(2175, 3913)
                self.spawn_nade(2175, 3921)
                self.spawn_zips(2174, 3690, 4)
                self.lay_zip(2166, 3818, 1060, 480)
                self.lay_zip(2174, 3846, 965, 380)
                self.lay_zip(2174, 3904, 961, 420)
                self.teleport_host(2174, 3690)
                self.teleport_players(team_a, 2096, 3883)
                self.teleport_players(team_b, 2250, 3883)
            case "Pyramid":
                self.spawn_nade(1403, 2792)
                self.spawn_nade(1403, 2798)
                self.spawn_nade(1403, 2802)
                self.spawn_nade(1403, 2810)
                self.spawn_nade(1403, 2816)
                self.spawn_nade(1403, 2822)
                self.spawn_nade(1403, 2827)
                self.spawn_zips(1403, 2692, 2)
                self.lay_zip(1403, 2791, 963, 290)
                self.lay_zip(1479, 2806, 967, 410)
                self.teleport_host(1403, 2692)
                self.teleport_players(team_a, 1343, 2819)
                self.teleport_players(team_b, 1471, 2819)
            case "Emu Ranch":
                self.spawn_nade(1893, 2557)
                self.spawn_nade(1893, 2561)
                self.spawn_nade(1893, 2564)
                self.spawn_nade(1893, 2571)
                self.spawn_nade(1893, 2590)
                self.spawn_nade(1893, 2596)
                self.spawn_zips(1900, 2530, 4)
                self.break_boxes(1891, 2574, 1050, 343)
                self.lay_zip(1893, 2552, 957, 220)
                self.lay_zip(1881, 2546, 1340, 535)
                self.lay_zip(1825, 2570, 954, 430)
                self.lay_zip(1960, 2566, 952, 390)
                self.teleport_host(1900, 2530)
                self.teleport_players(team_a, 1838, 2580)
                self.teleport_players(team_b, 1952, 2580)
            case "Shooting Range":
                self.spawn_nade(930, 1073)
                self.spawn_nade(930, 1081)
                self.spawn_nade(930, 1089)
                self.spawn_nade(930, 1096)
                self.spawn_nade(930, 1124)
                self.spawn_nade(930, 1128)
                self.spawn_zips(930, 1016, 4)
                self.lay_zip(930, 1064, 954, 330)
                self.lay_zip(848, 1064, 954, 330)
                self.lay_zip(1009, 1064, 954, 330)
                self.lay_zip(938, 1119, 827, 480)
                self.teleport_host(930, 1016)
                self.teleport_players(team_a, 859, 1090)
                self.teleport_players(team_b, 1002, 1090)
            case "Juice Factory":
                self.spawn_nade(3415, 2750)
                self.spawn_nade(3423, 2750)
                self.spawn_nade(3431, 2750)
                self.spawn_nade(3439, 2750)
                self.spawn_nade(3447, 2750)
                self.spawn_zips(3433, 2655, 4)
                self.break_boxes(3428, 2744, 1050, 343)
                self.break_boxes(3450, 2740, 1050, 343)
                self.break_boxes(3427, 2723, 1050, 343)
                self.lay_zip(3372, 2711, 965, 100)
                self.lay_zip(3369, 2751, 1145, 539)
                self.lay_zip(3413, 2751, 1255, 539)
                self.lay_zip(3472, 2751, 1145   , 539)
                self.teleport_host(3433, 2665)
                self.teleport_players(team_a, 3433, 2701)
                self.teleport_players(team_b, 3433, 2799)
            case "Super Sea Land":
                self.spawn_nade(4140, 570)
                self.spawn_nade(4140, 588)
                self.spawn_nade(4140, 596)
                self.spawn_nade(4140, 618)
                self.spawn_nade(4140, 626)
                self.spawn_nade(4140, 634)
                self.spawn_zips(4028, 606, 4)
                self.break_boxes(4130, 573, 1050, 343)
                self.lay_zip(4142, 556, 948, 270)
                self.lay_zip(4142, 616, 948, 140)
                self.lay_zip(4090, 596, 950, 400)
                self.lay_zip(4193, 596, 950, 400)
                self.teleport_host(4028, 606)
                self.teleport_players(team_a, 4090, 607)
                self.teleport_players(team_b, 4193, 607)
        
        send_commands("god all")