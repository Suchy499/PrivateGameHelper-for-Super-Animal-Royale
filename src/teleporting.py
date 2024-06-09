import customtkinter
import pyperclip
import keyboard
import time
import pywinctl
from CTkToolTip import CTkToolTip
from CTkMessagebox import CTkMessagebox
from images import Images

class TeleportMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("768x950")
        self.title("Private Game Helper - Teleport Menu")
        self.resizable(False, False)
        self.FONT_TITLE = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.FONT_REGULAR = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        self.mode_var = customtkinter.IntVar(value=0)
        self.KEY_DELAY: float = 0.025
        
        # Title
        self.title = customtkinter.CTkLabel(self, text="Teleport Menu", font=self.FONT_TITLE)
        self.title.place(x=20, y=20)
        
        # Instructions
        self.copy_instructions = customtkinter.CTkLabel(self, font=self.FONT_REGULAR, justify="left", text=
                                                        "- Click on the map to copy the coordinates to your clipboard\n"
                                                        "- Type in game chat \"/tele [id/all] \"\n"
                                                        "- Press Ctrl + V to paste the coordinates")
        self.copy_instructions.place(x=20, y=100)
        self.instant_teleport_instructions = customtkinter.CTkLabel(self, font=self.FONT_REGULAR, justify="left", text=
                                                                    "- Type in a player's ID or \"All\"\n"
                                                                    "- Click on the map to teleport a player / all players to that location")
        
        # Player ID
        self.player_id_label = customtkinter.CTkLabel(self, text="Player ID: ", font=self.FONT_REGULAR)
        self.player_id_entry = customtkinter.CTkEntry(self, placeholder_text="ID / All")
        
        # Map
        self.sar_map = customtkinter.CTkLabel(self, width=768, height=768, text="", image=Images.SAR_MAP)
        self.sar_map.place(x=0, y=182)
        self.sar_map.bind("<Button-1>", self.copy_coordinates)
        
        # Coordinates
        self.coordinates = customtkinter.CTkLabel(self, text="Coordinates:\n(x, y)", font=self.FONT_REGULAR)
        self.coordinates.place(x=600, y=75)
        
        # Modes
        self.copy_mode = customtkinter.CTkRadioButton(self, text="Copy Mode", font=self.FONT_REGULAR, variable=self.mode_var, value=0, command=self.change_mode)
        self.copy_mode.place(x=20, y=60)
        self.tele_mode = customtkinter.CTkRadioButton(self, text="Instant Teleport Mode", font=self.FONT_REGULAR, variable=self.mode_var, value=1, command=self.change_mode)
        self.tele_mode.place(x=150, y=60)
        
        # Always on top
        self.alwaysontop_button = customtkinter.CTkButton(self, width=20, height=20, text="", image=Images.ICON_PIN, hover=False, fg_color="transparent", bg_color="transparent", command=self.always_on_top)
        self.alwaysontop_button.place(x=720, y=20)
        self.alwaysontop_tooltip = CTkToolTip(self.alwaysontop_button, delay=0, message="Keep this window on top")
        
    def copy_coordinates(self, event) -> None:
        x: int = event.x * 6
        y: int = (768 - event.y) * 6
        if self.mode_var.get() == 0:
            pyperclip.copy(f"{x} {y}")
            self.coordinates.configure(text=f"Coordinates:\n({x}, {y})")
        elif self.player_id_entry.get().isnumeric() and 1 <= int(self.player_id_entry.get()) <= 99 or (self.player_id_entry.get().lower() == "all"):
            self.coordinates.configure(text=f"Coordinates:\n({x}, {y})")
            if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
                return
            
            sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
            sar_window.activate()
            time.sleep(self.KEY_DELAY*16)
            keyboard.write(f"\n/tele {self.player_id_entry.get().lower()} {x} {y}\n", delay=self.KEY_DELAY)
        else:
            CTkMessagebox(title="Private Game Helper", message="Player ID has to be either \"all\" or between 1-99")
    
    def change_mode(self) -> None:
        if self.mode_var.get() == 1:
            self.copy_instructions.place_forget()
            self.instant_teleport_instructions.place(x=20, y=95)
            self.player_id_label.place(x=20, y=145)
            self.player_id_entry.place(x=110, y=145)
        else:
            self.instant_teleport_instructions.place_forget()
            self.player_id_label.place_forget()
            self.player_id_entry.place_forget()
            self.copy_instructions.place(x=20, y=100)
    
    def always_on_top(self) -> None:
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.alwaysontop_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.alwaysontop_button.configure(image=Images.ICON_PIN_VERTICAL)
