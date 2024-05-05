import tkinter
import tkinter.messagebox
from typing import Tuple
import customtkinter
import pyperclip
import keyboard
import time
import random
from pyWinActivate import win_activate, check_win_exist
from CTkMenuBar import *
from CTkToolTip import *
from tkinter.filedialog import askopenfile, asksaveasfile
from functools import partial
from PIL import Image

# System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
delay = 0.025

# Images
class Images:
    AVATAR = customtkinter.CTkImage(Image.open("Assets\\Avatar.png"), size=(80, 80))
    SAR_MAP = customtkinter.CTkImage(Image.open("Assets\\Map.png"), size=(768, 768))
    RARITY_COMMON = customtkinter.CTkImage(Image.open("Assets\\RarityCommon.png"), size=(100, 24))
    RARITY_UNCOMMON = customtkinter.CTkImage(Image.open("Assets\\RarityUncommon.png"), size=(100, 24))
    RARITY_RARE = customtkinter.CTkImage(Image.open("Assets\\RarityRare.png"), size=(100, 24))
    RARITY_EPIC = customtkinter.CTkImage(Image.open("Assets\\RarityEpic.png"), size=(100, 24))
    RARITY_LEGENDARY = customtkinter.CTkImage(Image.open("Assets\\RarityLegendary.png"), size=(100, 24))
    RARITY_COMMON_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityCommonOff.png"), size=(100, 24))
    RARITY_UNCOMMON_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityUncommonOff.png"), size=(100, 24))
    RARITY_RARE_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityRareOff.png"), size=(100, 24))
    RARITY_EPIC_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityEpicOff.png"), size=(100, 24))
    RARITY_LEGENDARY_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityLegendaryOff.png"), size=(100, 24))
    ICON_PISTOL = customtkinter.CTkImage(Image.open("Assets\\Pistol.png"), size=(100, 100))
    ICON_DUALIES = customtkinter.CTkImage(Image.open("Assets\\Dualies.png"), size=(100, 100))
    ICON_MAGNUM = customtkinter.CTkImage(Image.open("Assets\\Magnum.png"), size=(100, 100))
    ICON_DEAGLE = customtkinter.CTkImage(Image.open("Assets\\Deagle.png"), size=(100, 100))
    ICON_SILENCED_PISTOL = customtkinter.CTkImage(Image.open("Assets\\SilencedPistol.png"), size=(100, 100))
    ICON_SHOTGUN = customtkinter.CTkImage(Image.open("Assets\\Shotgun.png"), size=(100, 100))
    ICON_JAG = customtkinter.CTkImage(Image.open("Assets\\Jag.png"), size=(100, 100))
    ICON_SMG = customtkinter.CTkImage(Image.open("Assets\\Smg.png"), size=(100, 100))
    ICON_TOMMY = customtkinter.CTkImage(Image.open("Assets\\Tommy.png"), size=(100, 100))
    ICON_AK = customtkinter.CTkImage(Image.open("Assets\\Ak.png"), size=(100, 100))
    ICON_M16 = customtkinter.CTkImage(Image.open("Assets\\M16.png"), size=(100, 100))
    ICON_DART = customtkinter.CTkImage(Image.open("Assets\\Dart.png"), size=(100, 100))
    ICON_DARTFLY = customtkinter.CTkImage(Image.open("Assets\\Dartfly.png"), size=(100, 100))
    ICON_HUNTING_RIFLE = customtkinter.CTkImage(Image.open("Assets\\HuntingRifle.png"), size=(100, 100))
    ICON_SNIPER = customtkinter.CTkImage(Image.open("Assets\\Sniper.png"), size=(100, 100))
    ICON_LASER = customtkinter.CTkImage(Image.open("Assets\\Laser.png"), size=(100, 100))
    ICON_MINIGUN = customtkinter.CTkImage(Image.open("Assets\\Minigun.png"), size=(100, 100))
    ICON_BOW = customtkinter.CTkImage(Image.open("Assets\\Bow.png"), size=(100, 100))
    ICON_SPARROW_LAUNCHER = customtkinter.CTkImage(Image.open("Assets\\SparrowLauncher.png"), size=(100, 100))
    ICON_BCG = customtkinter.CTkImage(Image.open("Assets\\Bcg.png"), size=(100, 100))
    ICON_LITTLE_AMMO = customtkinter.CTkImage(Image.open("Assets\\LittleAmmo.png"), size=(45, 30))
    ICON_BIG_AMMO = customtkinter.CTkImage(Image.open("Assets\\BigAmmo.png"), size=(45, 30))
    ICON_SHELLS_AMMO = customtkinter.CTkImage(Image.open("Assets\\ShellsAmmo.png"), size=(45, 30))
    ICON_SNIPER_AMMO = customtkinter.CTkImage(Image.open("Assets\\SniperAmmo.png"), size=(45, 30))
    ICON_SPECIAL_AMMO = customtkinter.CTkImage(Image.open("Assets\\SpecialAmmo.png"), size=(45, 30))
    ICON_LASER_AMMO = customtkinter.CTkImage(Image.open("Assets\\LaserAmmo.png"), size=(45, 30))
    ICON_JUICE = customtkinter.CTkImage(Image.open("Assets\\Juice.png"), size=(80, 80))
    ICON_TAPE = customtkinter.CTkImage(Image.open("Assets\\Tape.png"), size=(30, 30))
    ICON_GRENADE = customtkinter.CTkImage(Image.open("Assets\\Grenade.png"), size=(30, 30))
    ICON_BANANA = customtkinter.CTkImage(Image.open("Assets\\Banana.png"), size=(30, 30))
    ICON_ZIPLINE = customtkinter.CTkImage(Image.open("Assets\\Zipline.png"), size=(30, 30))
    ICON_CLAW_BOOTS = customtkinter.CTkImage(Image.open("Assets\\ClawBoots.png"), size=(30, 30))
    ICON_BANANA_FORK = customtkinter.CTkImage(Image.open("Assets\\BananaFork.png"), size=(30, 30))
    ICON_NINJA_BOOTS = customtkinter.CTkImage(Image.open("Assets\\NinjaBoots.png"), size=(30, 30))
    ICON_SNORKEL = customtkinter.CTkImage(Image.open("Assets\\Snorkel.png"), size=(30, 30))
    ICON_CUPGRADE = customtkinter.CTkImage(Image.open("Assets\\Cupgrade.png"), size=(30, 30))
    ICON_BANDOLIER = customtkinter.CTkImage(Image.open("Assets\\Bandolier.png"), size=(30, 30))
    ICON_IMPOSSIBLE_TAPE = customtkinter.CTkImage(Image.open("Assets\\ImpossibleTape.png"), size=(30, 30))
    ICON_JUICER = customtkinter.CTkImage(Image.open("Assets\\Juicer.png"), size=(30, 30))
    ICON_ARMOR1 = customtkinter.CTkImage(Image.open("Assets\\Armor1.png"), size=(80, 80))
    ICON_ARMOR2 = customtkinter.CTkImage(Image.open("Assets\\Armor2.png"), size=(80, 80))
    ICON_ARMOR3 = customtkinter.CTkImage(Image.open("Assets\\Armor3.png"), size=(80, 80))
    ICON_EMU = customtkinter.CTkImage(Image.open("Assets\\Emu.png"), size=(80, 80))
    ICON_HAMBALL = customtkinter.CTkImage(Image.open("Assets\\Hamball.png"), size=(80, 80))
    ICON_PIN = customtkinter.CTkImage(Image.open("Assets\\Pin.png"), size=(20, 20))
    ICON_PIN_VERTICAL = customtkinter.CTkImage(Image.open("Assets\\PinVertical.png"), size=(26, 26))
    ICON_DICE = customtkinter.CTkImage(Image.open("Assets\\Dice.png"), size=(15, 15))

# Info
class InfoMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("880x150")
        self.title("Private Game Helper - Info")
        self.resizable(False, False)
        self.font_title = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.font_regular = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        
        customtkinter.CTkLabel(self, 
                               text="Made by Suchy499", 
                               font=self.font_title).place(x=20, y=20)
        customtkinter.CTkLabel(self, 
                               text=
                               "Important:\n"
                               "- Only apply settings once per custom lobby\n"
                               "- After using 'Apply Settings', do not press any keys until the program has finished working\n"
                               "For any kind of help, you can reach me through discord!", 
                               font=self.font_regular, 
                               justify="left").place(x=20, y=60)
        customtkinter.CTkLabel(self, 
                               width=80, 
                               height=80, 
                               text="", 
                               image=Images.AVATAR).place(x=770, y=40)

