import tkinter
from typing import Tuple
import customtkinter
import pyperclip
import keyboard
import time
from pyWinActivate import win_activate, check_win_exist
from CTkMenuBar import *
from CTkToolTip import *
from tkinter.filedialog import askopenfile, asksaveasfile
from functools import partial
from PIL import Image

# System settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("1200x600")
app.title("Private Game Helper")

# Fonts
titleFont = customtkinter.CTkFont(family="Roboto", size=24, weight="bold")
switchFont = customtkinter.CTkFont(family="Roboto", size=16, weight="bold")

# Images
AVATAR = customtkinter.CTkImage(Image.open("Assets\\Avatar.png"), size=(80, 80))
SAR_MAP = customtkinter.CTkImage(Image.open("Assets\\Map.png"), size=(768, 768))

RARITY_COMMON = customtkinter.CTkImage(Image.open("Assets\\RarityCommon.png"), size=(100, 24))
RARITY_UNCOMMON = customtkinter.CTkImage(Image.open("Assets\\RarityUncommon.png"), size=(100, 24))
RARITY_RARE = customtkinter.CTkImage(Image.open("Assets\\RarityRare.png"), size=(100, 24))
RARITY_EPIC = customtkinter.CTkImage(Image.open("Assets\\RarityEpic.png"), size=(100, 24))
RARITY_LEGENDARY = customtkinter.CTkImage(Image.open("Assets\\RarityLegendary.png"), size=(100, 24))
RARITY_COMMON_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityCommonOff.png"), size=(100, 24))
RARITY_UNCOMMON_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityUncommonOff.png"), size=(100, 24))
RARITY_RARE_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityRareOff.png"), size=(100, 24))
RARITY_EPIC_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityEpicOff.png"), size=(100, 24))
RARITY_LEGENDARY_OFF = customtkinter.CTkImage(Image.open("Assets\\RarityLegendaryOff.png"), size=(100, 24))

ICON_PISTOL = customtkinter.CTkImage(Image.open("Assets\\Pistol.png"), size=(100, 100))
ICON_DUALIES = customtkinter.CTkImage(Image.open("Assets\\Dualies.png"), size=(100, 100))
ICON_MAGNUM = customtkinter.CTkImage(Image.open("Assets\\Magnum.png"), size=(100, 100))
ICON_DEAGLE = customtkinter.CTkImage(Image.open("Assets\\Deagle.png"), size=(100, 100))
ICON_SILENCED_PISTOL = customtkinter.CTkImage(Image.open("Assets\\SilencedPistol.png"), size=(100, 100))
ICON_SHOTGUN = customtkinter.CTkImage(Image.open("Assets\\Shotgun.png"), size=(100, 100))
ICON_JAG = customtkinter.CTkImage(Image.open("Assets\\Jag.png"), size=(100, 100))
ICON_SMG = customtkinter.CTkImage(Image.open("Assets\\Smg.png"), size=(100, 100))
ICON_TOMMY = customtkinter.CTkImage(Image.open("Assets\\Tommy.png"), size=(100, 100))
ICON_AK = customtkinter.CTkImage(Image.open("Assets\\Ak.png"), size=(100, 100))
ICON_M16 = customtkinter.CTkImage(Image.open("Assets\\M16.png"), size=(100, 100))
ICON_DART = customtkinter.CTkImage(Image.open("Assets\\Dart.png"), size=(100, 100))
ICON_DARTFLY = customtkinter.CTkImage(Image.open("Assets\\Dartfly.png"), size=(100, 100))
ICON_HUNTING_RIFLE = customtkinter.CTkImage(Image.open("Assets\\HuntingRifle.png"), size=(100, 100))
ICON_SNIPER = customtkinter.CTkImage(Image.open("Assets\\Sniper.png"), size=(100, 100))
ICON_LASER = customtkinter.CTkImage(Image.open("Assets\\Laser.png"), size=(100, 100))
ICON_MINIGUN = customtkinter.CTkImage(Image.open("Assets\\Minigun.png"), size=(100, 100))
ICON_BOW = customtkinter.CTkImage(Image.open("Assets\\Bow.png"), size=(100, 100))
ICON_SPARROW_LAUNCHER = customtkinter.CTkImage(Image.open("Assets\\SparrowLauncher.png"), size=(100, 100))
ICON_BCG = customtkinter.CTkImage(Image.open("Assets\\Bcg.png"), size=(100, 100))

ICON_LITTLE_AMMO = customtkinter.CTkImage(Image.open("Assets\\LittleAmmo.png"), size=(45, 30))
ICON_BIG_AMMO = customtkinter.CTkImage(Image.open("Assets\\BigAmmo.png"), size=(45, 30))
ICON_SHELLS_AMMO = customtkinter.CTkImage(Image.open("Assets\\ShellsAmmo.png"), size=(45, 30))
ICON_SNIPER_AMMO = customtkinter.CTkImage(Image.open("Assets\\SniperAmmo.png"), size=(45, 30))
ICON_SPECIAL_AMMO = customtkinter.CTkImage(Image.open("Assets\\SpecialAmmo.png"), size=(45, 30))
ICON_LASER_AMMO = customtkinter.CTkImage(Image.open("Assets\\LaserAmmo.png"), size=(45, 30))
ICON_JUICE = customtkinter.CTkImage(Image.open("Assets\\Juice.png"), size=(80, 80))

ICON_TAPE = customtkinter.CTkImage(Image.open("Assets\\Tape.png"), size=(30, 30))
ICON_GRENADE = customtkinter.CTkImage(Image.open("Assets\\Grenade.png"), size=(30, 30))
ICON_BANANA = customtkinter.CTkImage(Image.open("Assets\\Banana.png"), size=(30, 30))
ICON_ZIPLINE = customtkinter.CTkImage(Image.open("Assets\\Zipline.png"), size=(30, 30))

ICON_CLAW_BOOTS = customtkinter.CTkImage(Image.open("Assets\\ClawBoots.png"), size=(30, 30))
ICON_BANANA_FORK = customtkinter.CTkImage(Image.open("Assets\\BananaFork.png"), size=(30, 30))
ICON_NINJA_BOOTS = customtkinter.CTkImage(Image.open("Assets\\NinjaBoots.png"), size=(30, 30))
ICON_SNORKEL = customtkinter.CTkImage(Image.open("Assets\\Snorkel.png"), size=(30, 30))
ICON_CUPGRADE = customtkinter.CTkImage(Image.open("Assets\\Cupgrade.png"), size=(30, 30))
ICON_BANDOLIER = customtkinter.CTkImage(Image.open("Assets\\Bandolier.png"), size=(30, 30))
ICON_IMPOSSIBLE_TAPE = customtkinter.CTkImage(Image.open("Assets\\ImpossibleTape.png"), size=(30, 30))
ICON_JUICER = customtkinter.CTkImage(Image.open("Assets\\Juicer.png"), size=(30, 30))

