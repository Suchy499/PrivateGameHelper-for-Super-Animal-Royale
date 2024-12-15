from core.qt_core import *
from .button import Button

class NavBar(QWidget):
    def __init__(
        self, 
        parent: QWidget | None = None
    ):
        super().__init__(parent)
        
        self.navbar_layout = QHBoxLayout(self)
        self.navbar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.navbar_layout.setContentsMargins(0, 0, 0, 0)
        self.navbar_layout.setSpacing(0)
        self.buttons = []
        
    def setup_buttons(self, btn_list: list[dict]) -> None:
        for btn in btn_list:
                button = Button(self, btn["text"], btn["page"])
                if btn["active"]:
                    button.select()
                self.navbar_layout.addWidget(button)
                self.buttons.append(button)
        self.navbar_layout.addStretch()
        
    def deselect_all(self) -> None:
        for btn in self.buttons:
            btn.deselect()
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return