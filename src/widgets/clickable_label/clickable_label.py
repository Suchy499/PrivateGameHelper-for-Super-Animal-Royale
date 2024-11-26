from core.qt_core import *

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
        self.clicked.emit()