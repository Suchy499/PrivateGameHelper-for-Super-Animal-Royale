from core import *

class ClickableLabel(QLabel):
    clicked = Signal()
    
    def __init__(
        self, 
        parent: QWidget | None = None,
        text: str = ""
    ):
        super().__init__(parent=parent, text=text)
        self.setContentsMargins(9, 9, 9, 9)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    
    def mousePressEvent(self, ev):
        if self.window().metaObject().className() == "Overlay":
            open_window("Super Animal Royale")
        self.clicked.emit()
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return