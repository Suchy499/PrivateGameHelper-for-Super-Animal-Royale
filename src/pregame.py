import customtkinter
import requests
import webbrowser
import pywinctl
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu
from CTkMessagebox import CTkMessagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from typing import Literal
from images import Images
from info import InfoMenu
from other import CommandsMenu
from spawning import SpawningMenu
from teleporting import TeleportMenu
from gamemodes import GameModesMenu
from settings import SettingsMenu
from _version import __version__
from packaging.version import Version
from functions import *
from widgets import *

class Pregame(customtkinter.CTk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("1200x600")
        self.title("Private Game Helper")
        self.resizable(False, False)
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
        self.info_dropdown.add_option(option="Info", command=lambda: self.open_menu("Info"))
        self.info_dropdown.add_option(option="Check for Updates", command=self.check_for_updates)
        self.settings_menu = self.menu_bar.add_cascade("Settings", command=lambda: self.open_menu("Settings"))
        
        # General settings
        Text(self, text="General Settings", font="title", place=(20, 40))
        self.allitems_switch = Switch(self, text="All Items", selected=True, place=(20, 80))
        self.guns_switch = Switch(self, text="Guns", selected=True, place=(20, 125))
        self.armors_switch = Switch(self, text="Armors", selected=True, place=(20, 170))
        self.throwables_switch = Switch(self, text="Throwables", selected=True, place=(20, 215))
        self.powerups_switch = Switch(self, text="Powerups", selected=True, place=(20, 260))
        self.onehits_switch = Switch(self, text="Onehits", place=(20, 305))
        self.bots_switch = Switch(self, text="Bots", place=(20, 350))
        self.emus_switch = Switch(self, text="Emus", selected=True, place=(220, 80))
        self.hamballs_switch = Switch(self, text="Hamballs", selected=True, place=(220, 125))
        self.moles_switch = Switch(self, text="Moles", selected=True, place=(220, 170))
        self.pets_switch = Switch(self, text="Pets", selected=True, place=(220, 215))
        self.gas_switch = Switch(self, text="Gas", selected=True, place=(220, 260))
        self.norolls_switch = Switch(self, text="No Rolls", place=(220, 305))
        self.hpm = Entry(self, text="250", width=50, place=(220, 347))
        Text(self, text="HPM", place=(280, 347))
        
        # Sliders
        self.gasspeed_slider = SliderFrame(self, element="gas_speed", randomize_button=True, place=(20, 400))
        self.gasdamage_slider = SliderFrame(self, element="gas_damage", randomize_button=True, place=(220, 400))
        self.bulletspeed_slider = SliderFrame(self, element="bullet_speed", randomize_button=True, place=(20, 480))
        self.damage_slider = SliderFrame(self, element="damage", randomize_button=True, place=(220, 480))
        
        # Spawn rates
        Text(self, text="Spawn Rates", font="title", place=(420, 40))
        self.pistol_slider = SliderFrame(self, element="pistol", randomize_button=True, place=(420, 80))
        self.magnum_slider = SliderFrame(self, element="magnum", randomize_button=True, place=(420, 160))
        self.deagle_slider = SliderFrame(self, element="deagle", randomize_button=True, place=(420, 240))
        self.silencedpistol_slider = SliderFrame(self, element="silenced_pistol", randomize_button=True, place=(420, 320))
        self.shotgun_slider = SliderFrame(self, element="shotgun", randomize_button=True, place=(420, 400))
        self.jag_slider = SliderFrame(self, element="jag", randomize_button=True, place=(420, 480))
        self.smg_slider = SliderFrame(self, element="smg", randomize_button=True, place=(620, 80))
        self.tommy_slider = SliderFrame(self, element="tommy", randomize_button=True, place=(620, 160))
        self.ak_slider = SliderFrame(self, element="ak", randomize_button=True, place=(620, 240))
        self.m16_slider = SliderFrame(self, element="m16", randomize_button=True, place=(620, 320))
        self.dart_slider = SliderFrame(self, element="dart", randomize_button=True, place=(620, 400))
        self.dartfly_slider = SliderFrame(self, element="dartfly", randomize_button=True, place=(620, 480))
        self.huntingrifle_slider = SliderFrame(self, element="hunting_rifle", randomize_button=True, place=(820, 80))
        self.sniper_slider = SliderFrame(self, element="sniper", randomize_button=True, place=(820, 160))
        self.laser_slider = SliderFrame(self, element="laser", randomize_button=True, place=(820, 240))
        self.minigun_slider = SliderFrame(self, element="minigun", randomize_button=True, place=(820, 320))
        self.bow_slider = SliderFrame(self, element="bow", randomize_button=True, place=(820, 400))
        self.sparrowlauncher_slider = SliderFrame(self, element="sparrow_launcher", randomize_button=True, place=(820, 480))
        self.bcg_slider = SliderFrame(self, element="bcg", randomize_button=True, place=(1020, 80))
        self.grenadefrag_slider = SliderFrame(self, element="grenade_frag", randomize_button=True, place=(1020, 160))
        self.grenadebanana_slider = SliderFrame(self, element="grenade_banana", randomize_button=True, place=(1020, 240))
        self.grenadeskunk_slider = SliderFrame(self, element="grenade_skunk", randomize_button=True, place=(1020, 320))
        self.grenademine_slider = SliderFrame(self, element="grenade_mine", randomize_button=True, place=(1020, 400))
        self.grenadezip_slider = SliderFrame(self, element="grenade_zip", randomize_button=True, place=(1020, 480))
        
        # Buttons
        Button(self, text="Spawning Menu", command=lambda: self.open_menu("Spawning Menu"), place=(20, 550))
        Button(self, text="Teleport Menu", command=lambda: self.open_menu("Teleport Menu"), place=(190, 550))
        Button(self, text="Other Commands", command=lambda: self.open_menu("Other Commands"), place=(360, 550))
        Button(self, text="Custom Game Modes", command=lambda: self.open_menu("Game Modes"), place=(530, 550))
        Button(self, text="Apply Settings", command=self.apply_settings, place=(700, 550))
        Button(self, text="Match ID", command=self.match_id, place=(870, 550))
        Button(self, text="Start Match", command=self.start_match, place=(1040, 550))
        
        self.always_on_top_button = ImageButton(self, image_type="always_on_top", image=Images.ICON_PIN, command=self.always_on_top, place=(1150, 40), tooltip="Keep this window on top")
        ImageButton(self, image_type="random_all", image=Images.ICON_DICE, command=self.randomize_all, place=(1120, 45), tooltip="Randomize all settings")
        
        Settings.update(self=Settings)
        if Settings.popups == "1":
            response = requests.get("https://api.github.com/repos/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases/latest")
            latest_version: str = response.json()["tag_name"]
            if Version(self.VERSION) < Version(latest_version):
                update_popup = CTkMessagebox(title="Private Game Helper", message=f"Current version: {self.VERSION}\nLatest version: {latest_version}\nDo you want to update?", option_1="Yes", option_2="No")
                if update_popup.get() == "Yes":
                    webbrowser.open("https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases/latest")

    def randomize_all(self) -> None:
        self.gasspeed_slider.randomize()
        self.gasdamage_slider.randomize()
        self.bulletspeed_slider.randomize()
        self.damage_slider.randomize()
        self.pistol_slider.randomize()
        self.magnum_slider.randomize()
        self.deagle_slider.randomize()
        self.silencedpistol_slider.randomize()
        self.shotgun_slider.randomize()
        self.jag_slider.randomize()
        self.smg_slider.randomize()
        self.tommy_slider.randomize()
        self.ak_slider.randomize()
        self.m16_slider.randomize()
        self.dart_slider.randomize()
        self.dartfly_slider.randomize()
        self.huntingrifle_slider.randomize()
        self.sniper_slider.randomize()
        self.laser_slider.randomize()
        self.minigun_slider.randomize()
        self.bow_slider.randomize()
        self.sparrowlauncher_slider.randomize()
        self.bcg_slider.randomize()
        self.grenadefrag_slider.randomize()
        self.grenadebanana_slider.randomize()
        self.grenadeskunk_slider.randomize()
        self.grenademine_slider.randomize()
        self.grenadezip_slider.randomize()
    
    def open_menu(self, menu: Literal["Spawning Menu", "Teleport Menu", "Other Commands", "Info", "Settings", "Game Modes"]) -> None:
        if len(pywinctl.getWindowsWithTitle(f"Private Game Helper - {menu}", flags="IS")) == 1:
            window = pywinctl.getWindowsWithTitle(f"Private Game Helper - {menu}", flags="IS")[0]
            window.activate()
            return
        
        match menu:
            case "Spawning Menu":
                window = SpawningMenu(self)
            case "Teleport Menu":
                window = TeleportMenu(self)
            case "Other Commands":
                window = CommandsMenu(self)
            case "Info":
                window = InfoMenu(self)
            case "Settings":
                window = SettingsMenu(self)
            case "Game Modes":
                window = GameModesMenu(self)
            case _:
                return
            
        window.after(100, window.lift)
            
    def apply_settings(self) -> None:
        if open_window("Super Animal Royale") is False:
            return
        
        if self.allitems_switch.get() == 0:
            send_commands("allitems")
        if self.guns_switch.get() == 0:
            send_commands("guns")
        if self.armors_switch.get() == 0:
            send_commands("armors")
        if self.throwables_switch.get() == 0:
            send_commands("throwables")
        if self.powerups_switch.get() == 0:
            send_commands("utils")
        if self.onehits_switch.get() == 1:
            send_commands("onehits")
        if self.emus_switch.get() == 0:
            send_commands("emus")
        if self.hamballs_switch.get() == 0:
            send_commands("hamballs")
        if self.moles_switch.get() == 0:
            send_commands("moles")
        if self.pets_switch.get() == 0:
            send_commands("pets")
        if self.gas_switch.get() == 0:
            send_commands("gasoff")
        if self.norolls_switch.get() == 1:
            send_commands("noroll")
        if self.hpm.get() != "":
            send_commands(f"hpm {self.hpm.get()}")
        send_commands(f"gasspeed {round(self.gasspeed_slider.get(), 1)}",
                      f"gasdmg {round(self.gasdamage_slider.get(), 1)}",
                      f"bulletspeed {round(self.bulletspeed_slider.get(), 1)}",
                      f"dmg {round(self.damage_slider.get(), 1)}",
                      f"weight gunpistol {round(self.pistol_slider.get(), 1)} gunmagnum {round(self.magnum_slider.get(), 1)} gundeagle {round(self.deagle_slider.get(), 1)}",
                      f"weight gunsilencedpistol {round(self.silencedpistol_slider.get(), 1)} gunshotgun {round(self.shotgun_slider.get(), 1)} gunjag7 {round(self.jag_slider.get(), 1)}",
                      f"weight gunsmg {round(self.smg_slider.get(), 1)} gunthomas {round(self.tommy_slider.get(), 1)} gunak {round(self.ak_slider.get(), 1)}",
                      f"weight gunm16 {round(self.m16_slider.get(), 1)} gundart {str(round(self.dart_slider.get(), 1))} gundartepic {round(self.dartfly_slider.get(), 1)}",
                      f"weight gunhuntingrifle {round(self.huntingrifle_slider.get(), 1)} gunsniper {round(self.sniper_slider.get(), 1)} gunlaser {round(self.laser_slider.get(), 1)}",
                      f"weight gunminigun {round(self.minigun_slider.get(), 1)} gunbow {round(self.bow_slider.get(), 1)} guncrossbow {round(self.sparrowlauncher_slider.get(), 1)}",
                      f"weight gunegglauncher {round(self.bcg_slider.get(), 1)} grenadefrag {round(self.grenadefrag_slider.get(), 1)} grenadebanana {round(self.grenadebanana_slider.get(), 1)}",
                      f"weight grenadeskunk {round(self.grenadeskunk_slider.get(), 1)} grenadecatmine {round(self.grenademine_slider.get(), 1)} grenadezipline {round(self.grenadezip_slider.get(), 1)}")

    def match_id(self) -> None:
        if open_window("Super Animal Royale"):
            send_commands("matchid")

    def start_match(self) -> None:
        if open_window("Super Animal Royale"):
            if self.bots_switch.get() == 0:
                send_commands("startp")
            else:
                send_commands("start")

    def always_on_top(self) -> None:
        if self.wm_attributes("-topmost"):
            self.wm_attributes("-topmost", False)
            self.always_on_top_button.configure(image=Images.ICON_PIN)
        else:
            self.wm_attributes("-topmost", True)
            self.always_on_top_button.configure(image=Images.ICON_PIN_VERTICAL)
    
    def open_preset(self) -> None:
        files: list[tuple] = [('Config Files', '*.cfg'),
                              ('Text Document', '*.txt'),
                              ('All Files', '*.*')] 
        try:
            with askopenfile(mode='r', initialdir="presets", filetypes=files) as file:
                if file is not None:
                    file_content: str = file.read()
                    lines: list[str] = file_content.split("\n")
                    settings: dict[str, str] = {}
                    for x in lines:
                        setting: list[str] = x.split("=")
                        settings[setting[0]] = setting[1]
                    self.allitems_switch.select() if settings["ALL_ITEMS"] == "1" else self.allitems_switch.deselect()
                    self.guns_switch.select() if settings["GUNS"] == "1" else self.guns_switch.deselect()
                    self.armors_switch.select() if settings["ARMORS"] == "1" else self.armors_switch.deselect()
                    self.throwables_switch.select() if settings["THROWABLES"] == "1" else self.throwables_switch.deselect()
                    self.powerups_switch.select() if settings["POWERUPS"] == "1" else self.throwables_switch.deselect()
                    self.onehits_switch.select() if settings["ONEHITS"] == "1" else self.onehits_switch.deselect()
                    self.emus_switch.select() if settings["EMUS"] == "1" else self.emus_switch.deselect()
                    self.hamballs_switch.select() if settings["HAMBALLS"] == "1" else self.hamballs_switch.deselect()
                    self.moles_switch.select() if settings["MOLES"] == "1" else self.moles_switch.deselect()
                    self.pets_switch.select() if settings["PETS"] == "1" else self.pets_switch.deselect()
                    self.gas_switch.select() if settings["GAS"] == "1" else self.gas_switch.deselect()
                    self.norolls_switch.select() if settings["NOROLLS"] == "1" else self.norolls_switch.deselect()
                    self.bots_switch.select() if settings["BOTS"] == "1" else self.bots_switch.deselect()
                    self.gasspeed_slider.set(float(settings["GAS_SPEED"]))
                    self.gasdamage_slider.set(float(settings["GAS_DAMAGE"]))
                    self.bulletspeed_slider.set(float(settings["BULLET_SPEED"]))
                    self.damage_slider.set(float(settings["DAMAGE"]))
                    self.pistol_slider.set(float(settings["PISTOL"]))
                    self.magnum_slider.set(float(settings["MAGNUM"]))
                    self.deagle_slider.set(float(settings["DEAGLE"]))
                    self.silencedpistol_slider.set(float(settings["SILENCED_PISTOL"]))
                    self.shotgun_slider.set(float(settings["SHOTGUN"]))
                    self.jag_slider.set(float(settings["JAG-7"]))
                    self.smg_slider.set(float(settings["SMG"]))
                    self.tommy_slider.set(float(settings["TOMMY_GUN"]))
                    self.ak_slider.set(float(settings["AK"]))
                    self.m16_slider.set(float(settings["M16"]))
                    self.dart_slider.set(float(settings["DART"]))
                    self.dartfly_slider.set(float(settings["DARTFLY"]))
                    self.huntingrifle_slider.set(float(settings["HUNTING_RIFLE"]))
                    self.sniper_slider.set(float(settings["SNIPER"]))
                    self.laser_slider.set(float(settings["LASER"]))
                    self.minigun_slider.set(float(settings["MINIGUN"]))
                    self.bow_slider.set(float(settings["BOW"]))
                    self.sparrowlauncher_slider.set(float(settings["SPARROW_LAUNCHER"]))
                    self.bcg_slider.set(float(settings["BCG"]))
                    self.grenadefrag_slider.set(float(settings["GRENADE"]))
                    self.grenadebanana_slider.set(float(settings["BANANA"]))
                    self.grenadeskunk_slider.set(float(settings["SKUNK"]))
                    self.grenademine_slider.set(float(settings["MINE"]))
                    self.grenadezip_slider.set(float(settings["ZIPLINE"]))
                    self.hpm.set(settings["HPM"])
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
        self.hpm.set("250")
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
    
    def check_for_updates(self) -> None:
        response = requests.get("https://api.github.com/repos/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases/latest")
        latest_version: str = response.json()["tag_name"]
        if Version(self.VERSION) < Version(latest_version):
            update_popup = CTkMessagebox(title="Private Game Helper", message=f"Current version: {self.VERSION}\nLatest version: {latest_version}\nDo you want to update?", option_1="Yes", option_2="No")
            if update_popup.get() == "Yes":
                webbrowser.open("https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases/latest")
        else:
            CTkMessagebox(title="Private Game Helper", message="There are currently no updates available")