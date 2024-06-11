import time
import keyboard
import pywinctl
import pyautogui

KEY_DELAY: float = 0.025

class Settings:
    use: str = "e"
    melee: str = "3"
    throwable: str = "4"
    popups: str = "1"
    
    def update(self) -> None:
        try:
            with open("config.cfg") as file:
                file_content: str = file.read()
                lines: list[str] = file_content.split("\n")
                settings: dict[str, str] = {}
                for x in lines:
                    setting: list[str] = x.split("=")
                    settings[setting[0]] = setting[1]
                self.use = settings["USE"].lower()
                self.melee = settings["MELEE"].lower()
                self.throwable = settings["THROWABLE"].lower()
                self.popups = settings["POPUPS"].lower()
        except FileNotFoundError:
            with open("config.cfg", "w") as file:
                file.write(f"USE={self.use}\n")
                file.write(f"MELEE={self.melee}\n")
                file.write(f"THROWABLE={self.throwable}\n")
                file.write(f"POPUPS={self.popups}")

def send_commands(*commands: str, delay: int = 2) -> None:
    for command in commands:
        time.sleep(KEY_DELAY*delay)
        keyboard.write(f"\n/{command}\n", delay=KEY_DELAY)
    
def open_window(window_title: str) -> bool:
    if len(pywinctl.getWindowsWithTitle(window_title, flags="IS")) == 0:
        return False
    
    window = pywinctl.getWindowsWithTitle(window_title, flags="IS")[0]
    window.activate()
    time.sleep(KEY_DELAY*16)
    return True

def mouse_click(x: int, y: int) -> None:
    pyautogui.moveTo(x, y)
    time.sleep(KEY_DELAY*8)
    pyautogui.click()
    time.sleep(KEY_DELAY*4)

def press_use() -> None:
    time.sleep(KEY_DELAY*2)
    match Settings.use:
        case "mouse0":
            pyautogui.click(button="left")
        case "mouse1":
            pyautogui.click(button="right")
        case "mouse2":
            pyautogui.click(button="middle")
        case _:
            keyboard.send(Settings.use)
    time.sleep(KEY_DELAY*2)

def press_melee() -> None:
    time.sleep(KEY_DELAY*2)
    match Settings.melee:
        case "mouse0":
            pyautogui.click(button="left")
        case "mouse1":
            pyautogui.click(button="right")
        case "mouse2":
            pyautogui.click(button="middle")
        case _:
            keyboard.send(Settings.melee)
    time.sleep(KEY_DELAY*2)

def press_throwable() -> None:
    time.sleep(KEY_DELAY*2)
    match Settings.throwable:
        case "mouse0":
            pyautogui.click(button="left")
        case "mouse1":
            pyautogui.click(button="right")
        case "mouse2":
            pyautogui.click(button="middle")
        case _:
            keyboard.send(Settings.throwable)
    time.sleep(KEY_DELAY*2)