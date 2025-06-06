from core import *
from typing import Literal

class SettingsComboBox(QWidget):
    def __init__(
        self,
        parent: QWidget | None = None,
        text: str = "",
        setting: Literal["DisplayMode", "OverlayPosition"] | None = None,
        w: int = 210
    ):
        super().__init__(parent)
        self.setting = setting
        
        self.setFixedWidth(w)
        self.settings_combobox_layout = QVBoxLayout(self)
        self.settings_combobox_layout.setContentsMargins(0, 0, 0, 0)
        
        self.label = QLabel(text, self)
        self.label.setObjectName("ComboBoxLabel")
        
        self.combobox = QComboBox(self)
        self.combobox.setFixedHeight(24)
        self.combobox.setObjectName("MapSelection")
        self.combobox.view().setObjectName("MapSelectionView")
        self.combobox.view().window().setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint)
        self.combobox.view().window().setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.combobox.setStyleSheet(f"""
            #MapSelection::down-arrow {{
                image: url(:/images/down_arrow.png);
                width: 10px;
            }}
            #MapSelection::drop-down {{
                padding-right: 10px;
                border: none;
            }}
        """)
        if self.setting:
            match self.setting:
                case "DisplayMode":
                    self.combobox.addItems(["App + Overlay", "App only", "Overlay only"])
                case "OverlayPosition":
                    self.combobox.addItems(["Right", "Left", "Bottom", "Top"])
            self.change_setting()
            self.combobox.currentIndexChanged.connect(self.setting_selected)
            glb.SIGNAL_MANAGER.settingChanged.connect(self.change_setting)
        
        self.settings_combobox_layout.addWidget(self.label)
        self.settings_combobox_layout.addWidget(self.combobox)
    
    def addItems(self, texts: list[str]) -> None:
        self.combobox.addItems(texts)
    
    def currentText(self) -> str:
        return self.combobox.currentText()
    
    def setting_selected(self, index: int) -> None:
        match self.setting:
            case "DisplayMode":
                glb.SETTINGS.setValue("DisplayMode", index)
            case "OverlayPosition":
                glb.SETTINGS.setValue("OverlayPosition", index)
        glb.SIGNAL_MANAGER.settingChanged.emit()
    
    def change_setting(self) -> None:
        if self.setting == "DisplayMode":
            self.combobox.setCurrentIndex(glb.SETTINGS.value("DisplayMode", 0))
        elif self.setting == "OverlayPosition":
            self.combobox.setCurrentIndex(glb.SETTINGS.value("OverlayPosition", 0))
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return
    
    def showEvent(self, event):
        if self.window().metaObject().className() == "Overlay":
            self.combobox.currentIndexChanged.connect(lambda: open_window("Super Animal Royale"))
        return super().showEvent(event)