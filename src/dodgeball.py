import customtkinter
import tkinter
import keyboard
import re
import time
import pywinctl
import pyautogui
import random
import pyperclip
from CTkMessagebox import CTkMessagebox

class Dodgeball(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("600x760")
        self.title("Private Game Helper - Dodgeball")
        self.resizable(False, False)
        self.FONT_TITLE = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.FONT_REGULAR = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        self.FONT_ITALIC = customtkinter.CTkFont(family="Roboto", weight="bold", slant="italic")
        self.KEY_DELAY: float = 0.025
        self.use_bind = tkinter.StringVar(self, "E")
        self.melee_bind = tkinter.StringVar(self, "3")
        self.throwable_bind = tkinter.StringVar(self, "4")
        
        # Title
        self.dodgeball_title = customtkinter.CTkLabel(self, text="Dodgeball", font=self.FONT_TITLE)
        self.dodgeball_title.place(x=20, y=20)
        
        # Maps
        self.map_label = customtkinter.CTkLabel(self, text="Map:", font=self.FONT_REGULAR)
        self.map_label.place(x=20, y=60)
        self.map_select = customtkinter.CTkOptionMenu(self, width=175, values=["Bamboo Resort", "SAW Security Grass", "SAW Research Labs", "Super Welcome Center", "Penguin Palace", "Pyramid", "Emu Ranch", "Shooting Range", "Juice Factory", "Super Sea Land"])
        self.map_select.place(x=20, y=90)
        
        # Host ID
        self.host_id_label = customtkinter.CTkLabel(self, text="Host ID:", font=self.FONT_REGULAR)
        self.host_id_label.place(x=20, y=140)
        self.host_id_entry = customtkinter.CTkEntry(self, width=175, placeholder_text="e.g. 1")
        self.host_id_entry.place(x=20, y=170)
        
        # Team A
        self.team_a_label = customtkinter.CTkLabel(self, text="Team A IDs (separated by spaces):", font=self.FONT_REGULAR)
        self.team_a_label.place(x=300, y=60)
        self.team_a_entry = customtkinter.CTkEntry(self, width=175, placeholder_text="e.g. 2 4 5 8")
        self.team_a_entry.place(x=300, y=90)
        
        # Team B
        self.team_b_label = customtkinter.CTkLabel(self, text="Team B IDs (separated by spaces):", font=self.FONT_REGULAR)
        self.team_b_label.place(x=300, y=140)
        self.team_b_entry = customtkinter.CTkEntry(self, width=175, placeholder_text="e.g. 3 6 7 9")
        self.team_b_entry.place(x=300, y=170)
        
        # Random nades
        self.random_nades_switch = customtkinter.CTkSwitch(self, text="Random Nades", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.random_nades_switch.place(x=20, y=220)
        
        # Disable hotkeys
        self.disable_hotkeys_switch = customtkinter.CTkSwitch(self, text="Disable Hotkeys", font=self.FONT_REGULAR, onvalue=1, offvalue=0, command=self.disable_hotkeys)
        self.disable_hotkeys_switch.place(x=300, y=220)
        
        # Damage
        self.damage_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=10.0, number_of_steps=100, command=self.damage_slider_ctrl)
        self.damage_slider.place(x=20, y=270)
        self.damage_slider.set(1.0)
        self.damage_text = customtkinter.CTkLabel(self, text="Damage:", font=self.FONT_REGULAR)
        self.damage_text.place(x=20, y=290)
        self.damage_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.damage_label.place(x=150, y=290)
        
        # Random teams
        self.random_teams_switch = customtkinter.CTkSwitch(self, text="Random Teams", font=self.FONT_REGULAR, onvalue=1, offvalue=0, command=self.enable_random_teams)
        self.random_teams_switch.place(x=300, y=270)
        
        # Hotkeys
        self.hotkeys_title = customtkinter.CTkLabel(self, text="Hotkeys", font=self.FONT_TITLE)
        self.hotkeys_title.place(x=20, y=340)
        
        # Spawn HR and ziplines
        self.hr_and_zip_label = customtkinter.CTkLabel(self, text="(Ctrl + Shift + S)", font=self.FONT_ITALIC)
        self.hr_and_zip_label.place(x=20, y=390)
        self.hr_and_zip_desc = customtkinter.CTkLabel(self, text="Spawn hunting rifle and ziplines", font=self.FONT_REGULAR)
        self.hr_and_zip_desc.place(x=300, y=390)
        keyboard.add_hotkey("ctrl+shift+s", self.hr_and_zip_hotkey)
        
        # Kill and ghost host
        self.kill_host_label = customtkinter.CTkLabel(self, text="(Ctrl + Shift + K)", font=self.FONT_ITALIC)
        self.kill_host_label.place(x=20, y=420)
        self.kill_host_desc = customtkinter.CTkLabel(self, text="Kill and ghost host", font=self.FONT_REGULAR)
        self.kill_host_desc.place(x=300, y=420)
        keyboard.add_hotkey("ctrl+shift+k", self.kill_host_hotkey)
        
        # Spawn a grenade
        self.spawn_grenade_label = customtkinter.CTkLabel(self, text="(Alt + Y)", font=self.FONT_ITALIC)
        self.spawn_grenade_label.place(x=20, y=450)
        self.spawn_grenade_desc = customtkinter.CTkLabel(self, text="Spawn a grenade", font=self.FONT_REGULAR)
        self.spawn_grenade_desc.place(x=300, y=450)
        keyboard.add_hotkey("alt+y", self.spawn_grenade_hotkey)
        
        # Spawn grenades for teams starting from the left
        self.spawn_grenades_from_left_label = customtkinter.CTkLabel(self, text="(Left + [1-3])", font=self.FONT_ITALIC)
        self.spawn_grenades_from_left_label.place(x=20, y=480)
        self.spawn_grenades_from_left_desc = customtkinter.CTkLabel(self, text="Spawn [1-3] grenades\nstarting from the left", font=self.FONT_REGULAR)
        self.spawn_grenades_from_left_desc.place(x=300, y=480)
        keyboard.add_hotkey("left+1", self.spawn_grenades_from_left_hotkey, args=(1,))
        keyboard.add_hotkey("left+2", self.spawn_grenades_from_left_hotkey, args=(2,))
        keyboard.add_hotkey("left+3", self.spawn_grenades_from_left_hotkey, args=(3,))
        
        # Spawn grenades for teams starting from the right
        self.spawn_grenades_from_right_label = customtkinter.CTkLabel(self, text="(Right + [1-3])", font=self.FONT_ITALIC)
        self.spawn_grenades_from_right_label.place(x=20, y=530)
        self.spawn_grenades_from_right_desc = customtkinter.CTkLabel(self, text="Spawn [1-3] grenades\nstarting from the right", font=self.FONT_REGULAR)
        self.spawn_grenades_from_right_desc.place(x=300, y=530)
        keyboard.add_hotkey("right+1", self.spawn_grenades_from_right_hotkey, args=(1,))
        keyboard.add_hotkey("right+2", self.spawn_grenades_from_right_hotkey, args=(2,))
        keyboard.add_hotkey("right+3", self.spawn_grenades_from_right_hotkey, args=(3,))
        
        # In-game keybinds
        self.keybinds_title = customtkinter.CTkLabel(self, text="In-game Keybinds", font=self.FONT_TITLE)
        self.keybinds_title.place(x=20, y=580)
        self.use_bind_label = customtkinter.CTkLabel(self, text="Use:", font=self.FONT_REGULAR)
        self.use_bind_label.place(x=20, y=630)
        self.use_bind_entry = customtkinter.CTkEntry(self, textvariable=self.use_bind, placeholder_text="e.g. E", validate="focusout", validatecommand=self.validate_use)
        self.use_bind_entry.place(x=20, y=660)
        self.melee_bind_label = customtkinter.CTkLabel(self, text="Melee:", font=self.FONT_REGULAR)
        self.melee_bind_label.place(x=220, y=630)
        self.melee_bind_entry = customtkinter.CTkEntry(self, textvariable=self.melee_bind, placeholder_text="e.g. 3", validate="focusout", validatecommand=self.validate_melee)
        self.melee_bind_entry.place(x=220, y=660)
        self.throwable_bind_label = customtkinter.CTkLabel(self, text="Throwable:", font=self.FONT_REGULAR)
        self.throwable_bind_label.place(x=420, y=630)
        self.throwable_bind_entry = customtkinter.CTkEntry(self, textvariable=self.throwable_bind, placeholder_text="e.g. 4", validate="focusout", validatecommand=self.validate_throwable)
        self.throwable_bind_entry.place(x=420, y=660)
        
        # Start
        self.start_button = customtkinter.CTkButton(self, text="Start Match", command=self.start_match)
        self.start_button.place(x=20, y=710)
    
    def enable_random_teams(self) -> None:
        if self.random_teams_switch.get() == 1:
            self.team_a_entry.configure(state="disable")
            self.team_b_entry.configure(state="disable")
        else:
            self.team_a_entry.configure(state="normal")
            self.team_b_entry.configure(state="normal")
    
    def get_teams(self) -> tuple[list[str], list[str]] | None:
        if self.random_teams_switch.get() == 1:
            if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
                return
        
            sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
            sar_window.activate()
            time.sleep(self.KEY_DELAY*16)
            keyboard.write("\n/getplayers\n", delay=self.KEY_DELAY)
            time.sleep(self.KEY_DELAY*16)
            clipboard: list[str] = pyperclip.paste().split("\n")
            clipboard.remove("")
            player_list: list[str] = []
            team_a: list[str] = []
            team_b: list[str] = []
            for player in clipboard:
                player_id = player.split("\t")[0]
                if player_id != "pID" and player_id != self.host_id_entry.get():
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
    
    def validate_use(self) -> bool:
        if re.fullmatch(r"[A-Z\d]|mouse[0-2]", self.use_bind.get(), re.IGNORECASE) is None:
            CTkMessagebox(self, message="Invalid keybind")
            self.use_bind_entry.delete(0, 99)
            self.use_bind_entry.insert(0, "E")
            self.use_bind.set("E")
            return False
        return True
    
    def validate_melee(self) -> bool:
        if re.fullmatch(r"[A-Z\d]|mouse[0-2]", self.melee_bind.get(), re.IGNORECASE) is None:
            CTkMessagebox(self, message="Invalid keybind")
            self.melee_bind_entry.delete(0, 99)
            self.melee_bind_entry.insert(0, "3")
            self.melee_bind.set("3")
            return False
        return True
    
    def validate_throwable(self) -> bool:
        if re.fullmatch(r"[A-Z\d]|mouse[0-2]", self.throwable_bind.get(), re.IGNORECASE) is None:
            CTkMessagebox(self, message="Invalid keybind")
            self.throwable_bind_entry.delete(0, 99)
            self.throwable_bind_entry.insert(0, "4")
            self.throwable_bind.set("4")
            return False
        return True
    
    def use_bind_input(self) -> None:
        match self.use_bind.get().lower():
            case "mouse0":
                pyautogui.click(button="left")
            case "mouse1":
                pyautogui.click(button="right")
            case "mouse2":
                pyautogui.click(button="middle")
            case _:
                keyboard.send(self.use_bind.get().lower())
    
    def melee_bind_input(self) -> None:
        match self.melee_bind.get().lower():
            case "mouse0":
                pyautogui.click(button="left")
            case "mouse1":
                pyautogui.click(button="right")
            case "mouse2":
                pyautogui.click(button="middle")
            case _:
                keyboard.send(self.melee_bind.get().lower())
    
    def throwable_bind_input(self) -> None:
        match self.throwable_bind.get().lower():
            case "mouse0":
                pyautogui.click(button="left")
            case "mouse1":
                pyautogui.click(button="right")
            case "mouse2":
                pyautogui.click(button="middle")
            case _:
                keyboard.send(self.throwable_bind.get().lower())
    
    def damage_slider_ctrl(self, value: float) -> None:
        value = round(value, 1)
        self.damage_label.configure(text=value)
        self.damage_slider.set(value)
    
    # Hotkeys
    def hr_and_zip_hotkey(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/gun13 2\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/zip 4\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
    
    def kill_host_hotkey(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/kill {self.host_id_entry.get()}\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write(f"\n/ghost {self.host_id_entry.get()}\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
    
    def spawn_grenade_hotkey(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/nade\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
    
    def spawn_grenades_from_left_hotkey(self, amount: int) -> None:
        match self.map_select.get():
            case "Bamboo Resort":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(2519, 2560)
                        y_a: int = random.randint(2126, 2207)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(2590, 2622)
                        y_b: int = random.randint(2126, 2207)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 2539
                    y_a: int = 2147
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 20
                    x_b: int = 2618
                    y_b: int = 2147
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 20
            case "SAW Security Grass":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(3358, 3397)
                        y_a: int = random.randint(1872, 1951)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(3461, 3500)
                        y_b: int = random.randint(1872, 1951)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 3380
                    y_a: int = 1893
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 20
                    x_b: int = 3479
                    y_b: int = 1893
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 20
            case "SAW Research Labs":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(2697, 2752)
                        y_a: int = random.randint(2944, 3028)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(2762, 2817)
                        y_b: int = random.randint(2944, 3028)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 2719
                    y_a: int = 2965
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 25
                    x_b: int = 2793
                    y_b: int = 2965
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 25
            case "Super Welcome Center":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(488, 548)
                        y_a: int = random.randint(540, 630)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(563, 609)
                        y_b: int = random.randint(540, 630)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 523
                    y_a: int = 549
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 40
                    x_b: int = 592
                    y_b: int = 549
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 40
            case "Penguin Palace":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(2111, 2167)
                        y_a: int = random.randint(3848, 3923)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(2179, 2239)
                        y_b: int = random.randint(3848, 3923)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 2133
                    y_a: int = 3860
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 24
                    x_b: int = 2216
                    y_b: int = 3860
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 24
            case "Pyramid":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(1339, 1396)
                        y_a: int = random.randint(2792, 2828)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(1410, 1471)
                        y_b: int = random.randint(2792, 2828)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 1365
                    y_a: int = 2796
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 18
                    x_b: int = 1441
                    y_b: int = 2796
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 18
            case "Emu Ranch":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(1835, 1887)
                        y_a: int = random.randint(2572, 2599)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(1898, 1953)
                        y_b: int = random.randint(2572, 2599)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 1862
                    y_a: int = 2568
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 15
                    x_b: int = 1930
                    y_b: int = 2568
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 15
            case "Shooting Range":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(862, 918)
                        y_a: int = random.randint(1071, 1123)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(944, 999)
                        y_b: int = random.randint(1071, 1123)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 890
                    y_a: int = 1080
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 12
                    x_b: int = 972
                    y_b: int = 1080
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 12
            case "Juice Factory":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(3376, 3497)
                        y_a: int = random.randint(2707, 2746)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(3376, 3497)
                        y_b: int = random.randint(2762, 2800)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 3411
                    y_a: int = 2711
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        x_a += 22
                    x_b: int = 3411
                    y_b: int = 2797
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        x_b += 22
            case "Super Sea Land":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_a: int = random.randint(4100, 4136)
                        y_a: int = random.randint(570, 636)
                        self.spawn_nade(x_a, y_a)
                    for i in range(amount):
                        x_b: int = random.randint(4148, 4182)
                        y_b: int = random.randint(570, 636)
                        self.spawn_nade(x_b, y_b)
                else:
                    x_a: int = 4114
                    y_a: int = 591
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 15
                    x_b: int = 4161
                    y_b: int = 591
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 15
        
    def spawn_grenades_from_right_hotkey(self, amount: int) -> None:
        match self.map_select.get():
            case "Bamboo Resort":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(2590, 2622)
                        y_b: int = random.randint(2126, 2207)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(2519, 2560)
                        y_a: int = random.randint(2126, 2207)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 2618
                    y_b: int = 2147
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 20
                    x_a: int = 2539
                    y_a: int = 2147
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 20
            case "SAW Security Grass":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(3461, 3500)
                        y_b: int = random.randint(1872, 1951)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(3358, 3397)
                        y_a: int = random.randint(1872, 1951)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 3479
                    y_b: int = 1893
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 20
                    x_a: int = 3380
                    y_a: int = 1893
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 20
            case "SAW Research Labs":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(2762, 2817)
                        y_b: int = random.randint(2944, 3028)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(2697, 2752)
                        y_a: int = random.randint(2944, 3028)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 2793
                    y_b: int = 2965
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 25
                    x_a: int = 2719
                    y_a: int = 2965
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 25
            case "Super Welcome Center":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(563, 609)
                        y_b: int = random.randint(540, 630)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(488, 548)
                        y_a: int = random.randint(540, 630)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 592
                    y_b: int = 549
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 40
                    x_a: int = 523
                    y_a: int = 549
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 40
            case "Penguin Palace":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(2179, 2239)
                        y_b: int = random.randint(3848, 3923)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(2111, 2167)
                        y_a: int = random.randint(3848, 3923)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 2216
                    y_b: int = 3860
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 24
                    x_a: int = 2133
                    y_a: int = 3860
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 24
            case "Pyramid":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(1410, 1471)
                        y_b: int = random.randint(2792, 2828)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(1339, 1396)
                        y_a: int = random.randint(2792, 2828)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 1441
                    y_b: int = 2796
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 18
                    x_a: int = 1365
                    y_a: int = 2796
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 18
            case "Emu Ranch":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(1898, 1953)
                        y_b: int = random.randint(2572, 2599)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(1835, 1887)
                        y_a: int = random.randint(2572, 2599)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 1930
                    y_b: int = 2568
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 15
                    x_a: int = 1862
                    y_a: int = 2568
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 15
            case "Shooting Range":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(944, 999)
                        y_b: int = random.randint(1071, 1123)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(862, 918)
                        y_a: int = random.randint(1071, 1123)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 972
                    y_b: int = 1080
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 12
                    x_a: int = 890
                    y_a: int = 1080
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 12
            case "Juice Factory":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(3376, 3497)
                        y_b: int = random.randint(2762, 2800)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(3376, 3497)
                        y_a: int = random.randint(2707, 2746)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 3411
                    y_b: int = 2797
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        x_b += 22
                    x_a: int = 3411
                    y_a: int = 2711
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        x_a += 22
            case "Super Sea Land":
                if self.random_nades_switch.get() == 1:
                    for i in range(amount):
                        x_b: int = random.randint(4148, 4182)
                        y_b: int = random.randint(570, 636)
                        self.spawn_nade(x_b, y_b)
                    for i in range(amount):
                        x_a: int = random.randint(4100, 4136)
                        y_a: int = random.randint(570, 636)
                        self.spawn_nade(x_a, y_a)
                else:
                    x_b: int = 4161
                    y_b: int = 591
                    for i in range(amount):
                        self.spawn_nade(x_b, y_b)
                        y_b += 15
                    x_a: int = 4114
                    y_a: int = 591
                    for i in range(amount):
                        self.spawn_nade(x_a, y_a)
                        y_a += 15
    
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
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/tele {self.host_id_entry.get()} {x} {y}\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/nade\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
    
    def spawn_zips(self, x: int, y: int, amount: int) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/tele {self.host_id_entry.get()} {x} {y}\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        self.use_bind_input()
        time.sleep(5)
        keyboard.write(f"\n/zip {amount}\n", delay=self.KEY_DELAY)
        time.sleep(2)
        self.throwable_bind_input()
        time.sleep(self.KEY_DELAY*2)
    
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
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/tele {self.host_id_entry.get()} {x_player} {y_player}\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        self.throwable_bind_input()
        time.sleep(self.KEY_DELAY*8)
        pyautogui.moveTo(click_x, click_y)
        time.sleep(self.KEY_DELAY*8)
        pyautogui.click()
        time.sleep(self.KEY_DELAY*8)
    
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
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/tele {self.host_id_entry.get()} {x_player} {y_player}\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        self.melee_bind_input()
        time.sleep(self.KEY_DELAY*8)
        pyautogui.moveTo(click_x, click_y)
        time.sleep(self.KEY_DELAY*8)
        pyautogui.click()
        time.sleep(self.KEY_DELAY*8)
    
    def teleport_host(self, x: int, y: int, zip_amount: int = 0) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/tele {self.host_id_entry.get()} {x} {y}\n", delay=self.KEY_DELAY)
        keyboard.write("\n/gun13 2\n", delay=self.KEY_DELAY)
        if zip_amount != 0:
            keyboard.write(f"\n/zip {zip_amount}\n", delay=self.KEY_DELAY)
    
    def teleport_players(self, team: list[str], x: int, y: int) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        for player in team:
            keyboard.write(f"\n/tele {player} {x} {y}\n", delay=self.KEY_DELAY)
            time.sleep(self.KEY_DELAY*2)
    
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
        
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        team_a, team_b = self.get_teams()
        
        # Disable items, emus, hamballs and gas
        keyboard.write("\n/allitems\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/emus\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/hamballs\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/gasoff\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        
        # Start game and instructions
        keyboard.write(f"\n/dmg {round(self.damage_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/startp\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/god all\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/yell Welcome to dodgeball!\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/yell Remember to stay in the arena and don't hit players with\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/yell anything other than grenades or you will be disqualified\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/yell Please jump out of the eagle as soon as possible\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/yell And of course good luck have fun gamers!\n", delay=self.KEY_DELAY)
        time.sleep(self.KEY_DELAY*2)
        
        # Wait for eagle and jump out
        time.sleep(16)
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        self.use_bind_input()
        
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
                self.lay_zip(2575, 2235, 960, 790)
                self.lay_zip(2575, 2090, 960, 165)
                self.lay_zip(2512, 2149, 950, 268)
                self.lay_zip(2639, 2149, 950, 268)
                self.teleport_host(2574, 2037, 4)
                self.teleport_players(team_a, 2513, 2165)
                self.teleport_players(team_b, 2637, 2165)
            case "SAW Security Grass":
                self.spawn_nade(3430, 1877)
                self.spawn_nade(3430, 1885)
                self.spawn_nade(3430, 1951)
                self.spawn_zips(3430, 1815, 3)
                
                # Opening the door
                keyboard.write(f"\n/tele {self.host_id_entry.get()} 3350 1816\n", delay=self.KEY_DELAY)
                time.sleep(1)
                keyboard.send(self.use_bind.get().lower())
                time.sleep(1)
                
                self.lay_zip(3430, 1865, 960, 80)
                self.lay_zip(3430, 1965, 960, 680)
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
                self.lay_zip(2757, 3038, 1485, 534)
                self.lay_zip(2757, 3038, 434, 534)
                self.lay_zip(2757, 2937, 434, 534)
                self.lay_zip(2757, 2937, 1485, 534)
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
                self.lay_zip(555, 538, 954, 323)
                self.lay_zip(555, 580, 954, 323)
                self.lay_zip(549, 619, 1081, 451)
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
                self.lay_zip(2166, 3818, 1100, 457)
                self.lay_zip(2174, 3846, 965, 339)
                self.lay_zip(2174, 3904, 961, 394)
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
                self.lay_zip(1403, 2791, 963, 240)
                self.lay_zip(1479, 2806, 967, 384)
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
                self.lay_zip(1893, 2552, 957, 148)
                self.lay_zip(1881, 2546, 1340, 535)
                self.lay_zip(1825, 2570, 954, 414)
                self.lay_zip(1960, 2566, 952, 363)
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
                self.lay_zip(930, 1064, 954, 294)
                self.lay_zip(848, 1064, 954, 294)
                self.lay_zip(1009, 1064, 954, 294)
                self.lay_zip(938, 1119, 827, 459)
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
                self.lay_zip(3372, 2711, 965, 20)
                self.lay_zip(3369, 2751, 1191, 539)
                self.lay_zip(3413, 2751, 1314, 539)
                self.lay_zip(3472, 2751, 1184, 539)
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
                self.lay_zip(4142, 556, 948, 214)
                self.lay_zip(4142, 616, 948, 77)
                self.lay_zip(4090, 596, 950, 362)
                self.lay_zip(4193, 596, 950, 362)
                self.teleport_host(4028, 606)
                self.teleport_players(team_a, 4090, 607)
                self.teleport_players(team_b, 4193, 607)
        
        time.sleep(self.KEY_DELAY*2)
        keyboard.write("\n/god all\n", delay=self.KEY_DELAY)