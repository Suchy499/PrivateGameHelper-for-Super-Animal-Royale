import customtkinter
from images import Images

class InfoMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("880x150")
        self.title("Private Game Helper - Info")
        self.resizable(False, False)
        self.FONT_TITLE = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.FONT_REGULAR = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        
        self.title = customtkinter.CTkLabel(self, text="Made by Suchy499", font=self.FONT_TITLE)
        self.title.place(x=20, y=20)
        self.info_text = customtkinter.CTkLabel(self, font=self.FONT_REGULAR, justify="left", text=
                                                "Important:\n"
                                                "- Only apply settings once per custom lobby\n"
                                                "- After using 'Apply Settings', do not press any keys until the program has finished working\n"
                                                "For any kind of help, you can reach me through discord!")
        self.info_text.place(x=20, y=60)
        self.avatar = customtkinter.CTkLabel(self, width=80, height=80, text="", image=Images.AVATAR)
        self.avatar.place(x=770, y=40)