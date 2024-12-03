from core import *
from widgets import MapComboBox, HLine, LabeledToggle, Button, LabeledSlider

class Settings(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(0, 0, 0, 0)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
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
        
        self.general_label = QLabel(self.content_area, text="General")
        self.general_label.setContentsMargins(0, 0, 0, 15)
        self.general_label.setObjectName("ItemsHeaderName")
        
        self.general_container = QWidget(self.content_area)
        self.general_container_layout = QVBoxLayout(self.general_container)
        self.general_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.general_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.map_selection = MapComboBox(self.general_container, "Map", "dodgeball")
        self.map_selection.addItems([
            "Bamboo Resort",
            "SAW Security",
            "SAW Research Labs",
            "Welcome Center",
            "Penguin Palace",
            "Pyramid",
            "Emu Ranch",
            "Shooting Range",
            "Juice Factory",
            "Super Sea Land"
        ])
        
        self.host_id_label = QLabel(self, text="Host ID")
        self.host_id_label.setObjectName("HostIDLabel")
        self.host_id_label.setContentsMargins(0, 0, 0, 0)
        
        self.host_id_edit = QLineEdit(self)
        self.host_id_edit.setText("1")
        self.host_id_edit.setFixedWidth(210)
        self.host_id_edit.setObjectName("LineEdit")
        self.host_id_edit.setContentsMargins(0, 0, 0, 0)
        self.host_id_edit.setValidator(QRegularExpressionValidator(r"[1-9]|[1-9]\d", self))
        self.host_id_edit.textChanged.connect(self.text_changed)
        
        self.general_container_layout.addWidget(self.map_selection)
        self.general_container_layout.addSpacing(15)
        self.general_container_layout.addWidget(self.host_id_label)
        self.general_container_layout.addWidget(self.host_id_edit)
        
        self.general_hline = HLine(self, h=self.line_height)
        self.general_hline.setObjectName("DivLine")
        
        self.settings_label = QLabel(self, text="Settings")
        self.settings_label.setObjectName("ItemsHeaderName")
        
        self.settings_container = QWidget(self.content_area)
        self.settings_container_layout = QHBoxLayout(self.settings_container)
        self.settings_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.settings_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.random_nades = LabeledToggle(self, text="Random nades", default_state=True)
        self.random_nades.setContentsMargins(0, 15, 0, 0)
        self.random_nades.stateChanged.connect(lambda: global_vars.SIGNAL_MANAGER.dodgeballSettingChanged.emit("random_nades", self.random_nades.isChecked()))
        self.hotkeys = LabeledToggle(self, text="Hotkeys", default_state=True)
        self.hotkeys.setContentsMargins(0, 15, 0, 0)
        self.hotkeys.stateChanged.connect(lambda: global_vars.SIGNAL_MANAGER.dodgeballSettingChanged.emit("hotkeys", self.hotkeys.isChecked()))
        self.damage = LabeledSlider(self, text="Damage")
        self.damage.valueChanged.connect(lambda: global_vars.SIGNAL_MANAGER.dodgeballDamageChanged.emit(self.damage.value()))
        
        self.settings_container_layout.addWidget(self.random_nades)
        self.settings_container_layout.addWidget(self.hotkeys)
        self.settings_container_layout.addWidget(self.damage)
        
        self.settings_hline = HLine(self, h=self.line_height)
        self.settings_hline.setObjectName("DivLine")
        
        self.start_button = Button(self, "Start")
        self.start_button.clicked.connect(start_dodgeball)
        
        self._layout.addWidget(self.general_label)
        self._layout.addWidget(self.general_container)
        self._layout.addSpacing(8)
        self._layout.addWidget(self.general_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.settings_label)
        self._layout.addWidget(self.settings_container)
        self._layout.addSpacing(8)
        self._layout.addWidget(self.settings_hline)
        self._layout.addSpacing(9)
        self._layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignRight)
        
        global_vars.SIGNAL_MANAGER.hostIdChanged.connect(self.host_id_changed)
        global_vars.SIGNAL_MANAGER.dodgeballSettingChanged.connect(self.setting_changed)
        global_vars.SIGNAL_MANAGER.dodgeballDamageChanged.connect(self.damage_changed)
    
    def text_changed(self, text: str) -> None:
        host_id = int(text)
        global_vars.HOST_ID = host_id
        global_vars.SIGNAL_MANAGER.hostIdChanged.emit(host_id)
    
    def host_id_changed(self, host_id: int) -> None:
        self.host_id_edit.setText(str(global_vars.HOST_ID))
    
    def setting_changed(self, setting: str, value: bool) -> None:
        global_vars.DODGEBALL_SETTINGS[setting] = value
        match setting:
            case "random_nades":
                self.random_nades.setChecked(value)
            case "hotkeys":
                self.hotkeys.setChecked(value)
    
    def damage_changed(self, value: float) -> None:
        global_vars.DODGEBALL_SETTINGS["damage"] = value
        self.damage.setValue(value)