ICON_ARMOR1 = customtkinter.CTkImage(Image.open("Assets\\Armor1.png"), size=(80, 80))
ICON_ARMOR2 = customtkinter.CTkImage(Image.open("Assets\\Armor2.png"), size=(80, 80))
ICON_ARMOR3 = customtkinter.CTkImage(Image.open("Assets\\Armor3.png"), size=(80, 80))

ICON_EMU = customtkinter.CTkImage(Image.open("Assets\\Emu.png"), size=(80, 80))
ICON_HAMBALL = customtkinter.CTkImage(Image.open("Assets\\Hamball.png"), size=(80, 80))

# Variables
delay = 0.01

allitemsVar = customtkinter.IntVar(value=1)
gunsVar = customtkinter.IntVar(value=1)
armorsVar = customtkinter.IntVar(value=1)
throwablesVar = customtkinter.IntVar(value=1)
powerupsVar = customtkinter.IntVar(value=1)
onehitsVar = customtkinter.IntVar(value=0)
emusVar = customtkinter.IntVar(value=1)
hamballsVar = customtkinter.IntVar(value=1)
molesVar = customtkinter.IntVar(value=1)
petsVar = customtkinter.IntVar(value=1)
gasVar = customtkinter.IntVar(value=1)
norollsVar = customtkinter.IntVar(value=0)
gasspeedVar = customtkinter.DoubleVar(value=1.0)
gasdamageVar = customtkinter.DoubleVar(value=1.0)
bulletspeedVar = customtkinter.DoubleVar(value=1.0)
damageVar = customtkinter.DoubleVar(value=1.0)

pistolVar = customtkinter.DoubleVar(value=1.0)
magnumVar = customtkinter.DoubleVar(value=1.0)
deagleVar = customtkinter.DoubleVar(value=1.0)
silencedpistolVar = customtkinter.DoubleVar(value=1.0)
shotgunVar = customtkinter.DoubleVar(value=1.0)
jagVar = customtkinter.DoubleVar(value=1.0)
smgVar = customtkinter.DoubleVar(value=1.0)
tommyVar = customtkinter.DoubleVar(value=1.0)
akVar = customtkinter.DoubleVar(value=1.0)
m16Var = customtkinter.DoubleVar(value=1.0)
dartVar = customtkinter.DoubleVar(value=1.0)
dartflyVar = customtkinter.DoubleVar(value=1.0)
huntingrifleVar = customtkinter.DoubleVar(value=1.0)
sniperVar = customtkinter.DoubleVar(value=1.0)
laserVar = customtkinter.DoubleVar(value=1.0)
minigunVar = customtkinter.DoubleVar(value=1.0)
bowVar = customtkinter.DoubleVar(value=1.0)
sparrowlauncherVar = customtkinter.DoubleVar(value=1.0)
bcgVar = customtkinter.DoubleVar(value=1.0)
grenadefragVar = customtkinter.DoubleVar(value=1.0)
grenadebananaVar = customtkinter.DoubleVar(value=1.0)
grenadeskunkVar = customtkinter.DoubleVar(value=1.0)
grenademineVar = customtkinter.DoubleVar(value=1.0)
grenadezipVar = customtkinter.DoubleVar(value=1.0)

# Menu Bar Functions
def open_preset():
    files = [('Config Files', '*.cfg'),
             ('Text Document', '*.txt'),
             ('All Files', '*.*')] 
    file = askopenfile(mode='r', filetypes=files)
    if file is not None:
        content = file.read().split("\n")
        settings = []
        for x in content:
            setting = x.split("=")
            settings.append(setting[1])
        file.close()
        
        allitemsVar.set(settings[0])
        gunsVar.set(settings[1])
        armorsVar.set(settings[2])
        throwablesVar.set(settings[3])
        powerupsVar.set(settings[4])
        onehitsVar.set(settings[5])
        emusVar.set(settings[6])
        hamballsVar.set(settings[7])
        molesVar.set(settings[8])
        petsVar.set(settings[9])
        gasVar.set(settings[10])
        norollsVar.set(settings[11])
        gasspeedVar.set(settings[12])
        gasspeedTextVal.configure(text=settings[12])
        gasdamageVar.set(settings[13])
        gasdamageTextVal.configure(text=settings[13])
        bulletspeedVar.set(settings[14])
        bulletspeedTextVal.configure(text=settings[14])
        damageVar.set(settings[15])
        damageTextVal.configure(text=settings[15])
        pistolVar.set(settings[16])
        pistolTextVal.configure(text=settings[16])
        magnumVar.set(settings[17])
        magnumTextVal.configure(text=settings[17])
        deagleVar.set(settings[18])
        deagleTextVal.configure(text=settings[18])
        silencedpistolVar.set(settings[19])
        silencedpistolTextVal.configure(text=settings[19])
        shotgunVar.set(settings[20])
        shotgunTextVal.configure(text=settings[20])
        jagVar.set(settings[21])
        jagTextVal.configure(text=settings[21])
        smgVar.set(settings[22])
        smgTextVal.configure(text=settings[22])
        tommyVar.set(settings[23])
        tommyTextVal.configure(text=settings[23])
        akVar.set(settings[24])
        akTextVal.configure(text=settings[24])
        m16Var.set(settings[25])
        m16TextVal.configure(text=settings[25])
        dartVar.set(settings[26])
        dartTextVal.configure(text=settings[26])
        dartflyVar.set(settings[27])
        dartflyTextVal.configure(text=settings[27])
        huntingrifleVar.set(settings[28])
        huntingrifleTextVal.configure(text=settings[28])
        sniperVar.set(settings[29])
        sniperTextVal.configure(text=settings[29])
        laserVar.set(settings[30])
        laserTextVal.configure(text=settings[30])
        minigunVar.set(settings[31])
        minigunTextVal.configure(text=settings[31])
        bowVar.set(settings[32])
        bowTextVal.configure(text=settings[32])
        sparrowlauncherVar.set(settings[33])
        sparrowlauncherTextVal.configure(text=settings[33])
        bcgVar.set(settings[34])
        bcgTextVal.configure(text=settings[34])
        grenadefragVar.set(settings[35])
        grenadefragTextVal.configure(text=settings[35])
        grenadebananaVar.set(settings[36])
        grenadebananaTextVal.configure(text=settings[36])
        grenadeskunkVar.set(settings[37])
        grenadeskunkTextVal.configure(text=settings[37])
        grenademineVar.set(settings[38])
        grenademineTextVal.configure(text=settings[38])
        grenadezipVar.set(settings[39])
        grenadezipTextVal.configure(text=settings[39])
    return

