import tkinter
import customtkinter
import random
from CTkToolTip import CTkToolTip
from typing import Union, Callable, Any, Literal, Optional
from PIL import ImageTk
from images import Images

class Text(customtkinter.CTkLabel):
    def __init__(self, 
                 master: Any,
                 text: str = "Text",
                 font: Literal["title", "regular", "italic"] = "regular",
                 tooltip: Optional[str] = None,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        match font:
            case "title":
                font = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
            case "regular":
                font = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
            case "italic":
                font = customtkinter.CTkFont(family="Roboto", weight="bold", slant="italic")
            case _:
                font = None
        super().__init__(master=master, text=text, font=font, **kwargs)
        if place is not None:
            x, y = place
            self.place(x=x, y=y)
        if tooltip is not None:
            CTkToolTip(self, delay=0.1, message=tooltip)
            
class ImageButton(customtkinter.CTkButton):
    def __init__(self, 
                 master: Any,
                 image_type: Literal["rarity", "gun", "ammo", "juice", "armor", "vehicle", "tape", "throwable", "powerup", "random", "random_all", "always_on_top"] = "gun",
                 image: Union[customtkinter.CTkImage, "ImageTk.PhotoImage", None] = None, 
                 command: Optional[Callable[[], Any]] = None,
                 tooltip: Optional[str] = None,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        match image_type:
            case "rarity":
                width: int = 100
                height: int = 24
            case "gun":
                width: int = 100
                height: int = 100
            case "ammo":
                width: int = 45
                height: int = 30
            case "juice" | "armor" | "vehicle":
                width: int = 80
                height: int = 80
            case "tape" | "throwable" | "powerup":
                width: int = 30
                height: int = 30
            case "random":
                width: int = 15
                height: int = 15
            case "random_all" | "always_on_top":
                width: int = 20
                height: int = 20
            case _:
                raise ValueError("'item_type' argument can only be 'rarity', 'gun', 'ammo', 'juice', 'armor', 'vehicle', 'tape', 'throwable', 'powerup', 'always_on_top'")
        super().__init__(master=master, width=width, height=height, text="", image=image, fg_color="transparent", bg_color="transparent", hover=False, command=command, **kwargs)
        if place is not None:
            x, y = place
            self.place(x=x, y=y)
        if tooltip is not None:
            CTkToolTip(self, delay=0.1, message=tooltip)

class Slider(customtkinter.CTkSlider):
    def __init__(self, 
                 master: Any,
                 slider_type: Literal["ammo", "tape", "gas_speed", "gas_damage", "bullet_speed", "damage", "weight"] = "ammo",
                 command: Optional[Callable[[], Any]] = None,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        match slider_type:
            case "ammo":
                width: int = 280
                from_: int = 10
                to: int = 200
                number_of_steps: int = 19
            case "tape":
                width: int = 280
                from_: int = 1
                to: int = 10
                number_of_steps: int = 9
            case "gas_speed":
                width: int = 160
                from_: float = 0.4
                to: float = 3.0
                number_of_steps: int = 26
            case "gas_damage":
                width: int = 160
                from_: float = 1.0
                to: float = 10.0
                number_of_steps: int = 90
            case 'bullet_speed':
                width: int = 160
                from_: float = 0.5
                to: float = 2.0
                number_of_steps: int = 15
            case 'damage':
                width: int = 160
                from_: float = 0.0
                to: float = 10.0
                number_of_steps: int = 100
            case 'weight':
                width: int = 160
                from_: float = 0.0
                to: float = 5.0
                number_of_steps: int = 50
            case _:
                raise ValueError("'slider_type' argument can only be 'ammo', 'tape', 'gas_speed', 'gas_damage', 'bullet_speed', 'damage', 'weight'")
        super().__init__(master=master, width=width, from_=from_, to=to, number_of_steps=number_of_steps, command=command, **kwargs)
        if place is not None:
            x, y = place
            self.place(x=x, y=y)
        match slider_type:
            case "ammo":
                self.set(100)
            case "tape":
                self.set(5)
            case "gas_speed":
                self.set(1.0)
            case "gas_damage":
                self.set(1.0)
            case 'bullet_speed':
                self.set(1.0)
            case 'damage':
                self.set(1.0)
            case 'weight':
                self.set(1.0)
            case _:
                raise ValueError("'slider_type' argument can only be 'ammo', 'tape', 'gas_speed', 'gas_damage', 'bullet_speed', 'damage', 'weight'")

class Entry(customtkinter.CTkEntry):
    def __init__(self,
                 master: Any,
                 text: Optional[str] = None,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        super().__init__(master=master, **kwargs)
        if place is not None:
            x, y = place
            self.place(x=x, y=y)
        if text is not None:
            self.insert(0, text)
    
    def set(self, value: Any) -> None:
        self.delete(0, 999)
        self.insert(0, value)

class Image(customtkinter.CTkLabel):
    def __init__(self,
                 master: Any,
                 image: Union[customtkinter.CTkImage, "ImageTk.PhotoImage", None] = None, 
                 width: int = 100,
                 height: int = 100,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        super().__init__(master=master, width=width, height=height, image=image, text="", **kwargs)
        if place is not None:
            x, y = place
            self.place(x=x, y=y)

class Radio(customtkinter.CTkRadioButton):
    def __init__(self,
                 master: Any,
                 text: str = "Radio",
                 font: Literal["title", "regular", "italic"] = "regular",
                 variable: Union[tkinter.Variable, None] = None,
                 value: Union[int, str] = 0,
                 command: Optional[Callable[[], Any]] = None,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        match font:
            case "title":
                font = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
            case "regular":
                font = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
            case "italic":
                font = customtkinter.CTkFont(family="Roboto", weight="bold", slant="italic")
            case _:
                font = None
        super().__init__(master=master, text=text, font=font, variable=variable, value=value, command=command, **kwargs)
        if place is not None:
            x, y = place
            self.place(x=x, y=y)

class Switch(customtkinter.CTkSwitch):
    def __init__(self,
                 master: Any,
                 text: str = "Switch",
                 font: Literal["title", "regular", "italic"] = "regular",
                 selected: bool = False,
                 tooltip: Optional[str] = None,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        match font:
            case "title":
                font = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
            case "regular":
                font = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
            case "italic":
                font = customtkinter.CTkFont(family="Roboto", weight="bold", slant="italic")
            case _:
                font = None
        super().__init__(master=master, text=text, font=font, **kwargs)
        if place is not None:
            x, y = place
            self.place(x=x, y=y)
        if selected:
            self.select()
        if tooltip is not None:
            CTkToolTip(self, delay=0.1, message=tooltip)

class Button(customtkinter.CTkButton):
    def __init__(self,
                 master: Any,
                 text: str = "Button",
                 font: Optional[Literal["title", "regular", "italic"]] = None,
                 command: Optional[Callable[[], Any]] = None,
                 tooltip: Optional[str] = None,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        match font:
            case "title":
                font = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
            case "regular":
                font = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
            case "italic":
                font = customtkinter.CTkFont(family="Roboto", weight="bold", slant="italic")
            case _:
                font = None
        super().__init__(master=master, text=text, font=font, command=command, **kwargs)
        if place is not None:
            x, y = place
            self.place(x=x, y=y)
        if tooltip is not None:
            CTkToolTip(self, delay=0.1, message=tooltip)
            
class OptionMenu(customtkinter.CTkOptionMenu):
    def __init__(self,
                 master: Any,
                 values: Optional[list] = None,
                 command: Optional[Callable[[], Any]] = None,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        super().__init__(master=master, values=values, command=command, **kwargs)
        if place is not None:
            x, y = place
            self.place(x=x, y=y)

class SliderFrame(customtkinter.CTkFrame):
    def __init__(self,
                 master: Any,
                 element: Literal[
                     "ammo",
                     "tape",
                     "gas_speed",
                     "gas_damage",
                     "bullet_speed",
                     "damage",
                     "pistol",
                     "magnum",
                     "deagle",
                     "silenced_pistol",
                     "shotgun",
                     "jag",
                     "smg",
                     "tommy",
                     "ak",
                     "m16",
                     "dart",
                     "dartfly",
                     "hunting_rifle",
                     "sniper",
                     "laser",
                     "minigun",
                     "bow",
                     "sparrow_launcher",
                     "bcg",
                     "grenade_frag",
                     "grenade_banana",
                     "grenade_skunk",
                     "grenade_mine",
                     "grenade_zip"],
                 randomize_button: bool = False,
                 place: Optional[tuple[int, int]] = None,
                 **kwargs) -> None:
        super().__init__(master=master, width=400, fg_color="transparent", **kwargs)
        match element:
            case "ammo":
                self.slider_type: str = "ammo"
                left_text: str = "Amount:"
                right_text: str = "100"
                right_text_place: tuple[int, int] = (250, 20)
            case "tape":
                self.slider_type: str = "tape"
                left_text: str = "Amount:"
                right_text: str = "5"
                right_text_place: tuple[int, int] = (250, 20)
            case "gas_speed":
                self.slider_type: str = "gas_speed"
                left_text: str = "Gas Speed:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "gas_damage":
                self.slider_type: str = "gas_damage"
                left_text: str = "Gas Damage:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "bullet_speed":
                self.slider_type: str = "bullet_speed"
                left_text: str = "Bullet Speed:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "damage":
                self.slider_type: str = "damage"
                left_text: str = "Damage:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "pistol":
                self.slider_type: str = "weight"
                left_text: str = "Pistol:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "magnum":
                self.slider_type: str = "weight"
                left_text: str = "Magnum:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "deagle":
                self.slider_type: str = "weight"
                left_text: str = "Deagle:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "silenced_pistol":
                self.slider_type: str = "weight"
                left_text: str = "S. Pistol:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "shotgun":
                self.slider_type: str = "weight"
                left_text: str = "Shotgun:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "jag":
                self.slider_type: str = "weight"
                left_text: str = "JAG-7:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "smg":
                self.slider_type: str = "weight"
                left_text: str = "SMG"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "tommy":
                self.slider_type: str = "weight"
                left_text: str = "Tommy Gun:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "ak":
                self.slider_type: str = "weight"
                left_text: str = "AK:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "m16":
                self.slider_type: str = "weight"
                left_text: str = "M16:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "dart":
                self.slider_type: str = "weight"
                left_text: str = "Dartgun:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "dartfly":
                self.slider_type: str = "weight"
                left_text: str = "Dartflygun:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "hunting_rifle":
                self.slider_type: str = "weight"
                left_text: str = "Hunting Rifle:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "sniper":
                self.slider_type: str = "weight"
                left_text: str = "Sniper:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "laser":
                self.slider_type: str = "weight"
                left_text: str = "Laser:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "minigun":
                self.slider_type: str = "weight"
                left_text: str = "Minigun:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "bow":
                self.slider_type: str = "weight"
                left_text: str = "Bow:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "sparrow_launcher":
                self.slider_type: str = "weight"
                left_text: str = "S. Launcher:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "bcg":
                self.slider_type: str = "weight"
                left_text: str = "BCG:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "grenade_frag":
                self.slider_type: str = "weight"
                left_text: str = "Grenade:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "grenade_banana":
                self.slider_type: str = "weight"
                left_text: str = "Banana:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "grenade_skunk":
                self.slider_type: str = "weight"
                left_text: str = "Skunk Bomb:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "grenade_mine":
                self.slider_type: str = "weight"
                left_text: str = "Cat Mine:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
            case "grenade_zip":
                self.slider_type: str = "weight"
                left_text: str = "Zipline:"
                right_text: str = "1.0"
                right_text_place: tuple[int, int] = (130, 20)
        self.slider = Slider(self, slider_type=self.slider_type, command=self.on_change, place=(0, 0))
        Text(self, text=left_text, place=(0, 20))
        self.label = Text(self, text=right_text, place=right_text_place)
        if randomize_button:
            ImageButton(self, image_type="random", image=Images.ICON_DICE, command=self.randomize, place=(100, 22))
        if place is not None:
            x, y = place
            self.place(x=x, y=y)
    
    def on_change(self, value: float) -> None:
        value = round(value, 1)
        self.set(value)
    
    def randomize(self) -> None:
        value: float = round(random.uniform(0.0, 5.0), 1)
        self.set(value)
    
    def get(self) -> float:
        return self.slider.get()
    
    def set(self, value: float) -> None:
        if self.slider_type in("ammo", "tape"):
            value = int(value)
        self.slider.set(value)
        self.label.configure(text=value)