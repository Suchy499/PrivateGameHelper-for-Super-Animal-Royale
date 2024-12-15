from core import *
from images import IMAGES

class PageHome(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QHBoxLayout(self)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_layout.setContentsMargins(9, 9, 9, 9)
        self.page_layout.setSpacing(10)
        
        self.logo_pixmap = QPixmap(IMAGES["logo"])
        self.logo_pixmap_initial = self.logo_pixmap.scaledToWidth(400, Qt.TransformationMode.SmoothTransformation)
        self.logo = QLabel(self)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo.setPixmap(self.logo_pixmap_initial)
        
        self.page_layout.addWidget(self.logo)
        
    def scaledPixmap(self) -> QPixmap:
        scaled = self.logo_pixmap.scaled(
            self.width() - self.width() / 6,
            self.height() - self.height() / 6,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        return scaled
    
    def resizeEvent(self, event) -> None:
        self.logo.setPixmap(self.scaledPixmap())