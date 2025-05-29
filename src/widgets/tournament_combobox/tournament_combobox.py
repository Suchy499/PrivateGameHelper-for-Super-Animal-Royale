from core import *

class TournamentComboBox(QWidget):
    def __init__(
        self,
        parent: QWidget | None = None,
        text: str = "",
        w: int = 210
    ):
        super().__init__(parent)
        
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
        self.combobox.currentTextChanged.connect(glb.SIGNAL_MANAGER.tournamentModeChanged.emit)
        glb.SIGNAL_MANAGER.tournamentModeChanged.connect(self.combobox.setCurrentText)
        
        self.map_combobox_layout.addWidget(self.label)
        self.map_combobox_layout.addWidget(self.combobox)
    
    def addItems(self, texts: list[str]) -> None:
        self.combobox.addItems(texts)
    
    def currentText(self) -> str:
        return self.combobox.currentText()

    def setCurrentText(self, text: str) -> None:
        self.combobox.setCurrentText(text)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return
    
    def showEvent(self, event):
        if self.window().metaObject().className() == "Overlay":
            self.combobox.currentTextChanged.connect(lambda: open_window("Super Animal Royale"))
        return super().showEvent(event)