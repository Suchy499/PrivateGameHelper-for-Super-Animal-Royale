from core.qt_core import *
from typing import Literal

class Button(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None,
        btn_text: str = "",
        btn_icon: QIcon | QPixmap | None = None,
        w: int = 100,
        h: int = 30,
        btn_style: Literal["ButtonDefault", "ButtonDelete"] = "ButtonDefault"
    ):
        super().__init__(parent)
        self.w = w
        self.h = h
        self.btn_style = btn_style
        self.btn_icon = btn_icon
        self.btn_text = btn_text
        
        self.setFixedSize(self.w, self.h)
        self.setObjectName(self.btn_style)
        self.setText(self.btn_text)
        if self.btn_icon is not None:
            self.setIcon(self.btn_icon)
            self.setIconSize(self.btn_icon.size())