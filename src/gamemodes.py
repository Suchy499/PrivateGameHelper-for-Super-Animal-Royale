import customtkinter
import pywinctl
from typing import Literal
from duels import Duels
from dodgeball import Dodgeball
from racing import Racing
from widgets import *

class GameModesMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("520x130")
        self.title("Private Game Helper - Game Modes")
        self.resizable(False, False)
        
        Text(self, text="Custom Game Modes", font="title", place=(140, 20))
        Button(self, text="Duels", command=lambda: self.open_menu("Duels"), place=(20, 80))
        Button(self, text="Dodgeball", command=lambda: self.open_menu("Dodgeball"), place=(190, 80))
        Button(self, text="Hamball Racing", command=lambda: self.open_menu("Racing"), place=(360, 80))
        
    def open_menu(self, menu: Literal["Duels", "Dodgeball", "Racing"]) -> None:
        if len(pywinctl.getWindowsWithTitle(f"Private Game Helper - {menu}", flags="IS")) == 1:
            window = pywinctl.getWindowsWithTitle(f"Private Game Helper - {menu}", flags="IS")[0]
            window.activate()
            self.after(100, self.destroy)
            return
        
        match menu:
            case "Duels":
                window = Duels()
            case "Dodgeball":
                window = Dodgeball()
            case "Racing":
                window = Racing()
            case _:
                return
            
        window.after(100, window.lift)
        self.after(100, self.destroy)