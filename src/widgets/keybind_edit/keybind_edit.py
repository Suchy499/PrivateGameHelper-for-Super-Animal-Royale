from core import *
from win32api import MapVirtualKey

class KeybindEdit(QLineEdit):
    def __init__(
        self,
        parent: QWidget | None = None,
        setting_key: str = "",
        default_value: str = "",
        width: int = 210,
    ):
        super().__init__(parent)
        self.setObjectName("LineEdit")
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedWidth(width)
        self.setting_key = setting_key
        self.default_value = default_value
        self.setText(global_vars.SETTINGS.value(f"Keybinds/{self.setting_key}", self.default_value))
        
        self.textChanged.connect(self.save_text)

    def keyPressEvent(self, event) -> None:
        keyname = ''
        key_vk = event.nativeVirtualKey()
        key = MapVirtualKey(key_vk, 2)
        modifiers: Qt.KeyboardModifier = event.modifiers()
        if key == 13:
            self.clearFocus()
        
        elif (
            key > 0 and
            modifiers == Qt.KeyboardModifier.KeypadModifier
        ):
            keyname = QKeySequence(key).toString()
            self.setText(keyname)
            
        elif (key > 0):
            keyname = QKeySequence(modifiers.value | key).toString()
            self.setText(keyname)
        
        elif (
            key == 0 and
            modifiers != Qt.KeyboardModifier.KeypadModifier
        ):
            
            keyname = QKeySequence(modifiers.value).toString()[:-1]
            self.setText(keyname)
        
    def save_text(self, text: str) -> None:
        if text == "" or 0 <= ord(text[0]) <= 31:
            self.setText(global_vars.SETTINGS.value(f"Keybinds/{self.setting_key}", self.default_value))
            return
    
        global_vars.SETTINGS.setValue(f"Keybinds/{self.setting_key}", text)
        global_vars.SETTINGS.sync()
        update_hotkeys()