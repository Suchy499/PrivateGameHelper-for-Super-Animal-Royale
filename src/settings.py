import customtkinter
import keyboard
import time
from CTkToolTip import CTkToolTip
from pynput import mouse
from functions import *
from widgets import *

class SettingsMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("580x280")
        self.title("Private Game Helper - Settings")
        self.resizable(False, False)
        
        # In-game keybinds
        Text(self, text="In-game Keybinds", font="title", place=(20, 20))
        Text(self, text="Use:", place=(20, 70))
        self.use_bind_entry = Text(self, text="E", width=100, fg_color="#343638", corner_radius=10, place=(20, 100), tooltip="Click to set")
        self.use_bind_entry.bind("<Button-1>", self.get_use_bind)
        Text(self, text="Melee:", place=(220, 70))
        self.melee_bind_entry = Text(self, text="3", width=100, fg_color="#343638", corner_radius=10, place=(220, 100), tooltip="Click to set")
        self.melee_bind_entry.bind("<Button-1>", self.get_melee_bind)
        Text(self, text="Throwable:", place=(420, 70))
        self.throwable_bind_entry = Text(self, text="4", width=100, fg_color="#343638", corner_radius=10, place=(420, 100), tooltip="Click to set")
        self.throwable_bind_entry.bind("<Button-1>", self.get_throwable_bind)
        
        # Updates
        Text(self, text="Updates", font="title", place=(20, 160))
        self.updates_popup_switch = Switch(self, text="New update popups", place=(20, 200))
        
        Button(self, text="OK", command=self.apply_settings, place=(420, 230))
        
        self.get_settings()
    
    def get_use_bind(self, event) -> None:
        self.selected_bind: str = "Use"
        self.use_bind_entry.configure(text="...")
        keyboard.unhook_all()
        keyboard.hook(self.key_pressed)
        self.mouse_listener = mouse.Listener(on_click=self.mouse_pressed)
        time.sleep(0.1)
        self.mouse_listener.start()
        
    def get_melee_bind(self, event) -> None:
        self.selected_bind: str = "Melee"
        self.melee_bind_entry.configure(text="...")
        keyboard.unhook_all()
        keyboard.hook(self.key_pressed)
        self.mouse_listener = mouse.Listener(on_click=self.mouse_pressed)
        time.sleep(0.1)
        self.mouse_listener.start()
        
    def get_throwable_bind(self, event) -> None:
        self.selected_bind: str = "Throwable"
        self.throwable_bind_entry.configure(text="...")
        keyboard.unhook_all()
        keyboard.hook(self.key_pressed)
        self.mouse_listener = mouse.Listener(on_click=self.mouse_pressed)
        time.sleep(0.1)
        self.mouse_listener.start()
        
    def key_pressed(self, event) -> None:
        keyboard.unhook_all()
        self.mouse_listener.stop()
        match self.selected_bind:
            case "Use":
                self.use_bind_entry.configure(text=event.name.upper())
            case "Melee":
                self.melee_bind_entry.configure(text=event.name.upper())
            case "Throwable":
                self.throwable_bind_entry.configure(text=event.name.upper())
    
    def mouse_pressed(self, x, y, button, pressed) -> None:
        keyboard.unhook_all()
        self.mouse_listener.stop()
        match button:
            case mouse.Button.left:
                button_pressed: str = "MOUSE0"
            case mouse.Button.right:
                button_pressed: str = "MOUSE1"
            case mouse.Button.middle:
                button_pressed: str = "MOUSE2"
            case _:
                button_pressed: str = "INVALID"
        match self.selected_bind:
            case "Use":
                self.use_bind_entry.configure(text=button_pressed)
            case "Melee":
                self.melee_bind_entry.configure(text=button_pressed)
            case "Throwable":
                self.throwable_bind_entry.configure(text=button_pressed)
    
    def get_settings(self) -> None:
        try:
            with open("config.cfg") as file:
                file_content: str = file.read()
                lines: list[str] = file_content.split("\n")
                settings: dict[str, str] = {}
                for x in lines:
                    setting: list[str] = x.split("=")
                    settings[setting[0]] = setting[1]
                self.use_bind_entry.configure(text=settings["USE"].upper())
                self.melee_bind_entry.configure(text=settings["MELEE"].upper())
                self.throwable_bind_entry.configure(text=settings["THROWABLE"].upper())
                self.updates_popup_switch.select() if settings["POPUPS"] == "1" else self.updates_popup_switch.deselect()
        except FileNotFoundError:
            with open("config.cfg", "w") as file:
                file.write("USE=e\n"
                           "MELEE=3\n"
                           "THROWABLE=4\n"
                           "POPUPS=1")
    
    def apply_settings(self) -> None:
        with open("config.cfg", "w") as file:
            file.write(f"USE={self.use_bind_entry.cget("text").lower()}\n")
            file.write(f"MELEE={self.melee_bind_entry.cget("text").lower()}\n")
            file.write(f"THROWABLE={self.throwable_bind_entry.cget("text").lower()}\n")
            file.write(f"POPUPS={self.updates_popup_switch.get()}")
        Settings.update(self=Settings)
        self.destroy()