# Other commands
class CommandsMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("780x310")
        self.title("Private Game Helper - Other Commands")
        self.resizable(False, False)
        self.font_title = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.font_regular = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        
        self.other_commands_title = customtkinter.CTkLabel(self,
                                                           text="Other Commands",
                                                           font=self.font_title).place(x=20, y=20)
        self.flight = customtkinter.CTkButton(self,
                                              text="/flight",
                                              command=self.flight_ctrl)
        self.flight.place(x=20, y=60)
        self.flight_tooltip = CTkToolTip(self.flight,
                                         delay=0,
                                         message="Can be used to regenerate the Eagle flight path. Must run before the game timer has started.")
        self.noboss = customtkinter.CTkButton(self,
                                              text="/noboss",
                                              command=self.noboss_ctrl)
        self.noboss.place(x=20, y=100)
        self.noboss_tooltip = CTkToolTip(self.noboss,
                                         delay=0,
                                         message="Toggle to enable or disable Giant Star-nosed Mole from arriving.")
        self.soccer = customtkinter.CTkButton(self,
                                              text="/soccer",
                                              command=self.soccer_ctrl)
        self.soccer.place(x=20, y=140)
        self.soccer_tooltip = CTkToolTip(self.soccer,
                                         delay=0,
                                         message="Spawns a Fox Ball (only 1 at a time).")
        self.rain = customtkinter.CTkButton(self,
                                            text="/rain",
                                            command=self.rain_ctrl)
        self.rain.place(x=20, y=180)
        self.rain_tooltip = CTkToolTip(self.rain,
                                       delay=0,
                                       message="Forces a rain weather event.")
        self.rainoff = customtkinter.CTkButton(self,
                                               text="/rainoff",
                                               command=self.rainoff_ctrl)
        self.rainoff.place(x=20, y=220)
        self.rainoff_tooltip = CTkToolTip(self.rainoff,
                                          delay=0,
                                          message="Disables rain for entirity of a match. Won't work if it's already raining in-game.")
        self.night = customtkinter.CTkButton(self,
                                             text="/night",
                                             command=self.night_ctrl)
        self.night.place(x=170, y=60)
        self.night_tooltip = CTkToolTip(self.night,
                                        delay=0,
                                        message="Toggles the night mode.")
        self.getplayers = customtkinter.CTkButton(self,
                                                  text="/getplayers",
                                                  command=self.getplayers_ctrl)
        self.getplayers.place(x=170, y=100)
        self.getplayers_tooltip = CTkToolTip(self.getplayers,
                                             delay=0,
                                             message="Copies a list of all players in the match. After running the command, can be pasted into notepad.\n"
                                             "At the end of a match, you can use this command to grab the stats of the players.")
        self.gasstart = customtkinter.CTkButton(self,
                                                text="/gasstart",
                                                command=self.gasstart_ctrl)
        self.gasstart.place(x=170, y=140)
        self.gasstart_tooltip = CTkToolTip(self.gasstart,
                                           delay=0,
                                           message="Makes the first skunk gas timer start right away (if in lobby, it just means it'll start right when the eagle starts).")
        self.boss = customtkinter.CTkButton(self,
                                            text="/boss",
                                            command=self.boss_ctrl)
        self.boss.place(x=170, y=180)
        self.boss_tooltip = CTkToolTip(self.boss,
                                       delay=0,
                                       message="Spawns a Giant Star-nosed Mole.")
        self.getpid = customtkinter.CTkButton(self,
                                              text="/getpid",
                                              command=self.getpid_ctrl)
        self.getpid.place(x=170, y=220)
        self.getpid_tooltip = CTkToolTip(self.getpid,
                                         delay=0,
                                         message="Shows your in-game player id #.")
        self.mystery_options = customtkinter.CTkOptionMenu(self,
                                                           values=["Shotgun & Sniper", 
                                                                   "Wild West", 
                                                                   "Slow Bullets", 
                                                                   "Bananarama", 
                                                                   "Handguns Only", 
                                                                   "Fast Bullets", 
                                                                   "One Hit Kill"])
        self.mystery_options.place(x=20, y=260)
        self.mystery_select = customtkinter.CTkButton(self,
                                                      text="Select",
                                                      command=self.mystery_ctrl)
        self.mystery_select.place(x=170, y=260)
        self.mystery_select_tooltip = CTkToolTip(self.mystery_select,
                                                 delay=0,
                                                 message="In Mystery Mode, selects which mystery mode will be ran.")
        
        # Player specific commands
        self.player_specific_commands_title = customtkinter.CTkLabel(self,
                                                                     text="Player specific commands",
                                                                     font=self.font_title).place(x=400, y=20)
        self.player_id_text = customtkinter.CTkLabel(self,
                                                     text="Player ID:",
                                                     font=self.font_regular).place(x=400, y=60)
        self.player_id_input = customtkinter.CTkEntry(self,
                                                      placeholder_text="ID / all")
        self.player_id_input.place(x=550, y=60)
        self.saw = customtkinter.CTkButton(self,
                                           text="/saw #",
                                           command=self.saw_ctrl)
        self.saw.place(x=400, y=100)
        self.saw_tooltip = CTkToolTip(self.saw,
                                      delay=0,
                                      message="The command can be used to change the team of player with given ID to S.A.W. Security Forces.")
        self.admin = customtkinter.CTkButton(self,
                                             text="/admin #",
                                             command=self.admin_ctrl)
        self.admin.place(x=400, y=140)
        self.admin_tooltip = CTkToolTip(self.admin,
                                        delay=0,
                                        message="Makes the user a \"helper admin\" which allows them to use all of the admin commands except the kick command on the primary admin.\n"
                                        "Repeating the command on same user will revoke their helper admin status.")
        self.kick = customtkinter.CTkButton(self,
                                            text="/kick #",
                                            command=self.kick_ctrl)
        self.kick.place(x=400, y=180)
        self.kick_tooltip = CTkToolTip(self.kick,
                                       delay=0,
                                       message="Kicks player with specified in-game id #. Player cannot rejoin until next match.")
        self.getpos = customtkinter.CTkButton(self,
                                              text="/getpos #",
                                              command=self.getpos_ctrl)
        self.getpos.place(x=400, y=220)
        self.getpos_tooltip = CTkToolTip(self.getpos,
                                         delay=0,
                                         message="Tells you world position of a player with given number.")
        self.infect = customtkinter.CTkButton(self,
                                              text="/infect #",
                                              command=self.infect_ctrl)
        self.infect.place(x=400, y=260)
        self.infect_tooltip = CTkToolTip(self.infect,
                                         delay=0,
                                         message="Makes given player infected.")
        self.rebel = customtkinter.CTkButton(self,
                                             text="/rebel #",
                                             command=self.rebel_ctrl)
        self.rebel.place(x=550, y=100)
        self.rebel_tooltip = CTkToolTip(self.rebel,
                                        delay=0,
                                        message="The command can be used to change the team of player with given ID to Super Animal Super Resistance.")
        self.ghost = customtkinter.CTkButton(self,
                                             text="/ghost #",
                                             command=self.ghost_ctrl)
        self.ghost.place(x=550, y=140)
        self.ghost_tooltip = CTkToolTip(self.ghost,
                                        delay=0,
                                        message="Goes into spectate ghost mode. Can be run in lobby, or in-game after death only.")
        self.kill = customtkinter.CTkButton(self,
                                            text="/kill #",
                                            command=self.kill_ctrl)
        self.kill.place(x=550, y=180)
        self.kill_tooltip = CTkToolTip(self.kill,
                                       delay=0,
                                       message="Kills player (or bot) with specified in-game id #. Writing all in place of # will enable kill all players.\n"
                                       "Only works on players who have finished parachuting.")
        self.god = customtkinter.CTkButton(self,
                                           text="/god #",
                                           command=self.god_ctrl)
        self.god.place(x=550, y=220)
        self.god_tooltip = CTkToolTip(self.god,
                                      delay=0,
                                      message="Set a player to god-mode with ID #. Applies only to player damage. Writing all in place of # will enable god-mode for all players.")
        
        # Always on top
        self.alwaysontop_button = customtkinter.CTkButton(self, 
                                                          width=20,
                                                          height=20,
                                                          text="", 
                                                          image=Images.ICON_PIN, 
                                                          hover=False, 
                                                          fg_color="transparent",
                                                          bg_color="transparent", 
                                                          command=self.always_on_top)
        self.alwaysontop_button.place(x=730, y=20)
        self.alwaysontop_tooltip = CTkToolTip(self.alwaysontop_button, 
                                              delay=0,
                                              message="Keep this window on top")
    
    def flight_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/flight", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def noboss_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/noboss", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            
    def soccer_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/soccer", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            
    def rain_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/rain", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def rainoff_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/rainoff", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def night_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/night", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            
    def getplayers_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/getplayers", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            
    def gasstart_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/gasstart", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def boss_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/boss", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def getpid_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/getpid", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def saw_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/saw {self.player_id_input.get()}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def admin_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/admin {self.player_id_input.get()}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def kick_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/kick {self.player_id_input.get()}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def getpos_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/getpos {self.player_id_input.get()}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            
    def infect_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/infect {self.player_id_input.get()}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def rebel_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/rebel {self.player_id_input.get()}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def ghost_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/ghost {self.player_id_input.get()}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def kill_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/kill {self.player_id_input.get()}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def god_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/god {self.player_id_input.get()}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def mystery_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            match self.mystery_options.get():
                case "Shotgun & Sniper": mystery_mode = 0
                case "Wild West": mystery_mode = 1
                case "Slow Bullets": mystery_mode = 2
                case "Bananarama": mystery_mode = 3
                case "Handguns Only": mystery_mode = 4
                case "Fast Bullets": mystery_mode = 5
                case "One Hit Kill": mystery_mode = 6
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/mystery {mystery_mode}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
    
    def always_on_top(self):
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.alwaysontop_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.alwaysontop_button.configure(image=Images.ICON_PIN_VERTICAL)

