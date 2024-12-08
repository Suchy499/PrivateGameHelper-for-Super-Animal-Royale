from core import *
from images import IMAGES
from widgets import HLine, Button, Notification

class General(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        
        self.preset_label = QLabel(self, text="Preset")
        self.preset_label.setContentsMargins(0, 0, 0, 15)
        self.preset_label.setObjectName("PregameHeaderName")
        
        self.name_label = QLabel(self, text="Name")
        self.name_label.setObjectName("PresetNameLabel")
        self.name_label.setContentsMargins(9, 0, 0, 0)
        
        self.name_edit = QLineEdit(self)
        self.name_edit.setFixedWidth(221)
        self.name_edit.setObjectName("LineEdit")
        self.name_edit.setContentsMargins(9, 0, 0, 0)
        self.name_edit.textChanged.connect(self.name_edited)
        
        self.preset_buttons = QWidget(self)
        self.preset_buttons_layout = QHBoxLayout(self.preset_buttons)
        self.preset_buttons_layout.setContentsMargins(9, 0, 0, 9)
        self.preset_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.preset_buttons_layout.setSpacing(10)
        
        self.new_icon = QPixmap(IMAGES["save"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.new_button = Button(self.preset_buttons, " New", self.new_icon)
        self.new_button.clicked.connect(save_preset)
        self.preset_buttons_layout.addWidget(self.new_button)
        
        self.edit_icon = QPixmap(IMAGES["pencil"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.edit_button = Button(self.preset_buttons, " Edit", self.edit_icon)
        self.edit_button.clicked.connect(edit_preset)
        self.edit_button.setVisible(False)
        self.preset_buttons_layout.addWidget(self.edit_button)
        
        self.delete_icon = QPixmap(IMAGES["trash"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.delete_button = Button(self.preset_buttons, " Delete", self.delete_icon, btn_style="ButtonDelete")
        self.delete_button.clicked.connect(delete_preset)
        self.delete_button.setVisible(False)
        self.preset_buttons_layout.addWidget(self.delete_button)
        
        self.preset_hline = HLine(self, h=self.line_height)
        self.preset_hline.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.preset_hline.setObjectName("DivLine")
        
        self.control_buttons = QWidget(self)
        self.control_buttons_layout = QHBoxLayout(self.control_buttons)
        self.control_buttons_layout.setContentsMargins(0, 9, 9, 0)
        self.control_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.control_buttons_layout.setSpacing(10)
        
        self.restore_defaults_button = Button(self.control_buttons, "Restore")
        self.restore_defaults_button.clicked.connect(lambda: glb.SIGNAL_MANAGER.presetRestored.emit(glb.PREGAME_DEFAULT_SETTINGS))
        self.control_buttons_layout.addWidget(self.restore_defaults_button)
        
        self.match_id_button = Button(self.control_buttons, "Match ID")
        self.match_id_button.clicked.connect(get_match_id)
        self.control_buttons_layout.addWidget(self.match_id_button)
        
        self.apply_button = Button(self.control_buttons, "Apply")
        self.apply_button.clicked.connect(apply_settings)
        self.control_buttons_layout.addWidget(self.apply_button)
        
        self.start_button = Button(self.control_buttons, "Start")
        self.start_button.clicked.connect(start_game)
        self.control_buttons_layout.addWidget(self.start_button)
        
        self._layout.addWidget(self.preset_label)
        self._layout.addWidget(self.name_label)
        self._layout.addWidget(self.name_edit)
        self._layout.addSpacing(15)
        self._layout.addWidget(self.preset_buttons)
        self._layout.addWidget(self.preset_hline)
        self._layout.addWidget(self.control_buttons)
        
        glb.SIGNAL_MANAGER.presetDeleted.connect(self.delete_settings)
        glb.SIGNAL_MANAGER.presetNameChanged.connect(self.name_changed)
        glb.SIGNAL_MANAGER.presetEdited.connect(self.edit_settings)
        glb.SIGNAL_MANAGER.presetSaved.connect(self.save_settings)
        glb.SIGNAL_MANAGER.presetRestored.connect(self.restore_defaults)
    
    def load_settings(self, settings: dict) -> None:
        self.name_edit.setText(settings["name"])
        self.edit_button.setVisible(True)
        self.delete_button.setVisible(True)
        send_notification("Preset has been loaded!")
    
    def reset_settings(self) -> None:
        glb.PREGAME_SETTINGS["name"] = self.name_edit.text()
    
    def save_settings(self) -> None:
        self.name_edit.setText(glb.PREGAME_SETTINGS["name"])
        self.edit_button.setVisible(True)
        self.delete_button.setVisible(True)
        send_notification("New preset has been saved!", "NotifSuccess")
        
    def edit_settings(self) -> None:
        send_notification("Preset has been edited!", "NotifSuccess")
    
    def delete_settings(self) -> None:
        self.name_edit.setText("")
        self.edit_button.setVisible(False)
        self.delete_button.setVisible(False)
        send_notification("Preset has been deleted", "NotifWarning")
    
    def name_edited(self, new_name: str) -> None:
        glb.PREGAME_SETTINGS["name"] = new_name
        glb.SIGNAL_MANAGER.presetNameChanged.emit(new_name)
    
    def name_changed(self, new_name: str) -> None:
        self.name_edit.setText(new_name)
    
    def restore_defaults(self) -> None:
        send_notification("Settings restored to default")
        