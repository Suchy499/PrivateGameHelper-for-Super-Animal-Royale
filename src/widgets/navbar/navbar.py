from core.qt_core import *
from .button import Button

class NavBar(QWidget):
    def __init__(
        self, 
        parent: QWidget | None = None
    ):
        super().__init__(parent)
        
        self._layout = QHBoxLayout(self)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self.buttons = []
        
    def setup_buttons(self, btn_list: list[dict]) -> None:
        for btn in btn_list:
                button = Button(self, btn["text"], btn["page"])
                if btn["active"]:
                    button.select()
                self._layout.addWidget(button)
                self.buttons.append(button)
        self._layout.addStretch()
        
    def deselect_all(self) -> None:
        for btn in self.buttons:
            btn.deselect()
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return