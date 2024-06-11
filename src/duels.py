import customtkinter
import re
import time
import random
from CTkToolTip import CTkToolTip
from CTkMessagebox import CTkMessagebox
from functions import *

class Duels(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("600x620")
        self.title("Private Game Helper - Duels")
        self.resizable(False, False)
        self.FONT_TITLE = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.FONT_REGULAR = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        
        # Title
        self.duels_title = customtkinter.CTkLabel(self, text="Duels", font=self.FONT_TITLE)
        self.duels_title.place(x=20, y=20)
        
        # Maps
        self.map_label = customtkinter.CTkLabel(self, text="Map:", font=self.FONT_REGULAR)
        self.map_label.place(x=20, y=60)
        self.map_select = customtkinter.CTkOptionMenu(self, width=175, values=["Bamboo Resort", "SAW Security", "SAW Research Labs", "Super Welcome Center", "Penguin Palace"])
        self.map_select.place(x=20, y=90)
        
        # Host ID
        self.host_id_label = customtkinter.CTkLabel(self, text="Host ID:", font=self.FONT_REGULAR)
        self.host_id_label.place(x=20, y=140)
        self.host_id_entry = customtkinter.CTkEntry(self, width=175, placeholder_text="e.g. 1")
        self.host_id_entry.place(x=20, y=170)
        
        # HPM
        self.hpm_label = customtkinter.CTkLabel(self, text="HPM:", font=self.FONT_REGULAR)
        self.hpm_label.place(x=20, y=220)
        self.hpm_entry = customtkinter.CTkEntry(self, width=175, placeholder_text="e.g. 250")
        self.hpm_entry.place(x=20, y=250)
        self.hpm_entry.insert(0, "250")
        
        # Players per team
        self.players_per_team_label = customtkinter.CTkLabel(self, text="Players per team:", font=self.FONT_REGULAR)
        self.players_per_team_label.place(x=300, y=60)
        self.players_per_team_select = customtkinter.CTkOptionMenu(self, width=175, values=["1", "2", "3", "4"])
        self.players_per_team_select.place(x=300, y=90)
        
        # Team A
        self.team_a_label = customtkinter.CTkLabel(self, text="Team A IDs (separated by spaces):", font=self.FONT_REGULAR)
        self.team_a_label.place(x=300, y=140)
        self.team_a_entry = customtkinter.CTkEntry(self, width=175, placeholder_text="e.g. 2 4 5 8")
        self.team_a_entry.place(x=300, y=170)
        
        # Team B
        self.team_b_label = customtkinter.CTkLabel(self, text="Team B IDs (separated by spaces):", font=self.FONT_REGULAR)
        self.team_b_label.place(x=300, y=220)
        self.team_b_entry = customtkinter.CTkEntry(self, width=175, placeholder_text="e.g. 3 6 7 9")
        self.team_b_entry.place(x=300, y=250)
        
        # Weapons
        self.weapons_switch = customtkinter.CTkSwitch(self, text="Weapons", font=self.FONT_REGULAR, onvalue=1, offvalue=0, command=self.enable_random_weapons)
        self.weapons_switch.place(x=20, y=320)
        self.weapons_switch.select()
        
        # Armor
        self.armor_switch = customtkinter.CTkSwitch(self, text="Armor", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.armor_switch.place(x=20, y=370)
        self.armor_switch.select()
        
        # Powerups
        self.powerups_switch = customtkinter.CTkSwitch(self, text="Powerups", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.powerups_switch.place(x=20, y=420)
        self.powerups_switch.select()
        
        # Throwables
        self.throwables_switch = customtkinter.CTkSwitch(self, text="Throwables", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.throwables_switch.place(x=20, y=470)
        self.throwables_switch.select()
        
        # Random weapons
        self.random_weapons_switch = customtkinter.CTkSwitch(self, text="Random Weapons", font=self.FONT_REGULAR, onvalue=1, offvalue=0, command=self.enable_match_random_weapons)
        self.random_weapons_switch.place(x=20, y=520)
        self.random_weapons_tooltip = CTkToolTip(self.random_weapons_switch, delay=0, message="Spawns a selection of 4 random weapons for both teams (instead of all weapons)")
        
        # No pets
        self.no_pets_switch = customtkinter.CTkSwitch(self, text="No Pets", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.no_pets_switch.place(x=300, y=320)
        
        # One hit kills
        self.one_hit_kills_switch = customtkinter.CTkSwitch(self, text="One Hit Kills", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.one_hit_kills_switch.place(x=300, y=370)
        
        # No jumprolls
        self.no_jumprolls_switch = customtkinter.CTkSwitch(self, text="No Jumprolls", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.no_jumprolls_switch.place(x=300, y=420)
        
        # Kill host
        self.kill_host_switch = customtkinter.CTkSwitch(self, text="Kill Host", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.kill_host_switch.place(x=300, y=470)
        
        # Match random weapons
        self.match_random_weapons_switch = customtkinter.CTkSwitch(self, text="Match Random Weapons", font=self.FONT_REGULAR, onvalue=1, offvalue=0, state="disabled")
        self.match_random_weapons_switch.place(x=300, y=520)
        self.match_random_weapons_tooltip = CTkToolTip(self.match_random_weapons_switch, delay=0, message="Makes the random weapons same for both teams")
        
        # Start
        self.start_button = customtkinter.CTkButton(self, text="Start Match", command=self.start_match)
        self.start_button.place(x=20, y=570)
        
        Settings.update(self=Settings)
    
    def enable_random_weapons(self) -> None:
        if self.weapons_switch.get() == 1:
            self.random_weapons_switch.configure(state="normal")
            self.match_random_weapons_switch.configure(state="normal")
        else:
            self.random_weapons_switch.deselect()
            self.match_random_weapons_switch.deselect()
            self.random_weapons_switch.configure(state="disabled")
            self.match_random_weapons_switch.configure(state="disabled")
        
    def enable_match_random_weapons(self) -> None:
        if self.random_weapons_switch.get() == 1:
            self.match_random_weapons_switch.configure(state="normal")
        else:
            self.match_random_weapons_switch.deselect()
            self.match_random_weapons_switch.configure(state="disabled")
            
    def validate_host(self, value: str) -> bool:
        return re.fullmatch(r"\d{1,2}", value) is not None
    
    def validate_teams(self, value: str) -> bool:
        return re.fullmatch(r"[\d\s]+", value) is not None
    
    def validate_hpm(self, value: str) -> bool:
        return value.isnumeric()
    
    def teleport_players(self, team: str, x: int, y: int) -> None:
        if open_window("Super Animal Royale"):
            team = team.strip().split(sep=" ")
            for player in team:
                send_commands(f"tele {player} {x} {y}")
        
    def spawn_armor(self, x: int, y: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tele {self.host_id_entry.get()} {x} {y}")
            for _ in range(int(self.players_per_team_select.get())):
                send_commands("armor3")
                
    def spawn_weapon(self, x: int, y: int, id: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tele {self.host_id_entry.get()} {x} {y}")
            for _ in range(int(self.players_per_team_select.get())):
                send_commands(f"gun{id} 3")
                
    def spawn_ammo(self, x: int, y: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tele {self.host_id_entry.get()} {x} {y}")
            for _ in range(int(self.players_per_team_select.get())):
                for i in range(6):
                    send_commands(f"ammo{i} 500")
                send_commands("juice 200", "tape 5")
    
    def spawn_powerups(self, x: int, y: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tele {self.host_id_entry.get()} {x} {y}")
            for _ in range(int(self.players_per_team_select.get())):
                send_commands("util2", "util4")
    
    def spawn_throwables(self, x: int, y: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tele {self.host_id_entry.get()} {x} {y}")
            for _ in range(int(self.players_per_team_select.get())):
                send_commands("banana 10", "nade 4")
    
    def start_match(self) -> None: # Sourcery, shut your mouth. Fuck you >:c my boyfriend is perfect
        # Guard clauses
        if self.validate_host(self.host_id_entry.get()) is False:
            CTkMessagebox(self, message="Invalid host ID")
            return
        
        if self.validate_teams(self.team_a_entry.get()) is False:
            CTkMessagebox(self, message="Invalid team A IDs")
            return
        
        if self.validate_teams(self.team_b_entry.get()) is False:
            CTkMessagebox(self, message="Invalid team B IDs")
            return
        
        if self.validate_hpm(self.hpm_entry.get()) is False:
            CTkMessagebox(self, message="Invalid HPM")
            return
        
        if open_window("Super Animal Royale") is False:
            return
        
        # Disable items, emus, hamballs, gas and set HPM
        send_commands("allitems", "emus", "hamballs", "gasoff", f"highping {self.hpm_entry.get()}")
        
        # Set pets
        if self.no_pets_switch.get() == 1:
            send_commands("pets")
        
        # Set one hits
        if self.one_hit_kills_switch.get() == 1:
            send_commands("onehits")
        
        # Set jumprolls
        if self.no_jumprolls_switch.get() == 1:
            send_commands("noroll")
        
        # Start game and instructions
        send_commands("startp", "god all")
        send_commands("yell Welcome to duels!",
                      "yell Please jump out of the eagle as soon as possible",
                      "yell So you can be teleported to weapon selection",
                      f"yell Selected map: {self.map_select.get()}")
        
        # Wait for eagle and jump out
        time.sleep(16)
        open_window("Super Animal Royale")
        press_use()
        
        # Spawn ammo
        self.spawn_ammo(705, 1335)
        self.spawn_ammo(3845, 1535)
        
        # Spawn throwables
        if self.throwables_switch.get() == 1:
            self.spawn_throwables(735, 1335)
            self.spawn_throwables(3875, 1545)
            
        # Spawn armor
        if self.armor_switch.get() == 1:
            self.spawn_armor(755, 1335)
            self.spawn_armor(3895, 1545)
        
        # Spawn powerups
        if self.powerups_switch.get() == 1:
            self.spawn_powerups(775, 1335)
            self.spawn_powerups(3915, 1545)
        
        # Spawn weapons
        if self.weapons_switch.get() == 1:
            # Starting positions
            x_a: int = 735
            y_a: int = 1305
            x_b: int = 3875
            y_b: int = 1515
            if self.random_weapons_switch.get() == 1:
                if self.match_random_weapons_switch.get() == 1:
                    # Spawn random weapons for both teams
                    random_weapons_list: list[int] = []
                    for _ in range(4):
                        random_weapon_id: int = random.randint(0, 19)
                        while random_weapon_id in random_weapons_list:
                            random_weapon_id: int = random.randint(0, 19)
                        random_weapons_list.append(random_weapon_id)
                        self.spawn_weapon(x_a, y_a, random_weapon_id)
                        self.spawn_weapon(x_b, y_b, random_weapon_id)
                        x_a += 10
                        x_b += 10
                else:
                    # Spawn random weapons for team A
                    random_weapons_a_list: list[int] = []
                    for _ in range(4):
                        random_weapon_id: int = random.randint(0, 19)
                        while random_weapon_id in random_weapons_a_list:
                            random_weapon_id: int = random.randint(0, 19)
                        random_weapons_a_list.append(random_weapon_id)
                        self.spawn_weapon(x_a, y_a, random_weapon_id)
                        x_a += 10
                    
                    # Spawn random weapons for team B
                    random_weapons_b_list: list[int] = []
                    for _ in range(4):
                        random_weapon_id: int = random.randint(0, 19)
                        while random_weapon_id in random_weapons_b_list:
                            random_weapon_id: int = random.randint(0, 19)
                        random_weapons_b_list.append(random_weapon_id)
                        self.spawn_weapon(x_b, y_b, random_weapon_id)
                        x_b += 10
            else:
                # Spawn all weapons for both teams
                for i in range(20):
                    self.spawn_weapon(x_a, y_a, i)
                    self.spawn_weapon(x_b, y_b, i)
                    x_a += 10
                    x_b += 10
                    if i == 9:
                        x_a = 735
                        y_a -= 20
                    if i in (6, 13):
                        x_b = 3875
                        y_b -= 20
        
        # Teleport players
        self.teleport_players(self.team_a_entry.get(), 715, 1310)
        self.teleport_players(self.team_b_entry.get(), 3855, 1535)
        
        # Wait 30 seconds
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
        send_commands("god all")
        
        # Kill host
        if self.kill_host_switch.get() == 1:
            send_commands(f"kill {self.host_id_entry.get()}")
            send_commands(f"ghost {self.host_id_entry.get()}")
        
        # Teleport to selected map
        match self.map_select.get():
            case "Bamboo Resort":
                self.teleport_players(self.team_a_entry.get(), 2430, 1830)
                self.teleport_players(self.team_b_entry.get(), 2725, 1830)
                send_commands("yell Fight!")
            case "SAW Security":
                self.teleport_players(self.team_a_entry.get(), 3335, 1910)
                self.teleport_players(self.team_b_entry.get(), 3520, 1910)
                send_commands("yell Fight!")
            case "SAW Research Labs":
                self.teleport_players(self.team_a_entry.get(), 2600, 2985)
                self.teleport_players(self.team_b_entry.get(), 2900, 2985)
                send_commands("yell Fight!")
            case "Super Welcome Center":
                self.teleport_players(self.team_a_entry.get(), 510, 735)
                self.teleport_players(self.team_b_entry.get(), 865, 735)
                send_commands("yell Fight!")
            case "Penguin Palace":
                self.teleport_players(self.team_a_entry.get(), 2052, 3886)
                self.teleport_players(self.team_b_entry.get(), 2295, 3886)
                send_commands("yell Fight!")