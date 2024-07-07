import customtkinter
from images import Images
from widgets import *

class InfoMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("880x150")
        self.title("Private Game Helper - Info")
        self.resizable(False, False)
        
        Text(self, text="Made by Suchy499", font="title", place=(20, 20))
        Text(self, 
             text="Important:\n"
                  "- Only apply settings once per custom lobby\n"
                  "- After using 'Apply Settings', do not press any keys until the program has finished working\n"
                  "For any kind of help, you can reach me through discord!",
             justify="left",
             place=(20, 60))
        Image(self, image=Images.AVATAR, width=80, height=80, place=(770, 40))