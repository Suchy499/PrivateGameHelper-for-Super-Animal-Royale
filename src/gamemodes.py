import customtkinter
import pywinctl
from duels import Duels
from dodgeball import Dodgeball
from racing import Racing

class GameModesMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("520x130")
        self.title("Private Game Helper - Game Modes")
        self.resizable(False, False)
        self.FONT_TITLE = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.FONT_REGULAR = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        
        # Title
        self.gamemodes_title = customtkinter.CTkLabel(self, text="Custom Game Modes", font=self.FONT_TITLE)
        self.gamemodes_title.place(x=140, y=20)
        
        # Buttons
        self.duels_button = customtkinter.CTkButton(self, text="Duels", command=self.open_duels)
        self.duels_button.place(x=20, y=80)
        self.dodgeball_button = customtkinter.CTkButton(self, text="Dodgeball", command=self.open_dodgeball)
        self.dodgeball_button.place(x=190, y=80)
        self.racing_button = customtkinter.CTkButton(self, text="Hamball Racing", command=self.open_racing)
        self.racing_button.place(x=360, y=80)
        
    # Button Controls
    def open_duels(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Private Game Helper - Duels", flags="IS")) == 1:
            duels_window = pywinctl.getWindowsWithTitle("Private Game Helper - Duels", flags="IS")[0]
            duels_window.activate()
        else:
            duels_window = Duels()
            duels_window.after(100, duels_window.lift)
        self.after(100, self.destroy)
    
    def open_dodgeball(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Private Game Helper - Dodgeball", flags="IS")) == 1:
            dodgeball_window = pywinctl.getWindowsWithTitle("Private Game Helper - Dodgeball", flags="IS")[0]
            dodgeball_window.activate()
        else:
            dodgeball_window = Dodgeball()
            dodgeball_window.after(100, dodgeball_window.lift)
        self.after(100, self.destroy)
        
    def open_racing(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Private Game Helper - Racing", flags="IS")) == 1:
            racing_window = pywinctl.getWindowsWithTitle("Private Game Helper - Racing", flags="IS")[0]
            racing_window.activate()
        else:
            racing_window = Racing()
            racing_window.after(100, racing_window.lift)
        self.after(100, self.destroy)