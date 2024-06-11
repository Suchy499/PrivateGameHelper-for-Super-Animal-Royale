import customtkinter
from CTkToolTip import CTkToolTip
from images import Images
from functions import *

class SpawningMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("1350x520")
        self.title("Private Game Helper - Spawning Menu")
        self.resizable(False, False)
        self.FONT_TITLE = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.FONT_REGULAR = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")
        self.selected_rarity: int = 2
        
        # Spawn Guns
        self.spawn_guns_title = customtkinter.CTkLabel(self, text="Spawn Guns", font=self.FONT_TITLE)
        self.spawn_guns_title.place(x=20, y=20)
        
        # Common
        self.rarity_common = customtkinter.CTkButton(self, width=100, height=24, text="", image=Images.RARITY_COMMON_OFF, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.select_rarity("common"))
        self.rarity_common.place(x=20, y=60)
        
        # Uncommon
        self.rarity_uncommon = customtkinter.CTkButton(self, width=100, height=24, text="", image=Images.RARITY_UNCOMMON_OFF, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.select_rarity("uncommon"))
        self.rarity_uncommon.place(x=130, y=60)
        
        # Rare
        self.rarity_rare = customtkinter.CTkButton(self, width=100, height=24, text="", image=Images.RARITY_RARE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.select_rarity("rare"))
        self.rarity_rare.place(x=240, y=60)
        
        # Epic
        self.rarity_epic = customtkinter.CTkButton(self, width=100, height=24, text="", image=Images.RARITY_EPIC_OFF, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.select_rarity("epic"))
        self.rarity_epic.place(x=350, y=60)
        
        # Legendary
        self.rarity_legendary = customtkinter.CTkButton(self, width=100, height=24, text="", image=Images.RARITY_LEGENDARY_OFF, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.select_rarity("legendary"))
        self.rarity_legendary.place(x=460, y=60)
        
        # Pistol
        self.spawn_pistol = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_PISTOL, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(0))
        self.spawn_pistol.place(x=20, y=90)
        
        # Dualies
        self.spawn_dualies = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_DUALIES, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(1))
        self.spawn_dualies.place(x=130, y=90)
        
        # Magnum
        self.spawn_magnum = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_MAGNUM, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(2))
        self.spawn_magnum.place(x=240, y=90)
        
        # Deagle
        self.spawn_deagle = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_DEAGLE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(3))
        self.spawn_deagle.place(x=350, y=90)
        
        # Silenced pistol
        self.spawn_silenced_pistol = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_SILENCED_PISTOL, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(4))
        self.spawn_silenced_pistol.place(x=460, y=90)
        
        # Shotgun
        self.spawn_shotgun = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_SHOTGUN, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(5))
        self.spawn_shotgun.place(x=20, y=190)
        
        # JAG
        self.spawn_jag = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_JAG, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(6))
        self.spawn_jag.place(x=130, y=190)
        
        # SMG
        self.spawn_smg = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_SMG, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(7))
        self.spawn_smg.place(x=240, y=190)
        
        # Tommy gun
        self.spawn_tommy = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_TOMMY, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(8))
        self.spawn_tommy.place(x=350, y=190)
        
        # AK
        self.spawn_ak = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_AK, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(9))
        self.spawn_ak.place(x=460, y=190)
        
        # M16
        self.spawn_m16 = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_M16, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(10))
        self.spawn_m16.place(x=20, y=290)
        
        # Dartgun
        self.spawn_dart = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_DART, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(11))
        self.spawn_dart.place(x=130, y=290)
        
        # Dartflygun
        self.spawn_dartfly = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_DARTFLY, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(12))
        self.spawn_dartfly.place(x=240, y=290)
        
        # Hunting rifle
        self.spawn_hunting_rifle = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_HUNTING_RIFLE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(13))
        self.spawn_hunting_rifle.place(x=350, y=290)
        
        # Sniper
        self.spawn_sniper = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_SNIPER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(14))
        self.spawn_sniper.place(x=460, y=290)
        
        # Superite laser
        self.spawn_laser = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_LASER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(15))
        self.spawn_laser.place(x=20, y=390)
        
        # Minigun
        self.spawn_minigun = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_MINIGUN, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(16))
        self.spawn_minigun.place(x=130, y=390)
        
        # Bow
        self.spawn_bow = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_BOW, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(17))
        self.spawn_bow.place(x=240, y=390)
        
        # Sparrow launcher
        self.spawn_sparrow_launcher = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_SPARROW_LAUNCHER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(18))
        self.spawn_sparrow_launcher.place(x=350, y=390)
        
        # BCG
        self.spawn_bcg = customtkinter.CTkButton(self, width=100, height=100, text="", image=Images.ICON_BCG, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_weapon_ctrl(19))
        self.spawn_bcg.place(x=460, y=390)
        
        # Spawn Juice and Ammo
        self.spawn_ammo_title = customtkinter.CTkLabel(self, text="Spawn Juice and Ammo", font=self.FONT_TITLE)
        self.spawn_ammo_title.place(x=620, y=20)
        
        # Ammo slider
        self.ammo_slider = customtkinter.CTkSlider(self, width=280, from_=10, to=200, number_of_steps=19, command=self.ammo_slider_ctrl)
        self.ammo_slider.place(x=620, y=60)
        self.ammo_text = customtkinter.CTkLabel(self, text="Amount:", font=self.FONT_REGULAR)
        self.ammo_text.place(x=620, y=80)
        self.ammo_label = customtkinter.CTkLabel(self, text="100", font=self.FONT_REGULAR)
        self.ammo_label.place(x=870, y=80)
        
        # Little ammo
        self.spawn_little_ammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=Images.ICON_LITTLE_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_ammo_ctrl(0))
        self.spawn_little_ammo.place(x=620, y=120)
        
        # Shells
        self.spawn_shells_ammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=Images.ICON_SHELLS_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_ammo_ctrl(1))
        self.spawn_shells_ammo.place(x=730, y=120)
        
        # Big ammo
        self.spawn_big_ammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=Images.ICON_BIG_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_ammo_ctrl(2))
        self.spawn_big_ammo.place(x=840, y=120)
        
        # Sniper ammo
        self.spawn_sniper_ammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=Images.ICON_SNIPER_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_ammo_ctrl(3))
        self.spawn_sniper_ammo.place(x=620, y=180)
        
        # Special ammo
        self.spawn_special_ammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=Images.ICON_SPECIAL_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_ammo_ctrl(4))
        self.spawn_special_ammo.place(x=730, y=180)
        
        # Laser ammo
        self.spawn_laser_ammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=Images.ICON_LASER_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_ammo_ctrl(5))
        self.spawn_laser_ammo.place(x=840, y=180)
        
        # Juice
        self.spawn_juice = customtkinter.CTkButton(self, width=80, height=80, text="", image=Images.ICON_JUICE, fg_color="transparent", bg_color="transparent", hover=False, command=self.spawn_juice_ctrl)
        self.spawn_juice.place(x=720, y=240)
        
        # Spawn Tape and Grenades
        self.spawn_tape_title = customtkinter.CTkLabel(self, text="Spawn Tape and Grenades", font=self.FONT_TITLE)
        self.spawn_tape_title.place(x=620, y=340)
        
        # Tape slider
        self.tape_slider = customtkinter.CTkSlider(self, width=280, from_=1, to=10, number_of_steps=9, command=self.tape_slider_ctrl)
        self.tape_slider.place(x=620, y=380)
        self.tape_text = customtkinter.CTkLabel(self, text="Amount:", font=self.FONT_REGULAR)
        self.tape_text.place(x=620, y=400)
        self.tape_label = customtkinter.CTkLabel(self, text="5", font=self.FONT_REGULAR)
        self.tape_label.place(x=870, y=400)
        
        # Tape
        self.spawn_tape = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_TAPE, fg_color="transparent", bg_color="transparent", hover=False, command=self.spawn_tape_ctrl)
        self.spawn_tape.place(x=620, y=440)
        
        # Grenade
        self.spawn_grenade = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_GRENADE, fg_color="transparent", bg_color="transparent", hover=False, command=self.spawn_grenade_ctrl)
        self.spawn_grenade.place(x=700, y=440)
        
        # Banana
        self.spawn_banana = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_BANANA, fg_color="transparent", bg_color="transparent", hover=False, command=self.spawn_banana_ctrl)
        self.spawn_banana.place(x=780, y=440)
        
        # Zipline
        self.spawn_zip = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_ZIPLINE, fg_color="transparent", bg_color="transparent", hover=False, command=self.spawn_zip_ctrl)
        self.spawn_zip.place(x=860, y=440)

        # Spawn Powerups and Armor
        self.spawn_powerups_title = customtkinter.CTkLabel(self, text="Spawn Powerups and Armor", font=self.FONT_TITLE)
        self.spawn_powerups_title.place(x=950, y=20)
        
        # Claw boots
        self.spawn_claw_boots = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_CLAW_BOOTS, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_powerup_ctrl(0))
        self.spawn_claw_boots.place(x=950, y=120)
        
        # Banana forker
        self.spawn_banana_fork = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_BANANA_FORK, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_powerup_ctrl(1))
        self.spawn_banana_fork.place(x=1040, y=120)
        
        # Ninja boots
        self.spawn_ninja_boots = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_NINJA_BOOTS, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_powerup_ctrl(2))
        self.spawn_ninja_boots.place(x=1130, y=120)
        
        # Snorkel
        self.spawn_snorkel = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_SNORKEL, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_powerup_ctrl(3))
        self.spawn_snorkel.place(x=1220, y=120)
        
        # Cupgrade
        self.spawn_cupgrade = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_CUPGRADE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_powerup_ctrl(4))
        self.spawn_cupgrade.place(x=950, y=180)
        
        # Bandolier
        self.spawn_bandolier = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_BANDOLIER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_powerup_ctrl(5))
        self.spawn_bandolier.place(x=1040, y=180)
        
        # Impossible tape
        self.spawn_impossible_tape = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_IMPOSSIBLE_TAPE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_powerup_ctrl(6))
        self.spawn_impossible_tape.place(x=1130, y=180)
        
        # Juicer
        self.spawn_juicer = customtkinter.CTkButton(self, width=30, height=30, text="", image=Images.ICON_JUICER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_powerup_ctrl(7))
        self.spawn_juicer.place(x=1220, y=180)
        
        # Armor 1
        self.spawn_armor1 = customtkinter.CTkButton(self, width=80, height=80, text="", image=Images.ICON_ARMOR1, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_armor_ctrl(1))
        self.spawn_armor1.place(x=940, y=240)
        
        # Armor 2
        self.spawn_armor2 = customtkinter.CTkButton(self, width=80, height=80, text="", image=Images.ICON_ARMOR2, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_armor_ctrl(2))
        self.spawn_armor2.place(x=1055, y=240)
        
        # Armor 3
        self.spawn_armor3 = customtkinter.CTkButton(self, width=80, height=80, text="", image=Images.ICON_ARMOR3, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: self.spawn_armor_ctrl(3))
        self.spawn_armor3.place(x=1170, y=240)

        # Spawn Vehicles
        self.spawn_vehicles_title = customtkinter.CTkLabel(self, text="Spawn Vehicles", font=self.FONT_TITLE)
        self.spawn_vehicles_title.place(x=950, y=340)
        
        # Emu
        self.spawn_emu = customtkinter.CTkButton(self, width=80, height=80, text="", image=Images.ICON_EMU, fg_color="transparent", bg_color="transparent", hover=False, command=self.spawn_emu_ctrl)
        self.spawn_emu.place(x=940, y=400)
        
        # Hamball
        self.spawn_hamball = customtkinter.CTkButton(self, width=80, height=80, text="", image=Images.ICON_HAMBALL, fg_color="transparent", bg_color="transparent", hover=False, command=self.spawn_hamball_ctrl)
        self.spawn_hamball.place(x=1055, y=400)
        
        # Always on top
        self.alwaysontop_button = customtkinter.CTkButton(self, width=20, height=20, text="", image=Images.ICON_PIN, hover=False, fg_color="transparent", bg_color="transparent", command=self.always_on_top)
        self.alwaysontop_button.place(x=1300, y=20)
        self.alwaysontop_tooltip = CTkToolTip(self.alwaysontop_button, delay=0, message="Keep this window on top")
        
    def select_rarity(self, rarity: str) -> None:
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
        
    def spawn_weapon_ctrl(self, id: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"gun{id} {self.selected_rarity}")
        
    def ammo_slider_ctrl(self, value: float) -> None:
        self.ammo_label.configure(text=round(value))
        
    def spawn_ammo_ctrl(self, id: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"ammo{id} {round(self.ammo_slider.get())}")
                
    def spawn_juice_ctrl(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"juice {round(self.ammo_slider.get())}")
        
    def tape_slider_ctrl(self, value: float) -> None:
        self.tape_label.configure(text=round(value))
        
    def spawn_tape_ctrl(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"tape {round(self.tape_slider.get())}")
        
    def spawn_grenade_ctrl(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"nade {round(self.tape_slider.get())}")
        
    def spawn_banana_ctrl(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"banana {round(self.tape_slider.get())}")
        
    def spawn_zip_ctrl(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"zip {round(self.tape_slider.get())}")
        
    def spawn_powerup_ctrl(self, id: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"util{id}")
        
    def spawn_armor_ctrl(self, id: int) -> None:
        if open_window("Super Animal Royale"):
            send_commands(f"armor{id}")
        
    def spawn_emu_ctrl(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands("emu")
                
    def spawn_hamball_ctrl(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands("hamball")
        
    def always_on_top(self) -> None:
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.alwaysontop_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.alwaysontop_button.configure(image=Images.ICON_PIN_VERTICAL)