def save_preset():
    files = [('Config Files', '*.cfg')] 
    file = asksaveasfile(filetypes=files, defaultextension=files, initialfile="DefaultPreset.cfg")
    if file is not None:
        file.write("ALL_ITEMS=" + str(allitemsVar.get()) + "\n")
        file.write("GUNS=" + str(gunsVar.get()) + "\n")
        file.write("ARMORS=" + str(armorsVar.get()) + "\n")
        file.write("THROWABLES=" + str(throwablesVar.get()) + "\n")
        file.write("POWERUPS=" + str(powerupsVar.get()) + "\n")
        file.write("ONEHITS=" + str(onehitsVar.get()) + "\n")
        file.write("EMUS=" + str(emusVar.get()) + "\n")
        file.write("HAMBALLS=" + str(hamballsVar.get()) + "\n")
        file.write("MOLES=" + str(molesVar.get()) + "\n")
        file.write("PETS=" + str(petsVar.get()) + "\n")
        file.write("GAS=" + str(gasVar.get()) + "\n")
        file.write("NOROLLS=" + str(norollsVar.get()) + "\n")
        file.write("GAS_SPEED=" + str(gasspeedVar.get()) + "\n")
        file.write("GAS_DAMAGE=" + str(gasdamageVar.get()) + "\n")
        file.write("BULLET_SPEED=" + str(bulletspeedVar.get()) + "\n")
        file.write("DAMAGE=" + str(damageVar.get()) + "\n")
        file.write("PISTOL=" + str(pistolVar.get()) + "\n")
        file.write("MAGNUM=" + str(magnumVar.get()) + "\n")
        file.write("DEAGLE=" + str(deagleVar.get()) + "\n")
        file.write("SILENCED_PISTOL=" + str(silencedpistolVar.get()) + "\n")
        file.write("SHOTGUN=" + str(shotgunVar.get()) + "\n")
        file.write("JAG-7=" + str(jagVar.get()) + "\n")
        file.write("SMG=" + str(smgVar.get()) + "\n")
        file.write("TOMMY_GUN=" + str(tommyVar.get()) + "\n")
        file.write("AK=" + str(akVar.get()) + "\n")
        file.write("M16=" + str(m16Var.get()) + "\n")
        file.write("DART=" + str(dartVar.get()) + "\n")
        file.write("DARTFLY=" + str(dartflyVar.get()) + "\n")
        file.write("HUNTING_RIFLE=" + str(huntingrifleVar.get()) + "\n")
        file.write("SNIPER=" + str(sniperVar.get()) + "\n")
        file.write("LASER=" + str(laserVar.get()) + "\n")
        file.write("MINIGUN=" + str(minigunVar.get()) + "\n")
        file.write("BOW=" + str(bowVar.get()) + "\n")
        file.write("SPARROW_LAUNCHER=" + str(sparrowlauncherVar.get()) + "\n")
        file.write("BCG=" + str(bcgVar.get()) + "\n")
        file.write("GRENADE=" + str(grenadefragVar.get()) + "\n")
        file.write("BANANA=" + str(grenadebananaVar.get()) + "\n")
        file.write("SKUNK=" + str(grenadeskunkVar.get()) + "\n")
        file.write("MINE=" + str(grenademineVar.get()) + "\n")
        file.write("ZIPLINE=" + str(grenadezipVar.get()))
        file.close()
    return

def restore_default():
    allitemsVar.set(1)
    gunsVar.set(1)
    armorsVar.set(1)
    throwablesVar.set(1)
    powerupsVar.set(1)
    onehitsVar.set(0)
    emusVar.set(1)
    hamballsVar.set(1)
    molesVar.set(1)
    petsVar.set(1)
    gasVar.set(1)
    norollsVar.set(0)
    gasspeedVar.set(1.0)
    gasspeedTextVal.configure(text="1.0")
    gasdamageVar.set(1.0)
    gasdamageTextVal.configure(text="1.0")
    bulletspeedVar.set(1.0)
    bulletspeedTextVal.configure(text="1.0")
    damageVar.set(1.0)
    damageTextVal.configure(text="1.0")
    pistolVar.set(1.0)
    pistolTextVal.configure(text="1.0")
    magnumVar.set(1.0)
    magnumTextVal.configure(text="1.0")
    deagleVar.set(1.0)
    deagleTextVal.configure(text="1.0")
    silencedpistolVar.set(1.0)
    silencedpistolTextVal.configure(text="1.0")
    shotgunVar.set(1.0)
    shotgunTextVal.configure(text="1.0")
    jagVar.set(1.0)
    jagTextVal.configure(text="1.0")
    smgVar.set(1.0)
    smgTextVal.configure(text="1.0")
    tommyVar.set(1.0)
    tommyTextVal.configure(text="1.0")
    akVar.set(1.0)
    akTextVal.configure(text="1.0")
    m16Var.set(1.0)
    m16TextVal.configure(text="1.0")
    dartVar.set(1.0)
    dartTextVal.configure(text="1.0")
    dartflyVar.set(1.0)
    dartflyTextVal.configure(text="1.0")
    huntingrifleVar.set(1.0)
    huntingrifleTextVal.configure(text="1.0")
    sniperVar.set(1.0)
    sniperTextVal.configure(text="1.0")
    laserVar.set(1.0)
    laserTextVal.configure(text="1.0")
    minigunVar.set(1.0)
    minigunTextVal.configure(text="1.0")
    bowVar.set(1.0)
    bowTextVal.configure(text="1.0")
    sparrowlauncherVar.set(1.0)
    sparrowlauncherTextVal.configure(text="1.0")
    bcgVar.set(1.0)
    bcgTextVal.configure(text="1.0")
    grenadefragVar.set(1.0)
    grenadefragTextVal.configure(text="1.0")
    grenadebananaVar.set(1.0)
    grenadebananaTextVal.configure(text="1.0")
    grenadeskunkVar.set(1.0)
    grenadeskunkTextVal.configure(text="1.0")
    grenademineVar.set(1.0)
    grenademineTextVal.configure(text="1.0")
    grenadezipVar.set(1.0)
    grenadezipTextVal.configure(text="1.0")
    return

