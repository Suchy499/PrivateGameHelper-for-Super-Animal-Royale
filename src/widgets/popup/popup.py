from core.qt_core import *
from widgets import Button

class Popup(QFrame):
    def __init__(
        self,
        parent: QWidget | None = None,
        title: str = "",
        text: str = "",
        w: int = 300,
        h: int = 150,
        *buttons: Button
    ):
        super().__init__(parent)
        self.title = title
        self.text = text
        self.setFixedSize(w, h)
        self.setObjectName("UpdatePopup")
        self.popup_layout = QGridLayout(self)
        self.popup_layout.setContentsMargins(0, 0, 0, 0)
        self.popup_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.title = QLabel(self.title, self)
        self.title.setObjectName("PlayersHeaderName")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text = QLabel(self.text, self)
        self.text.setObjectName("HostIDLabel")
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.buttons: list[Button] = []
        
        self.popup_layout.addWidget(self.title, 0, 0, 1, len(buttons))
        self.popup_layout.addWidget(self.text, 1, 0, 1, len(buttons))
        
        for index, button in enumerate(buttons):
            button.setParent(self)
            self.popup_layout.addWidget(button, 2, index)
            self.buttons.append(button)