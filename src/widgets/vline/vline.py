from core.qt_core import *

class VLine(QFrame):
    def __init__(
        self, 
        parent: QWidget | None = None, 
        w: int | None = None, 
        h: int | None = None
    ):
        super().__init__(parent)
        self.w = w
        self.h = h
        self.setFrameShape(QFrame.Shape.VLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        
        if self.w is not None:
            self.setFixedWidth(self.w)
        
        if self.h is not None:
            self.setFixedHeight(self.h)