def info_menu():
    if check_win_exist("Private Game Helper - Info"):
        win_activate("Private Game Helper - Info", partial_match=False)
    else:
        infomenuWindow = InfoMenu(app)
        infomenuWindow.after(100, infomenuWindow.lift)
    return

class InfoMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("880x150")
        self.title("Private Game Helper - Info")
        self.resizable(False, False)
        
        customtkinter.CTkLabel(self, text="Made by Suchy499", font=titleFont).place(x=20, y=20)
        customtkinter.CTkLabel(self, text="Important:\n- Only apply settings once per custom lobby\n- After using 'Apply Settings', do not press any keys until the program has finished working\nFor any kind of help, you can reach me through discord!", font=switchFont, justify="left").place(x=20, y=60)
        customtkinter.CTkLabel(self, width=80, height=80, text="", image=AVATAR).place(x=770, y=40)

# Menu Bar
menuBar = CTkMenuBar(master=app)
fileMenu = menuBar.add_cascade("File")
fileDropdown = CustomDropdownMenu(widget=fileMenu)
fileDropdown.add_option(option="Open Preset", command=open_preset)
fileDropdown.add_option(option="Save Preset", command=save_preset)
fileDropdown.add_option(option="Restore Default", command=restore_default)
infoMenu = menuBar.add_cascade("Info", command=info_menu)

# Slider Controls
def gasspeed_slider(value):
    value = round(value, 1)
    gasspeedTextVal.configure(text=value)
    gasspeedVar.set(value)
    return
    
def gasdamage_slider(value):
    value = round(value, 1)
    gasdamageTextVal.configure(text=value)
    gasdamageVar.set(value)
    return
    
def bulletspeed_slider(value):
    value = round(value, 1)
    bulletspeedTextVal.configure(text=value)
    bulletspeedVar.set(value)
    return

def damage_slider(value):
    value = round(value, 1)
    damageTextVal.configure(text=value)
    damageVar.set(value)
    return

def weight_slider(weapon, value):
    exec("value = " + "round(" + str(value) + ", 1)\n" + str(weapon) + "TextVal.configure(text=value)\n" + str(weapon) + "Var.set(value)")
    return
    
# Button Controls
def open_spawningmenu():
    if check_win_exist("Private Game Helper - Spawning Menu"):
        win_activate("Private Game Helper - Spawning Menu", partial_match=False)
    else:
        spawningmenuWindow = SpawningMenu(app)
        spawningmenuWindow.after(100, spawningmenuWindow.lift)
    return

def open_teleportmenu():
    if check_win_exist("Private Game Helper - Teleport Menu"):
        win_activate("Private Game Helper - Teleport Menu", partial_match=False)
    else:
        teleportmenuWindow = TeleportMenu(app)
        teleportmenuWindow.after(100, teleportmenuWindow.lift)
    return
        
