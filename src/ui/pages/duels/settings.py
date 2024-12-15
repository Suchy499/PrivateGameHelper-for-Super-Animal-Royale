from core import *
from widgets import MapComboBox, HLine, LabeledToggle, Button

class Settings(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0, 0, 0, 0)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        self.page_layout.addWidget(self.scroll_area)
        
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(0, 0, 9, 0)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        
        self.general_label = QLabel(self.content_area, text="General")
        self.general_label.setContentsMargins(0, 0, 0, 15)
        self.general_label.setObjectName("ItemsHeaderName")
        
        self.general_container = QWidget(self.content_area)
        self.general_container_layout = QVBoxLayout(self.general_container)
        self.general_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.general_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.map_selection = MapComboBox(self.general_container, "Map", "duels")
        self.map_selection.addItems(["Bamboo Resort", "SAW Security", "SAW Research Labs", "Welcome Center", "Penguin Palace"])
        
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
        
        self.items_label = QLabel(self, text="Items")
        self.items_label.setContentsMargins(0, 0, 0, 15)
        self.items_label.setObjectName("ItemsHeaderName")
        
        self.items_container = QWidget(self.content_area)
        self.items_container_layout = QHBoxLayout(self.items_container)
        self.items_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.items_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.weapons_toggle = LabeledToggle(self, text="Weapons", default_state=True)
        self.weapons_toggle.stateChanged.connect(lambda: glb.SIGNAL_MANAGER.duelsSettingChanged.emit("weapons", self.weapons_toggle.isChecked()))
        self.armor_toggle = LabeledToggle(self, text="Armor", default_state=True)
        self.armor_toggle.stateChanged.connect(lambda: glb.SIGNAL_MANAGER.duelsSettingChanged.emit("armor", self.armor_toggle.isChecked()))
        self.powerups_toggle = LabeledToggle(self, text="Powerups", default_state=True)
        self.powerups_toggle.stateChanged.connect(lambda: glb.SIGNAL_MANAGER.duelsSettingChanged.emit("powerups", self.powerups_toggle.isChecked()))
        self.throwables_toggle = LabeledToggle(self, text="Throwables", default_state=True)
        self.throwables_toggle.stateChanged.connect(lambda: glb.SIGNAL_MANAGER.duelsSettingChanged.emit("throwables", self.throwables_toggle.isChecked()))
        
        self.items_container_layout.addWidget(self.weapons_toggle)
        self.items_container_layout.addWidget(self.armor_toggle)
        self.items_container_layout.addWidget(self.powerups_toggle)
        self.items_container_layout.addWidget(self.throwables_toggle)
        
        self.items_hline = HLine(self, h=self.line_height)
        self.items_hline.setObjectName("DivLine")
        
        self.misc_label = QLabel(self, text="Miscellaneous")
        self.misc_label.setContentsMargins(0, 0, 0, 15)
        self.misc_label.setObjectName("ItemsHeaderName")
        
        self.misc_container = QWidget(self.content_area)
        self.misc_container_layout = QHBoxLayout(self.misc_container)
        self.misc_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.misc_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.no_pets_toggle = LabeledToggle(self, text="No pets")
        self.no_pets_toggle.stateChanged.connect(lambda: glb.SIGNAL_MANAGER.duelsSettingChanged.emit("no_pets", self.no_pets_toggle.isChecked()))
        self.ohk_toggle = LabeledToggle(self, text="One hit kills")
        self.ohk_toggle.stateChanged.connect(lambda: glb.SIGNAL_MANAGER.duelsSettingChanged.emit("onehits", self.ohk_toggle.isChecked()))
        self.no_jumprolls_toggle = LabeledToggle(self, text="No jumprolls")
        self.no_jumprolls_toggle.stateChanged.connect(lambda: glb.SIGNAL_MANAGER.duelsSettingChanged.emit("noroll", self.no_jumprolls_toggle.isChecked()))
        self.boundaries_toggle = LabeledToggle(self, text="Banan boundaries")
        self.boundaries_toggle.stateChanged.connect(lambda: glb.SIGNAL_MANAGER.duelsSettingChanged.emit("boundaries", self.boundaries_toggle.isChecked()))
        
        self.misc_container_layout.addWidget(self.no_pets_toggle)
        self.misc_container_layout.addWidget(self.ohk_toggle)
        self.misc_container_layout.addWidget(self.no_jumprolls_toggle)
        self.misc_container_layout.addWidget(self.boundaries_toggle)
        
        self.misc_hline = HLine(self, h=self.line_height)
        self.misc_hline.setObjectName("DivLine")
        
        self.start_button = Button(self, "Start")
        self.start_button.clicked.connect(start_duel)
        
        self.content_layout.addWidget(self.general_label)
        self.content_layout.addWidget(self.general_container)
        self.content_layout.addSpacing(8)
        self.content_layout.addWidget(self.general_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.items_label)
        self.content_layout.addWidget(self.items_container)
        self.content_layout.addSpacing(8)
        self.content_layout.addWidget(self.items_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.misc_label)
        self.content_layout.addWidget(self.misc_container)
        self.content_layout.addSpacing(8)
        self.content_layout.addWidget(self.misc_hline)
        self.content_layout.addSpacing(9)
        self.content_layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignRight)
        
        glb.SIGNAL_MANAGER.hostIdChanged.connect(self.host_id_changed)
        glb.SIGNAL_MANAGER.duelsSettingChanged.connect(self.setting_changed)
    
    def text_changed(self, text: str) -> None:
        host_id = int(text)
        glb.HOST_ID = host_id
        glb.SIGNAL_MANAGER.hostIdChanged.emit(host_id)
    
    def host_id_changed(self, host_id: int) -> None:
        self.host_id_edit.setText(str(glb.HOST_ID))
    
    def setting_changed(self, setting: str, value: bool) -> None:
        glb.DUELS_SETTINGS[setting] = value
        match setting:
            case "weapons":
                self.weapons_toggle.setChecked(value)
            case "armor":
                self.armor_toggle.setChecked(value)
            case "throwables":
                self.throwables_toggle.setChecked(value)
            case "powerups":
                self.powerups_toggle.setChecked(value)
            case "no_pets":
                self.no_pets_toggle.setChecked(value)
            case "onehits":
                self.ohk_toggle.setChecked(value)
            case "noroll":
                self.no_jumprolls_toggle.setChecked(value)
            case "boundaries":
                self.boundaries_toggle.setChecked(value)