# Spawning menu
class SpawningMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1350x520")
        self.title("Private Game Helper - Spawning Menu")
        self.resizable(False, False)
        self.font_title = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.font_regular = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        self.selected_rarity = 2
        
        # Spawn Guns
        self.spawn_guns_title = customtkinter.CTkLabel(self, 
                                                       text="Spawn Guns", 
                                                       font=self.font_title).place(x=20, y=20)
        self.rarity_common = customtkinter.CTkButton(self, 
                                                     width=100, 
                                                     height=24, 
                                                     text="", 
                                                     image=Images.RARITY_COMMON_OFF, 
                                                     fg_color="transparent", 
                                                     bg_color="transparent", 
                                                     hover=False, 
                                                     command= lambda: self.select_rarity("common"))
        self.rarity_common.place(x=20, y=60)
        self.rarity_uncommon = customtkinter.CTkButton(self, 
                                                       width=100, 
                                                       height=24, 
                                                       text="", 
                                                       image=Images.RARITY_UNCOMMON_OFF, 
                                                       fg_color="transparent", 
                                                       bg_color="transparent", 
                                                       hover=False, 
                                                       command= lambda: self.select_rarity("uncommon"))
        self.rarity_uncommon.place(x=130, y=60)
        self.rarity_rare = customtkinter.CTkButton(self, 
                                                   width=100, 
                                                   height=24, 
                                                   text="", 
                                                   image=Images.RARITY_RARE, 
                                                   fg_color="transparent", 
                                                   bg_color="transparent", 
                                                   hover=False, 
                                                   command= lambda: self.select_rarity("rare"))
        self.rarity_rare.place(x=240, y=60)
        self.rarity_epic = customtkinter.CTkButton(self, 
                                                   width=100,
                                                   height=24, 
                                                   text="", 
                                                   image=Images.RARITY_EPIC_OFF, 
                                                   fg_color="transparent", 
                                                   bg_color="transparent", 
                                                   hover=False, 
                                                   command= lambda: self.select_rarity("epic"))
        self.rarity_epic.place(x=350, y=60)
        self.rarity_legendary = customtkinter.CTkButton(self,
                                                        width=100, 
                                                        height=24,
                                                        text="", 
                                                        image=Images.RARITY_LEGENDARY_OFF, 
                                                        fg_color="transparent", 
                                                        bg_color="transparent", 
                                                        hover=False,
                                                        command= lambda: self.select_rarity("legendary"))
        self.rarity_legendary.place(x=460, y=60)
        self.spawn_pistol = customtkinter.CTkButton(self,
                                                    width=100, 
                                                    height=100, 
                                                    text="", 
                                                    image=Images.ICON_PISTOL, 
                                                    fg_color="transparent",
                                                    bg_color="transparent", 
                                                    hover=False, command= lambda: self.spawn_weapon_ctrl(0))
        self.spawn_pistol.place(x=20, y=90)
        self.spawn_dualies = customtkinter.CTkButton(self, 
                                                     width=100,
                                                     height=100, 
                                                     text="", 
                                                     image=Images.ICON_DUALIES, 
                                                     fg_color="transparent", 
                                                     bg_color="transparent", 
                                                     hover=False, 
                                                     command= lambda: self.spawn_weapon_ctrl(1))
        self.spawn_dualies.place(x=130, y=90)
        self.spawn_magnum = customtkinter.CTkButton(self, 
                                                    width=100, 
                                                    height=100, 
                                                    text="", 
                                                    image=Images.ICON_MAGNUM, 
                                                    fg_color="transparent", 
                                                    bg_color="transparent", 
                                                    hover=False, 
                                                    command= lambda: self.spawn_weapon_ctrl(2))
        self.spawn_magnum.place(x=240, y=90)
        self.spawn_deagle = customtkinter.CTkButton(self, 
                                                    width=100, 
                                                    height=100, 
                                                    text="", 
                                                    image=Images.ICON_DEAGLE, 
                                                    fg_color="transparent", 
                                                    bg_color="transparent", 
                                                    hover=False, 
                                                    command= lambda: self.spawn_weapon_ctrl(3))
        self.spawn_deagle.place(x=350, y=90)
        self.spawn_silenced_pistol = customtkinter.CTkButton(self, 
                                                             width=100,
                                                             height=100, 
                                                             text="", 
                                                             image=Images.ICON_SILENCED_PISTOL, 
                                                             fg_color="transparent",
                                                             bg_color="transparent", 
                                                             hover=False, 
                                                             command= lambda: self.spawn_weapon_ctrl(4))
        self.spawn_silenced_pistol.place(x=460, y=90)
        self.spawn_shotgun = customtkinter.CTkButton(self, 
                                                     width=100,
                                                     height=100, 
                                                     text="", 
                                                     image=Images.ICON_SHOTGUN, 
                                                     fg_color="transparent", 
                                                     bg_color="transparent",
                                                     hover=False, 
                                                     command= lambda: self.spawn_weapon_ctrl(5))
        self.spawn_shotgun.place(x=20, y=190)
        self.spawn_jag = customtkinter.CTkButton(self,
                                                 width=100,
                                                 height=100, 
                                                 text="", 
                                                 image=Images.ICON_JAG,
                                                 fg_color="transparent", 
                                                 bg_color="transparent", 
                                                 hover=False,
                                                 command= lambda: self.spawn_weapon_ctrl(6))
        self.spawn_jag.place(x=130, y=190)
        self.spawn_smg = customtkinter.CTkButton(self, 
                                                 width=100,
                                                 height=100, 
                                                 text="", 
                                                 image=Images.ICON_SMG,
                                                 fg_color="transparent", 
                                                 bg_color="transparent",
                                                 hover=False, 
                                                 command= lambda: self.spawn_weapon_ctrl(7))
        self.spawn_smg.place(x=240, y=190)
        self.spawn_tommy = customtkinter.CTkButton(self, 
                                                   width=100,
                                                   height=100, 
                                                   text="",
                                                   image=Images.ICON_TOMMY, 
                                                   fg_color="transparent", 
                                                   bg_color="transparent", 
                                                   hover=False, 
                                                   command= lambda: self.spawn_weapon_ctrl(8))
        self.spawn_tommy.place(x=350, y=190)
        self.spawn_ak = customtkinter.CTkButton(self, 
                                                width=100,
                                                height=100, 
                                                text="", 
                                                image=Images.ICON_AK, 
                                                fg_color="transparent",
                                                bg_color="transparent",
                                                hover=False, 
                                                command= lambda: self.spawn_weapon_ctrl(9))
        self.spawn_ak.place(x=460, y=190)
        self.spawn_m16 = customtkinter.CTkButton(self, 
                                                 width=100, 
                                                 height=100, 
                                                 text="", 
                                                 image=Images.ICON_M16,
                                                 fg_color="transparent", 
                                                 bg_color="transparent", 
                                                 hover=False, 
                                                 command= lambda: self.spawn_weapon_ctrl(10))
        self.spawn_m16.place(x=20, y=290)
        self.spawn_dart = customtkinter.CTkButton(self, 
                                                  width=100, 
                                                  height=100, 
                                                  text="",
                                                  image=Images.ICON_DART, 
                                                  fg_color="transparent", 
                                                  bg_color="transparent", 
                                                  hover=False, 
                                                  command= lambda: self.spawn_weapon_ctrl(11))
        self.spawn_dart.place(x=130, y=290)
        self.spawn_dartfly = customtkinter.CTkButton(self, 
                                                     width=100, 
                                                     height=100, 
                                                     text="", 
                                                     image=Images.ICON_DARTFLY, 
                                                     fg_color="transparent", 
                                                     bg_color="transparent", 
                                                     hover=False, 
                                                     command= lambda: self.spawn_weapon_ctrl(12))
        self.spawn_dartfly.place(x=240, y=290)
        self.spawn_hunting_rifle = customtkinter.CTkButton(self,
                                                           width=100,
                                                           height=100, 
                                                           text="",
                                                           image=Images.ICON_HUNTING_RIFLE,
                                                           fg_color="transparent", 
                                                           bg_color="transparent", 
                                                           hover=False, 
                                                           command= lambda: self.spawn_weapon_ctrl(13))
        self.spawn_hunting_rifle.place(x=350, y=290)
        self.spawn_sniper = customtkinter.CTkButton(self, width=100, 
                                                    height=100, 
                                                    text="", 
                                                    image=Images.ICON_SNIPER, 
                                                    fg_color="transparent", 
                                                    bg_color="transparent", 
                                                    hover=False, 
                                                    command= lambda: self.spawn_weapon_ctrl(14))
        self.spawn_sniper.place(x=460, y=290)
        self.spawn_laser = customtkinter.CTkButton(self,
                                                   width=100, 
                                                   height=100,
                                                   text="", 
                                                   image=Images.ICON_LASER, 
                                                   fg_color="transparent", 
                                                   bg_color="transparent",
                                                   hover=False, 
                                                   command= lambda: self.spawn_weapon_ctrl(15))
        self.spawn_laser.place(x=20, y=390)
        self.spawn_minigun = customtkinter.CTkButton(self, 
                                                     width=100, 
                                                     height=100, 
                                                     text="", 
                                                     image=Images.ICON_MINIGUN, 
                                                     fg_color="transparent",
                                                     bg_color="transparent", 
                                                     hover=False, 
                                                     command= lambda: self.spawn_weapon_ctrl(16))
        self.spawn_minigun.place(x=130, y=390)
        self.spawn_bow = customtkinter.CTkButton(self,
                                                 width=100, 
                                                 height=100,
                                                 text="", 
                                                 image=Images.ICON_BOW, 
                                                 fg_color="transparent", 
                                                 bg_color="transparent", 
                                                 hover=False, 
                                                 command= lambda: self.spawn_weapon_ctrl(17))
        self.spawn_bow.place(x=240, y=390)
        self.spawn_sparrow_launcher = customtkinter.CTkButton(self, 
                                                              width=100, 
                                                              height=100, 
                                                              text="", 
                                                              image=Images.ICON_SPARROW_LAUNCHER, 
                                                              fg_color="transparent", 
                                                              bg_color="transparent", 
                                                              hover=False, 
                                                              command= lambda: self.spawn_weapon_ctrl(18))
        self.spawn_sparrow_launcher.place(x=350, y=390)
        self.spawn_bcg = customtkinter.CTkButton(self, 
                                                 width=100, 
                                                 height=100, 
                                                 text="", 
                                                 image=Images.ICON_BCG,
                                                 fg_color="transparent",
                                                 bg_color="transparent", 
                                                 hover=False, 
                                                 command= lambda: self.spawn_weapon_ctrl(19))
        self.spawn_bcg.place(x=460, y=390)
        
        # Spawn Juice and Ammo
        self.spawn_ammo_title = customtkinter.CTkLabel(self, 
                                                       text="Spawn Juice and Ammo", 
                                                       font=self.font_title).place(x=620, y=20)
        self.ammo_slider = customtkinter.CTkSlider(self, 
                                                   width=280,
                                                   from_=10,
                                                   to=200, 
                                                   number_of_steps=19, 
                                                   command=self.ammo_slider_ctrl)
        self.ammo_slider.place(x=620, y=60)
        self.ammo_text = customtkinter.CTkLabel(self, 
                                                text="Amount:", 
                                                font=self.font_regular).place(x=620, y=80)
        self.label_ammo = customtkinter.CTkLabel(self, 
                                                 text="100", 
                                                 font=self.font_regular)
        self.label_ammo.place(x=870, y=80)
        self.spawn_little_ammo = customtkinter.CTkButton(self, 
                                                         width=45, 
                                                         height=30, 
                                                         text="",
                                                         image=Images.ICON_LITTLE_AMMO, 
                                                         fg_color="transparent",
                                                         bg_color="transparent", 
                                                         hover=False, 
                                                         command= lambda: self.spawn_ammo_ctrl(0))
        self.spawn_little_ammo.place(x=620, y=120)
        self.spawn_shells_ammo = customtkinter.CTkButton(self, 
                                                         width=45, 
                                                         height=30, 
                                                         text="", 
                                                         image=Images.ICON_SHELLS_AMMO,
                                                         fg_color="transparent", 
                                                         bg_color="transparent",
                                                         hover=False, 
                                                         command= lambda: self.spawn_ammo_ctrl(1))
        self.spawn_shells_ammo.place(x=730, y=120)
        self.spawn_big_ammo = customtkinter.CTkButton(self, 
                                                      width=45, 
                                                      height=30,
                                                      text="",
                                                      image=Images.ICON_BIG_AMMO,
                                                      fg_color="transparent", 
                                                      bg_color="transparent",
                                                      hover=False, 
                                                      command= lambda: self.spawn_ammo_ctrl(2))
        self.spawn_big_ammo.place(x=840, y=120)
        self.spawn_sniper_ammo = customtkinter.CTkButton(self, 
                                                         width=45,
                                                         height=30,
                                                         text="",
                                                         image=Images.ICON_SNIPER_AMMO,
                                                         fg_color="transparent", 
                                                         bg_color="transparent",
                                                         hover=False, 
                                                         command= lambda: self.spawn_ammo_ctrl(3))
        self.spawn_sniper_ammo.place(x=620, y=180)
        self.spawn_special_ammo = customtkinter.CTkButton(self, 
                                                          width=45, 
                                                          height=30, 
                                                          text="", 
                                                          image=Images.ICON_SPECIAL_AMMO, 
                                                          fg_color="transparent",
                                                          bg_color="transparent", 
                                                          hover=False, 
                                                          command= lambda: self.spawn_ammo_ctrl(4))
        self.spawn_special_ammo.place(x=730, y=180)
        self.spawn_laser_ammo = customtkinter.CTkButton(self, 
                                                        width=45, 
                                                        height=30, 
                                                        text="", 
                                                        image=Images.ICON_LASER_AMMO, 
                                                        fg_color="transparent", 
                                                        bg_color="transparent", 
                                                        hover=False, 
                                                        command= lambda: self.spawn_ammo_ctrl(5))
        self.spawn_laser_ammo.place(x=840, y=180)
        self.spawn_juice = customtkinter.CTkButton(self, 
                                                   width=80, 
                                                   height=80,
                                                   text="",
                                                   image=Images.ICON_JUICE, 
                                                   fg_color="transparent", 
                                                   bg_color="transparent",
                                                   hover=False, 
                                                   command=self.spawn_juice_ctrl)
        self.spawn_juice.place(x=720, y=240)
        
        # Spawn Tape and Grenades
        self.spawn_tape_title = customtkinter.CTkLabel(self,
                                                       text="Spawn Tape and Grenades", 
                                                       font=self.font_title).place(x=620, y=340)
        self.tape_slider = customtkinter.CTkSlider(self, 
                                                   width=280, 
                                                   from_=1, 
                                                   to=10, 
                                                   number_of_steps=9, 
                                                   command=self.tape_slider_ctrl)
        self.tape_slider.place(x=620, y=380)
        self.tape_text = customtkinter.CTkLabel(self, 
                                                text="Amount:", 
                                                font=self.font_regular).place(x=620, y=400)
        self.label_tape = customtkinter.CTkLabel(self, 
                                                 text="5", 
                                                 font=self.font_regular)
        self.label_tape.place(x=870, y=400)
        self.spawn_tape = customtkinter.CTkButton(self, 
                                                  width=30,
                                                  height=30,
                                                  text="",
                                                  image=Images.ICON_TAPE, 
                                                  fg_color="transparent", 
                                                  bg_color="transparent",
                                                  hover=False, 
                                                  command=self.spawn_tape_ctrl)
        self.spawn_tape.place(x=620, y=440)
        self.spawn_grenade = customtkinter.CTkButton(self, 
                                                     width=30, 
                                                     height=30, 
                                                     text="", 
                                                     image=Images.ICON_GRENADE, 
                                                     fg_color="transparent", 
                                                     bg_color="transparent", 
                                                     hover=False, 
                                                     command=self.spawn_grenade_ctrl)
        self.spawn_grenade.place(x=700, y=440)
        self.spawn_banana = customtkinter.CTkButton(self, 
                                                    width=30,
                                                    height=30, 
                                                    text="", 
                                                    image=Images.ICON_BANANA,
                                                    fg_color="transparent", 
                                                    bg_color="transparent", 
                                                    hover=False, 
                                                    command=self.spawn_banana_ctrl)
        self.spawn_banana.place(x=780, y=440)
        self.spawn_zip = customtkinter.CTkButton(self,
                                                 width=30,
                                                 height=30, 
                                                 text="", 
                                                 image=Images.ICON_ZIPLINE, 
                                                 fg_color="transparent", 
                                                 bg_color="transparent", 
                                                 hover=False, 
                                                 command=self.spawn_zip_ctrl)
        self.spawn_zip.place(x=860, y=440)

        # Spawn Powerups and Armor
        self.spawn_powerups_title = customtkinter.CTkLabel(self,
                                                           text="Spawn Powerups and Armor", 
                                                           font=self.font_title).place(x=950, y=20)
        self.spawn_claw_boots = customtkinter.CTkButton(self,
                                                        width=30,
                                                        height=30,
                                                        text="", 
                                                        image=Images.ICON_CLAW_BOOTS, 
                                                        fg_color="transparent",
                                                        bg_color="transparent", 
                                                        hover=False,
                                                        command= lambda: self.spawn_powerup_ctrl(0))
        self.spawn_claw_boots.place(x=950, y=120)
        self.spawn_banana_fork = customtkinter.CTkButton(self, 
                                                         width=30, 
                                                         height=30, 
                                                         text="", 
                                                         image=Images.ICON_BANANA_FORK,
                                                         fg_color="transparent",
                                                         bg_color="transparent", 
                                                         hover=False, 
                                                         command= lambda: self.spawn_powerup_ctrl(1))
        self.spawn_banana_fork.place(x=1040, y=120)
        self.spawn_ninja_boots = customtkinter.CTkButton(self, 
                                                         width=30, 
                                                         height=30, 
                                                         text="", 
                                                         image=Images.ICON_NINJA_BOOTS,
                                                         fg_color="transparent", 
                                                         bg_color="transparent",
                                                         hover=False, 
                                                         command= lambda: self.spawn_powerup_ctrl(2))
        self.spawn_ninja_boots.place(x=1130, y=120)
        self.spawn_snorkel = customtkinter.CTkButton(self, 
                                                     width=30,
                                                     height=30, 
                                                     text="", 
                                                     image=Images.ICON_SNORKEL, 
                                                     fg_color="transparent", 
                                                     bg_color="transparent", 
                                                     hover=False, 
                                                     command= lambda: self.spawn_powerup_ctrl(3))
        self.spawn_snorkel.place(x=1220, y=120)
        self.spawn_cupgrade = customtkinter.CTkButton(self, 
                                                      width=30,
                                                      height=30,
                                                      text="", 
                                                      image=Images.ICON_CUPGRADE, 
                                                      fg_color="transparent", 
                                                      bg_color="transparent", 
                                                      hover=False,
                                                      command= lambda: self.spawn_powerup_ctrl(4))
        self.spawn_cupgrade.place(x=950, y=180)
        self.spawn_bandolier = customtkinter.CTkButton(self,
                                                       width=30,
                                                       height=30, 
                                                       text="", 
                                                       image=Images.ICON_BANDOLIER, 
                                                       fg_color="transparent", 
                                                       bg_color="transparent",
                                                       hover=False, 
                                                       command= lambda: self.spawn_powerup_ctrl(5))
        self.spawn_bandolier.place(x=1040, y=180)
        self.spawn_impossible_tape = customtkinter.CTkButton(self, 
                                                             width=30,
                                                             height=30, 
                                                             text="", 
                                                             image=Images.ICON_IMPOSSIBLE_TAPE, 
                                                             fg_color="transparent", 
                                                             bg_color="transparent", 
                                                             hover=False, 
                                                             command= lambda: self.spawn_powerup_ctrl(6))
        self.spawn_impossible_tape.place(x=1130, y=180)
        self.spawn_juicer = customtkinter.CTkButton(self, 
                                                    width=30, 
                                                    height=30, 
                                                    text="", 
                                                    image=Images.ICON_JUICER, 
                                                    fg_color="transparent", 
                                                    bg_color="transparent", 
                                                    hover=False, 
                                                    command= lambda: self.spawn_powerup_ctrl(7))
        self.spawn_juicer.place(x=1220, y=180)
        self.spawn_armor1 = customtkinter.CTkButton(self, 
                                                    width=80, 
                                                    height=80, 
                                                    text="", 
                                                    image=Images.ICON_ARMOR1, 
                                                    fg_color="transparent", 
                                                    bg_color="transparent", 
                                                    hover=False, 
                                                    command= lambda: self.spawn_armor_ctrl(1))
        self.spawn_armor1.place(x=940, y=240)
        self.spawn_armor2 = customtkinter.CTkButton(self, 
                                                    width=80,
                                                    height=80,
                                                    text="",
                                                    image=Images.ICON_ARMOR2,
                                                    fg_color="transparent",
                                                    bg_color="transparent", 
                                                    hover=False, 
                                                    command= lambda: self.spawn_armor_ctrl(2))
        self.spawn_armor2.place(x=1055, y=240)
        self.spawn_armor3 = customtkinter.CTkButton(self, 
                                                    width=80, 
                                                    height=80, text="", 
                                                    image=Images.ICON_ARMOR3, 
                                                    fg_color="transparent",
                                                    bg_color="transparent",
                                                    hover=False,
                                                    command= lambda: self.spawn_armor_ctrl(3))
        self.spawn_armor3.place(x=1170, y=240)

        # Spawn Vehicles
        self.spawn_vehicles_title = customtkinter.CTkLabel(self, 
                                                           text="Spawn Vehicles",
                                                           font=self.font_title).place(x=950, y=340)
        self.spawn_emu = customtkinter.CTkButton(self, 
                                                 width=80,
                                                 height=80, 
                                                 text="", 
                                                 image=Images.ICON_EMU, 
                                                 fg_color="transparent", 
                                                 bg_color="transparent", 
                                                 hover=False, 
                                                 command=self.spawn_emu_ctrl)
        self.spawn_emu.place(x=940, y=400)
        self.spawn_hamball = customtkinter.CTkButton(self, 
                                                     width=80, 
                                                     height=80, 
                                                     text="", 
                                                     image=Images.ICON_HAMBALL, 
                                                     fg_color="transparent",
                                                     bg_color="transparent", 
                                                     hover=False, 
                                                     command=self.spawn_hamball_ctrl)
        self.spawn_hamball.place(x=1055, y=400)
        
        # Always on top
        self.alwaysontop_button = customtkinter.CTkButton(self, 
                                                          width=20,
                                                          height=20, 
                                                          text="", 
                                                          image=Images.ICON_PIN, 
                                                          hover=False,
                                                          fg_color="transparent", 
                                                          bg_color="transparent",
                                                          command=self.always_on_top)
        self.alwaysontop_button.place(x=1300, y=20)
        self.alwaysontop_tooltip = CTkToolTip(self.alwaysontop_button, 
                                              delay=0, 
                                              message="Keep this window on top")
        
    def select_rarity(self, rarity):
        match rarity:
            case "common":
                self.rarity_common.configure(image=Images.RARITY_COMMON)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON_OFF)
                self.rarity_rare.configure(image=Images.RARITY_RARE_OFF)
                self.rarity_epic.configure(image=Images.RARITY_EPIC_OFF)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY_OFF)
                self.selected_rarity = 0
            case "uncommon":
                self.rarity_common.configure(image=Images.RARITY_COMMON_OFF)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON)
                self.rarity_rare.configure(image=Images.RARITY_RARE_OFF)
                self.rarity_epic.configure(image=Images.RARITY_EPIC_OFF)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY_OFF)
                self.selected_rarity = 1
            case "rare":
                self.rarity_common.configure(image=Images.RARITY_COMMON_OFF)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON_OFF)
                self.rarity_rare.configure(image=Images.RARITY_RARE)
                self.rarity_epic.configure(image=Images.RARITY_EPIC_OFF)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY_OFF)
                self.selected_rarity = 2
            case "epic":
                self.rarity_common.configure(image=Images.RARITY_COMMON_OFF)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON_OFF)
                self.rarity_rare.configure(image=Images.RARITY_RARE_OFF)
                self.rarity_epic.configure(image=Images.RARITY_EPIC)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY_OFF)
                self.selected_rarity = 3
            case "legendary":
                self.rarity_common.configure(image=Images.RARITY_COMMON_OFF)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON_OFF)
                self.rarity_rare.configure(image=Images.RARITY_RARE_OFF)
                self.rarity_epic.configure(image=Images.RARITY_EPIC_OFF)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY)
                self.selected_rarity = 4
        
    def spawn_weapon_ctrl(self, id):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/gun{str(id)} {str(self.selected_rarity)}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def ammo_slider_ctrl(self, value):
        self.label_ammo.configure(text=int(value))
        
    def spawn_ammo_ctrl(self, id):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/ammo{str(id)} {str(round(self.ammo_slider.get()))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
                
    def spawn_juice_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/juice {str(round(self.ammo_slider.get()))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def tape_slider_ctrl(self, value):
        self.label_tape.configure(text=int(value))
        
    def spawn_tape_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/tape {str(round(self.tape_slider.get()))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def spawn_grenade_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/nade {str(round(self.tape_slider.get()))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def spawn_banana_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/banana {str(round(self.tape_slider.get()))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def spawn_zip_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/zip {str(round(self.tape_slider.get()))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def spawn_powerup_ctrl(self, id):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/util{str(id)}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def spawn_armor_ctrl(self, id):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/armor{str(id)}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def spawn_emu_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/emu", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
                
    def spawn_hamball_ctrl(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/hamball", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
        
    def always_on_top(self):
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.alwaysontop_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.alwaysontop_button.configure(image=Images.ICON_PIN_VERTICAL)
        
# Teleport Menu 
class TeleportMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("768x950")
        self.title("Private Game Helper - Teleport Menu")
        self.resizable(False, False)
        self.font_title = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.font_regular = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        self.mode_var = customtkinter.IntVar(value=0)
        
        self.title = customtkinter.CTkLabel(self, 
                                            text="Teleport Menu", 
                                            font=self.font_title).place(x=20, y=20)
        self.copy_instructions = customtkinter.CTkLabel(self, 
                                                        text=
                                                        "- Click on the map to copy the coordinates to your clipboard\n"
                                                        "- Type in game chat \"/tele [id/all] \"\n"
                                                        "- Press Ctrl + V to paste the coordinates",
                                                        font=self.font_regular, 
                                                        justify="left")
        self.copy_instructions.place(x=20, y=100)
        self.instant_teleport_instructions = customtkinter.CTkLabel(self,
                                                                    text=
                                                                    "- Type in a player's ID or \"All\"\n"
                                                                    "- Click on the map to teleport a player / all players to that location", 
                                                                    font=self.font_regular, 
                                                                    justify="left")
        self.player_id = customtkinter.CTkLabel(self,
                                                text="Player ID: ", 
                                                font=self.font_regular)
        self.input_id = customtkinter.CTkEntry(self, placeholder_text="ID / All")
        self.sar_map = customtkinter.CTkLabel(self, 
                                              width=768, 
                                              height=768, 
                                              text="", 
                                              image=Images.SAR_MAP)
        self.sar_map.place(x=0, y=182)
        self.sar_map.bind("<Button-1>", self.copy_coordinates)
        self.coordinates = customtkinter.CTkLabel(self, 
                                                  text="Coordinates:\n(x, y)", 
                                                  font=self.font_regular)
        self.coordinates.place(x=600, y=75)
        self.copy_mode = customtkinter.CTkRadioButton(self, 
                                                      text="Copy Mode", 
                                                      font=self.font_regular, 
                                                      variable=self.mode_var, 
                                                      value=0, 
                                                      command=self.change_mode)
        self.copy_mode.place(x=20, y=60)
        self.tele_mode = customtkinter.CTkRadioButton(self, 
                                                      text="Instant Teleport Mode", 
                                                      font=self.font_regular, 
                                                      variable=self.mode_var,
                                                      value=1,
                                                      command=self.change_mode)
        self.tele_mode.place(x=150, y=60)
        
        # Always on top
        self.alwaysontop_button = customtkinter.CTkButton(self,
                                                          width=20,
                                                          height=20, 
                                                          text="", 
                                                          image=Images.ICON_PIN,
                                                          hover=False, 
                                                          fg_color="transparent", 
                                                          bg_color="transparent", 
                                                          command=self.always_on_top)
        self.alwaysontop_button.place(x=720, y=20)
        self.alwaysontop_tooltip = CTkToolTip(self.alwaysontop_button, 
                                              delay=0,
                                              message="Keep this window on top")
        
    def copy_coordinates(self, event):
        x = event.x * 6
        y = (768 - event.y) * 6
        if self.mode_var.get() == 0:
            pyperclip.copy(f"{str(x)} {str(y)}")
            self.coordinates.configure(text=f"Coordinates:\n({str(x)}, {str(y)})")
        else:
            if self.input_id.get().isnumeric() and 1 <= int(self.input_id.get()) <= 99 or (self.input_id.get().lower() == "all"):
                self.coordinates.configure(text=f"Coordinates:\n({str(x)}, {str(y)})")
                if check_win_exist("Super Animal Royale"):
                    win_activate(window_title="Super Animal Royale", partial_match=False)
                    time.sleep(delay*2)
                    keyboard.send('enter')
                    time.sleep(delay*2)
                    keyboard.write(f"/tele {self.input_id.get().lower()} {str(x)} {str(y)}", delay=delay)
                    time.sleep(delay*2)
                    keyboard.send('enter')
            else:
                tkinter.messagebox.Message(self, message="Player ID has to be either \"all\" or between 1-99", parent=self).show()
    
    def change_mode(self):
        if self.mode_var.get() == 1:
            self.copy_instructions.place_forget()
            self.instant_teleport_instructions.place(x=20, y=95)
            self.player_id.place(x=20, y=145)
            self.input_id.place(x=110, y=145)
        else:
            self.instant_teleport_instructions.place_forget()
            self.player_id.place_forget()
            self.input_id.place_forget()
            self.copy_instructions.place(x=20, y=100)
    
    def always_on_top(self):
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.alwaysontop_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.alwaysontop_button.configure(image=Images.ICON_PIN_VERTICAL)

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1200x600")
        self.title("Private Game Helper")
        self.resizable(False, False)
        self.font_title = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.font_regular = customtkinter.CTkFont(family="Roboto", size=14, weight="bold")
        
        # Menu Bar
        self.menu_bar = CTkMenuBar(master=self)
        self.file_menu = self.menu_bar.add_cascade("File")
        self.file_dropdown = CustomDropdownMenu(widget=self.file_menu)
        self.file_dropdown.add_option(option="Open Preset", command=self.open_preset)
        self.file_dropdown.add_option(option="Save Preset", command=self.save_preset)
        self.file_dropdown.add_option(option="Restore Default", command=self.restore_default)
        self.info_menu_bar = self.menu_bar.add_cascade("Info", command=self.info_menu)
        
        # Main
        self.general_title = customtkinter.CTkLabel(self, 
                                                    text="General Settings", 
                                                    font=self.font_title).place(x=20, y=40)
        self.allitems_switch = customtkinter.CTkSwitch(self, 
                                                       text="All Items", 
                                                       font=self.font_regular, 
                                                       onvalue=1, 
                                                       offvalue=0)
        self.allitems_switch.place(x=20, y=80)
        self.allitems_switch.select()
        self.guns_switch = customtkinter.CTkSwitch(self,
                                                   text="Guns", 
                                                   font=self.font_regular, 
                                                   onvalue=1, 
                                                   offvalue=0)
        self.guns_switch.place(x=20, y=125)
        self.guns_switch.select()
        self.armors_switch = customtkinter.CTkSwitch(self, 
                                                     text="Armors",
                                                     font=self.font_regular,
                                                     onvalue=1, 
                                                     offvalue=0)
        self.armors_switch.place(x=20, y=170)
        self.armors_switch.select()
        self.throwables_switch = customtkinter.CTkSwitch(self, 
                                                         text="Throwables", 
                                                         font=self.font_regular,
                                                         onvalue=1,
                                                         offvalue=0)
        self.throwables_switch.place(x=20, y=215)
        self.throwables_switch.select()
        self.powerups_switch = customtkinter.CTkSwitch(self, 
                                                       text="Powerups",
                                                       font=self.font_regular,
                                                       onvalue=1, 
                                                       offvalue=0)
        self.powerups_switch.place(x=20, y=260)
        self.powerups_switch.select()
        self.onehits_switch = customtkinter.CTkSwitch(self, 
                                                      text="Onehits", 
                                                      font=self.font_regular, 
                                                      onvalue=1, 
                                                      offvalue=0)
        self.onehits_switch.place(x=20, y=305)
        self.onehits_switch.deselect()
        self.bots_switch = customtkinter.CTkSwitch(self, 
                                                   text="Bots",
                                                   font=self.font_regular, 
                                                   onvalue=1, 
                                                   offvalue=0)
        self.bots_switch.place(x=20, y=350)
        self.bots_switch.deselect()
        self.emus_switch = customtkinter.CTkSwitch(self, 
                                                   text="Emus",
                                                   font=self.font_regular, 
                                                   onvalue=1, 
                                                   offvalue=0)
        self.emus_switch.place(x=220, y=80)
        self.emus_switch.select()
        self.hamballs_switch = customtkinter.CTkSwitch(self, 
                                                       text="Hamballs", 
                                                       font=self.font_regular,
                                                       onvalue=1, 
                                                       offvalue=0)
        self.hamballs_switch.place(x=220, y=125)
        self.hamballs_switch.select()
        self.moles_switch = customtkinter.CTkSwitch(self, 
                                                    text="Moles", 
                                                    font=self.font_regular,
                                                    onvalue=1, 
                                                    offvalue=0)
        self.moles_switch.place(x=220, y=170)
        self.moles_switch.select()
        self.pets_switch = customtkinter.CTkSwitch(self,
                                                   text="Pets", 
                                                   font=self.font_regular, 
                                                   onvalue=1,
                                                   offvalue=0)
        self.pets_switch.place(x=220, y=215)
        self.pets_switch.select()
        self.gas_switch = customtkinter.CTkSwitch(self, 
                                                  text="Gas", 
                                                  font=self.font_regular, 
                                                  onvalue=1,
                                                  offvalue=0)
        self.gas_switch.place(x=220, y=260)
        self.gas_switch.select()
        self.norolls_switch = customtkinter.CTkSwitch(self, 
                                                      text="No Rolls", 
                                                      font=self.font_regular,
                                                      onvalue=1, 
                                                      offvalue=0)
        self.norolls_switch.place(x=220, y=305)
        self.norolls_switch.deselect()
        self.hpm = customtkinter.CTkEntry(self,
                                          width=50)
        self.hpm.place(x=220, y=347)
        self.hpm.insert(0, "250")
        self.hpm_text = customtkinter.CTkLabel(self,
                                               text="HPM",
                                               font=self.font_regular).place(x=280, y=347)
        self.gasspeed_slider = customtkinter.CTkSlider(self, 
                                                       width=160, 
                                                       from_=0.4,
                                                       to=3.0,
                                                       number_of_steps=26, 
                                                       command=self.gasspeed_slider_ctrl)
        self.gasspeed_slider.set(1.0)
        self.gasspeed_slider.place(x=20, y=400)
        self.gasspeed_text = customtkinter.CTkLabel(self, 
                                                    text="Gas Speed:",
                                                    font=self.font_regular).place(x=20, y=420)
        self.label_gasspeed = customtkinter.CTkLabel(self, 
                                                     text="1.0", 
                                                     font=self.font_regular)
        self.label_gasspeed.place(x=150, y=420)
        self.gasspeed_random = customtkinter.CTkButton(self,
                                                       width=15,
                                                       height=15,
                                                       text="",
                                                       image=Images.ICON_DICE,
                                                       hover=False,
                                                       fg_color="transparent",
                                                       bg_color="transparent",
                                                       command=self.randomize_gasspeed)
        self.gasspeed_random.place(x=120, y=422)
        self.gasdamage_slider = customtkinter.CTkSlider(self,
                                                        width=160,
                                                        from_=1.0, 
                                                        to=10.0, 
                                                        number_of_steps=90, 
                                                        command=self.gasdamage_slider_ctrl)
        self.gasdamage_slider.place(x=220, y=400)
        self.gasdamage_slider.set(1.0)
        self.gasdamage_text = customtkinter.CTkLabel(self, 
                                                     text="Gas Damage:", 
                                                     font=self.font_regular).place(x=220, y=420)
        self.label_gasdamage = customtkinter.CTkLabel(self, 
                                                      text="1.0",
                                                      font=self.font_regular)
        self.label_gasdamage.place(x=350, y=420)
        self.gasdamage_random = customtkinter.CTkButton(self,
                                                        width=15,
                                                        height=15,
                                                        text="",
                                                        image=Images.ICON_DICE,
                                                        hover=False,
                                                        fg_color="transparent",
                                                        bg_color="transparent",
                                                        command=self.randomize_gasdamage)
        self.gasdamage_random.place(x=320, y=422)
        self.bulletspeed_slider = customtkinter.CTkSlider(self, 
                                                          width=160,
                                                          from_=0.5, 
                                                          to=2.0, 
                                                          number_of_steps=15, 
                                                          command=self.bulletspeed_slider_ctrl)
        self.bulletspeed_slider.place(x=20, y=480)
        self.bulletspeed_slider.set(1.0)
        self.bulletspeed_text = customtkinter.CTkLabel(self, 
                                                       text="Bullet Speed:", 
                                                       font=self.font_regular).place(x=20, y=500)
        self.label_bulletspeed = customtkinter.CTkLabel(self, 
                                                        text="1.0", 
                                                        font=self.font_regular)
        self.label_bulletspeed.place(x=150, y=500)
        self.bulletspeed_random = customtkinter.CTkButton(self,
                                                          width=15,
                                                          height=15,
                                                          text="",
                                                          image=Images.ICON_DICE,
                                                          hover=False,
                                                          fg_color="transparent",
                                                          bg_color="transparent",
                                                          command=self.randomize_bulletspeed)
        self.bulletspeed_random.place(x=120, y=502)
        self.damage_slider = customtkinter.CTkSlider(self, 
                                                     width=160, 
                                                     from_=0.0, 
                                                     to=10.0, 
                                                     number_of_steps=100, 
                                                     command=self.damage_slider_ctrl)
        self.damage_slider.place(x=220, y=480)
        self.damage_slider.set(1.0)
        self.damage_text = customtkinter.CTkLabel(self, 
                                                  text="Damage:", 
                                                  font=self.font_regular).place(x=220, y=500)
        self.label_damage = customtkinter.CTkLabel(self, 
                                                   text="1.0", 
                                                   font=self.font_regular)
        self.label_damage.place(x=350, y=500)
        self.damage_random = customtkinter.CTkButton(self,
                                                     width=15,
                                                     height=15,
                                                     text="",
                                                     image=Images.ICON_DICE,
                                                     hover=False,
                                                     fg_color="transparent",
                                                     bg_color="transparent",
                                                     command=self.randomize_damage)
        self.damage_random.place(x=320, y=502)
        
        # Spawn rates
        self.spawnrates_title = customtkinter.CTkLabel(self, 
                                                       text="Spawn Rates",
                                                       font=self.font_title).place(x=420, y=40)
        self.pistol_slider = customtkinter.CTkSlider(self, 
                                                     width=160, 
                                                     from_=0.0,
                                                     to=5.0, 
                                                     number_of_steps=50, 
                                                     command=partial(self.weight_slider, "pistol"))
        self.pistol_slider.place(x=420, y=80)
        self.pistol_slider.set(1.0)
        self.pistol_text = customtkinter.CTkLabel(self, 
                                                  text="Pistol:", 
                                                  font=self.font_regular).place(x=420, y=100)
        self.label_pistol = customtkinter.CTkLabel(self,
                                                   text="1.0", 
                                                   font=self.font_regular)
        self.label_pistol.place(x=550, y=100)
        self.pistol_random = customtkinter.CTkButton(self,
                                                     width=15,
                                                     height=15,
                                                     text="",
                                                     image=Images.ICON_DICE,
                                                     hover=False,
                                                     fg_color="transparent",
                                                     bg_color="transparent",
                                                     command=partial(self.randomize_weapon, "pistol"))
        self.pistol_random.place(x=520, y=102)
        self.magnum_slider = customtkinter.CTkSlider(self, 
                                                     width=160,
                                                     from_=0.0,
                                                     to=5.0, 
                                                     number_of_steps=50, 
                                                     command=partial(self.weight_slider, "magnum"))
        self.magnum_slider.place(x=420, y=160)
        self.magnum_slider.set(1.0)
        self.magnum_text = customtkinter.CTkLabel(self, 
                                                  text="Magnum:", 
                                                  font=self.font_regular).place(x=420, y=180)
        self.label_magnum = customtkinter.CTkLabel(self,
                                                   text="1.0", 
                                                   font=self.font_regular)
        self.label_magnum.place(x=550, y=180)
        self.magnum_random = customtkinter.CTkButton(self,
                                                     width=15,
                                                     height=15,
                                                     text="",
                                                     image=Images.ICON_DICE,
                                                     hover=False,
                                                     fg_color="transparent",
                                                     bg_color="transparent",
                                                     command=partial(self.randomize_weapon, "magnum"))
        self.magnum_random.place(x=520, y=182)
        self.deagle_slider = customtkinter.CTkSlider(self, 
                                                     width=160, 
                                                     from_=0.0,
                                                     to=5.0, 
                                                     number_of_steps=50,
                                                     command=partial(self.weight_slider, "deagle"))
        self.deagle_slider.place(x=420, y=240)
        self.deagle_slider.set(1.0)
        self.deagle_text = customtkinter.CTkLabel(self, 
                                                  text="Deagle:", 
                                                  font=self.font_regular).place(x=420, y=260)
        self.label_deagle = customtkinter.CTkLabel(self,
                                                   text="1.0",
                                                   font=self.font_regular)
        self.label_deagle.place(x=550, y=260)
        self.deagle_random = customtkinter.CTkButton(self,
                                                     width=15,
                                                     height=15,
                                                     text="",
                                                     image=Images.ICON_DICE,
                                                     hover=False,
                                                     fg_color="transparent",
                                                     bg_color="transparent",
                                                     command=partial(self.randomize_weapon, "deagle"))
        self.deagle_random.place(x=520, y=262)
        self.silencedpistol_slider = customtkinter.CTkSlider(self,
                                                             width=160, 
                                                             from_=0.0, 
                                                             to=5.0, 
                                                             number_of_steps=50,
                                                             command=partial(self.weight_slider, "silencedpistol"))
        self.silencedpistol_slider.place(x=420, y=320)
        self.silencedpistol_slider.set(1.0)
        self.silencedpistol_text = customtkinter.CTkLabel(self, 
                                                          text="S. Pistol:",
                                                          font=self.font_regular).place(x=420, y=340)
        self.label_silencedpistol = customtkinter.CTkLabel(self, 
                                                           text="1.0", 
                                                           font=self.font_regular)
        self.label_silencedpistol.place(x=550, y=340)
        self.silencedpistol_random = customtkinter.CTkButton(self,
                                                             width=15,
                                                             height=15,
                                                             text="",
                                                             image=Images.ICON_DICE,
                                                             hover=False,
                                                             fg_color="transparent",
                                                             bg_color="transparent",
                                                             command=partial(self.randomize_weapon, "silencedpistol"))
        self.silencedpistol_random.place(x=520, y=342)
        self.shotgun_slider = customtkinter.CTkSlider(self, 
                                                      width=160,
                                                      from_=0.0,
                                                      to=5.0, 
                                                      number_of_steps=50, 
                                                      command=partial(self.weight_slider, "shotgun"))
        self.shotgun_slider.place(x=420, y=400)
        self.shotgun_slider.set(1.0)
        self.shotgun_text = customtkinter.CTkLabel(self, 
                                                   text="Shotgun:", 
                                                   font=self.font_regular).place(x=420, y=420)
        self.label_shotgun = customtkinter.CTkLabel(self, 
                                                    text="1.0", 
                                                    font=self.font_regular)
        self.label_shotgun.place(x=550, y=420)
        self.shotgun_random = customtkinter.CTkButton(self,
                                                      width=15,
                                                      height=15,
                                                      text="",
                                                      image=Images.ICON_DICE,
                                                      hover=False,
                                                      fg_color="transparent",
                                                      bg_color="transparent",
                                                      command=partial(self.randomize_weapon, "shotgun"))
        self.shotgun_random.place(x=520, y=422)
        self.jag_slider = customtkinter.CTkSlider(self,
                                                  width=160,
                                                  from_=0.0,
                                                  to=5.0, 
                                                  number_of_steps=50, 
                                                  command=partial(self.weight_slider, "jag"))
        self.jag_slider.place(x=420, y=480)
        self.jag_slider.set(1.0)
        self.jag_text = customtkinter.CTkLabel(self, 
                                               text="JAG-7:", 
                                               font=self.font_regular).place(x=420, y=500)
        self.label_jag = customtkinter.CTkLabel(self, 
                                                text="1.0",
                                                font=self.font_regular)
        self.label_jag.place(x=550, y=500)
        self.jag_random = customtkinter.CTkButton(self,
                                                  width=15,
                                                  height=15,
                                                  text="",
                                                  image=Images.ICON_DICE,
                                                  hover=False,
                                                  fg_color="transparent",
                                                  bg_color="transparent",
                                                  command=partial(self.randomize_weapon, "jag"))
        self.jag_random.place(x=520, y=502)
        self.smg_slider = customtkinter.CTkSlider(self, 
                                                  width=160, 
                                                  from_=0.0, 
                                                  to=5.0, 
                                                  number_of_steps=50, 
                                                  command=partial(self.weight_slider, "smg"))
        self.smg_slider.place(x=620, y=80)
        self.smg_slider.set(1.0)
        self.smg_text = customtkinter.CTkLabel(self, 
                                               text="SMG:", 
                                               font=self.font_regular).place(x=620, y=100)
        self.label_smg = customtkinter.CTkLabel(self, 
                                                text="1.0", 
                                                font=self.font_regular)
        self.label_smg.place(x=750, y=100)
        self.smg_random = customtkinter.CTkButton(self,
                                                  width=15,
                                                  height=15,
                                                  text="",
                                                  image=Images.ICON_DICE,
                                                  hover=False,
                                                  fg_color="transparent",
                                                  bg_color="transparent",
                                                  command=partial(self.randomize_weapon, "smg"))
        self.smg_random.place(x=720, y=102)
        self.tommy_slider = customtkinter.CTkSlider(self,
                                                    width=160, 
                                                    from_=0.0,
                                                    to=5.0,
                                                    number_of_steps=50, 
                                                    command=partial(self.weight_slider, "tommy"))
        self.tommy_slider.place(x=620, y=160)
        self.tommy_slider.set(1.0)
        self.tommy_text = customtkinter.CTkLabel(self,
                                                 text="Tommy Gun:", 
                                                 font=self.font_regular).place(x=620, y=180)
        self.label_tommy = customtkinter.CTkLabel(self, 
                                                  text="1.0",
                                                  font=self.font_regular)
        self.label_tommy.place(x=750, y=180)
        self.tommy_random = customtkinter.CTkButton(self,
                                                    width=15,
                                                    height=15,
                                                    text="",
                                                    image=Images.ICON_DICE,
                                                    hover=False,
                                                    fg_color="transparent",
                                                    bg_color="transparent",
                                                    command=partial(self.randomize_weapon, "tommy"))
        self.tommy_random.place(x=720, y=182)
        self.ak_slider = customtkinter.CTkSlider(self, 
                                                 width=160,
                                                 from_=0.0,
                                                 to=5.0, 
                                                 number_of_steps=50, 
                                                 command=partial(self.weight_slider, "ak"))
        self.ak_slider.place(x=620, y=240)
        self.ak_slider.set(1.0)
        self.ak_text = customtkinter.CTkLabel(self, 
                                              text="AK:",
                                              font=self.font_regular).place(x=620, y=260)
        self.label_ak = customtkinter.CTkLabel(self,
                                               text="1.0",
                                               font=self.font_regular)
        self.label_ak.place(x=750, y=260)
        self.ak_random = customtkinter.CTkButton(self,
                                                 width=15,
                                                 height=15,
                                                 text="",
                                                 image=Images.ICON_DICE,
                                                 hover=False,
                                                 fg_color="transparent",
                                                 bg_color="transparent",
                                                 command=partial(self.randomize_weapon, "ak"))
        self.ak_random.place(x=720, y=262)
        self.m16_slider = customtkinter.CTkSlider(self, 
                                                  width=160, 
                                                  from_=0.0,
                                                  to=5.0, 
                                                  number_of_steps=50,
                                                  command=partial(self.weight_slider, "m16"))
        self.m16_slider.place(x=620, y=320)
        self.m16_slider.set(1.0)
        self.m16_text = customtkinter.CTkLabel(self,
                                               text="M16:",
                                               font=self.font_regular).place(x=620, y=340)
        self.label_m16 = customtkinter.CTkLabel(self, 
                                                text="1.0",
                                                font=self.font_regular)
        self.label_m16.place(x=750, y=340)
        self.m16_random = customtkinter.CTkButton(self,
                                                  width=15,
                                                  height=15,
                                                  text="",
                                                  image=Images.ICON_DICE,
                                                  hover=False,
                                                  fg_color="transparent",
                                                  bg_color="transparent",
                                                  command=partial(self.randomize_weapon, "m16"))
        self.m16_random.place(x=720, y=342)
        self.dart_slider = customtkinter.CTkSlider(self, 
                                                   width=160, 
                                                   from_=0.0,
                                                   to=5.0, 
                                                   number_of_steps=50, 
                                                   command=partial(self.weight_slider, "dart"))
        self.dart_slider.place(x=620, y=400)
        self.dart_slider.set(1.0)
        self.dart_text = customtkinter.CTkLabel(self,
                                                text="Dart Gun:", 
                                                font=self.font_regular).place(x=620, y=420)
        self.label_dart = customtkinter.CTkLabel(self, 
                                                 text="1.0", 
                                                 font=self.font_regular)
        self.label_dart.place(x=750, y=420)
        self.dart_random = customtkinter.CTkButton(self,
                                                   width=15,
                                                   height=15,
                                                   text="",
                                                   image=Images.ICON_DICE,
                                                   hover=False,
                                                   fg_color="transparent",
                                                   bg_color="transparent",
                                                   command=partial(self.randomize_weapon, "dart"))
        self.dart_random.place(x=720, y=422)
        self.dartfly_slider = customtkinter.CTkSlider(self, 
                                                      width=160, 
                                                      from_=0.0, 
                                                      to=5.0,
                                                      number_of_steps=50, 
                                                      command=partial(self.weight_slider, "dartfly"))
        self.dartfly_slider.place(x=620, y=480)
        self.dartfly_slider.set(1.0)
        self.dartfly_text = customtkinter.CTkLabel(self, 
                                                   text="Dartfly Gun:",
                                                   font=self.font_regular).place(x=620, y=500)
        self.label_dartfly = customtkinter.CTkLabel(self, 
                                                    text="1.0",
                                                    font=self.font_regular)
        self.label_dartfly.place(x=750, y=500)
        self.dartfly_random = customtkinter.CTkButton(self,
                                                      width=15,
                                                      height=15,
                                                      text="",
                                                      image=Images.ICON_DICE,
                                                      hover=False,
                                                      fg_color="transparent",
                                                      bg_color="transparent",
                                                      command=partial(self.randomize_weapon, "dartfly"))
        self.dartfly_random.place(x=720, y=502)
        self.huntingrifle_slider = customtkinter.CTkSlider(self, 
                                                           width=160,
                                                           from_=0.0, 
                                                           to=5.0, 
                                                           number_of_steps=50, 
                                                           command=partial(self.weight_slider, "huntingrifle"))
        self.huntingrifle_slider.place(x=820, y=80)
        self.huntingrifle_slider.set(1.0)
        self.huntingrifle_text = customtkinter.CTkLabel(self, 
                                                        text="Hunting Rifle:", 
                                                        font=self.font_regular).place(x=820, y=100)
        self.label_huntingrifle = customtkinter.CTkLabel(self, 
                                                         text="1.0",
                                                         font=self.font_regular)
        self.label_huntingrifle.place(x=950, y=100)
        self.huntingrifle_random = customtkinter.CTkButton(self,
                                                           width=15,
                                                           height=15,
                                                           text="",
                                                           image=Images.ICON_DICE,
                                                           hover=False,
                                                           fg_color="transparent",
                                                           bg_color="transparent",
                                                           command=partial(self.randomize_weapon, "huntingrifle"))
        self.huntingrifle_random.place(x=920, y=102)
        self.sniper_slider = customtkinter.CTkSlider(self, 
                                                     width=160, 
                                                     from_=0.0,
                                                     to=5.0, 
                                                     number_of_steps=50, 
                                                     command=partial(self.weight_slider, "sniper"))
        self.sniper_slider.place(x=820, y=160)
        self.sniper_slider.set(1.0)
        self.sniper_text = customtkinter.CTkLabel(self, 
                                                  text="Sniper:", 
                                                  font=self.font_regular).place(x=820, y=180)
        self.label_sniper = customtkinter.CTkLabel(self, 
                                                   text="1.0", 
                                                   font=self.font_regular)
        self.label_sniper.place(x=950, y=180)
        self.sniper_random = customtkinter.CTkButton(self,
                                                     width=15,
                                                     height=15,
                                                     text="",
                                                     image=Images.ICON_DICE,
                                                     hover=False,
                                                     fg_color="transparent",
                                                     bg_color="transparent",
                                                     command=partial(self.randomize_weapon, "sniper"))
        self.sniper_random.place(x=920, y=182)
        self.laser_slider = customtkinter.CTkSlider(self, 
                                                    width=160, 
                                                    from_=0.0,
                                                    to=5.0,
                                                    number_of_steps=50, 
                                                    command=partial(self.weight_slider, "laser"))
        self.laser_slider.place(x=820, y=240)
        self.laser_slider.set(1.0)
        self.laser_text = customtkinter.CTkLabel(self, 
                                                 text="S. Laser:", 
                                                 font=self.font_regular).place(x=820, y=260)
        self.label_laser = customtkinter.CTkLabel(self, 
                                                  text="1.0", 
                                                  font=self.font_regular)
        self.label_laser.place(x=950, y=260)
        self.laser_random = customtkinter.CTkButton(self,
                                                    width=15,
                                                    height=15,
                                                    text="",
                                                    image=Images.ICON_DICE,
                                                    hover=False,
                                                    fg_color="transparent",
                                                    bg_color="transparent",
                                                    command=partial(self.randomize_weapon, "laser"))
        self.laser_random.place(x=920, y=262)
        self.minigun_slider = customtkinter.CTkSlider(self, 
                                                      width=160,
                                                      from_=0.0,
                                                      to=5.0, 
                                                      number_of_steps=50, 
                                                      command=partial(self.weight_slider, "minigun"))
        self.minigun_slider.place(x=820, y=320)
        self.minigun_slider.set(1.0)
        self.minigun_text = customtkinter.CTkLabel(self,
                                                   text="Minigun:", 
                                                   font=self.font_regular).place(x=820, y=340)
        self.label_minigun = customtkinter.CTkLabel(self, 
                                                    text="1.0", 
                                                    font=self.font_regular)
        self.label_minigun.place(x=950, y=340)
        self.minigun_random = customtkinter.CTkButton(self,
                                                      width=15,
                                                      height=15,
                                                      text="",
                                                      image=Images.ICON_DICE,
                                                      hover=False,
                                                      fg_color="transparent",
                                                      bg_color="transparent",
                                                      command=partial(self.randomize_weapon, "minigun"))
        self.minigun_random.place(x=920, y=342)
        self.bow_slider = customtkinter.CTkSlider(self,
                                                  width=160, 
                                                  from_=0.0,
                                                  to=5.0, 
                                                  number_of_steps=50, 
                                                  command=partial(self.weight_slider, "bow"))
        self.bow_slider.place(x=820, y=400)
        self.bow_slider.set(1.0)
        self.bow_text = customtkinter.CTkLabel(self,
                                               text="Bow:",
                                               font=self.font_regular).place(x=820, y=420)
        self.label_bow = customtkinter.CTkLabel(self, 
                                                text="1.0", 
                                                font=self.font_regular)
        self.label_bow.place(x=950, y=420)
        self.bow_random = customtkinter.CTkButton(self,
                                                  width=15,
                                                  height=15,
                                                  text="",
                                                  image=Images.ICON_DICE,
                                                  hover=False,
                                                  fg_color="transparent",
                                                  bg_color="transparent",
                                                  command=partial(self.randomize_weapon, "bow"))
        self.bow_random.place(x=920, y=422)
        self.sparrowlauncher_slider = customtkinter.CTkSlider(self, 
                                                              width=160, 
                                                              from_=0.0,
                                                              to=5.0, 
                                                              number_of_steps=50, 
                                                              command=partial(self.weight_slider, "sparrowlauncher"))
        self.sparrowlauncher_slider.place(x=820, y=480)
        self.sparrowlauncher_slider.set(1.0)
        self.sparrowlauncher_text = customtkinter.CTkLabel(self, 
                                                           text="S. Launcher:",
                                                           font=self.font_regular).place(x=820, y=500)
        self.label_sparrowlauncher = customtkinter.CTkLabel(self,
                                                            text="1.0",
                                                            font=self.font_regular)
        self.label_sparrowlauncher.place(x=950, y=500)
        self.sparrowlauncher_random = customtkinter.CTkButton(self,
                                                              width=15,
                                                              height=15,
                                                              text="",
                                                              image=Images.ICON_DICE,
                                                              hover=False,
                                                              fg_color="transparent",
                                                              bg_color="transparent",
                                                              command=partial(self.randomize_weapon, "sparrowlauncher"))
        self.sparrowlauncher_random.place(x=920, y=502)
        self.bcg_slider = customtkinter.CTkSlider(self,
                                                  width=160, 
                                                  from_=0.0, 
                                                  to=5.0, 
                                                  number_of_steps=50, 
                                                  command=partial(self.weight_slider, "bcg"))
        self.bcg_slider.place(x=1020, y=80)
        self.bcg_slider.set(1.0)
        self.bcg_text = customtkinter.CTkLabel(self, 
                                               text="BCG:", 
                                               font=self.font_regular).place(x=1020, y=100)
        self.label_bcg = customtkinter.CTkLabel(self,
                                                text="1.0", 
                                                font=self.font_regular)
        self.label_bcg.place(x=1150, y=100)
        self.bcg_random = customtkinter.CTkButton(self,
                                                  width=15,
                                                  height=15,
                                                  text="",
                                                  image=Images.ICON_DICE,
                                                  hover=False,
                                                  fg_color="transparent",
                                                  bg_color="transparent",
                                                  command=partial(self.randomize_weapon, "bcg"))
        self.bcg_random.place(x=1120, y=102)
        self.grenadefrag_slider = customtkinter.CTkSlider(self,
                                                          width=160,
                                                          from_=0.0,
                                                          to=5.0, 
                                                          number_of_steps=50,
                                                          command=partial(self.weight_slider, "grenadefrag"))
        self.grenadefrag_slider.place(x=1020, y=160)
        self.grenadefrag_slider.set(1.0)
        self.grenadefrag_text = customtkinter.CTkLabel(self, 
                                                       text="Grenade:", 
                                                       font=self.font_regular).place(x=1020, y=180)
        self.label_grenadefrag = customtkinter.CTkLabel(self, 
                                                        text="1.0", 
                                                        font=self.font_regular)
        self.label_grenadefrag.place(x=1150, y=180)
        self.grenadefrag_random = customtkinter.CTkButton(self,
                                                          width=15,
                                                          height=15,
                                                          text="",
                                                          image=Images.ICON_DICE,
                                                          hover=False,
                                                          fg_color="transparent",
                                                          bg_color="transparent",
                                                          command=partial(self.randomize_weapon, "grenadefrag"))
        self.grenadefrag_random.place(x=1120, y=182)
        self.grenadebanana_slider = customtkinter.CTkSlider(self, 
                                                            width=160, 
                                                            from_=0.0,
                                                            to=5.0, 
                                                            number_of_steps=50,
                                                            command=partial(self.weight_slider, "grenadebanana"))
        self.grenadebanana_slider.place(x=1020, y=240)
        self.grenadebanana_slider.set(1.0)
        self.grenadebanana_text = customtkinter.CTkLabel(self, 
                                                         text="Banana:", 
                                                         font=self.font_regular).place(x=1020, y=260)
        self.label_grenadebanana = customtkinter.CTkLabel(self, 
                                                          text="1.0", 
                                                          font=self.font_regular)
        self.label_grenadebanana.place(x=1150, y=260)
        self.grenadebanana_random = customtkinter.CTkButton(self,
                                                            width=15,
                                                            height=15,
                                                            text="",
                                                            image=Images.ICON_DICE,
                                                            hover=False,
                                                            fg_color="transparent",
                                                            bg_color="transparent",
                                                            command=partial(self.randomize_weapon, "grenadebanana"))
        self.grenadebanana_random.place(x=1120, y=262)
        self.grenadeskunk_slider = customtkinter.CTkSlider(self, 
                                                           width=160,
                                                           from_=0.0, 
                                                           to=5.0, 
                                                           number_of_steps=50,
                                                           command=partial(self.weight_slider, "grenadeskunk"))
        self.grenadeskunk_slider.place(x=1020, y=320)
        self.grenadeskunk_slider.set(1.0)
        self.grenadeskunk_text = customtkinter.CTkLabel(self,
                                                        text="Skunk Bomb:", 
                                                        font=self.font_regular).place(x=1020, y=340)
        self.label_grenadeskunk = customtkinter.CTkLabel(self, 
                                                         text="1.0",
                                                         font=self.font_regular)
        self.label_grenadeskunk.place(x=1150, y=340)
        self.grenadeskunk_random = customtkinter.CTkButton(self,
                                                           width=15,
                                                           height=15,
                                                           text="",
                                                           image=Images.ICON_DICE,
                                                           hover=False,
                                                           fg_color="transparent",
                                                           bg_color="transparent",
                                                           command=partial(self.randomize_weapon, "grenadeskunk"))
        self.grenadeskunk_random.place(x=1120, y=342)
        self.grenademine_slider = customtkinter.CTkSlider(self,
                                                          width=160, 
                                                          from_=0.0,
                                                          to=5.0,
                                                          number_of_steps=50,
                                                          command=partial(self.weight_slider, "grenademine"))
        self.grenademine_slider.place(x=1020, y=400)
        self.grenademine_slider.set(1.0)
        self.grenademine_text = customtkinter.CTkLabel(self, 
                                                       text="Cat Mine:", 
                                                       font=self.font_regular).place(x=1020, y=420)
        self.label_grenademine = customtkinter.CTkLabel(self, 
                                                        text="1.0", 
                                                        font=self.font_regular)
        self.label_grenademine.place(x=1150, y=420)
        self.grenademine_random = customtkinter.CTkButton(self,
                                                          width=15,
                                                          height=15,
                                                          text="",
                                                          image=Images.ICON_DICE,
                                                          hover=False,
                                                          fg_color="transparent",
                                                          bg_color="transparent",
                                                          command=partial(self.randomize_weapon, "grenademine"))
        self.grenademine_random.place(x=1120, y=422)
        self.grenadezip_slider = customtkinter.CTkSlider(self, 
                                                         width=160, 
                                                         from_=0.0,
                                                         to=5.0, 
                                                         number_of_steps=50,
                                                         command=partial(self.weight_slider, "grenadezip"))
        self.grenadezip_slider.place(x=1020, y=480)
        self.grenadezip_slider.set(1.0)
        self.grenadezip_text = customtkinter.CTkLabel(self, 
                                                      text="Zipline:",
                                                      font=self.font_regular).place(x=1020, y=500)
        self.label_grenadezip = customtkinter.CTkLabel(self, 
                                                       text="1.0", 
                                                       font=self.font_regular)
        self.label_grenadezip.place(x=1150, y=500)
        self.grenadezip_random = customtkinter.CTkButton(self,
                                                         width=15,
                                                         height=15,
                                                         text="",
                                                         image=Images.ICON_DICE,
                                                         hover=False,
                                                         fg_color="transparent",
                                                         bg_color="transparent",
                                                         command=partial(self.randomize_weapon, "grenadezip"))
        self.grenadezip_random.place(x=1120, y=502)
        self.spawningmenu_button = customtkinter.CTkButton(self, 
                                                           text="Spawning Menu", 
                                                           command=self.open_spawningmenu)
        self.spawningmenu_button.place(x=20, y=550)
        self.teleportmenu_button = customtkinter.CTkButton(self, 
                                                           text="Teleport Menu", 
                                                           command=self.open_teleportmenu)
        self.teleportmenu_button.place(x=170, y=550)
        self.commandsmenu_button = customtkinter.CTkButton(self, 
                                                           text="Other Commands", 
                                                           command=self.open_commandsmenu)
        self.commandsmenu_button.place(x=320, y=550)
        self.applysettings_button = customtkinter.CTkButton(self, 
                                                            text="Apply Settings",
                                                            command=self.apply_settings)
        self.applysettings_button.place(x=740, y=550)
        self.matchid_button = customtkinter.CTkButton(self, 
                                                      text="Match ID",
                                                      command=self.match_id)
        self.matchid_button.place(x=890, y=550)
        self.start_button = customtkinter.CTkButton(self, 
                                                    text="Start Match", 
                                                    command=self.start_match)
        self.start_button.place(x=1040, y=550)
        
        # Always on top
        self.alwaysontop_button = customtkinter.CTkButton(self, 
                                                          width=20,
                                                          height=20,
                                                          text="", 
                                                          image=Images.ICON_PIN, 
                                                          hover=False, 
                                                          fg_color="transparent",
                                                          bg_color="transparent", 
                                                          command=self.always_on_top)
        self.alwaysontop_button.place(x=1150, y=40)
        self.alwaysontop_tooltip = CTkToolTip(self.alwaysontop_button, 
                                              delay=0,
                                              message="Keep this window on top")
        
        # Randomize all
        self.all_random = customtkinter.CTkButton(self,
                                                  width=20,
                                                  height=20,
                                                  text="",
                                                  image=Images.ICON_DICE,
                                                  hover=False,
                                                  fg_color="transparent",
                                                  bg_color="transparent",
                                                  command=self.randomize_all)
        self.all_random.place(x=1120, y=45)
        self.all_random_tooltip = CTkToolTip(self.all_random,
                                             delay=0,
                                             message="Randomize all settings")

    # Slider Controls
    def gasspeed_slider_ctrl(self, value):
        value = round(value, 1)
        self.label_gasspeed.configure(text=value)
        self.gasspeed_slider.set(value)
        
    def gasdamage_slider_ctrl(self, value):
        value = round(value, 1)
        self.label_gasdamage.configure(text=value)
        self.gasdamage_slider.set(value)
        
    def bulletspeed_slider_ctrl(self, value):
        value = round(value, 1)
        self.label_bulletspeed.configure(text=value)
        self.bulletspeed_slider.set(value)

    def damage_slider_ctrl(self, value):
        value = round(value, 1)
        self.label_damage.configure(text=value)
        self.damage_slider.set(value)

    def weight_slider(self, weapon, value):
        exec(f"value = round({str(value)}, 1)\nself.label_{str(weapon)}.configure(text=value)\nself.{str(weapon)}_slider.set(value)")
    
    def randomize_gasspeed(self):
        value = round(random.uniform(0.4, 3.0), 1)
        self.label_gasspeed.configure(text=value)
        self.gasspeed_slider.set(value)
    
    def randomize_gasdamage(self):
        value = round(random.uniform(1.0, 10.0), 1)
        self.label_gasdamage.configure(text=value)
        self.gasdamage_slider.set(value)
        
    def randomize_bulletspeed(self):
        value = round(random.uniform(0.5, 2.0), 1)
        self.label_bulletspeed.configure(text=value)
        self.bulletspeed_slider.set(value)
        
    def randomize_damage(self):
        value = round(random.uniform(0.0, 10.0), 1)
        self.label_damage.configure(text=value)
        self.damage_slider.set(value)
    
    def randomize_weapon(self, weapon):
        exec(f"value = round(random.uniform(0.0, 5.0), 1)\nself.label_{str(weapon)}.configure(text=value)\nself.{str(weapon)}_slider.set(value)")
    
    def randomize_all(self):
        self.randomize_gasspeed()
        self.randomize_gasdamage()
        self.randomize_bulletspeed()
        self.randomize_damage()
        self.randomize_weapon("pistol")
        self.randomize_weapon("magnum")
        self.randomize_weapon("deagle")
        self.randomize_weapon("silencedpistol")
        self.randomize_weapon("shotgun")
        self.randomize_weapon("jag")
        self.randomize_weapon("smg")
        self.randomize_weapon("tommy")
        self.randomize_weapon("ak")
        self.randomize_weapon("m16")
        self.randomize_weapon("dart")
        self.randomize_weapon("dartfly")
        self.randomize_weapon("huntingrifle")
        self.randomize_weapon("sniper")
        self.randomize_weapon("laser")
        self.randomize_weapon("minigun")
        self.randomize_weapon("bow")
        self.randomize_weapon("sparrowlauncher")
        self.randomize_weapon("bcg")
        self.randomize_weapon("grenadefrag")
        self.randomize_weapon("grenadebanana")
        self.randomize_weapon("grenadeskunk")
        self.randomize_weapon("grenademine")
        self.randomize_weapon("grenadezip")
    
    # Button Controls
    def open_spawningmenu(self):
        if check_win_exist("Private Game Helper - Spawning Menu"):
            win_activate("Private Game Helper - Spawning Menu", partial_match=False)
        else:
            spawningmenu_window = SpawningMenu(self)
            spawningmenu_window.after(100, spawningmenu_window.lift)

    def open_teleportmenu(self):
        if check_win_exist("Private Game Helper - Teleport Menu"):
            win_activate("Private Game Helper - Teleport Menu", partial_match=False)
        else:
            teleportmenu_window = TeleportMenu(self)
            teleportmenu_window.after(100, teleportmenu_window.lift)
    
    def open_commandsmenu(self):
        if check_win_exist("Private Game Helper - Other Commands"):
            win_activate("Private Game Helper - Other Commands", partial_match=False)
        else:
            commandsmenu_window = CommandsMenu(self)
            commandsmenu_window.after(100, commandsmenu_window.lift)
            
    def apply_settings(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*4)
            if (self.allitems_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/allitems", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.guns_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/guns", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.armors_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/armors", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.throwables_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/throwables", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.powerups_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/utils", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.onehits_switch.get() == 1):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/onehits", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.emus_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/emus", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.hamballs_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/hamballs", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.moles_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/moles", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.pets_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/pets", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.gas_switch.get() == 0):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/gasoff", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.norolls_switch.get() == 1):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/noroll", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            if (self.hpm.get() != ""):
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write(f"/hpm {self.hpm.get()}", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/gasspeed {str(round(self.gasspeed_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/gasdmg {str(round(self.gasdamage_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/bulletspeed {str(round(self.bulletspeed_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/dmg {str(round(self.damage_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/weight gunpistol {str(round(self.pistol_slider.get(), 1))} gunmagnum {str(round(self.magnum_slider.get(), 1))} gundeagle {str(round(self.deagle_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/weight gunsilencedpistol {str(round(self.silencedpistol_slider.get(), 1))} gunshotgun {str(round(self.shotgun_slider.get(), 1))} gunjag7 {str(round(self.jag_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/weight gunsmg {str(round(self.smg_slider.get(), 1))} gunthomas {str(round(self.tommy_slider.get(), 1))} gunak {str(round(self.ak_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/weight gunm16 {str(round(self.m16_slider.get(), 1))} gundart {str(round(self.dart_slider.get(), 1))} gundartepic {str(round(self.dartfly_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/weight gunhuntingrifle {str(round(self.huntingrifle_slider.get(), 1))} gunsniper {str(round(self.sniper_slider.get(), 1))} gunlaser {str(round(self.laser_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/weight gunminigun {str(round(self.minigun_slider.get(), 1))} gunbow {str(round(self.bow_slider.get(), 1))} guncrossbow {str(round(self.sparrowlauncher_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/weight gunegglauncher {str(round(self.bcg_slider.get(), 1))} grenadefrag {str(round(self.grenadefrag_slider.get(), 1))} grenadebanana {str(round(self.grenadebanana_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write(f"/weight grenadeskunk {str(round(self.grenadeskunk_slider.get(), 1))} grenadecatmine {str(round(self.grenademine_slider.get(), 1))} grenadezipline {str(round(self.grenadezip_slider.get(), 1))}", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')

    def match_id(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            time.sleep(delay*2)
            keyboard.send('enter')
            time.sleep(delay*2)
            keyboard.write("/matchid", delay=delay)
            time.sleep(delay*2)
            keyboard.send('enter')

    def start_match(self):
        if check_win_exist("Super Animal Royale"):
            win_activate(window_title="Super Animal Royale", partial_match=False)
            if self.bots_switch.get() == 0:
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/startp", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')
            else:
                time.sleep(delay*2)
                keyboard.send('enter')
                time.sleep(delay*2)
                keyboard.write("/start", delay=delay)
                time.sleep(delay*2)
                keyboard.send('enter')

    def always_on_top(self):
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.alwaysontop_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.alwaysontop_button.configure(image=Images.ICON_PIN_VERTICAL)
    
    def open_preset(self):
        files = [('Config Files', '*.cfg'),
                ('Text Document', '*.txt'),
                ('All Files', '*.*')] 
        with askopenfile(mode='r', filetypes=files) as file:
            if file is not None:
                content = file.read().split("\n")
                settings = []
                for x in content:
                    setting = x.split("=")
                    settings.append(setting[1])
                self.allitems_switch.select() if int(settings[0]) == 1 else self.allitems_switch.deselect()
                self.guns_switch.select() if int(settings[1]) == 1 else self.guns_switch.deselect()
                self.armors_switch.select() if int(settings[2]) == 1 else self.armors_switch.deselect()
                self.throwables_switch.select() if int(settings[3]) == 1 else self.throwables_switch.deselect()
                self.powerups_switch.select() if int(settings[4]) == 1 else self.throwables_switch.deselect()
                self.onehits_switch.select() if int(settings[5]) == 1 else self.onehits_switch.deselect()
                self.emus_switch.select() if int(settings[6]) == 1 else self.emus_switch.deselect()
                self.hamballs_switch.select() if int(settings[7]) == 1 else self.hamballs_switch.deselect()
                self.moles_switch.select() if int(settings[8]) == 1 else self.moles_switch.deselect()
                self.pets_switch.select() if int(settings[9]) == 1 else self.pets_switch.deselect()
                self.gas_switch.select() if int(settings[10]) == 1 else self.gas_switch.deselect()
                self.norolls_switch.select() if int(settings[11]) == 1 else self.norolls_switch.deselect()
                self.bots_switch.select() if int(settings[40]) == 1 else self.bots_switch.deselect()
                self.gasspeed_slider.set(float(settings[12]))
                self.label_gasspeed.configure(text=settings[12])
                self.gasdamage_slider.set(float(settings[13]))
                self.label_gasdamage.configure(text=settings[13])
                self.bulletspeed_slider.set(float(settings[14]))
                self.label_bulletspeed.configure(text=settings[14])
                self.damage_slider.set(float(settings[15]))
                self.label_damage.configure(text=settings[15])
                self.pistol_slider.set(float(settings[16]))
                self.label_pistol.configure(text=settings[16])
                self.magnum_slider.set(float(settings[17]))
                self.label_magnum.configure(text=settings[17])
                self.deagle_slider.set(float(settings[18]))
                self.label_deagle.configure(text=settings[18])
                self.silencedpistol_slider.set(float(settings[19]))
                self.label_silencedpistol.configure(text=settings[19])
                self.shotgun_slider.set(float(settings[20]))
                self.label_shotgun.configure(text=settings[20])
                self.jag_slider.set(float(settings[21]))
                self.label_jag.configure(text=settings[21])
                self.smg_slider.set(float(settings[22]))
                self.label_smg.configure(text=settings[22])
                self.tommy_slider.set(float(settings[23]))
                self.label_tommy.configure(text=settings[23])
                self.ak_slider.set(float(settings[24]))
                self.label_ak.configure(text=settings[24])
                self.m16_slider.set(float(settings[25]))
                self.label_m16.configure(text=settings[25])
                self.dart_slider.set(float(settings[26]))
                self.label_dart.configure(text=settings[26])
                self.dartfly_slider.set(float(settings[27]))
                self.label_dartfly.configure(text=settings[27])
                self.huntingrifle_slider.set(float(settings[28]))
                self.label_huntingrifle.configure(text=settings[28])
                self.sniper_slider.set(float(settings[29]))
                self.label_sniper.configure(text=settings[29])
                self.laser_slider.set(float(settings[30]))
                self.label_laser.configure(text=settings[30])
                self.minigun_slider.set(float(settings[31]))
                self.label_minigun.configure(text=settings[31])
                self.bow_slider.set(float(settings[32]))
                self.label_bow.configure(text=settings[32])
                self.sparrowlauncher_slider.set(float(settings[33]))
                self.label_sparrowlauncher.configure(text=settings[33])
                self.bcg_slider.set(float(settings[34]))
                self.label_bcg.configure(text=settings[34])
                self.grenadefrag_slider.set(float(settings[35]))
                self.label_grenadefrag.configure(text=settings[35])
                self.grenadebanana_slider.set(float(settings[36]))
                self.label_grenadebanana.configure(text=settings[36])
                self.grenadeskunk_slider.set(float(settings[37]))
                self.label_grenadeskunk.configure(text=settings[37])
                self.grenademine_slider.set(float(settings[38]))
                self.label_grenademine.configure(text=settings[38])
                self.grenadezip_slider.set(float(settings[39]))
                self.label_grenadezip.configure(text=settings[39])
                self.hpm.delete(0, 99)
                self.hpm.insert(0, settings[41])

    def save_preset(self):
        files = [('Config Files', '*.cfg')] 
        with asksaveasfile(filetypes=files, defaultextension=files, initialfile="DefaultPreset.cfg") as file:
            if file is not None:
                file.write(f"ALL_ITEMS={str(round(self.allitems_switch.get(), 1))}\n")
                file.write(f"GUNS={str(round(self.guns_switch.get(), 1))}\n")
                file.write(f"ARMORS={str(round(self.armors_switch.get(), 1))}\n")
                file.write(f"THROWABLES={str(round(self.throwables_switch.get(), 1))}\n")
                file.write(f"POWERUPS={str(round(self.powerups_switch.get(), 1))}\n")
                file.write(f"ONEHITS={str(round(self.onehits_switch.get(), 1))}\n")
                file.write(f"EMUS={str(round(self.emus_switch.get(), 1))}\n")
                file.write(f"HAMBALLS={str(round(self.hamballs_switch.get(), 1))}\n")
                file.write(f"MOLES={str(round(self.moles_switch.get(), 1))}\n")
                file.write(f"PETS={str(round(self.pets_switch.get(), 1))}\n")
                file.write(f"GAS={str(round(self.gas_switch.get(), 1))}\n")
                file.write(f"NOROLLS={str(round(self.norolls_switch.get(), 1))}\n")
                file.write(f"GAS_SPEED={str(round(self.gasspeed_slider.get(), 1))}\n")
                file.write(f"GAS_DAMAGE={str(round(self.gasdamage_slider.get(), 1))}\n")
                file.write(f"BULLET_SPEED={str(round(self.bulletspeed_slider.get(), 1))}\n")
                file.write(f"DAMAGE={str(round(self.damage_slider.get(), 1))}\n")
                file.write(f"PISTOL={str(round(self.pistol_slider.get(), 1))}\n")
                file.write(f"MAGNUM={str(round(self.magnum_slider.get(), 1))}\n")
                file.write(f"DEAGLE={str(round(self.deagle_slider.get(), 1))}\n")
                file.write(f"SILENCED_PISTOL={str(round(self.silencedpistol_slider.get(), 1))}\n")
                file.write(f"SHOTGUN={str(round(self.shotgun_slider.get(), 1))}\n")
                file.write(f"JAG-7={str(round(self.jag_slider.get(), 1))}\n")
                file.write(f"SMG={str(round(self.smg_slider.get(), 1))}\n")
                file.write(f"TOMMY_GUN={str(round(self.tommy_slider.get(), 1))}\n")
                file.write(f"AK={str(round(self.ak_slider.get(), 1))}\n")
                file.write(f"M16={str(round(self.m16_slider.get(), 1))}\n")
                file.write(f"DART={str(round(self.dart_slider.get(), 1))}\n")
                file.write(f"DARTFLY={str(round(self.dartfly_slider.get(), 1))}\n")
                file.write(f"HUNTING_RIFLE={str(round(self.huntingrifle_slider.get(), 1))}\n")
                file.write(f"SNIPER={str(round(self.sniper_slider.get(), 1))}\n")
                file.write(f"LASER={str(round(self.laser_slider.get(), 1))}\n")
                file.write(f"MINIGUN={str(round(self.minigun_slider.get(), 1))}\n")
                file.write(f"BOW={str(round(self.bow_slider.get(), 1))}\n")
                file.write(f"SPARROW_LAUNCHER={str(round(self.sparrowlauncher_slider.get(), 1))}\n")
                file.write(f"BCG={str(round(self.bcg_slider.get(), 1))}\n")
                file.write(f"GRENADE={str(round(self.grenadefrag_slider.get(), 1))}\n")
                file.write(f"BANANA={str(round(self.grenadebanana_slider.get(), 1))}\n")
                file.write(f"SKUNK={str(round(self.grenadeskunk_slider.get(), 1))}\n")
                file.write(f"MINE={str(round(self.grenademine_slider.get(), 1))}\n")
                file.write(f"ZIPLINE={str(round(self.grenadezip_slider.get(), 1))}\n")
                file.write(f"BOTS={str(round(self.bots_switch.get(), 1))}\n")
                file.write(f"HPM={str(self.hpm.get())}")

    def restore_default(self):
        self.allitems_switch.select()
        self.guns_switch.select()
        self.armors_switch.select()
        self.throwables_switch.select()
        self.powerups_switch.select()
        self.onehits_switch.deselect()
        self.bots_switch.deselect()
        self.emus_switch.select()
        self.hamballs_switch.select()
        self.moles_switch.select()
        self.pets_switch.select()
        self.gas_switch.select()
        self.norolls_switch.deselect()
        self.hpm.delete(0, 99)
        self.hpm.insert(0, "250")
        self.gasspeed_slider.set(1.0)
        self.gasdamage_slider.set(1.0)
        self.bulletspeed_slider.set(1.0)
        self.damage_slider.set(1.0)
        self.pistol_slider.set(1.0)
        self.magnum_slider.set(1.0)
        self.deagle_slider.set(1.0)
        self.silencedpistol_slider.set(1.0)
        self.shotgun_slider.set(1.0)
        self.jag_slider.set(1.0)
        self.smg_slider.set(1.0)
        self.tommy_slider.set(1.0)
        self.ak_slider.set(1.0)
        self.m16_slider.set(1.0)
        self.dart_slider.set(1.0)
        self.dartfly_slider.set(1.0)
        self.huntingrifle_slider.set(1.0)
        self.sniper_slider.set(1.0)
        self.laser_slider.set(1.0)
        self.minigun_slider.set(1.0)
        self.bow_slider.set(1.0)
        self.sparrowlauncher_slider.set(1.0)
        self.bcg_slider.set(1.0)
        self.grenadefrag_slider.set(1.0)
        self.grenadebanana_slider.set(1.0)
        self.grenadeskunk_slider.set(1.0)
        self.grenademine_slider.set(1.0)
        self.grenadezip_slider.set(1.0)
        self.label_gasspeed.configure(text="1.0")
        self.label_gasdamage.configure(text="1.0")
        self.label_bulletspeed.configure(text="1.0")
        self.label_damage.configure(text="1.0")
        self.label_pistol.configure(text="1.0")
        self.label_magnum.configure(text="1.0")
        self.label_deagle.configure(text="1.0")
        self.label_silencedpistol.configure(text="1.0")
        self.label_shotgun.configure(text="1.0")
        self.label_jag.configure(text="1.0")
        self.label_smg.configure(text="1.0")
        self.label_tommy.configure(text="1.0")
        self.label_ak.configure(text="1.0")
        self.label_m16.configure(text="1.0")
        self.label_dart.configure(text="1.0")
        self.label_dartfly.configure(text="1.0")
        self.label_huntingrifle.configure(text="1.0")
        self.label_sniper.configure(text="1.0")
        self.label_laser.configure(text="1.0")
        self.label_minigun.configure(text="1.0")
        self.label_bow.configure(text="1.0")
        self.label_sparrowlauncher.configure(text="1.0")
        self.label_bcg.configure(text="1.0")
        self.label_grenadefrag.configure(text="1.0")
        self.label_grenadebanana.configure(text="1.0")
        self.label_grenadeskunk.configure(text="1.0")
        self.label_grenademine.configure(text="1.0")
        self.label_grenadezip.configure(text="1.0")

    def info_menu(self):
        if check_win_exist("Private Game Helper - Info"):
            win_activate("Private Game Helper - Info", partial_match=False)
        else:
            window_info = InfoMenu(self)
            window_info.after(100, window_info.lift)

if __name__ == "__main__":
    app = App()
    app.mainloop()