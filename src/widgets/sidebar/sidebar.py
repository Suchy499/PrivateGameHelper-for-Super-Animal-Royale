from core.qt_core import *
from .button import Button
from widgets.hline import HLine

class Sidebar(QFrame):
    def __init__(
        self,
        parent: QWidget | None = None
    ):
        super().__init__(parent)
        
        self.setObjectName("Sidebar")
        self.setMinimumSize(160, 540)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 8, 0, 8)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
    def setup_buttons(self, btn_list: list[dict]) -> None:
        self.buttons = {}
        for index, btn in enumerate(btn_list):
            if btn["show_top"]:
                if btn["category"] != btn_list[index-1]["category"] and index > 0:
                    line = HLine(self, h=1)
                    line.setObjectName("SidebarLine")
                    self._layout.addWidget(line)
                button = Button(self, btn["icon"], btn["text"], btn["page"])
                if btn["active"]:
                    button.select()
                self._layout.addWidget(button)
                self.buttons[btn["text"]] = button
        self._layout.addStretch()
        for index, btn in enumerate(btn_list):
            if not btn["show_top"]:
                button = Button(self, btn["icon"], btn["text"], btn["page"])
                if btn["active"]:
                    button.select()
                self._layout.addWidget(button)
                self.buttons[btn["text"]] = button
                try:
                    if btn["category"] != btn_list[index+1]["category"]:
                        line = HLine(self, h=1)
                        line.setObjectName("SidebarLine")
                        self._layout.addWidget(line)
                except IndexError:
                    pass
        
    def deselect_all(self) -> None:
        for btn in self.buttons.values():
            btn.deselect()
    