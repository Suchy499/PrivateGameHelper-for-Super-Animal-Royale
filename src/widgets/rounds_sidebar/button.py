from core import *
from styles import Style
from typing import Literal

class Button(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None, 
        icon: str | None = None,
        text: str = "",
        page: QWidget | None = None,
        orientation: Qt.Orientation = Qt.Orientation.Vertical
    ):
        super().__init__(parent)
        self.icon = icon
        self.text = text
        self.page = page
        
        self.setObjectName("RoundsButton")
        if orientation == Qt.Orientation.Vertical:
            self.setFixedHeight(30)
            self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        else:
            self.setFixedWidth(39)
            self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
            
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if self.icon:
            self.icon_pixmap = QPixmap(self.icon).scaledToWidth(13, Qt.TransformationMode.SmoothTransformation)
            self.setIcon(self.icon_pixmap)
            self.setIconSize(self.icon_pixmap.size())
        if self.text != "":
            self.setText(self.text)
        if self.text != "" and self.icon:
            self.setText(f"    {self.text}")
    
    def select(self) -> None:
        self.setProperty("selected", "True")
        self.setStyleSheet(self.styleSheet())
        
    def deselect(self) -> None:
        self.setProperty("selected", "False")
        self.setStyleSheet(self.styleSheet())
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return