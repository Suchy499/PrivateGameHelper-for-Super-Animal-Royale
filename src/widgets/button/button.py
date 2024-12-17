from core import *
from typing import Literal

class Button(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None,
        btn_text: str = "",
        btn_icon: QIcon | QPixmap | None = None,
        w: int = 100,
        h: int = 30,
        btn_style: Literal["ButtonDefault", "ButtonDelete"] = "ButtonDefault",
        command: str | None = None
    ):
        super().__init__(parent)
        self.w = w
        self.h = h
        self.btn_style = btn_style
        self.btn_icon = btn_icon
        self.btn_text = btn_text
        self.command = command
        
        self.setFixedSize(self.w, self.h)
        self.setObjectName("Button")
        self.setProperty("style", btn_style)
        self.setText(self.btn_text)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if self.btn_icon is not None:
            self.setIcon(self.btn_icon)
            self.setIconSize(self.btn_icon.size())

        if self.command is not None:
            self.clicked.connect(lambda: send_other_command(self.command))
            
        if self.window().metaObject().className() == "Overlay":
            self.clicked.connect(lambda: open_window("Super Animal Royale"))
            
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return