def apply_settings():
    if check_win_exist("Super Animal Royale"):
        win_activate(window_title="Super Animal Royale", partial_match=False)
        if (allitemsVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/allitems", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (gunsVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/guns", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (armorsVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/armors", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (throwablesVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/throwables", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (powerupsVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/utils", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (onehitsVar.get() == 1):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/onehits", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (emusVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/emus", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (hamballsVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/hamballs", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (molesVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/moles", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (petsVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/pets", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (gasVar.get() == 0):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/gasoff", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        if (norollsVar.get() == 1):
            time.sleep(delay)
            keyboard.send('enter')
            time.sleep(delay)
            keyboard.write("/noroll", delay=delay)
            time.sleep(delay)
            keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/gasspeed " + str(gasspeedVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/gasdmg " + str(gasdamageVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/bulletspeed " + str(bulletspeedVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/dmg " + str(damageVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/weight gunpistol " + str(pistolVar.get()) + " gunmagnum " + str(magnumVar.get()) + " gundeagle " + str(deagleVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/weight gunsilencedpistol " + str(silencedpistolVar.get()) + " gunshotgun " + str(shotgunVar.get()) + " gunjag7 " + str(jagVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/weight gunsmg " + str(smgVar.get()) + " gunthomas " + str(tommyVar.get()) + " gunak " + str(akVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/weight gunm16 " + str(m16Var.get()) + " gundart " + str(dartVar.get()) + " gundartepic " + str(dartflyVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/weight gunhuntingrifle " + str(huntingrifleVar.get()) + " gunsniper " + str(sniperVar.get()) + " gunlaser " + str(laserVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/weight gunminigun " + str(minigunVar.get()) + " gunbow " + str(bowVar.get()) + " guncrossbow " + str(sparrowlauncherVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/weight gunegglauncher " + str(bcgVar.get()) + " grenadefrag " + str(grenadefragVar.get()) + " grenadebanana " + str(grenadebananaVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/weight grenadeskunk " + str(grenadeskunkVar.get()) + " grenadecatmine " + str(grenademineVar.get()) + " grenadezipline " + str(grenadezipVar.get()), delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
    return

def match_id():
    if check_win_exist("Super Animal Royale"):
        win_activate(window_title="Super Animal Royale", partial_match=False)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/matchid", delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
    return

def start_match():
    if check_win_exist("Super Animal Royale"):
        win_activate(window_title="Super Animal Royale", partial_match=False)
        time.sleep(delay)
        keyboard.send('enter')
        time.sleep(delay)
        keyboard.write("/startp", delay=delay)
        time.sleep(delay)
        keyboard.send('enter')
    return

# Spawning menu
class SpawningMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1300x520")
        self.title("Private Game Helper - Spawning Menu")
        self.resizable(False, False)
        
        def select_rarity(rarity):
            match rarity:
                case "common":
                    self.rarityCommon.configure(image=RARITY_COMMON)
                    self.rarityUnommon.configure(image=RARITY_UNCOMMON_OFF)
                    self.rarityRare.configure(image=RARITY_RARE_OFF)
                    self.rarityEpic.configure(image=RARITY_EPIC_OFF)
                    self.rarityLegendary.configure(image=RARITY_LEGENDARY_OFF)
                    self.selectedRarity = 0
                case "uncommon":
                    self.rarityCommon.configure(image=RARITY_COMMON_OFF)
                    self.rarityUnommon.configure(image=RARITY_UNCOMMON)
                    self.rarityRare.configure(image=RARITY_RARE_OFF)
                    self.rarityEpic.configure(image=RARITY_EPIC_OFF)
                    self.rarityLegendary.configure(image=RARITY_LEGENDARY_OFF)
                    self.selectedRarity = 1
                case "rare":
                    self.rarityCommon.configure(image=RARITY_COMMON_OFF)
                    self.rarityUnommon.configure(image=RARITY_UNCOMMON_OFF)
                    self.rarityRare.configure(image=RARITY_RARE)
                    self.rarityEpic.configure(image=RARITY_EPIC_OFF)
                    self.rarityLegendary.configure(image=RARITY_LEGENDARY_OFF)
                    self.selectedRarity = 2
                case "epic":
                    self.rarityCommon.configure(image=RARITY_COMMON_OFF)
                    self.rarityUnommon.configure(image=RARITY_UNCOMMON_OFF)
                    self.rarityRare.configure(image=RARITY_RARE_OFF)
                    self.rarityEpic.configure(image=RARITY_EPIC)
                    self.rarityLegendary.configure(image=RARITY_LEGENDARY_OFF)
                    self.selectedRarity = 3
                case "legendary":
                    self.rarityCommon.configure(image=RARITY_COMMON_OFF)
                    self.rarityUnommon.configure(image=RARITY_UNCOMMON_OFF)
                    self.rarityRare.configure(image=RARITY_RARE_OFF)
                    self.rarityEpic.configure(image=RARITY_EPIC_OFF)
                    self.rarityLegendary.configure(image=RARITY_LEGENDARY)
                    self.selectedRarity = 4
            return
        
        def spawn_weapon(id):
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/gun" + str(id) + " " + str(self.selectedRarity), delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
        
        def ammo_slider(value):
            self.ammoTextVal.configure(text=int(value))
            return
        
        def spawn_ammo(id):
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/ammo" + str(id) + " " + str(self.ammoVar.get()), delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
                
        def spawn_juice():
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/juice " + str(self.ammoVar.get()), delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
        
        def tape_slider(value):
            self.tapeTextVal.configure(text=int(value))
            return
        
        def spawn_tape():
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/tape " + str(self.tapeVar.get()), delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
        
        def spawn_grenade():
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/nade " + str(self.tapeVar.get()), delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
        
        def spawn_banana():
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/banana " + str(self.tapeVar.get()), delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
        
        def spawn_zip():
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/zip " + str(self.tapeVar.get()), delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
        
        def spawn_powerup(id):
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/util" + str(id), delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
        
        def spawn_armor(id):
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/armor" + str(id), delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
        
        def spawn_emu():
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/emu", delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
                
        def spawn_hamball():
            if check_win_exist("Super Animal Royale"):
                win_activate(window_title="Super Animal Royale", partial_match=False)
                time.sleep(delay)
                keyboard.send('enter')
                time.sleep(delay)
                keyboard.write("/hamball", delay=delay)
                time.sleep(delay)
                keyboard.send('enter')
            return
        
        self.ammoVar = customtkinter.IntVar(value=100)
        self.tapeVar = customtkinter.IntVar(value=5)
        
        # Spawn Guns
        self.selectedRarity = 2
        self.spawnGunsTitle = customtkinter.CTkLabel(self, text="Spawn Guns", font=titleFont).place(x=20, y=20)
        self.rarityCommon = customtkinter.CTkButton(self, width=100, height=24, text="", image=RARITY_COMMON_OFF, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: select_rarity("common"))
        self.rarityCommon.place(x=20, y=60)
        self.rarityUnommon = customtkinter.CTkButton(self, width=100, height=24, text="", image=RARITY_UNCOMMON_OFF, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: select_rarity("uncommon"))
        self.rarityUnommon.place(x=130, y=60)
        self.rarityRare = customtkinter.CTkButton(self, width=100, height=24, text="", image=RARITY_RARE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: select_rarity("rare"))
        self.rarityRare.place(x=240, y=60)
        self.rarityEpic = customtkinter.CTkButton(self, width=100, height=24, text="", image=RARITY_EPIC_OFF, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: select_rarity("epic"))
        self.rarityEpic.place(x=350, y=60)
        self.rarityLegendary = customtkinter.CTkButton(self, width=100, height=24, text="", image=RARITY_LEGENDARY_OFF, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: select_rarity("legendary"))
        self.rarityLegendary.place(x=460, y=60)
        
        self.spawnPistol = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_PISTOL, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(0))
        self.spawnPistol.place(x=20, y=90)
        self.spawnDualies = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_DUALIES, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(1))
        self.spawnDualies.place(x=130, y=90)
        self.spawnMagnum = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_MAGNUM, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(2))
        self.spawnMagnum.place(x=240, y=90)
        self.spawnDeagle = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_DEAGLE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(3))
        self.spawnDeagle.place(x=350, y=90)
        self.spawnSilencedPistol = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_SILENCED_PISTOL, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(4))
        self.spawnSilencedPistol.place(x=460, y=90)
        
        self.spawnShotgun = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_SHOTGUN, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(5))
        self.spawnShotgun.place(x=20, y=190)
        self.spawnJag = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_JAG, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(6))
        self.spawnJag.place(x=130, y=190)
        self.spawnSmg = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_SMG, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(7))
        self.spawnSmg.place(x=240, y=190)
        self.spawnTommy = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_TOMMY, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(8))
        self.spawnTommy.place(x=350, y=190)
        self.spawnAk = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_AK, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(9))
        self.spawnAk.place(x=460, y=190)
        
        self.spawnM16 = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_M16, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(10))
        self.spawnM16.place(x=20, y=290)
        self.spawnDart = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_DART, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(11))
        self.spawnDart.place(x=130, y=290)
        self.spawnDartfly = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_DARTFLY, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(12))
        self.spawnDartfly.place(x=240, y=290)
        self.spawnHuntingrifle = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_HUNTING_RIFLE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(13))
        self.spawnHuntingrifle.place(x=350, y=290)
        self.spawnSniper = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_SNIPER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(14))
        self.spawnSniper.place(x=460, y=290)
        
        self.spawnLaser = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_LASER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(15))
        self.spawnLaser.place(x=20, y=390)
        self.spawnMinigun = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_MINIGUN, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(16))
        self.spawnMinigun.place(x=130, y=390)
        self.spawnBow = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_BOW, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(17))
        self.spawnBow.place(x=240, y=390)
        self.spawnSparrowlauncher = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_SPARROW_LAUNCHER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(18))
        self.spawnSparrowlauncher.place(x=350, y=390)
        self.spawnBcg = customtkinter.CTkButton(self, width=100, height=100, text="", image=ICON_BCG, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_weapon(19))
        self.spawnBcg.place(x=460, y=390)
        
        # Spawn Juice and Ammo
        self.spawnAmmoTitle = customtkinter.CTkLabel(self, text="Spawn Juice and Ammo", font=titleFont).place(x=620, y=20)
        self.ammoSlider = customtkinter.CTkSlider(self, width=280, from_=10, to=200, number_of_steps=19, variable=self.ammoVar, command=ammo_slider).place(x=620, y=60)
        self.ammoText = customtkinter.CTkLabel(self, text="Amount:", font=switchFont).place(x=620, y=80)
        self.ammoTextVal = customtkinter.CTkLabel(self, text="100", font=switchFont)
        self.ammoTextVal.place(x=870, y=80)
        
        self.spawnLittleammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=ICON_LITTLE_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_ammo(0))
        self.spawnLittleammo.place(x=620, y=120)
        self.spawnShellsammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=ICON_SHELLS_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_ammo(1))
        self.spawnShellsammo.place(x=730, y=120)
        self.spawnBigammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=ICON_BIG_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_ammo(2))
        self.spawnBigammo.place(x=840, y=120)
        
        self.spawnSniperammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=ICON_SNIPER_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_ammo(3))
        self.spawnSniperammo.place(x=620, y=180)
        self.spawnSpecialammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=ICON_SPECIAL_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_ammo(4))
        self.spawnSpecialammo.place(x=730, y=180)
        self.spawnLaserammo = customtkinter.CTkButton(self, width=45, height=30, text="", image=ICON_LASER_AMMO, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_ammo(5))
        self.spawnLaserammo.place(x=840, y=180)
        
        self.spawnJuice = customtkinter.CTkButton(self, width=80, height=80, text="", image=ICON_JUICE, fg_color="transparent", bg_color="transparent", hover=False, command=spawn_juice)
        self.spawnJuice.place(x=720, y=240)
        
        # Spawn Tape and Grenades
        self.spawnTapeTitle = customtkinter.CTkLabel(self, text="Spawn Tape and Grenades", font=titleFont).place(x=620, y=340)
        self.tapeSlider = customtkinter.CTkSlider(self, width=280, from_=1, to=10, number_of_steps=9, variable=self.tapeVar, command=tape_slider).place(x=620, y=380)
        self.tapeText = customtkinter.CTkLabel(self, text="Amount:", font=switchFont).place(x=620, y=400)
        self.tapeTextVal = customtkinter.CTkLabel(self, text="5", font=switchFont)
        self.tapeTextVal.place(x=870, y=400)
        
        self.spawnTape = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_TAPE, fg_color="transparent", bg_color="transparent", hover=False, command=spawn_tape)
        self.spawnTape.place(x=620, y=440)
        self.spawnGrenade = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_GRENADE, fg_color="transparent", bg_color="transparent", hover=False, command=spawn_grenade)
        self.spawnGrenade.place(x=700, y=440)
        self.spawnBanana = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_BANANA, fg_color="transparent", bg_color="transparent", hover=False, command=spawn_banana)
        self.spawnBanana.place(x=780, y=440)
        self.spawnZip = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_ZIPLINE, fg_color="transparent", bg_color="transparent", hover=False, command=spawn_zip)
        self.spawnZip.place(x=860, y=440)

        # Spawn Powerups and Armor
        self.spawnPowerupsTitle = customtkinter.CTkLabel(self, text="Spawn Powerups and Armor", font=titleFont).place(x=950, y=20)
        self.spawnClawboots = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_CLAW_BOOTS, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_powerup(0))
        self.spawnClawboots.place(x=950, y=120)
        self.spawnBananafork = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_BANANA_FORK, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_powerup(1))
        self.spawnBananafork.place(x=1040, y=120)
        self.spawnNinjaboots = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_NINJA_BOOTS, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_powerup(2))
        self.spawnNinjaboots.place(x=1130, y=120)
        self.spawnSnorkel = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_SNORKEL, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_powerup(3))
        self.spawnSnorkel.place(x=1220, y=120)
        
        self.spawnCupgrade = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_CUPGRADE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_powerup(4))
        self.spawnCupgrade.place(x=950, y=180)
        self.spawnBandolier = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_BANDOLIER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_powerup(5))
        self.spawnBandolier.place(x=1040, y=180)
        self.spawnImpossibletape = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_IMPOSSIBLE_TAPE, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_powerup(6))
        self.spawnImpossibletape.place(x=1130, y=180)
        self.spawnJuicer = customtkinter.CTkButton(self, width=30, height=30, text="", image=ICON_JUICER, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_powerup(7))
        self.spawnJuicer.place(x=1220, y=180)
        
        self.spawnArmor1 = customtkinter.CTkButton(self, width=80, height=80, text="", image=ICON_ARMOR1, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_armor(1))
        self.spawnArmor1.place(x=940, y=240)
        self.spawnArmor2 = customtkinter.CTkButton(self, width=80, height=80, text="", image=ICON_ARMOR2, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_armor(2))
        self.spawnArmor2.place(x=1055, y=240)
        self.spawnArmor3 = customtkinter.CTkButton(self, width=80, height=80, text="", image=ICON_ARMOR3, fg_color="transparent", bg_color="transparent", hover=False, command= lambda: spawn_armor(3))
        self.spawnArmor3.place(x=1170, y=240)
        
        # Spawn Vehicles
        self.spawnVehiclesTitle = customtkinter.CTkLabel(self, text="Spawn Vehicles", font=titleFont).place(x=950, y=340)
        self.spawnEmu = customtkinter.CTkButton(self, width=80, height=80, text="", image=ICON_EMU, fg_color="transparent", bg_color="transparent", hover=False, command=spawn_emu)
        self.spawnEmu.place(x=940, y=400)
        self.spawnHamball = customtkinter.CTkButton(self, width=80, height=80, text="", image=ICON_HAMBALL, fg_color="transparent", bg_color="transparent", hover=False, command=spawn_hamball)
        self.spawnHamball.place(x=1055, y=400)
        
