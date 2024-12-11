from core import *
from images import IMAGES

class PageHome(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QHBoxLayout(self)
        _layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.setContentsMargins(9, 9, 9, 9)
        _layout.setSpacing(10)
        
        self.logo_pixmap = QPixmap(IMAGES["logo"]).scaledToHeight(400, Qt.TransformationMode.SmoothTransformation)
        self.logo = QLabel(self)
        self.logo.setPixmap(self.logo_pixmap)
        
        _layout.addWidget(self.logo)
        