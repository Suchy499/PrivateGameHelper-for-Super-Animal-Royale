from core import *
from typing import Literal

class MapComboBox(QWidget):
    def __init__(
        self,
        parent: QWidget | None = None,
        text: str = "",
        mode: Literal["duels", "dodgeball"] = "duels",
        w: int = 210
    ):
        super().__init__(parent)
        self.mode = mode
        
        self.setFixedWidth(w)
        self.map_combobox_layout = QVBoxLayout(self)
        self.map_combobox_layout.setContentsMargins(0, 0, 0, 0)
        
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
        self.combobox.currentTextChanged.connect(self.set_map)
        if self.mode == "duels":
            glb.SIGNAL_MANAGER.duelsMapSelected.connect(self.change_map)
        elif self.mode == "dodgeball":
            glb.SIGNAL_MANAGER.dodgeballMapSelected.connect(self.change_map)
        
        self.map_combobox_layout.addWidget(self.label)
        self.map_combobox_layout.addWidget(self.combobox)
    
    def addItems(self, texts: list[str]) -> None:
        self.combobox.addItems(texts)
    
    def currentText(self) -> str:
        return self.combobox.currentText()
    
    def set_map(self, text: str) -> None:
        if self.mode == "duels":
            glb.SIGNAL_MANAGER.duelsMapSelected.emit(text)
        elif self.mode == "dodgeball":
            glb.SIGNAL_MANAGER.dodgeballMapSelected.emit(text)
    
    def change_map(self, text: str) -> None:
        if self.mode == "duels":
            glb.SELECTED_MAP_DUELS = text
        elif self.mode == "dodgeball":
            glb.SELECTED_MAP_DODGEBALL = text
        self.combobox.setCurrentText(text)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return