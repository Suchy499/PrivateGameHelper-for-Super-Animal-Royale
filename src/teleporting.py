import customtkinter
import pyperclip
from CTkMessagebox import CTkMessagebox
from images import Images
from functions import *
from widgets import *

class TeleportMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("768x950")
        self.title("Private Game Helper - Teleport Menu")
        self.resizable(False, False)
        self.mode_var = customtkinter.IntVar(value=0)
        
        Text(self, text="Teleport Menu", font="title", place=(20, 20))
        self.copy_instructions = Text(self, text="- Click on the map to copy the coordinates to your clipboard\n- Type in game chat \"/tele [id/all] \"\n- Press Ctrl + V to paste the coordinates", place=(20, 100), justify="left")
        self.instant_teleport_instructions = Text(self, text="- Type in a player's ID or \"All\"\n- Click on the map to teleport a player / all players to that location", justify="left")
        self.player_id_label = Text(self, text="Player ID:")
        self.player_id_entry = Entry(self, placeholder_text="ID / All")
        self.sar_map = Image(self, width=768, height=768, image=Images.SAR_MAP, place=(0, 182))
        self.sar_map.bind("<Button-1>", self.copy_coordinates)
        self.coordinates = Text(self, text="Coordinates:\n(x, y)", place=(600, 75))
        self.copy_mode = Radio(self, text="Copy Mode", variable=self.mode_var, value=0, command=self.change_mode, place=(20, 60))
        self.tele_mode = Radio(self, text="Instant Teleport Mode", variable=self.mode_var, value=1, command=self.change_mode, place=(150, 60))
        self.always_on_top_button = ImageButton(self, image_type="always_on_top", image=Images.ICON_PIN, command=self.always_on_top, place=(720, 20), tooltip="Keep this window on top")
        
    def copy_coordinates(self, event) -> None:
        x: int = event.x * 6
        y: int = (768 - event.y) * 6
        if self.mode_var.get() == 0:
            pyperclip.copy(f"{x} {y}")
            self.coordinates.configure(text=f"Coordinates:\n({x}, {y})")
        elif self.player_id_entry.get().isnumeric() and 1 <= int(self.player_id_entry.get()) <= 99 or (self.player_id_entry.get().lower() == "all"):
            self.coordinates.configure(text=f"Coordinates:\n({x}, {y})")
            if open_window("Super Animal Royale"):
                send_commands(f"tele {self.player_id_entry.get().lower()} {x} {y}")
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
            self.always_on_top_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.always_on_top_button.configure(image=Images.ICON_PIN_VERTICAL)