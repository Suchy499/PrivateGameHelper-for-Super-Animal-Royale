import customtkinter
import keyboard
import time
import random
import requests
import webbrowser
import pywinctl
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu
from CTkToolTip import CTkToolTip
from CTkMessagebox import CTkMessagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from functools import partial
from images import Images
from info import InfoMenu
from other import CommandsMenu
from spawning import SpawningMenu
from teleporting import TeleportMenu
from gamemodes import GameModesMenu
from _version import __version__

class Pregame(customtkinter.CTk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("1200x600")
        self.title("Private Game Helper")
        self.resizable(False, False)
        self.FONT_TITLE = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
        self.FONT_REGULAR = customtkinter.CTkFont(family="Roboto", size=14, weight="bold")
        self.KEY_DELAY: float = 0.025
        self.VERSION: str = __version__
        
        # Menu bar
        self.menu_bar = CTkMenuBar(master=self)
        self.file_menu = self.menu_bar.add_cascade("File")
        self.file_dropdown = CustomDropdownMenu(widget=self.file_menu)
        self.file_dropdown.add_option(option="Open Preset", command=self.open_preset)
        self.file_dropdown.add_option(option="Save Preset", command=self.save_preset)
        self.file_dropdown.add_option(option="Restore Default", command=self.restore_default)
        self.info_menu = self.menu_bar.add_cascade("Info")
        self.info_dropdown = CustomDropdownMenu(widget=self.info_menu)
        self.info_dropdown.add_option(option="Info", command=self.open_infomenu)
        self.info_dropdown.add_option(option="Check for Updates", command=self.check_for_updates)
        
        # General settings
        self.general_title = customtkinter.CTkLabel(self, text="General Settings", font=self.FONT_TITLE)
        self.general_title.place(x=20, y=40)
        
        # All items
        self.allitems_switch = customtkinter.CTkSwitch(self, text="All Items", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.allitems_switch.place(x=20, y=80)
        self.allitems_switch.select()
        
        # Guns
        self.guns_switch = customtkinter.CTkSwitch(self, text="Guns", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.guns_switch.place(x=20, y=125)
        self.guns_switch.select()
        
        # Armor
        self.armors_switch = customtkinter.CTkSwitch(self, text="Armors", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.armors_switch.place(x=20, y=170)
        self.armors_switch.select()
        
        # Throwables
        self.throwables_switch = customtkinter.CTkSwitch(self, text="Throwables", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.throwables_switch.place(x=20, y=215)
        self.throwables_switch.select()
        
        # Powerups
        self.powerups_switch = customtkinter.CTkSwitch(self, text="Powerups", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.powerups_switch.place(x=20, y=260)
        self.powerups_switch.select()
        
        # One hits
        self.onehits_switch = customtkinter.CTkSwitch(self, text="Onehits", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.onehits_switch.place(x=20, y=305)
        self.onehits_switch.deselect()
        
        # Bots
        self.bots_switch = customtkinter.CTkSwitch(self, text="Bots", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.bots_switch.place(x=20, y=350)
        self.bots_switch.deselect()
        
        # Emus
        self.emus_switch = customtkinter.CTkSwitch(self, text="Emus", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.emus_switch.place(x=220, y=80)
        self.emus_switch.select()
        
        # Hamballs
        self.hamballs_switch = customtkinter.CTkSwitch(self, text="Hamballs", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.hamballs_switch.place(x=220, y=125)
        self.hamballs_switch.select()
        
        # Moles
        self.moles_switch = customtkinter.CTkSwitch(self, text="Moles", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.moles_switch.place(x=220, y=170)
        self.moles_switch.select()
        
        # Pets
        self.pets_switch = customtkinter.CTkSwitch(self, text="Pets", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.pets_switch.place(x=220, y=215)
        self.pets_switch.select()
        
        # Gas
        self.gas_switch = customtkinter.CTkSwitch(self, text="Gas", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.gas_switch.place(x=220, y=260)
        self.gas_switch.select()
        
        # Jumprolls
        self.norolls_switch = customtkinter.CTkSwitch(self, text="No Rolls", font=self.FONT_REGULAR, onvalue=1, offvalue=0)
        self.norolls_switch.place(x=220, y=305)
        self.norolls_switch.deselect()
        
        # HPM
        self.hpm = customtkinter.CTkEntry(self, width=50)
        self.hpm.place(x=220, y=347)
        self.hpm.insert(0, "250")
        self.hpm_text = customtkinter.CTkLabel(self, text="HPM", font=self.FONT_REGULAR)
        self.hpm_text.place(x=280, y=347)
        
        # Gas speed
        self.gasspeed_slider = customtkinter.CTkSlider(self, width=160, from_=0.4, to=3.0, number_of_steps=26, command=self.gasspeed_slider_ctrl)
        self.gasspeed_slider.set(1.0)
        self.gasspeed_slider.place(x=20, y=400)
        self.gasspeed_text = customtkinter.CTkLabel(self, text="Gas Speed:", font=self.FONT_REGULAR)
        self.gasspeed_text.place(x=20, y=420)
        self.gasspeed_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.gasspeed_label.place(x=150, y=420)
        self.gasspeed_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=self.randomize_gasspeed)
        self.gasspeed_random.place(x=120, y=422)
        
        # Gas damage
        self.gasdamage_slider = customtkinter.CTkSlider(self, width=160, from_=1.0, to=10.0, number_of_steps=90, command=self.gasdamage_slider_ctrl)
        self.gasdamage_slider.place(x=220, y=400)
        self.gasdamage_slider.set(1.0)
        self.gasdamage_text = customtkinter.CTkLabel(self, text="Gas Damage:", font=self.FONT_REGULAR)
        self.gasdamage_text.place(x=220, y=420)
        self.gasdamage_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.gasdamage_label.place(x=350, y=420)
        self.gasdamage_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=self.randomize_gasdamage)
        self.gasdamage_random.place(x=320, y=422)
        
        # Bullet speed
        self.bulletspeed_slider = customtkinter.CTkSlider(self, width=160, from_=0.5, to=2.0, number_of_steps=15, command=self.bulletspeed_slider_ctrl)
        self.bulletspeed_slider.place(x=20, y=480)
        self.bulletspeed_slider.set(1.0)
        self.bulletspeed_text = customtkinter.CTkLabel(self, text="Bullet Speed:", font=self.FONT_REGULAR)
        self.bulletspeed_text.place(x=20, y=500)
        self.bulletspeed_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.bulletspeed_label.place(x=150, y=500)
        self.bulletspeed_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=self.randomize_bulletspeed)
        self.bulletspeed_random.place(x=120, y=502)
        
        # Damage
        self.damage_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=10.0, number_of_steps=100, command=self.damage_slider_ctrl)
        self.damage_slider.place(x=220, y=480)
        self.damage_slider.set(1.0)
        self.damage_text = customtkinter.CTkLabel(self, text="Damage:", font=self.FONT_REGULAR)
        self.damage_text.place(x=220, y=500)
        self.damage_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.damage_label.place(x=350, y=500)
        self.damage_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=self.randomize_damage)
        self.damage_random.place(x=320, y=502)
        
        # Spawn rates
        self.spawnrates_title = customtkinter.CTkLabel(self, text="Spawn Rates", font=self.FONT_TITLE)
        self.spawnrates_title.place(x=420, y=40)
        
        # Pistol
        self.pistol_slider = customtkinter.CTkSlider(self, width=160, from_=0.0,to=5.0, number_of_steps=50, command=partial(self.weight_slider, "pistol"))
        self.pistol_slider.place(x=420, y=80)
        self.pistol_slider.set(1.0)
        self.pistol_text = customtkinter.CTkLabel(self, text="Pistol:", font=self.FONT_REGULAR)
        self.pistol_text.place(x=420, y=100)
        self.pistol_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.pistol_label.place(x=550, y=100)
        self.pistol_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "pistol"))
        self.pistol_random.place(x=520, y=102)
        
        # Magnum
        self.magnum_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "magnum"))
        self.magnum_slider.place(x=420, y=160)
        self.magnum_slider.set(1.0)
        self.magnum_text = customtkinter.CTkLabel(self, text="Magnum:", font=self.FONT_REGULAR)
        self.magnum_text.place(x=420, y=180)
        self.magnum_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.magnum_label.place(x=550, y=180)
        self.magnum_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "magnum"))
        self.magnum_random.place(x=520, y=182)
        
        # Deagle
        self.deagle_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "deagle"))
        self.deagle_slider.place(x=420, y=240)
        self.deagle_slider.set(1.0)
        self.deagle_text = customtkinter.CTkLabel(self, text="Deagle:", font=self.FONT_REGULAR)
        self.deagle_text.place(x=420, y=260)
        self.deagle_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.deagle_label.place(x=550, y=260)
        self.deagle_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "deagle"))
        self.deagle_random.place(x=520, y=262)
        
        # Silenced pistol
        self.silencedpistol_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "silencedpistol"))
        self.silencedpistol_slider.place(x=420, y=320)
        self.silencedpistol_slider.set(1.0)
        self.silencedpistol_text = customtkinter.CTkLabel(self, text="S. Pistol:", font=self.FONT_REGULAR)
        self.silencedpistol_text.place(x=420, y=340)
        self.silencedpistol_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.silencedpistol_label.place(x=550, y=340)
        self.silencedpistol_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "silencedpistol"))
        self.silencedpistol_random.place(x=520, y=342)
        
        # Shotgun
        self.shotgun_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "shotgun"))
        self.shotgun_slider.place(x=420, y=400)
        self.shotgun_slider.set(1.0)
        self.shotgun_text = customtkinter.CTkLabel(self, text="Shotgun:", font=self.FONT_REGULAR)
        self.shotgun_text.place(x=420, y=420)
        self.shotgun_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.shotgun_label.place(x=550, y=420)
        self.shotgun_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "shotgun"))
        self.shotgun_random.place(x=520, y=422)
        
        # JAG
        self.jag_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "jag"))
        self.jag_slider.place(x=420, y=480)
        self.jag_slider.set(1.0)
        self.jag_text = customtkinter.CTkLabel(self, text="JAG-7:", font=self.FONT_REGULAR)
        self.jag_text.place(x=420, y=500)
        self.jag_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.jag_label.place(x=550, y=500)
        self.jag_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "jag"))
        self.jag_random.place(x=520, y=502)
        
        # SMG
        self.smg_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "smg"))
        self.smg_slider.place(x=620, y=80)
        self.smg_slider.set(1.0)
        self.smg_text = customtkinter.CTkLabel(self, text="SMG:", font=self.FONT_REGULAR)
        self.smg_text.place(x=620, y=100)
        self.smg_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.smg_label.place(x=750, y=100)
        self.smg_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "smg"))
        self.smg_random.place(x=720, y=102)
        
        # Tommy gun
        self.tommy_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "tommy"))
        self.tommy_slider.place(x=620, y=160)
        self.tommy_slider.set(1.0)
        self.tommy_text = customtkinter.CTkLabel(self, text="Tommy Gun:", font=self.FONT_REGULAR)
        self.tommy_text.place(x=620, y=180)
        self.tommy_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.tommy_label.place(x=750, y=180)
        self.tommy_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "tommy"))
        self.tommy_random.place(x=720, y=182)
        
        # AK
        self.ak_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "ak"))
        self.ak_slider.place(x=620, y=240)
        self.ak_slider.set(1.0)
        self.ak_text = customtkinter.CTkLabel(self, text="AK:", font=self.FONT_REGULAR)
        self.ak_text.place(x=620, y=260)
        self.ak_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.ak_label.place(x=750, y=260)
        self.ak_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "ak"))
        self.ak_random.place(x=720, y=262)
        
        # M16
        self.m16_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "m16"))
        self.m16_slider.place(x=620, y=320)
        self.m16_slider.set(1.0)
        self.m16_text = customtkinter.CTkLabel(self, text="M16:", font=self.FONT_REGULAR)
        self.m16_text.place(x=620, y=340)
        self.m16_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.m16_label.place(x=750, y=340)
        self.m16_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "m16"))
        self.m16_random.place(x=720, y=342)
        
        # Dartgun
        self.dart_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "dart"))
        self.dart_slider.place(x=620, y=400)
        self.dart_slider.set(1.0)
        self.dart_text = customtkinter.CTkLabel(self, text="Dart Gun:", font=self.FONT_REGULAR)
        self.dart_text.place(x=620, y=420)
        self.dart_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.dart_label.place(x=750, y=420)
        self.dart_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "dart"))
        self.dart_random.place(x=720, y=422)
        
        # Darftlygun
        self.dartfly_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "dartfly"))
        self.dartfly_slider.place(x=620, y=480)
        self.dartfly_slider.set(1.0)
        self.dartfly_text = customtkinter.CTkLabel(self, text="Dartfly Gun:", font=self.FONT_REGULAR)
        self.dartfly_text.place(x=620, y=500)
        self.dartfly_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.dartfly_label.place(x=750, y=500)
        self.dartfly_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "dartfly"))
        self.dartfly_random.place(x=720, y=502)
        
        # Hunting rifle
        self.huntingrifle_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "huntingrifle"))
        self.huntingrifle_slider.place(x=820, y=80)
        self.huntingrifle_slider.set(1.0)
        self.huntingrifle_text = customtkinter.CTkLabel(self, text="Hunting Rifle:", font=self.FONT_REGULAR)
        self.huntingrifle_text.place(x=820, y=100)
        self.huntingrifle_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.huntingrifle_label.place(x=950, y=100)
        self.huntingrifle_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "huntingrifle"))
        self.huntingrifle_random.place(x=920, y=102)
        
        # Sniper
        self.sniper_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "sniper"))
        self.sniper_slider.place(x=820, y=160)
        self.sniper_slider.set(1.0)
        self.sniper_text = customtkinter.CTkLabel(self, text="Sniper:", font=self.FONT_REGULAR)
        self.sniper_text.place(x=820, y=180)
        self.sniper_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.sniper_label.place(x=950, y=180)
        self.sniper_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "sniper"))
        self.sniper_random.place(x=920, y=182)
        
        # Superite laser
        self.laser_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "laser"))
        self.laser_slider.place(x=820, y=240)
        self.laser_slider.set(1.0)
        self.laser_text = customtkinter.CTkLabel(self, text="S. Laser:", font=self.FONT_REGULAR)
        self.laser_text.place(x=820, y=260)
        self.laser_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.laser_label.place(x=950, y=260)
        self.laser_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "laser"))
        self.laser_random.place(x=920, y=262)
        
        # Minigun
        self.minigun_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "minigun"))
        self.minigun_slider.place(x=820, y=320)
        self.minigun_slider.set(1.0)
        self.minigun_text = customtkinter.CTkLabel(self, text="Minigun:", font=self.FONT_REGULAR)
        self.minigun_text.place(x=820, y=340)
        self.minigun_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.minigun_label.place(x=950, y=340)
        self.minigun_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "minigun"))
        self.minigun_random.place(x=920, y=342)
        
        # Bow
        self.bow_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "bow"))
        self.bow_slider.place(x=820, y=400)
        self.bow_slider.set(1.0)
        self.bow_text = customtkinter.CTkLabel(self, text="Bow:", font=self.FONT_REGULAR)
        self.bow_text.place(x=820, y=420)
        self.bow_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.bow_label.place(x=950, y=420)
        self.bow_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "bow"))
        self.bow_random.place(x=920, y=422)
        
        # Sparrow launcher
        self.sparrowlauncher_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "sparrowlauncher"))
        self.sparrowlauncher_slider.place(x=820, y=480)
        self.sparrowlauncher_slider.set(1.0)
        self.sparrowlauncher_text = customtkinter.CTkLabel(self, text="S. Launcher:", font=self.FONT_REGULAR)
        self.sparrowlauncher_text.place(x=820, y=500)
        self.sparrowlauncher_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.sparrowlauncher_label.place(x=950, y=500)
        self.sparrowlauncher_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "sparrowlauncher"))
        self.sparrowlauncher_random.place(x=920, y=502)
        
        # BCG
        self.bcg_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "bcg"))
        self.bcg_slider.place(x=1020, y=80)
        self.bcg_slider.set(1.0)
        self.bcg_text = customtkinter.CTkLabel(self, text="BCG:", font=self.FONT_REGULAR)
        self.bcg_text.place(x=1020, y=100)
        self.bcg_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.bcg_label.place(x=1150, y=100)
        self.bcg_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "bcg"))
        self.bcg_random.place(x=1120, y=102)
        
        # Grenade
        self.grenadefrag_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "grenadefrag"))
        self.grenadefrag_slider.place(x=1020, y=160)
        self.grenadefrag_slider.set(1.0)
        self.grenadefrag_text = customtkinter.CTkLabel(self, text="Grenade:", font=self.FONT_REGULAR)
        self.grenadefrag_text.place(x=1020, y=180)
        self.grenadefrag_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.grenadefrag_label.place(x=1150, y=180)
        self.grenadefrag_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "grenadefrag"))
        self.grenadefrag_random.place(x=1120, y=182)
        
        # Banana
        self.grenadebanana_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "grenadebanana"))
        self.grenadebanana_slider.place(x=1020, y=240)
        self.grenadebanana_slider.set(1.0)
        self.grenadebanana_text = customtkinter.CTkLabel(self, text="Banana:", font=self.FONT_REGULAR)
        self.grenadebanana_text.place(x=1020, y=260)
        self.grenadebanana_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.grenadebanana_label.place(x=1150, y=260)
        self.grenadebanana_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "grenadebanana"))
        self.grenadebanana_random.place(x=1120, y=262)
        
        # Skunk grenade
        self.grenadeskunk_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "grenadeskunk"))
        self.grenadeskunk_slider.place(x=1020, y=320)
        self.grenadeskunk_slider.set(1.0)
        self.grenadeskunk_text = customtkinter.CTkLabel(self, text="Skunk Bomb:", font=self.FONT_REGULAR)
        self.grenadeskunk_text.place(x=1020, y=340)
        self.grenadeskunk_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.grenadeskunk_label.place(x=1150, y=340)
        self.grenadeskunk_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "grenadeskunk"))
        self.grenadeskunk_random.place(x=1120, y=342)
        
        # Cat mine
        self.grenademine_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "grenademine"))
        self.grenademine_slider.place(x=1020, y=400)
        self.grenademine_slider.set(1.0)
        self.grenademine_text = customtkinter.CTkLabel(self, text="Cat Mine:", font=self.FONT_REGULAR)
        self.grenademine_text.place(x=1020, y=420)
        self.grenademine_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.grenademine_label.place(x=1150, y=420)
        self.grenademine_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "grenademine"))
        self.grenademine_random.place(x=1120, y=422)
        
        # Zipline
        self.grenadezip_slider = customtkinter.CTkSlider(self, width=160, from_=0.0, to=5.0, number_of_steps=50, command=partial(self.weight_slider, "grenadezip"))
        self.grenadezip_slider.place(x=1020, y=480)
        self.grenadezip_slider.set(1.0)
        self.grenadezip_text = customtkinter.CTkLabel(self, text="Zipline:", font=self.FONT_REGULAR)
        self.grenadezip_text.place(x=1020, y=500)
        self.grenadezip_label = customtkinter.CTkLabel(self, text="1.0", font=self.FONT_REGULAR)
        self.grenadezip_label.place(x=1150, y=500)
        self.grenadezip_random = customtkinter.CTkButton(self, width=15, height=15, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=partial(self.randomize_weapon, "grenadezip"))
        self.grenadezip_random.place(x=1120, y=502)
        
        # Buttons
        self.spawningmenu_button = customtkinter.CTkButton(self, text="Spawning Menu", command=self.open_spawningmenu)
        self.spawningmenu_button.place(x=20, y=550)
        self.teleportmenu_button = customtkinter.CTkButton(self, text="Teleport Menu", command=self.open_teleportmenu)
        self.teleportmenu_button.place(x=190, y=550)
        self.commandsmenu_button = customtkinter.CTkButton(self, text="Other Commands", command=self.open_commandsmenu)
        self.commandsmenu_button.place(x=360, y=550)
        self.gamemodesmenu_button = customtkinter.CTkButton(self, text="Custom Game Modes", command=self.open_gamemodesmenu)
        self.gamemodesmenu_button.place(x=530, y=550)
        self.applysettings_button = customtkinter.CTkButton(self, text="Apply Settings", command=self.apply_settings)
        self.applysettings_button.place(x=700, y=550)
        self.matchid_button = customtkinter.CTkButton(self, text="Match ID", command=self.match_id)
        self.matchid_button.place(x=870, y=550)
        self.start_button = customtkinter.CTkButton(self, text="Start Match", command=self.start_match)
        self.start_button.place(x=1040, y=550)
        
        # Always on top
        self.alwaysontop_button = customtkinter.CTkButton(self, width=20, height=20, text="", image=Images.ICON_PIN, hover=False, fg_color="transparent", bg_color="transparent", command=self.always_on_top)
        self.alwaysontop_button.place(x=1150, y=40)
        self.alwaysontop_tooltip = CTkToolTip(self.alwaysontop_button, delay=0, message="Keep this window on top")
        
        # Randomize all
        self.all_random = customtkinter.CTkButton(self, width=20, height=20, text="", image=Images.ICON_DICE, hover=False, fg_color="transparent", bg_color="transparent", command=self.randomize_all)
        self.all_random.place(x=1120, y=45)
        self.all_random_tooltip = CTkToolTip(self.all_random, delay=0, message="Randomize all settings")

    # Slider Controls
    def gasspeed_slider_ctrl(self, value: float) -> None:
        value = round(value, 1)
        self.gasspeed_label.configure(text=value)
        self.gasspeed_slider.set(value)
        
    def gasdamage_slider_ctrl(self, value: float) -> None:
        value = round(value, 1)
        self.gasdamage_label.configure(text=value)
        self.gasdamage_slider.set(value)
        
    def bulletspeed_slider_ctrl(self, value: float) -> None:
        value = round(value, 1)
        self.bulletspeed_label.configure(text=value)
        self.bulletspeed_slider.set(value)

    def damage_slider_ctrl(self, value: float) -> None:
        value = round(value, 1)
        self.damage_label.configure(text=value)
        self.damage_slider.set(value)

    def weight_slider(self, weapon: str, value: float) -> None:
        exec(f"value = round({str(value)}, 1)\nself.{weapon}_label.configure(text=value)\nself.{weapon}_slider.set(value)")
        # me when the the me when uuuh the yes
    
    def randomize_gasspeed(self) -> None:
        value: float = round(random.uniform(0.4, 3.0), 1)
        self.gasspeed_label.configure(text=value)
        self.gasspeed_slider.set(value)
    
    def randomize_gasdamage(self) -> None:
        value: float = round(random.uniform(1.0, 10.0), 1)
        self.gasdamage_label.configure(text=value)
        self.gasdamage_slider.set(value)
        
    def randomize_bulletspeed(self) -> None:
        value: float = round(random.uniform(0.5, 2.0), 1)
        self.bulletspeed_label.configure(text=value)
        self.bulletspeed_slider.set(value)
        
    def randomize_damage(self) -> None:
        value: float = round(random.uniform(0.0, 10.0), 1)
        self.damage_label.configure(text=value)
        self.damage_slider.set(value)
    
    def randomize_weapon(self, weapon: str) -> None:
        exec(f"value = round(random.uniform(0.0, 5.0), 1)\nself.{weapon}_label.configure(text=value)\nself.{weapon}_slider.set(value)")
        # so basically i am monkey
        # thanks copilot, very cool
        # when the exec is sus, call the among us
        # ඞ <--- this is the impostor
        # (the second part of every one of those comments were written by me, not copilot (totally not a copilot simp) (i am a copilot simp))
    def randomize_all(self) -> None:
        self.randomize_gasspeed()
        self.randomize_gasdamage()
        self.randomize_bulletspeed()
        self.randomize_damage()
        self.randomize_weapon("pistol")
        self.randomize_weapon("magnum")
        self.randomize_weapon("deagle")
        self.randomize_weapon("silencedpistol")
        self.randomize_weapon("shotgun")
        self.randomize_weapon("jag")
        self.randomize_weapon("smg")
        self.randomize_weapon("tommy")
        self.randomize_weapon("ak")
        self.randomize_weapon("m16")
        self.randomize_weapon("dart")
        self.randomize_weapon("dartfly")
        self.randomize_weapon("huntingrifle")
        self.randomize_weapon("sniper")
        self.randomize_weapon("laser")
        self.randomize_weapon("minigun")
        self.randomize_weapon("bow")
        self.randomize_weapon("sparrowlauncher")
        self.randomize_weapon("bcg")
        self.randomize_weapon("grenadefrag")
        self.randomize_weapon("grenadebanana")
        self.randomize_weapon("grenadeskunk")
        self.randomize_weapon("grenademine")
        self.randomize_weapon("grenadezip")
    
    # Button Controls
    def open_spawningmenu(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Private Game Helper - Spawning Menu", flags="IS")) == 1:
            spawningmenu_window = pywinctl.getWindowsWithTitle("Private Game Helper - Spawning Menu", flags="IS")[0]
            spawningmenu_window.activate()
        else:
            spawningmenu_window = SpawningMenu(self)
            spawningmenu_window.after(100, spawningmenu_window.lift)

    def open_teleportmenu(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Private Game Helper - Teleport Menu", flags="IS")) == 1:
            teleportmenu_window = pywinctl.getWindowsWithTitle("Private Game Helper - Teleport Menu", flags="IS")[0]
            teleportmenu_window.activate()
        else:
            teleportmenu_window = TeleportMenu(self)
            teleportmenu_window.after(100, teleportmenu_window.lift)
    
    def open_commandsmenu(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Private Game Helper - Other Commands", flags="IS")) == 1:
            commandsmenu_window = pywinctl.getWindowsWithTitle("Private Game Helper - Other Commands", flags="IS")[0]
            commandsmenu_window.activate()
        else:
            commandsmenu_window = CommandsMenu(self)
            commandsmenu_window.after(100, commandsmenu_window.lift)
            
    def open_infomenu(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Private Game Helper - Info", flags="IS")) == 1:
            infomenu_window = pywinctl.getWindowsWithTitle("Private Game Helper - Info", flags="IS")[0]
            infomenu_window.activate()
        else:
            infomenu_window = InfoMenu(self)
            infomenu_window.after(100, infomenu_window.lift)
                    
    def open_gamemodesmenu(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Private Game Helper - Game Modes", flags="IS")) == 1:
            gamemodes_window = pywinctl.getWindowsWithTitle("Private Game Helper - Game Modes", flags="IS")[0]
            gamemodes_window.activate()
        else:
            gamemodes_window = GameModesMenu(self)
            gamemodes_window.after(100, gamemodes_window.lift)
            
    def apply_settings(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        if self.allitems_switch.get() == 0:
            keyboard.write("\n/allitems\n", delay=self.KEY_DELAY)
        if self.guns_switch.get() == 0:
            keyboard.write("\n/guns\n", delay=self.KEY_DELAY)
        if self.armors_switch.get() == 0:
            keyboard.write("\n/armors\n", delay=self.KEY_DELAY)
        if self.throwables_switch.get() == 0:
            keyboard.write("\n/throwables\n", delay=self.KEY_DELAY)
        if self.powerups_switch.get() == 0:
            keyboard.write("\n/utils\n", delay=self.KEY_DELAY)
        if self.onehits_switch.get() == 1:
            keyboard.write("\n/onehits\n", delay=self.KEY_DELAY)
        if self.emus_switch.get() == 0:
            keyboard.write("\n/emus\n", delay=self.KEY_DELAY)
        if self.hamballs_switch.get() == 0:
            keyboard.write("\n/hamballs\n", delay=self.KEY_DELAY)
        if self.moles_switch.get() == 0:
            keyboard.write("\n/moles\n", delay=self.KEY_DELAY)
        if self.pets_switch.get() == 0:
            keyboard.write("\n/pets\n", delay=self.KEY_DELAY)
        if self.gas_switch.get() == 0:
            keyboard.write("\n/gasoff\n", delay=self.KEY_DELAY)
        if self.norolls_switch.get() == 1:
            keyboard.write("\n/noroll\n", delay=self.KEY_DELAY)
        if self.hpm.get() != "":
            keyboard.write(f"\n/hpm {self.hpm.get()}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/gasspeed {round(self.gasspeed_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/gasdmg {round(self.gasdamage_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/bulletspeed {round(self.bulletspeed_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/dmg {round(self.damage_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/weight gunpistol {round(self.pistol_slider.get(), 1)} gunmagnum {round(self.magnum_slider.get(), 1)} gundeagle {round(self.deagle_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/weight gunsilencedpistol {round(self.silencedpistol_slider.get(), 1)} gunshotgun {round(self.shotgun_slider.get(), 1)} gunjag7 {round(self.jag_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/weight gunsmg {round(self.smg_slider.get(), 1)} gunthomas {round(self.tommy_slider.get(), 1)} gunak {round(self.ak_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/weight gunm16 {round(self.m16_slider.get(), 1)} gundart {str(round(self.dart_slider.get(), 1))} gundartepic {round(self.dartfly_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/weight gunhuntingrifle {round(self.huntingrifle_slider.get(), 1)} gunsniper {round(self.sniper_slider.get(), 1)} gunlaser {round(self.laser_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/weight gunminigun {round(self.minigun_slider.get(), 1)} gunbow {round(self.bow_slider.get(), 1)} guncrossbow {round(self.sparrowlauncher_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/weight gunegglauncher {round(self.bcg_slider.get(), 1)} grenadefrag {round(self.grenadefrag_slider.get(), 1)} grenadebanana {round(self.grenadebanana_slider.get(), 1)}\n", delay=self.KEY_DELAY)
        keyboard.write(f"\n/weight grenadeskunk {round(self.grenadeskunk_slider.get(), 1)} grenadecatmine {round(self.grenademine_slider.get(), 1)} grenadezipline {round(self.grenadezip_slider.get(), 1)}\n", delay=self.KEY_DELAY)

    def match_id(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        keyboard.write("\n/matchid\n", delay=self.KEY_DELAY)

    def start_match(self) -> None:
        if len(pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")) == 0:
            return
        
        sar_window = pywinctl.getWindowsWithTitle("Super Animal Royale", flags="IS")[0]
        sar_window.activate()
        time.sleep(self.KEY_DELAY*16)
        if self.bots_switch.get() == 0:
            keyboard.write("\n/startp\n", delay=self.KEY_DELAY)
        else:
            keyboard.write("\n/start\n", delay=self.KEY_DELAY)

    def always_on_top(self) -> None:
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.alwaysontop_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.alwaysontop_button.configure(image=Images.ICON_PIN_VERTICAL)
    
    def open_preset(self) -> None:
        files: list[tuple] = [('Config Files', '*.cfg'),
                              ('Text Document', '*.txt'),
                              ('All Files', '*.*')] 
        try:
            with askopenfile(mode='r', initialdir="presets", filetypes=files) as file:
                if file is not None:
                    file_content: str = file.read()
                    lines: list[str] = file_content.split("\n")
                    settings: list[str] = []
                    for x in lines:
                        setting: list[str] = x.split("=")
                        settings.append(setting[1])
                    self.allitems_switch.select() if int(settings[0]) == 1 else self.allitems_switch.deselect()
                    self.guns_switch.select() if int(settings[1]) == 1 else self.guns_switch.deselect()
                    self.armors_switch.select() if int(settings[2]) == 1 else self.armors_switch.deselect()
                    self.throwables_switch.select() if int(settings[3]) == 1 else self.throwables_switch.deselect()
                    self.powerups_switch.select() if int(settings[4]) == 1 else self.throwables_switch.deselect()
                    self.onehits_switch.select() if int(settings[5]) == 1 else self.onehits_switch.deselect()
                    self.emus_switch.select() if int(settings[6]) == 1 else self.emus_switch.deselect()
                    self.hamballs_switch.select() if int(settings[7]) == 1 else self.hamballs_switch.deselect()
                    self.moles_switch.select() if int(settings[8]) == 1 else self.moles_switch.deselect()
                    self.pets_switch.select() if int(settings[9]) == 1 else self.pets_switch.deselect()
                    self.gas_switch.select() if int(settings[10]) == 1 else self.gas_switch.deselect()
                    self.norolls_switch.select() if int(settings[11]) == 1 else self.norolls_switch.deselect()
                    self.bots_switch.select() if int(settings[40]) == 1 else self.bots_switch.deselect()
                    self.gasspeed_slider.set(float(settings[12]))
                    self.gasspeed_label.configure(text=settings[12])
                    self.gasdamage_slider.set(float(settings[13]))
                    self.gasdamage_label.configure(text=settings[13])
                    self.bulletspeed_slider.set(float(settings[14]))
                    self.bulletspeed_label.configure(text=settings[14])
                    self.damage_slider.set(float(settings[15]))
                    self.damage_label.configure(text=settings[15])
                    self.pistol_slider.set(float(settings[16]))
                    self.pistol_label.configure(text=settings[16])
                    self.magnum_slider.set(float(settings[17]))
                    self.magnum_label.configure(text=settings[17])
                    self.deagle_slider.set(float(settings[18]))
                    self.deagle_label.configure(text=settings[18])
                    self.silencedpistol_slider.set(float(settings[19]))
                    self.silencedpistol_label.configure(text=settings[19])
                    self.shotgun_slider.set(float(settings[20]))
                    self.shotgun_label.configure(text=settings[20])
                    self.jag_slider.set(float(settings[21]))
                    self.jag_label.configure(text=settings[21])
                    self.smg_slider.set(float(settings[22]))
                    self.smg_label.configure(text=settings[22])
                    self.tommy_slider.set(float(settings[23]))
                    self.tommy_label.configure(text=settings[23])
                    self.ak_slider.set(float(settings[24]))
                    self.ak_label.configure(text=settings[24])
                    self.m16_slider.set(float(settings[25]))
                    self.m16_label.configure(text=settings[25])
                    self.dart_slider.set(float(settings[26]))
                    self.dart_label.configure(text=settings[26])
                    self.dartfly_slider.set(float(settings[27]))
                    self.dartfly_label.configure(text=settings[27])
                    self.huntingrifle_slider.set(float(settings[28]))
                    self.huntingrifle_label.configure(text=settings[28])
                    self.sniper_slider.set(float(settings[29]))
                    self.sniper_label.configure(text=settings[29])
                    self.laser_slider.set(float(settings[30]))
                    self.laser_label.configure(text=settings[30])
                    self.minigun_slider.set(float(settings[31]))
                    self.minigun_label.configure(text=settings[31])
                    self.bow_slider.set(float(settings[32]))
                    self.bow_label.configure(text=settings[32])
                    self.sparrowlauncher_slider.set(float(settings[33]))
                    self.sparrowlauncher_label.configure(text=settings[33])
                    self.bcg_slider.set(float(settings[34]))
                    self.bcg_label.configure(text=settings[34])
                    self.grenadefrag_slider.set(float(settings[35]))
                    self.grenadefrag_label.configure(text=settings[35])
                    self.grenadebanana_slider.set(float(settings[36]))
                    self.grenadebanana_label.configure(text=settings[36])
                    self.grenadeskunk_slider.set(float(settings[37]))
                    self.grenadeskunk_label.configure(text=settings[37])
                    self.grenademine_slider.set(float(settings[38]))
                    self.grenademine_label.configure(text=settings[38])
                    self.grenadezip_slider.set(float(settings[39]))
                    self.grenadezip_label.configure(text=settings[39])
                    self.hpm.delete(0, 99)
                    self.hpm.insert(0, settings[41])
        except TypeError:
            pass

    def save_preset(self) -> None:
        files: list[tuple] = [('Config Files', '*.cfg')]
        try:
            with asksaveasfile(filetypes=files, defaultextension=".cfg", initialdir="presets", initialfile="DefaultPreset.cfg") as file:
                if file is not None:
                    file.write(f"ALL_ITEMS={round(self.allitems_switch.get(), 1)}\n")
                    file.write(f"GUNS={round(self.guns_switch.get(), 1)}\n")
                    file.write(f"ARMORS={round(self.armors_switch.get(), 1)}\n")
                    file.write(f"THROWABLES={round(self.throwables_switch.get(), 1)}\n")
                    file.write(f"POWERUPS={round(self.powerups_switch.get(), 1)}\n")
                    file.write(f"ONEHITS={round(self.onehits_switch.get(), 1)}\n")
                    file.write(f"EMUS={round(self.emus_switch.get(), 1)}\n")
                    file.write(f"HAMBALLS={round(self.hamballs_switch.get(), 1)}\n")
                    file.write(f"MOLES={round(self.moles_switch.get(), 1)}\n")
                    file.write(f"PETS={round(self.pets_switch.get(), 1)}\n")
                    file.write(f"GAS={round(self.gas_switch.get(), 1)}\n")
                    file.write(f"NOROLLS={round(self.norolls_switch.get(), 1)}\n")
                    file.write(f"GAS_SPEED={round(self.gasspeed_slider.get(), 1)}\n")
                    file.write(f"GAS_DAMAGE={round(self.gasdamage_slider.get(), 1)}\n")
                    file.write(f"BULLET_SPEED={round(self.bulletspeed_slider.get(), 1)}\n")
                    file.write(f"DAMAGE={round(self.damage_slider.get(), 1)}\n")
                    file.write(f"PISTOL={round(self.pistol_slider.get(), 1)}\n")
                    file.write(f"MAGNUM={round(self.magnum_slider.get(), 1)}\n")
                    file.write(f"DEAGLE={round(self.deagle_slider.get(), 1)}\n")
                    file.write(f"SILENCED_PISTOL={round(self.silencedpistol_slider.get(), 1)}\n")
                    file.write(f"SHOTGUN={round(self.shotgun_slider.get(), 1)}\n")
                    file.write(f"JAG-7={round(self.jag_slider.get(), 1)}\n")
                    file.write(f"SMG={round(self.smg_slider.get(), 1)}\n")
                    file.write(f"TOMMY_GUN={round(self.tommy_slider.get(), 1)}\n")
                    file.write(f"AK={round(self.ak_slider.get(), 1)}\n")
                    file.write(f"M16={round(self.m16_slider.get(), 1)}\n")
                    file.write(f"DART={round(self.dart_slider.get(), 1)}\n")
                    file.write(f"DARTFLY={round(self.dartfly_slider.get(), 1)}\n")
                    file.write(f"HUNTING_RIFLE={round(self.huntingrifle_slider.get(), 1)}\n")
                    file.write(f"SNIPER={round(self.sniper_slider.get(), 1)}\n")
                    file.write(f"LASER={round(self.laser_slider.get(), 1)}\n")
                    file.write(f"MINIGUN={round(self.minigun_slider.get(), 1)}\n")
                    file.write(f"BOW={round(self.bow_slider.get(), 1)}\n")
                    file.write(f"SPARROW_LAUNCHER={round(self.sparrowlauncher_slider.get(), 1)}\n")
                    file.write(f"BCG={round(self.bcg_slider.get(), 1)}\n")
                    file.write(f"GRENADE={round(self.grenadefrag_slider.get(), 1)}\n")
                    file.write(f"BANANA={round(self.grenadebanana_slider.get(), 1)}\n")
                    file.write(f"SKUNK={round(self.grenadeskunk_slider.get(), 1)}\n")
                    file.write(f"MINE={round(self.grenademine_slider.get(), 1)}\n")
                    file.write(f"ZIPLINE={round(self.grenadezip_slider.get(), 1)}\n")
                    file.write(f"BOTS={round(self.bots_switch.get(), 1)}\n")
                    file.write(f"HPM={self.hpm.get()}")
        except TypeError:
            pass

    def restore_default(self) -> None:
        self.allitems_switch.select()
        self.guns_switch.select()
        self.armors_switch.select()
        self.throwables_switch.select()
        self.powerups_switch.select()
        self.onehits_switch.deselect()
        self.bots_switch.deselect()
        self.emus_switch.select()
        self.hamballs_switch.select()
        self.moles_switch.select()
        self.pets_switch.select()
        self.gas_switch.select()
        self.norolls_switch.deselect()
        self.hpm.delete(0, 99)
        self.hpm.insert(0, "250")
        self.gasspeed_slider.set(1.0)
        self.gasdamage_slider.set(1.0)
        self.bulletspeed_slider.set(1.0)
        self.damage_slider.set(1.0)
        self.pistol_slider.set(1.0)
        self.magnum_slider.set(1.0)
        self.deagle_slider.set(1.0)
        self.silencedpistol_slider.set(1.0)
        self.shotgun_slider.set(1.0)
        self.jag_slider.set(1.0)
        self.smg_slider.set(1.0)
        self.tommy_slider.set(1.0)
        self.ak_slider.set(1.0)
        self.m16_slider.set(1.0)
        self.dart_slider.set(1.0)
        self.dartfly_slider.set(1.0)
        self.huntingrifle_slider.set(1.0)
        self.sniper_slider.set(1.0)
        self.laser_slider.set(1.0)
        self.minigun_slider.set(1.0)
        self.bow_slider.set(1.0)
        self.sparrowlauncher_slider.set(1.0)
        self.bcg_slider.set(1.0)
        self.grenadefrag_slider.set(1.0)
        self.grenadebanana_slider.set(1.0)
        self.grenadeskunk_slider.set(1.0)
        self.grenademine_slider.set(1.0)
        self.grenadezip_slider.set(1.0)
        self.gasspeed_label.configure(text="1.0")
        self.gasdamage_label.configure(text="1.0")
        self.bulletspeed_label.configure(text="1.0")
        self.damage_label.configure(text="1.0")
        self.pistol_label.configure(text="1.0")
        self.magnum_label.configure(text="1.0")
        self.deagle_label.configure(text="1.0")
        self.silencedpistol_label.configure(text="1.0")
        self.shotgun_label.configure(text="1.0")
        self.jag_label.configure(text="1.0")
        self.smg_label.configure(text="1.0")
        self.tommy_label.configure(text="1.0")
        self.ak_label.configure(text="1.0")
        self.m16_label.configure(text="1.0")
        self.dart_label.configure(text="1.0")
        self.dartfly_label.configure(text="1.0")
        self.huntingrifle_label.configure(text="1.0")
        self.sniper_label.configure(text="1.0")
        self.laser_label.configure(text="1.0")
        self.minigun_label.configure(text="1.0")
        self.bow_label.configure(text="1.0")
        self.sparrowlauncher_label.configure(text="1.0")
        self.bcg_label.configure(text="1.0")
        self.grenadefrag_label.configure(text="1.0")
        self.grenadebanana_label.configure(text="1.0")
        self.grenadeskunk_label.configure(text="1.0")
        self.grenademine_label.configure(text="1.0")
        self.grenadezip_label.configure(text="1.0")
    
    def check_for_updates(self) -> None:
        response = requests.get("https://api.github.com/repos/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases/latest")
        latest_version: str = response.json()["tag_name"]
        if self.VERSION != latest_version:
            update_popup = CTkMessagebox(title="Private Game Helper", message=f"Current version: {self.VERSION}\nLatest version: {latest_version}\nDo you want to update?", option_1="Yes", option_2="No")
            if update_popup.get() == "Yes":
                webbrowser.open("https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases/latest")
        else:
            CTkMessagebox(title="Private Game Helper", message="There are currently no updates available")
            