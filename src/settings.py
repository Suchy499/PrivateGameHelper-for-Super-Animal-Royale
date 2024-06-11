import customtkinter
import keyboard
import time
from CTkToolTip import CTkToolTip
from pynput import mouse
from functions import *

class SettingsMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("580x280")
        self.title("Private Game Helper - Settings")
        self.resizable(False, False)
        self.FONT_TITLE = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.FONT_REGULAR = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        self.FONT_ITALIC = customtkinter.CTkFont(family="Roboto", weight="bold", slant="italic")
        
        # In-game keybinds
        self.keybinds_title = customtkinter.CTkLabel(self, text="In-game Keybinds", font=self.FONT_TITLE)
        self.keybinds_title.place(x=20, y=20)
        self.use_bind_label = customtkinter.CTkLabel(self, text="Use:", font=self.FONT_REGULAR)
        self.use_bind_label.place(x=20, y=70)
        self.use_bind_entry = customtkinter.CTkLabel(self, width=100, text="E", font=self.FONT_REGULAR, fg_color="#343638", corner_radius=10)
        self.use_bind_entry.place(x=20, y=100)
        self.use_bind_entry.bind("<Button-1>", self.get_use_bind)
        self.use_bind_tooltip = CTkToolTip(self.use_bind_entry, "Click to set", delay=0.1)
        self.melee_bind_label = customtkinter.CTkLabel(self, text="Melee:", font=self.FONT_REGULAR)
        self.melee_bind_label.place(x=220, y=70)
        self.melee_bind_entry = customtkinter.CTkLabel(self, width=100, text="3", font=self.FONT_REGULAR, fg_color="#343638", corner_radius=10)
        self.melee_bind_entry.place(x=220, y=100)
        self.melee_bind_entry.bind("<Button-1>", self.get_melee_bind)
        self.melee_bind_tooltip = CTkToolTip(self.melee_bind_entry, "Click to set", delay=0.1)
        self.throwable_bind_label = customtkinter.CTkLabel(self, text="Throwable:", font=self.FONT_REGULAR)
        self.throwable_bind_label.place(x=420, y=70)
        self.throwable_bind_entry = customtkinter.CTkLabel(self, width=100, text="4", font=self.FONT_REGULAR, fg_color="#343638", corner_radius=10)
        self.throwable_bind_entry.place(x=420, y=100)
        self.throwable_bind_entry.bind("<Button-1>", self.get_throwable_bind)
        self.throwable_bind_tooltip = CTkToolTip(self.throwable_bind_entry, "Click to set", delay=0.1)
        
        # Updates
        self.updates_title = customtkinter.CTkLabel(self, text="Updates", font=self.FONT_TITLE)
        self.updates_title.place(x=20, y=160)
        self.updates_popup_switch = customtkinter.CTkSwitch(self, text="New update popups")
        self.updates_popup_switch.place(x=20, y=200)
        
        # Apply
        self.apply_button = customtkinter.CTkButton(self, text="OK", command=self.apply_settings)
        self.apply_button.place(x=420, y=230)
        
        self.get_settings()
    
    def get_use_bind(self, event) -> None:
        self.selected_bind = "Use"
        self.use_bind_entry.configure(text="...")
        keyboard.unhook_all()
        keyboard.hook(self.key_pressed)
        self.mouse_listener = mouse.Listener(on_click=self.mouse_pressed)
        time.sleep(0.1)
        self.mouse_listener.start()
        
    def get_melee_bind(self, event) -> None:
        self.selected_bind = "Melee"
        self.melee_bind_entry.configure(text="...")
        keyboard.unhook_all()
        keyboard.hook(self.key_pressed)
        self.mouse_listener = mouse.Listener(on_click=self.mouse_pressed)
        time.sleep(0.1)
        self.mouse_listener.start()
        
    def get_throwable_bind(self, event) -> None:
        self.selected_bind = "Throwable"
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
                button_pressed = "MOUSE0"
            case mouse.Button.right:
                button_pressed = "MOUSE1"
            case mouse.Button.middle:
                button_pressed = "MOUSE2"
            case _:
                button_pressed = "INVALID"
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