import customtkinter
from images import Images
from functions import *
from widgets import *

class CommandsMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("780x310")
        self.title("Private Game Helper - Other Commands")
        self.resizable(False, False)
        
        Text(self, text="Other Commands", font="title", place=(20, 20))
        
        # Commands
        Button(self, text="/flight", command=lambda: self.change_setting("flight"), place=(20, 60), tooltip="Can be used to regenerate the Eagle flight path. Must run before the game timer has started.")
        Button(self, text="/noboss", command=lambda: self.change_setting("noboss"), place=(20, 100), tooltip="Toggle to enable or disable Giant Star-nosed Mole from arriving.")
        Button(self, text="/soccer", command=lambda: self.change_setting("soccer"), place=(20, 140), tooltip="Spawns a Fox Ball (only 1 at a time).")
        Button(self, text="/rain", command=lambda: self.change_setting("rain"), place=(20, 180), tooltip="Forces a rain weather event.")
        Button(self, text="/rainoff", command=lambda: self.change_setting("rainoff"), place=(20, 220), tooltip="Disables rain for entirity of a match. Won't work if it's already raining in-game.")
        Button(self, text="/night", command=lambda: self.change_setting("night"), place=(170, 60), tooltip="Toggles the night mode.")
        Button(self, text="/getplayers", command=lambda: self.change_setting("getplayers"), place=(170, 100), tooltip="Copies a list of all players in the match. After running the command, can be pasted into notepad.\nAt the end of a match, you can use this command to grab the stats of the players.")
        Button(self, text="/gasstart", command=lambda: self.change_setting("gasstart"), place=(170, 140), tooltip="Makes the first skunk gas timer start right away (if in lobby, it just means it'll start right when the eagle starts).")
        Button(self, text="/boss", command=lambda: self.change_setting("boss"), place=(170, 180), tooltip="Spawns a Giant Star-nosed Mole.")
        Button(self, text="/getpid", command=lambda: self.change_setting("getpid"), place=(170, 220), tooltip="Shows your in-game player id #.")
        self.mystery_options = OptionMenu(self, values=["Shotgun & Sniper", "Wild West", "Slow Bullets", "Bananarama", "Handguns Only", "Fast Bullets", "One Hit Kill"], place=(20, 260))
        Button(self, text="Select", command=self.change_mystery, place=(170, 270), tooltip="In Mystery Mode, selects which mystery mode will be ran.")
        
        # Player specific commands
        Text(self, text="Player specific commands", font="title", place=(400, 20))
        Text(self, text="Player ID:", place=(400, 60))
        self.player_id_input = Entry(self, placeholder_text="ID / all", place=(550, 60))
        
        Button(self, text="/saw #", command=lambda: self.change_setting("saw", True), place=(400, 100), tooltip="The command can be used to change the team of player with given ID to S.A.W. Security Forces.")
        Button(self, text="/admin #", command=lambda: self.change_setting("admin", True), place=(400, 140), tooltip="Makes the user a \"helper admin\" which allows them to use all of the admin commands except the kick command on the primary admin.\nRepeating the command on same user will revoke their helper admin status.")
        Button(self, text="/kick #", command=lambda: self.change_setting("kick", True), place=(400, 180), tooltip="Kicks player with specified in-game id #. Player cannot rejoin until next match.")
        Button(self, text="/getpos #", command=lambda: self.change_setting("getpos", True), place=(400, 220), tooltip="Tells you world position of a player with given number.")
        Button(self, text="/infect #", command=lambda: self.change_setting("infect", True), place=(400, 260), tooltip="Makes given player infected.")
        Button(self, text="/rebel #", command=lambda: self.change_setting("rebel", True), place=(550, 100), tooltip="The command can be used to change the team of player with given ID to Super Animal Super Resistance.")
        Button(self, text="/ghost #", command=lambda: self.change_setting("ghost", True), place=(550, 140), tooltip="Goes into spectate ghost mode. Can be run in lobby, or in-game after death only.")
        Button(self, text="/kill #", command=lambda: self.change_setting("kill", True), place=(550, 180), tooltip="Kills player (or bot) with specified in-game id #. Writing all in place of # will enable kill all players.\nOnly works on players who have finished parachuting.")
        Button(self, text="/god #", command=lambda: self.change_setting("god", True), place=(550, 220), tooltip="Set a player to god-mode with ID #. Applies only to player damage. Writing all in place of # will enable god-mode for all players.")
        
        self.always_on_top_button = ImageButton(self, image_type="always_on_top", image=Images.ICON_PIN, command=self.always_on_top, place=(730, 20), tooltip="Keep this window on top")
    
    def change_setting(self, command: str, with_id: bool = False) -> None:
        if open_window("Super Animal Royale"):
            if with_id:
                send_commands(f"{command} {self.player_id_input.get()}")
            else:
                send_commands(command)
    
    def change_mystery(self) -> None:
        if open_window("Super Animal Royale") is False:
            return
        
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
        send_commands(f"mystery {mystery_mode}")
    
    def always_on_top(self) -> None:
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.always_on_top_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.always_on_top_button.configure(image=Images.ICON_PIN_VERTICAL)