# Teleport Menu
class TeleportMenu(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("768x900")
        self.title("Private Game Helper - Teleport Menu")
        self.resizable(False, False)
        
        customtkinter.CTkLabel(self, text="Teleport Menu", font=titleFont).place(x=20, y=20)
        customtkinter.CTkLabel(self, text="- Click on the map to copy the coordinates to your clipboard\n- Type in game chat '/tele [id/all] '\n- Press Ctrl + V to paste the coordinates", font=switchFont, justify="left").place(x=20, y=50)
        
        self.sarmap = customtkinter.CTkLabel(self, width=768, height=768, text="", image=SAR_MAP)
        self.sarmap.place(x=0, y=132)
        self.sarmap.bind("<Button-1>", self.copy_coordinates)
        self.coordinates = customtkinter.CTkLabel(self, text="Coordinates:\n(x, y)", font=switchFont)
        self.coordinates.place(x=600, y=50)
        
    def copy_coordinates(self, event):
        x = event.x * 6
        y = (768 - event.y) * 6
        pyperclip.copy(str(x) + " " + str(y))
        self.coordinates.configure(text="Coordinates:\n(" + str(x) + ", " + str(y) + ")")
        return

# UI elements
generalTitle = customtkinter.CTkLabel(app, text="General Settings", font=titleFont).place(x=20, y=40)
allitemsSwitch = customtkinter.CTkSwitch(app, text="All Items", font=switchFont, variable=allitemsVar, onvalue=1, offvalue=0).place(x=20, y=80)
gunsSwitch = customtkinter.CTkSwitch(app, text="Guns", font=switchFont, variable=gunsVar, onvalue=1, offvalue=0).place(x=20, y=130)
armorsSwitch = customtkinter.CTkSwitch(app, text="Armors", font=switchFont, variable=armorsVar, onvalue=1, offvalue=0).place(x=20, y=180)
throwablesSwitch = customtkinter.CTkSwitch(app, text="Throwables", font=switchFont, variable=throwablesVar, onvalue=1, offvalue=0).place(x=20, y=230)
powerupsSwitch = customtkinter.CTkSwitch(app, text="Powerups", font=switchFont, variable=powerupsVar, onvalue=1, offvalue=0).place(x=20, y=280)
onehitsSwitch = customtkinter.CTkSwitch(app, text="Onehits", font=switchFont, variable=onehitsVar, onvalue=1, offvalue=0).place(x=20, y=330)

emusSwitch = customtkinter.CTkSwitch(app, text="Emus", font=switchFont, variable=emusVar, onvalue=1, offvalue=0).place(x=220, y=80)
hamballsSwitch = customtkinter.CTkSwitch(app, text="Hamballs", font=switchFont, variable=hamballsVar, onvalue=1, offvalue=0).place(x=220, y=130)
molesSwitch = customtkinter.CTkSwitch(app, text="Moles", font=switchFont, variable=molesVar, onvalue=1, offvalue=0).place(x=220, y=180)
petsSwitch = customtkinter.CTkSwitch(app, text="Pets", font=switchFont, variable=petsVar, onvalue=1, offvalue=0).place(x=220, y=230)
gasSwitch = customtkinter.CTkSwitch(app, text="Gas", font=switchFont, variable=gasVar, onvalue=1, offvalue=0).place(x=220, y=280)
norollsSwitch = customtkinter.CTkSwitch(app, text="No Rolls", font=switchFont, variable=norollsVar, onvalue=1, offvalue=0).place(x=220, y=330)

gasspeedSlider = customtkinter.CTkSlider(app, width=160, from_=0.4, to=3.0, number_of_steps=26, variable=gasspeedVar, command=gasspeed_slider).place(x=20, y=400)
gasspeedText = customtkinter.CTkLabel(app, text="Gas Speed:", font=switchFont).place(x=20, y=420)
gasspeedTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
gasspeedTextVal.place(x=150, y=420)

gasdamageSlider = customtkinter.CTkSlider(app, width=160, from_=1.0, to=10.0, number_of_steps=90, variable=gasdamageVar, command=gasdamage_slider).place(x=220, y=400)
gasdamageText = customtkinter.CTkLabel(app, text="Gas Damage:", font=switchFont).place(x=220, y=420)
gasdamageTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
gasdamageTextVal.place(x=350, y=420)

bulletspeedSlider = customtkinter.CTkSlider(app, width=160, from_=0.5, to=2.0, number_of_steps=15, variable=bulletspeedVar, command=bulletspeed_slider).place(x=20, y=480)
bulletspeedText = customtkinter.CTkLabel(app, text="Bullet Speed:", font=switchFont).place(x=20, y=500)
bulletspeedTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
bulletspeedTextVal.place(x=150, y=500)

damageSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=10.0, number_of_steps=100, variable=damageVar, command=damage_slider).place(x=220, y=480)
damageText = customtkinter.CTkLabel(app, text="Damage:", font=switchFont).place(x=220, y=500)
damageTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
damageTextVal.place(x=350, y=500)

