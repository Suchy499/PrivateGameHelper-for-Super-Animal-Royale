from core import *
from widgets import LabeledSlider

class SpawnRates(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(0, 0, 0, 0)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        _layout.addWidget(self.scroll_area)
        
        self._layout = QVBoxLayout(self.content_area)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        
        self.spawn_rates_label = QLabel(self, text="Spawn Rates")
        self.spawn_rates_label.setContentsMargins(0, 0, 0, 15)
        self.spawn_rates_label.setObjectName("PregameHeaderName")
        self.spawn_rates_settings = QWidget(self)
        self.spawn_rates_settings_layout = QGridLayout(self.spawn_rates_settings)
        self.spawn_rates_settings_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.spawn_rates_settings_layout.setVerticalSpacing(25)
        
        self.pistol_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Pistol", icon="pistol")
        self.pistol_slider.valueChanged.connect(lambda: self.set_setting("gunpistol", self.pistol_slider.value()))
        
        self.magnum_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Magnum", icon="magnum")
        self.magnum_slider.valueChanged.connect(lambda: self.set_setting("gunmagnum", self.magnum_slider.value()))
        
        self.deagle_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Deagle", icon="deagle")
        self.deagle_slider.valueChanged.connect(lambda: self.set_setting("gundeagle", self.deagle_slider.value()))
        
        self.silenced_pistol_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Silenced Pistol", icon="silenced_pistol")
        self.silenced_pistol_slider.valueChanged.connect(lambda: self.set_setting("gunsilencedpistol", self.silenced_pistol_slider.value()))
        
        self.shotgun_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Shotgun", icon="shotgun")
        self.shotgun_slider.valueChanged.connect(lambda: self.set_setting("gunshotgun", self.shotgun_slider.value()))
        
        self.jag7_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "JAG-7", icon="jag7")
        self.jag7_slider.valueChanged.connect(lambda: self.set_setting("gunjag7", self.jag7_slider.value()))
        
        self.smg_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "SMG", icon="smg")
        self.smg_slider.valueChanged.connect(lambda: self.set_setting("gunsmg", self.smg_slider.value()))
        
        self.tommy_gun_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Tommy Gun", icon="tommy_gun")
        self.tommy_gun_slider.valueChanged.connect(lambda: self.set_setting("gunthomas", self.tommy_gun_slider.value()))
        
        self.ak_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "AK", icon="ak")
        self.ak_slider.valueChanged.connect(lambda: self.set_setting("gunak", self.ak_slider.value()))
        
        self.m16_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "M16", icon="m16")
        self.m16_slider.valueChanged.connect(lambda: self.set_setting("gunm16", self.m16_slider.value()))
        
        self.dart_gun_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Dart Gun", icon="dart_gun")
        self.dart_gun_slider.valueChanged.connect(lambda: self.set_setting("gundart", self.dart_gun_slider.value()))
        
        self.dartfly_gun_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Dartfly Gun", icon="dartfly_gun")
        self.dartfly_gun_slider.valueChanged.connect(lambda: self.set_setting("gundartepic", self.dartfly_gun_slider.value()))
        
        self.hunting_rifle_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Hunting Rifle", icon="hunting_rifle")
        self.hunting_rifle_slider.valueChanged.connect(lambda: self.set_setting("gunhuntingrifle", self.hunting_rifle_slider.value()))
        
        self.sniper_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Sniper", icon="sniper")
        self.sniper_slider.valueChanged.connect(lambda: self.set_setting("gunsniper", self.sniper_slider.value()))
        
        self.superite_laser_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Superite Laser", icon="superite_laser")
        self.superite_laser_slider.valueChanged.connect(lambda: self.set_setting("gunlaser", self.superite_laser_slider.value()))
        
        self.minigun_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Minigun", icon="minigun")
        self.minigun_slider.valueChanged.connect(lambda: self.set_setting("gunminigun", self.minigun_slider.value()))
        
        self.bow_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Bow", icon="bow")
        self.bow_slider.valueChanged.connect(lambda: self.set_setting("gunbow", self.bow_slider.value()))
        
        self.sparrow_launcher_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Sparrow Launcher", icon="sparrow_launcher")
        self.sparrow_launcher_slider.valueChanged.connect(lambda: self.set_setting("guncrossbow", self.sparrow_launcher_slider.value()))
        
        self.bcg_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "BCG", icon="bcg")
        self.bcg_slider.valueChanged.connect(lambda: self.set_setting("gunegglauncher", self.bcg_slider.value()))
        
        self.grenade_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Grenade", icon="grenade")
        self.grenade_slider.valueChanged.connect(lambda: self.set_setting("grenadefrag", self.grenade_slider.value()))
        
        self.banana_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Banana", icon="banana")
        self.banana_slider.valueChanged.connect(lambda: self.set_setting("grenadebanana", self.banana_slider.value()))
        
        self.skunk_bomb_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Skunk Bomb", icon="skunk_bomb")
        self.skunk_bomb_slider.valueChanged.connect(lambda: self.set_setting("grenadeskunk", self.skunk_bomb_slider.value()))
        
        self.cat_mine_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Cat Mine", icon="cat_mine")
        self.cat_mine_slider.valueChanged.connect(lambda: self.set_setting("grenadecatmine", self.cat_mine_slider.value()))
        
        self.zipline_slider = LabeledSlider(self, Qt.Orientation.Horizontal, 0, 5, 0.1, 1, "Zipline", icon="zipline")
        self.zipline_slider.valueChanged.connect(lambda: self.set_setting("grenadezipline", self.zipline_slider.value()))
        
        self.spawn_rates_settings_layout.addWidget(self.pistol_slider, 0, 0)
        self.spawn_rates_settings_layout.addWidget(self.magnum_slider, 0, 1)
        self.spawn_rates_settings_layout.addWidget(self.deagle_slider, 0, 2)
        self.spawn_rates_settings_layout.addWidget(self.silenced_pistol_slider, 0, 3)
        self.spawn_rates_settings_layout.addWidget(self.shotgun_slider, 0, 4)
        self.spawn_rates_settings_layout.addWidget(self.jag7_slider, 1, 0)
        self.spawn_rates_settings_layout.addWidget(self.smg_slider, 1, 1)
        self.spawn_rates_settings_layout.addWidget(self.tommy_gun_slider, 1, 2)
        self.spawn_rates_settings_layout.addWidget(self.ak_slider, 1, 3)
        self.spawn_rates_settings_layout.addWidget(self.m16_slider, 1, 4)
        self.spawn_rates_settings_layout.addWidget(self.dart_gun_slider, 2, 0)
        self.spawn_rates_settings_layout.addWidget(self.dartfly_gun_slider, 2, 1)
        self.spawn_rates_settings_layout.addWidget(self.hunting_rifle_slider, 2, 2)
        self.spawn_rates_settings_layout.addWidget(self.sniper_slider, 2, 3)
        self.spawn_rates_settings_layout.addWidget(self.superite_laser_slider, 2, 4)
        self.spawn_rates_settings_layout.addWidget(self.minigun_slider, 3, 0)
        self.spawn_rates_settings_layout.addWidget(self.bow_slider, 3, 1)
        self.spawn_rates_settings_layout.addWidget(self.sparrow_launcher_slider, 3, 2)
        self.spawn_rates_settings_layout.addWidget(self.bcg_slider, 3, 3)
        self.spawn_rates_settings_layout.addWidget(self.grenade_slider, 3, 4)
        self.spawn_rates_settings_layout.addWidget(self.banana_slider, 4, 0)
        self.spawn_rates_settings_layout.addWidget(self.skunk_bomb_slider, 4, 1)
        self.spawn_rates_settings_layout.addWidget(self.cat_mine_slider, 4, 2)
        self.spawn_rates_settings_layout.addWidget(self.zipline_slider, 4, 3)
        
        self._layout.addWidget(self.spawn_rates_label)
        self._layout.addWidget(self.spawn_rates_settings)
        
        glb.SIGNAL_MANAGER.presetSettingChanged.connect(self.setting_changed)
    
    def load_settings(self, settings: dict) -> None:
        self.pistol_slider.setValue(settings["gunpistol"])
        self.magnum_slider.setValue(settings["gunmagnum"])
        self.deagle_slider.setValue(settings["gundeagle"])
        self.silenced_pistol_slider.setValue(settings["gunsilencedpistol"])
        self.shotgun_slider.setValue(settings["gunshotgun"])
        self.jag7_slider.setValue(settings["gunjag7"])
        self.smg_slider.setValue(settings["gunsmg"])
        self.tommy_gun_slider.setValue(settings["gunthomas"])
        self.ak_slider.setValue(settings["gunak"])
        self.m16_slider.setValue(settings["gunm16"])
        self.dart_gun_slider.setValue(settings["gundart"])
        self.dartfly_gun_slider.setValue(settings["gundartepic"])
        self.hunting_rifle_slider.setValue(settings["gunhuntingrifle"])
        self.sniper_slider.setValue(settings["gunsniper"])
        self.superite_laser_slider.setValue(settings["gunlaser"])
        self.minigun_slider.setValue(settings["gunminigun"])
        self.bow_slider.setValue(settings["gunbow"])
        self.sparrow_launcher_slider.setValue(settings["guncrossbow"])
        self.bcg_slider.setValue(settings["gunegglauncher"])
        self.grenade_slider.setValue(settings["grenadefrag"])
        self.banana_slider.setValue(settings["grenadebanana"])
        self.skunk_bomb_slider.setValue(settings["grenadeskunk"])
        self.cat_mine_slider.setValue(settings["grenadecatmine"])
        self.zipline_slider.setValue(settings["grenadezipline"])
    
    def set_setting(self, setting: str, value: bool | int | float) -> None:
        glb.PREGAME_SETTINGS["settings"]["gun_weights"][setting] = value
        glb.SIGNAL_MANAGER.presetSettingChanged.emit()
    
    def setting_changed(self) -> None:
        self.pistol_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunpistol"])
        self.magnum_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunmagnum"])
        self.deagle_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gundeagle"])
        self.silenced_pistol_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunsilencedpistol"])
        self.shotgun_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunshotgun"])
        self.jag7_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunjag7"])
        self.smg_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunsmg"])
        self.tommy_gun_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunthomas"])
        self.ak_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunak"])
        self.m16_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunm16"])
        self.dart_gun_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gundart"])
        self.dartfly_gun_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gundartepic"])
        self.hunting_rifle_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunhuntingrifle"])
        self.sniper_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunsniper"])
        self.superite_laser_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunlaser"])
        self.minigun_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunminigun"])
        self.bow_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunbow"])
        self.sparrow_launcher_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["guncrossbow"])
        self.bcg_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["gunegglauncher"])
        self.grenade_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["grenadefrag"])
        self.banana_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["grenadebanana"])
        self.skunk_bomb_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["grenadeskunk"])
        self.cat_mine_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["grenadecatmine"])
        self.zipline_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gun_weights"]["grenadezipline"])