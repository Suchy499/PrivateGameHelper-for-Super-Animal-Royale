import customtkinter
from pregame import Pregame

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    app = Pregame()
    app.mainloop()