spawnratesTitle = customtkinter.CTkLabel(app, text="Spawn Rates", font=titleFont).place(x=420, y=40)
pistolSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=pistolVar, command=partial(weight_slider, "pistol")).place(x=420, y=80)
pistolText = customtkinter.CTkLabel(app, text="Pistol:", font=switchFont).place(x=420, y=100)
pistolTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
pistolTextVal.place(x=550, y=100)

magnumSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=magnumVar, command=partial(weight_slider, "magnum")).place(x=420, y=160)
magnumText = customtkinter.CTkLabel(app, text="Magnum:", font=switchFont).place(x=420, y=180)
magnumTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
magnumTextVal.place(x=550, y=180)

deagleSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=deagleVar, command=partial(weight_slider, "deagle")).place(x=420, y=240)
deagleText = customtkinter.CTkLabel(app, text="Deagle:", font=switchFont).place(x=420, y=260)
deagleTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
deagleTextVal.place(x=550, y=260)

silencedpistolSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=silencedpistolVar, command=partial(weight_slider, "silencedpistol")).place(x=420, y=320)
silencedpistolText = customtkinter.CTkLabel(app, text="Silenced Pistol:", font=switchFont).place(x=420, y=340)
silencedpistolTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
silencedpistolTextVal.place(x=550, y=340)

shotgunSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=shotgunVar, command=partial(weight_slider, "shotgun")).place(x=420, y=400)
shotgunText = customtkinter.CTkLabel(app, text="Shotgun:", font=switchFont).place(x=420, y=420)
shotgunTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
shotgunTextVal.place(x=550, y=420)

jagSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=jagVar, command=partial(weight_slider, "jag")).place(x=420, y=480)
jagText = customtkinter.CTkLabel(app, text="JAG-7:", font=switchFont).place(x=420, y=500)
jagTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
jagTextVal.place(x=550, y=500)

smgSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=smgVar, command=partial(weight_slider, "smg")).place(x=620, y=80)
smgText = customtkinter.CTkLabel(app, text="SMG:", font=switchFont).place(x=620, y=100)
smgTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
smgTextVal.place(x=750, y=100)

tommySlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=tommyVar, command=partial(weight_slider, "tommy")).place(x=620, y=160)
tommyText = customtkinter.CTkLabel(app, text="Tommy Gun:", font=switchFont).place(x=620, y=180)
tommyTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
tommyTextVal.place(x=750, y=180)

akSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=akVar, command=partial(weight_slider, "ak")).place(x=620, y=240)
akText = customtkinter.CTkLabel(app, text="AK:", font=switchFont).place(x=620, y=260)
akTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
akTextVal.place(x=750, y=260)

m16Slider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=m16Var, command=partial(weight_slider, "m16")).place(x=620, y=320)
m16Text = customtkinter.CTkLabel(app, text="M16:", font=switchFont).place(x=620, y=340)
m16TextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
m16TextVal.place(x=750, y=340)

dartSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=dartVar, command=partial(weight_slider, "dart")).place(x=620, y=400)
dartText = customtkinter.CTkLabel(app, text="Dart Gun:", font=switchFont).place(x=620, y=420)
dartTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
dartTextVal.place(x=750, y=420)

dartflySlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=dartflyVar, command=partial(weight_slider, "dartfly")).place(x=620, y=480)
dartflyText = customtkinter.CTkLabel(app, text="Dartfly Gun:", font=switchFont).place(x=620, y=500)
dartflyTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
dartflyTextVal.place(x=750, y=500)

huntingrifleSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=huntingrifleVar, command=partial(weight_slider, "huntingrifle")).place(x=820, y=80)
huntingrifleText = customtkinter.CTkLabel(app, text="Hunting Rifle:", font=switchFont).place(x=820, y=100)
huntingrifleTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
huntingrifleTextVal.place(x=950, y=100)

sniperSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=sniperVar, command=partial(weight_slider, "sniper")).place(x=820, y=160)
sniperText = customtkinter.CTkLabel(app, text="Sniper:", font=switchFont).place(x=820, y=180)
sniperTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
sniperTextVal.place(x=950, y=180)

laserSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=laserVar, command=partial(weight_slider, "laser")).place(x=820, y=240)
laserText = customtkinter.CTkLabel(app, text="Superite Laser:", font=switchFont).place(x=820, y=260)
laserTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
laserTextVal.place(x=950, y=260)

minigunSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=minigunVar, command=partial(weight_slider, "minigun")).place(x=820, y=320)
minigunText = customtkinter.CTkLabel(app, text="Minigun:", font=switchFont).place(x=820, y=340)
minigunTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
minigunTextVal.place(x=950, y=340)

bowSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=bowVar, command=partial(weight_slider, "bow")).place(x=820, y=400)
bowText = customtkinter.CTkLabel(app, text="Bow:", font=switchFont).place(x=820, y=420)
bowTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
bowTextVal.place(x=950, y=420)

sparrowlauncherSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=sparrowlauncherVar, command=partial(weight_slider, "sparrowlauncher")).place(x=820, y=480)
sparrowlauncherText = customtkinter.CTkLabel(app, text="Crossbow:", font=switchFont).place(x=820, y=500)
sparrowlauncherTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
sparrowlauncherTextVal.place(x=950, y=500)

bcgSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=bcgVar, command=partial(weight_slider, "bcg")).place(x=1020, y=80)
bcgText = customtkinter.CTkLabel(app, text="BCG:", font=switchFont).place(x=1020, y=100)
bcgTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
bcgTextVal.place(x=1150, y=100)

grenadefragSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=grenadefragVar, command=partial(weight_slider, "grenadefrag")).place(x=1020, y=160)
grenadefragText = customtkinter.CTkLabel(app, text="Grenade:", font=switchFont).place(x=1020, y=180)
grenadefragTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
grenadefragTextVal.place(x=1150, y=180)

grenadebananaSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=grenadebananaVar, command=partial(weight_slider, "grenadebanana")).place(x=1020, y=240)
grenadebananaText = customtkinter.CTkLabel(app, text="Banana:", font=switchFont).place(x=1020, y=260)
grenadebananaTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
grenadebananaTextVal.place(x=1150, y=260)

grenadeskunkSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=grenadeskunkVar, command=partial(weight_slider, "grenadeskunk")).place(x=1020, y=320)
grenadeskunkText = customtkinter.CTkLabel(app, text="Skunk Bomb:", font=switchFont).place(x=1020, y=340)
grenadeskunkTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
grenadeskunkTextVal.place(x=1150, y=340)

grenademineSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=grenademineVar, command=partial(weight_slider, "grenademine")).place(x=1020, y=400)
grenademineText = customtkinter.CTkLabel(app, text="Cat Mine:", font=switchFont).place(x=1020, y=420)
grenademineTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
grenademineTextVal.place(x=1150, y=420)

grenadezipSlider = customtkinter.CTkSlider(app, width=160, from_=0.0, to=5.0, number_of_steps=50, variable=grenadezipVar, command=partial(weight_slider, "grenadezip")).place(x=1020, y=480)
grenadezipText = customtkinter.CTkLabel(app, text="Zipline:", font=switchFont).place(x=1020, y=500)
grenadezipTextVal = customtkinter.CTkLabel(app, text="1.0", font=switchFont)
grenadezipTextVal.place(x=1150, y=500)

spawningmenuButton = customtkinter.CTkButton(app, text="Spawning Menu", command=open_spawningmenu)
spawningmenuButton.place(x=20, y=550)
teleportmenuButton = customtkinter.CTkButton(app, text="Teleport Menu", command=open_teleportmenu)
teleportmenuButton.place(x=170, y=550)

applysettingsButton = customtkinter.CTkButton(app, text="Apply Settings", command=apply_settings)
applysettingsButton.place(x=740, y=550)
matchidButton = customtkinter.CTkButton(app, text="Match ID", command=match_id)
matchidButton.place(x=890, y=550)
startButton = customtkinter.CTkButton(app, text="Start Match", command=start_match)
startButton.place(x=1040, y=550)
    
# Run app
app.resizable(False, False)
app.mainloop()