import customtkinter
import keyboard
import time
import pywinctl
from CTkToolTip import CTkToolTip
from images import Images

class CommandsMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("780x310")
        self.title("Private Game Helper - Other Commands")
        self.resizable(False, False)
        self.FONT_TITLE = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.FONT_REGULAR = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        self.KEY_DELAY: float = 0.025
        
        # Title
        self.other_commands_title = customtkinter.CTkLabel(self, text="Other Commands", font=self.FONT_TITLE)
        self.other_commands_title.place(x=20, y=20)
        
        # Flight
        self.flight = customtkinter.CTkButton(self, text="/flight", command=self.flight_ctrl)
        self.flight.place(x=20, y=60)
        self.flight_tooltip = CTkToolTip(self.flight, delay=0, message="Can be used to regenerate the Eagle flight path. Must run before the game timer has started.")
        
        # Noboss
        self.noboss = customtkinter.CTkButton(self, text="/noboss", command=self.noboss_ctrl)
        self.noboss.place(x=20, y=100)
        self.noboss_tooltip = CTkToolTip(self.noboss, delay=0, message="Toggle to enable or disable Giant Star-nosed Mole from arriving.")
        
        # Soccer
        self.soccer = customtkinter.CTkButton(self, text="/soccer", command=self.soccer_ctrl)
        self.soccer.place(x=20, y=140)
        self.soccer_tooltip = CTkToolTip(self.soccer, delay=0, message="Spawns a Fox Ball (only 1 at a time).")
        
        # Rain
        self.rain = customtkinter.CTkButton(self, text="/rain", command=self.rain_ctrl)
        self.rain.place(x=20, y=180)
        self.rain_tooltip = CTkToolTip(self.rain, delay=0, message="Forces a rain weather event.")
        
        # Rainoff
        self.rainoff = customtkinter.CTkButton(self, text="/rainoff", command=self.rainoff_ctrl)
        self.rainoff.place(x=20, y=220)
        self.rainoff_tooltip = CTkToolTip(self.rainoff, delay=0, message="Disables rain for entirity of a match. Won't work if it's already raining in-game.")
        
        # Night
        self.night = customtkinter.CTkButton(self, text="/night", command=self.night_ctrl)
        self.night.place(x=170, y=60)
        self.night_tooltip = CTkToolTip(self.night, delay=0, message="Toggles the night mode.")
        
        # Getplayers
        self.getplayers = customtkinter.CTkButton(self, text="/getplayers", command=self.getplayers_ctrl)
        self.getplayers.place(x=170, y=100)
        self.getplayers_tooltip = CTkToolTip(self.getplayers, delay=0, message="Copies a list of all players in the match. After running the command, can be pasted into notepad.\nAt the end of a match, you can use this command to grab the stats of the players.")
        
        # Gasstart
        self.gasstart = customtkinter.CTkButton(self, text="/gasstart", command=self.gasstart_ctrl)
        self.gasstart.place(x=170, y=140)
        self.gasstart_tooltip = CTkToolTip(self.gasstart, delay=0, message="Makes the first skunk gas timer start right away (if in lobby, it just means it'll start right when the eagle starts).")
        
        # Boss
        self.boss = customtkinter.CTkButton(self, text="/boss", command=self.boss_ctrl)
        self.boss.place(x=170, y=180)
        self.boss_tooltip = CTkToolTip(self.boss, delay=0, message="Spawns a Giant Star-nosed Mole.")
        
        # Getpid
        self.getpid = customtkinter.CTkButton(self, text="/getpid", command=self.getpid_ctrl)
        self.getpid.place(x=170, y=220)
        self.getpid_tooltip = CTkToolTip(self.getpid, delay=0, message="Shows your in-game player id #.")
        
        # Mystery
        self.mystery_options = customtkinter.CTkOptionMenu(self, values=["Shotgun & Sniper", "Wild West", "Slow Bullets", "Bananarama", "Handguns Only", "Fast Bullets", "One Hit Kill"])
        self.mystery_options.place(x=20, y=260)
        self.mystery_select = customtkinter.CTkButton(self, text="Select", command=self.mystery_ctrl)
        self.mystery_select.place(x=170, y=260)
        self.mystery_select_tooltip = CTkToolTip(self.mystery_select, delay=0, message="In Mystery Mode, selects which mystery mode will be ran.")
        
        # Player specific commands
        self.player_specific_commands_title = customtkinter.CTkLabel(self, text="Player specific commands", font=self.FONT_TITLE)
        self.player_specific_commands_title.place(x=400, y=20)
        
        # Player id
        self.player_id_text = customtkinter.CTkLabel(self, text="Player ID:", font=self.FONT_REGULAR)
        self.player_id_text.place(x=400, y=60)
        self.player_id_input = customtkinter.CTkEntry(self, placeholder_text="ID / all")
        self.player_id_input.place(x=550, y=60)
        
        # SAW
        self.saw = customtkinter.CTkButton(self, text="/saw #", command=self.saw_ctrl)
        self.saw.place(x=400, y=100)
        self.saw_tooltip = CTkToolTip(self.saw, delay=0, message="The command can be used to change the team of player with given ID to S.A.W. Security Forces.")
        
        # Admin
        self.admin = customtkinter.CTkButton(self, text="/admin #", command=self.admin_ctrl)
        self.admin.place(x=400, y=140)
        self.admin_tooltip = CTkToolTip(self.admin, delay=0, message="Makes the user a \"helper admin\" which allows them to use all of the admin commands except the kick command on the primary admin.\nRepeating the command on same user will revoke their helper admin status.")
        
        # Kick
        self.kick = customtkinter.CTkButton(self, text="/kick #", command=self.kick_ctrl)
        self.kick.place(x=400, y=180)
        self.kick_tooltip = CTkToolTip(self.kick, delay=0, message="Kicks player with specified in-game id #. Player cannot rejoin until next match.")
        
        # Getpos
        self.getpos = customtkinter.CTkButton(self, text="/getpos #", command=self.getpos_ctrl)
        self.getpos.place(x=400, y=220)
        self.getpos_tooltip = CTkToolTip(self.getpos, delay=0, message="Tells you world position of a player with given number.")
        
        # Infect
        self.infect = customtkinter.CTkButton(self, text="/infect #", command=self.infect_ctrl)
        self.infect.place(x=400, y=260)
        self.infect_tooltip = CTkToolTip(self.infect, delay=0, message="Makes given player infected.")
        
        # Rebel
        self.rebel = customtkinter.CTkButton(self, text="/rebel #", command=self.rebel_ctrl)
        self.rebel.place(x=550, y=100)
        self.rebel_tooltip = CTkToolTip(self.rebel, delay=0, message="The command can be used to change the team of player with given ID to Super Animal Super Resistance.")
        
        # Ghost
        self.ghost = customtkinter.CTkButton(self, text="/ghost #", command=self.ghost_ctrl)
        self.ghost.place(x=550, y=140)
        self.ghost_tooltip = CTkToolTip(self.ghost, delay=0, message="Goes into spectate ghost mode. Can be run in lobby, or in-game after death only.")
        
        # Kill
        self.kill = customtkinter.CTkButton(self, text="/kill #", command=self.kill_ctrl)
        self.kill.place(x=550, y=180)
        self.kill_tooltip = CTkToolTip(self.kill, delay=0, message="Kills player (or bot) with specified in-game id #. Writing all in place of # will enable kill all players.\nOnly works on players who have finished parachuting.")
        
        # God
        self.god = customtkinter.CTkButton(self, text="/god #", command=self.god_ctrl)
        self.god.place(x=550, y=220)
        self.god_tooltip = CTkToolTip(self.god, delay=0, message="Set a player to god-mode with ID #. Applies only to player damage. Writing all in place of # will enable god-mode for all players.")
        
        # Always on top
        self.alwaysontop_button = customtkinter.CTkButton(self, width=20, height=20, text="", image=Images.ICON_PIN, hover=False, fg_color="transparent", bg_color="transparent", command=self.always_on_top)
        self.alwaysontop_button.place(x=730, y=20)
        self.alwaysontop_tooltip = CTkToolTip(self.alwaysontop_button, delay=0, message="Keep this window on top")
    
    def flight_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/flight\n", delay=self.KEY_DELAY)

    def noboss_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/noboss\n", delay=self.KEY_DELAY)
            
    def soccer_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/soccer\n", delay=self.KEY_DELAY)
            
    def rain_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/rain\n", delay=self.KEY_DELAY)
    
    def rainoff_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/rainoff\n", delay=self.KEY_DELAY)
    
    def night_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/night\n", delay=self.KEY_DELAY)
            
    def getplayers_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/getplayers\n", delay=self.KEY_DELAY)
            
    def gasstart_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/gasstart\n", delay=self.KEY_DELAY)
    
    def boss_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/boss\n", delay=self.KEY_DELAY)
    
    def getpid_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/getpid\n", delay=self.KEY_DELAY)
        
    def saw_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/saw {self.player_id_input.get()}\n", delay=self.KEY_DELAY)
    
    def admin_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/admin {self.player_id_input.get()}\n", delay=self.KEY_DELAY)
    
    def kick_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/kick {self.player_id_input.get()}\n", delay=self.KEY_DELAY)
    
    def getpos_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/getpos {self.player_id_input.get()}\n", delay=self.KEY_DELAY)
            
    def infect_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/infect {self.player_id_input.get()}\n", delay=self.KEY_DELAY)
    
    def rebel_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/rebel {self.player_id_input.get()}\n", delay=self.KEY_DELAY)
    
    def ghost_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/ghost {self.player_id_input.get()}\n", delay=self.KEY_DELAY)
    
    def kill_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/kill {self.player_id_input.get()}\n", delay=self.KEY_DELAY)
    
    def god_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write(f"\n/god {self.player_id_input.get()}\n", delay=self.KEY_DELAY)
    
    def mystery_ctrl(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        match self.mystery_options.get():
            case "Shotgun & Sniper": 
                mystery_mode: int = 0
            case "Wild West": 
                mystery_mode: int = 1
            case "Slow Bullets": 
                mystery_mode: int = 2
            case "Bananarama": 
                mystery_mode: int = 3
            case "Handguns Only": 
                mystery_mode: int = 4
            case "Fast Bullets": 
                mystery_mode: int = 5
            case "One Hit Kill":
                mystery_mode: int = 6
        keyboard.write(f"\n/mystery {mystery_mode}\n", delay=self.KEY_DELAY)
    
    def always_on_top(self) -> None:
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.alwaysontop_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.alwaysontop_button.configure(image=Images.ICON_PIN_VERTICAL)