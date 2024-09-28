import customtkinter
from typing import Literal
from images import Images
from functions import *
from widgets import *

class SpawningMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("1350x520")
        self.title("Private Game Helper - Spawning Menu")
        self.resizable(False, False)
        self.selected_rarity: int = 2
        
        # Guns
        Text(self, text="Spawn Guns", font="title", place=(20, 20))
        self.rarity_common = ImageButton(master=self, image_type="rarity", image=Images.RARITY_COMMON_OFF, command=lambda: self.select_rarity("common"), place=(20, 60))
        self.rarity_uncommon = ImageButton(master=self, image_type="rarity", image=Images.RARITY_UNCOMMON_OFF, command=lambda: self.select_rarity("uncommon"), place=(130, 60))
        self.rarity_rare = ImageButton(master=self, image_type="rarity", image=Images.RARITY_RARE, command=lambda: self.select_rarity("rare"), place=(240, 60))
        self.rarity_epic = ImageButton(master=self, image_type="rarity", image=Images.RARITY_EPIC_OFF, command=lambda: self.select_rarity("epic"), place=(350, 60))
        self.rarity_legendary = ImageButton(master=self, image_type="rarity", image=Images.RARITY_LEGENDARY_OFF, command=lambda: self.select_rarity("legendary"), place=(460, 60))
        ImageButton(self, image_type="gun", image=Images.ICON_PISTOL, command=lambda: self.spawn_weapon(0), place=(20, 90))
        ImageButton(self, image_type="gun", image=Images.ICON_DUALIES, command=lambda: self.spawn_weapon(1), place=(130, 90))
        ImageButton(self, image_type="gun", image=Images.ICON_MAGNUM, command=lambda: self.spawn_weapon(2), place=(240, 90))
        ImageButton(self, image_type="gun", image=Images.ICON_DEAGLE, command=lambda: self.spawn_weapon(3), place=(350, 90))
        ImageButton(self, image_type="gun", image=Images.ICON_SILENCED_PISTOL, command=lambda: self.spawn_weapon(4), place=(460, 90))
        ImageButton(self, image_type="gun", image=Images.ICON_SHOTGUN, command=lambda: self.spawn_weapon(5), place=(20, 190))
        ImageButton(self, image_type="gun", image=Images.ICON_JAG, command=lambda: self.spawn_weapon(6), place=(130, 190))
        ImageButton(self, image_type="gun", image=Images.ICON_SMG, command=lambda: self.spawn_weapon(7), place=(240, 190))
        ImageButton(self, image_type="gun", image=Images.ICON_TOMMY, command=lambda: self.spawn_weapon(8), place=(350, 190))
        ImageButton(self, image_type="gun", image=Images.ICON_AK, command=lambda: self.spawn_weapon(9), place=(460, 190))
        ImageButton(self, image_type="gun", image=Images.ICON_M16, command=lambda: self.spawn_weapon(10), place=(20, 290))
        ImageButton(self, image_type="gun", image=Images.ICON_DART, command=lambda: self.spawn_weapon(11), place=(130, 290))
        ImageButton(self, image_type="gun", image=Images.ICON_DARTFLY, command=lambda: self.spawn_weapon(12), place=(240, 290))
        ImageButton(self, image_type="gun", image=Images.ICON_HUNTING_RIFLE, command=lambda: self.spawn_weapon(13), place=(350, 290))
        ImageButton(self, image_type="gun", image=Images.ICON_SNIPER, command=lambda: self.spawn_weapon(14), place=(460, 290))
        ImageButton(self, image_type="gun", image=Images.ICON_LASER, command=lambda: self.spawn_weapon(15), place=(20, 390))
        ImageButton(self, image_type="gun", image=Images.ICON_MINIGUN, command=lambda: self.spawn_weapon(16), place=(130, 390))
        ImageButton(self, image_type="gun", image=Images.ICON_BOW, command=lambda: self.spawn_weapon(17), place=(240, 390))
        ImageButton(self, image_type="gun", image=Images.ICON_SPARROW_LAUNCHER, command=lambda: self.spawn_weapon(18), place=(350, 390))
        ImageButton(self, image_type="gun", image=Images.ICON_BCG, command=lambda: self.spawn_weapon(19), place=(460, 390))
        
        # Juice and Ammo
        Text(self, text="Spawn Juice and Ammo", font="title", place=(620, 20))
        self.ammo_slider = SliderFrame(self, element="ammo", place=(620, 60))
        ImageButton(self, image_type="ammo", image=Images.ICON_LITTLE_AMMO, command=lambda: self.spawn_ammo(0), place=(620, 120))
        ImageButton(self, image_type="ammo", image=Images.ICON_SHELLS_AMMO, command=lambda: self.spawn_ammo(1), place=(730, 120))
        ImageButton(self, image_type="ammo", image=Images.ICON_BIG_AMMO, command=lambda: self.spawn_ammo(2), place=(840, 120))
        ImageButton(self, image_type="ammo", image=Images.ICON_SNIPER_AMMO, command=lambda: self.spawn_ammo(3), place=(620, 180))
        ImageButton(self, image_type="ammo", image=Images.ICON_SPECIAL_AMMO, command=lambda: self.spawn_ammo(4), place=(730, 180))
        ImageButton(self, image_type="ammo", image=Images.ICON_LASER_AMMO, command=lambda: self.spawn_ammo(5), place=(840, 180))
        ImageButton(self, image_type="juice", image=Images.ICON_JUICE, command=self.spawn_juice, place=(720, 240))
        
        # Tape and Grenades
        Text(self, text="Spawn Tape and Grenades", font="title", place=(620, 340))
        self.tape_slider = SliderFrame(self, element="tape", place=(620, 380))
        ImageButton(self, image_type="tape", image=Images.ICON_TAPE, command=self.spawn_tape, place=(620, 440))
        ImageButton(self, image_type="throwable", image=Images.ICON_GRENADE, command=self.spawn_grenade, place=(700, 440))
        ImageButton(self, image_type="throwable", image=Images.ICON_BANANA, command=self.spawn_banana, place=(780, 440))
        ImageButton(self, image_type="throwable", image=Images.ICON_ZIPLINE, command=self.spawn_zip, place=(860, 440))
        
        # Spawn Powerups and Armor
        Text(self, text="Spawn Powerups and Armor", font="title", place=(950, 20))
        ImageButton(self, image_type="powerup", image=Images.ICON_CLAW_BOOTS, command=lambda: self.spawn_powerup(0), place=(950, 120))
        ImageButton(self, image_type="powerup", image=Images.ICON_BANANA_FORK, command=lambda: self.spawn_powerup(1), place=(1040, 120))
        ImageButton(self, image_type="powerup", image=Images.ICON_NINJA_BOOTS, command=lambda: self.spawn_powerup(2), place=(1130, 120))
        ImageButton(self, image_type="powerup", image=Images.ICON_SNORKEL, command=lambda: self.spawn_powerup(3), place=(1220, 120))
        ImageButton(self, image_type="powerup", image=Images.ICON_CUPGRADE, command=lambda: self.spawn_powerup(4), place=(950, 180))
        ImageButton(self, image_type="powerup", image=Images.ICON_BANDOLIER, command=lambda: self.spawn_powerup(5), place=(1040, 180))
        ImageButton(self, image_type="powerup", image=Images.ICON_IMPOSSIBLE_TAPE, command=lambda: self.spawn_powerup(6), place=(1130, 180))
        ImageButton(self, image_type="armor", image=Images.ICON_ARMOR1, command=lambda: self.spawn_armor(1), place=(940, 240))
        ImageButton(self, image_type="armor", image=Images.ICON_ARMOR2, command=lambda: self.spawn_armor(2), place=(1055, 240))
        ImageButton(self, image_type="armor", image=Images.ICON_ARMOR3, command=lambda: self.spawn_armor(3), place=(1170, 240))

        # Vehicles
        Text(self, text="Spawn Vehicles", font="title", place=(950, 340))
        ImageButton(self, image_type="vehicle", image=Images.ICON_EMU, command=self.spawn_emu, place=(940, 400))
        ImageButton(self, image_type="vehicle", image=Images.ICON_HAMBALL, command=self.spawn_hamball, place=(1055, 400))
        
        # Always on top
        self.always_on_top_button = ImageButton(self, image_type="always_on_top", image=Images.ICON_PIN, command=self.always_on_top, place=(1300, 20), tooltip="Keep this window on top")
        
    def select_rarity(self, rarity: Literal["common", "uncommon", "rare", "epic", "legendary"]) -> None:
        match rarity:
            case "common":
                self.rarity_common.configure(image=Images.RARITY_COMMON)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON_OFF)
                self.rarity_rare.configure(image=Images.RARITY_RARE_OFF)
                self.rarity_epic.configure(image=Images.RARITY_EPIC_OFF)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY_OFF)
                self.selected_rarity = 0
            case "uncommon":
                self.rarity_common.configure(image=Images.RARITY_COMMON_OFF)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON)
                self.rarity_rare.configure(image=Images.RARITY_RARE_OFF)
                self.rarity_epic.configure(image=Images.RARITY_EPIC_OFF)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY_OFF)
                self.selected_rarity = 1
            case "rare":
                self.rarity_common.configure(image=Images.RARITY_COMMON_OFF)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON_OFF)
                self.rarity_rare.configure(image=Images.RARITY_RARE)
                self.rarity_epic.configure(image=Images.RARITY_EPIC_OFF)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY_OFF)
                self.selected_rarity = 2
            case "epic":
                self.rarity_common.configure(image=Images.RARITY_COMMON_OFF)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON_OFF)
                self.rarity_rare.configure(image=Images.RARITY_RARE_OFF)
                self.rarity_epic.configure(image=Images.RARITY_EPIC)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY_OFF)
                self.selected_rarity = 3
            case "legendary":
                self.rarity_common.configure(image=Images.RARITY_COMMON_OFF)
                self.rarity_uncommon.configure(image=Images.RARITY_UNCOMMON_OFF)
                self.rarity_rare.configure(image=Images.RARITY_RARE_OFF)
                self.rarity_epic.configure(image=Images.RARITY_EPIC_OFF)
                self.rarity_legendary.configure(image=Images.RARITY_LEGENDARY)
                self.selected_rarity = 4
            case _:
                raise ValueError("'rarity' argument can only be 'common', 'uncommon', 'rare', 'epic', 'legendary'")
        
    def spawn_weapon(self, id: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"gun{id} {self.selected_rarity}")
        
    def spawn_ammo(self, id: Literal[0, 1, 2, 3, 4, 5]) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"ammo{id} {round(self.ammo_slider.get())}")
                
    def spawn_juice(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"juice {round(self.ammo_slider.get())}")
        
    def spawn_tape(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tape {round(self.tape_slider.get())}")
        
    def spawn_grenade(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"nade {round(self.tape_slider.get())}")
        
    def spawn_banana(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"banana {round(self.tape_slider.get())}")
        
    def spawn_zip(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"zip {round(self.tape_slider.get())}")
        
    def spawn_powerup(self, id: Literal[0, 1, 2, 3, 4, 5, 6, 7]) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"util{id}")
        
    def spawn_armor(self, id: Literal[1, 2, 3]) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"armor{id}")
        
    def spawn_emu(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands("emu")
                
    def spawn_hamball(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands("hamball")
        
    def always_on_top(self) -> None:
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.always_on_top_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.always_on_top_button.configure(image=Images.ICON_PIN_VERTICAL)