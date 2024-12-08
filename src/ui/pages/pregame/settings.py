from core import *
from widgets import LabeledToggle, HLine, LabeledSlider

class Settings(QWidget):
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
        self._layout.setContentsMargins(0, 0, 9, 0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        
        self.ground_loot_label = QLabel(self, text="Ground Loot")
        self.ground_loot_label.setContentsMargins(0, 0, 0, 15)
        self.ground_loot_label.setObjectName("PregameHeaderName")
        
        self.ground_loot_settings = QWidget(self)
        self.ground_loot_layout = QHBoxLayout(self.ground_loot_settings)
        self.ground_loot_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.all_items_toggle = LabeledToggle(self.ground_loot_settings, text="All Items", default_state=True)
        self.all_items_toggle.stateChanged.connect(lambda: self.set_setting("allitems", self.all_items_toggle.isChecked()))
        
        self.guns_toggle = LabeledToggle(self.ground_loot_settings, text="Guns", default_state=True)
        self.guns_toggle.stateChanged.connect(lambda: self.set_setting("guns", self.guns_toggle.isChecked()))
        
        self.armor_toggle = LabeledToggle(self.ground_loot_settings, text="Armor", default_state=True)
        self.armor_toggle.stateChanged.connect(lambda: self.set_setting("armors", self.armor_toggle.isChecked()))
        
        self.throwables_toggle = LabeledToggle(self.ground_loot_settings, text="Throwables", default_state=True)
        self.throwables_toggle.stateChanged.connect(lambda: self.set_setting("throwables", self.throwables_toggle.isChecked()))
        
        self.powerups_toggle = LabeledToggle(self.ground_loot_settings, text="Powerups", default_state=True)
        self.powerups_toggle.stateChanged.connect(lambda: self.set_setting("powerups", self.powerups_toggle.isChecked()))
        
        self.ground_loot_layout.addWidget(self.all_items_toggle)
        self.ground_loot_layout.addWidget(self.guns_toggle)
        self.ground_loot_layout.addWidget(self.armor_toggle)
        self.ground_loot_layout.addWidget(self.throwables_toggle)
        self.ground_loot_layout.addWidget(self.powerups_toggle)
        
        self.ground_loot_hline = HLine(self, h=self.line_height)
        self.ground_loot_hline.setObjectName("DivLine")
        
        self.vehicles_label = QLabel(self, text="Vehicles")
        self.vehicles_label.setContentsMargins(0, 0, 0, 15)
        self.vehicles_label.setObjectName("PregameHeaderName")
        
        self.vehicles_settings = QWidget(self)
        self.vehicles_settings_layout = QHBoxLayout(self.vehicles_settings)
        self.vehicles_settings_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.emus_toggle = LabeledToggle(self.vehicles_settings, text="Emus", default_state=True)
        self.emus_toggle.stateChanged.connect(lambda: self.set_setting("emus", self.emus_toggle.isChecked()))
        
        self.hamballs_toggle = LabeledToggle(self.vehicles_settings, text="Hamballs", default_state=True)
        self.hamballs_toggle.stateChanged.connect(lambda: self.set_setting("hamballs", self.hamballs_toggle.isChecked()))
        
        self.ziplines_toggle = LabeledToggle(self.vehicles_settings, text="Ziplines", default_state=True)
        self.ziplines_toggle.stateChanged.connect(lambda: self.set_setting("ziplines", self.ziplines_toggle.isChecked()))
        
        self.vehicles_settings_layout.addWidget(self.emus_toggle)
        self.vehicles_settings_layout.addWidget(self.hamballs_toggle)
        self.vehicles_settings_layout.addWidget(self.ziplines_toggle)
        
        self.vehicles_hline = HLine(self, h=self.line_height)
        self.vehicles_hline.setObjectName("DivLine")
        
        self.gas_label = QLabel(self, text="Gas")
        self.gas_label.setObjectName("PregameHeaderName")
        
        self.gas_settings = QWidget(self)
        self.gas_settings_layout = QHBoxLayout(self.gas_settings)
        self.gas_settings_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.gas_toggle = LabeledToggle(self.gas_settings, text="Gas", default_state=True)
        self.gas_toggle.setContentsMargins(0, 15, 0, 0)
        self.gas_toggle.stateChanged.connect(lambda: self.set_setting("gasoff", self.gas_toggle.isChecked()))
        
        self.gas_speed_slider = LabeledSlider(self.gas_settings, Qt.Orientation.Horizontal, 0.4, 3.0, 0.1, 1, "Gas Speed")
        self.gas_speed_slider.valueChanged.connect(lambda: self.set_setting("gasspeed", self.gas_speed_slider.value()))
        
        self.gas_damage_slider = LabeledSlider(self.gas_settings, Qt.Orientation.Horizontal, 1.0, 10.0, 0.1, 1, "Gas Damage")
        self.gas_damage_slider.valueChanged.connect(lambda: self.set_setting("gasdmg", self.gas_damage_slider.value()))
        
        self.gas_settings_layout.addWidget(self.gas_toggle)
        self.gas_settings_layout.addWidget(self.gas_speed_slider)
        self.gas_settings_layout.addWidget(self.gas_damage_slider)
        
        self.gas_hline = HLine(self, h=self.line_height)
        self.gas_hline.setObjectName("DivLine")
        
        self.combat_label = QLabel(self, text="Combat")
        self.combat_label.setContentsMargins(0, 0, 0, 15)
        self.combat_label.setObjectName("PregameHeaderName")
        
        self.combat_settings = QWidget(self)
        self.combat_settings_layout = QHBoxLayout(self.combat_settings)
        self.combat_settings_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.damage_slider = LabeledSlider(self.combat_settings, Qt.Orientation.Horizontal, 0.0, 10.0, 0.1, 1, "Damage")
        self.damage_slider.valueChanged.connect(lambda: self.set_setting("dmg", self.damage_slider.value()))
        
        self.bullet_speed_slider = LabeledSlider(self.combat_settings, Qt.Orientation.Horizontal, 0.5, 2.0, 0.1, 1, "Bullet Speed")
        self.bullet_speed_slider.valueChanged.connect(lambda: self.set_setting("bulletspeed", self.bullet_speed_slider.value()))
        
        self.hpm_slider = LabeledSlider(self.combat_settings, Qt.Orientation.Horizontal, 25, 300, 25, 250, "HPM", "int")
        self.hpm_slider.valueChanged.connect(lambda: self.set_setting("highping", self.hpm_slider.value()))
        
        self.combat_settings_layout.addWidget(self.damage_slider)
        self.combat_settings_layout.addWidget(self.bullet_speed_slider)
        self.combat_settings_layout.addWidget(self.hpm_slider)
        
        self.combat_hline = HLine(self, h=self.line_height)
        self.combat_hline.setObjectName("DivLine")
        
        self.misc_label = QLabel(self, text="Miscellaneous")
        self.misc_label.setContentsMargins(0, 0, 0, 15)
        self.misc_label.setObjectName("PregameHeaderName")
        
        self.misc_settings = QWidget(self)
        self.misc_settings_layout = QHBoxLayout(self.misc_settings)
        self.misc_settings_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.moles_toggle = LabeledToggle(self.misc_settings, text="Moles", default_state=True)
        self.moles_toggle.stateChanged.connect(lambda: self.set_setting("moles", self.moles_toggle.isChecked()))
        
        self.pets_toggle = LabeledToggle(self.misc_settings, text="Pets", default_state=True)
        self.pets_toggle.stateChanged.connect(lambda: self.set_setting("pets", self.pets_toggle.isChecked()))
        
        self.onehits_toggle = LabeledToggle(self.misc_settings, text="Onehits")
        self.onehits_toggle.stateChanged.connect(lambda: self.set_setting("onehits", self.onehits_toggle.isChecked()))
        
        self.no_rolls_toggle = LabeledToggle(self.misc_settings, text="No Rolls")
        self.no_rolls_toggle.stateChanged.connect(lambda: self.set_setting("noroll", self.no_rolls_toggle.isChecked()))
        
        self.bots_toggle = LabeledToggle(self.misc_settings, text="Bots")
        self.bots_toggle.stateChanged.connect(lambda: self.set_setting("bots", self.bots_toggle.isChecked()))
        
        self.misc_settings_layout.addWidget(self.moles_toggle)
        self.misc_settings_layout.addWidget(self.pets_toggle)
        self.misc_settings_layout.addWidget(self.onehits_toggle)
        self.misc_settings_layout.addWidget(self.no_rolls_toggle)
        self.misc_settings_layout.addWidget(self.bots_toggle)
        
        self._layout.addWidget(self.ground_loot_label)
        self._layout.addWidget(self.ground_loot_settings)
        self._layout.addWidget(self.ground_loot_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.vehicles_label)
        self._layout.addWidget(self.vehicles_settings)
        self._layout.addWidget(self.vehicles_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.gas_label)
        self._layout.addWidget(self.gas_settings)
        self._layout.addWidget(self.gas_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.combat_label)
        self._layout.addWidget(self.combat_settings)
        self._layout.addWidget(self.combat_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.misc_label)
        self._layout.addWidget(self.misc_settings)
        
        glb.SIGNAL_MANAGER.presetSettingChanged.connect(self.setting_changed)
    
    def load_settings(self, settings: dict) -> None:
        self.all_items_toggle.setChecked(settings["allitems"])
        self.guns_toggle.setChecked(settings["guns"])
        self.armor_toggle.setChecked(settings["armors"])
        self.throwables_toggle.setChecked(settings["throwables"])
        self.powerups_toggle.setChecked(settings["powerups"])
        self.emus_toggle.setChecked(settings["emus"])
        self.hamballs_toggle.setChecked(settings["hamballs"])
        self.ziplines_toggle.setChecked(settings["ziplines"])
        self.gas_toggle.setChecked(settings["gasoff"])
        self.moles_toggle.setChecked(settings["moles"])
        self.pets_toggle.setChecked(settings["pets"])
        self.onehits_toggle.setChecked(settings["onehits"])
        self.no_rolls_toggle.setChecked(settings["noroll"])
        self.bots_toggle.setChecked(settings["bots"])
        self.gas_speed_slider.setValue(settings["gasspeed"])
        self.gas_damage_slider.setValue(settings["gasdmg"])
        self.damage_slider.setValue(settings["dmg"])
        self.bullet_speed_slider.setValue(settings["bulletspeed"])
        self.hpm_slider.setValue(settings["highping"])
    
    def set_setting(self, setting: str, value: bool | int | float) -> None:
        glb.PREGAME_SETTINGS["settings"][setting] = value
        glb.SIGNAL_MANAGER.presetSettingChanged.emit()
    
    def setting_changed(self) -> None:
        self.all_items_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["allitems"])
        self.guns_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["guns"])
        self.armor_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["armors"])
        self.throwables_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["throwables"])
        self.powerups_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["powerups"])
        self.emus_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["emus"])
        self.hamballs_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["hamballs"])
        self.ziplines_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["ziplines"])
        self.gas_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["gasoff"])
        self.moles_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["moles"])
        self.pets_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["pets"])
        self.onehits_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["onehits"])
        self.no_rolls_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["noroll"])
        self.bots_toggle.setChecked(glb.PREGAME_SETTINGS["settings"]["bots"])
        self.gas_speed_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gasspeed"])
        self.gas_damage_slider.setValue(glb.PREGAME_SETTINGS["settings"]["gasdmg"])
        self.damage_slider.setValue(glb.PREGAME_SETTINGS["settings"]["dmg"])
        self.bullet_speed_slider.setValue(glb.PREGAME_SETTINGS["settings"]["bulletspeed"])
        self.hpm_slider.setValue(glb.PREGAME_SETTINGS["settings"]["highping"])
    