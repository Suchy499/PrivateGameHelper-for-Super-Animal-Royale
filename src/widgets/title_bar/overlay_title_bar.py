from core.qt_core import *
from images import IMAGES

class OverlayTitleBar(QFrame):
    def __init__(
        self, 
        parent: QWidget | None = None
    ):
        super().__init__(parent)
        
        self.setFixedHeight(32)
        self.setObjectName("OverlayTitleBar")
        
        self.titlebar_layout = QHBoxLayout(self)
        self.titlebar_layout.setContentsMargins(20, 0, 9, 0)
        self.titlebar_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        self.title = QLabel(self, text=self.window().windowTitle())
        self.title.setObjectName("Title")
        self.close_button = QToolButton(self)
        self.close_button.setObjectName("TitleButtonClose")
        self.close_pixmap = QPixmap(IMAGES["close"]).scaledToHeight(24, Qt.TransformationMode.SmoothTransformation)
        self.close_button.setIcon(self.close_pixmap)
        self.close_button.setFixedSize(self.close_pixmap.size())
        self.titlebar_layout.addWidget(self.title)
        self.titlebar_layout.addStretch()
        self.titlebar_layout.addWidget(self.close_button)
        
        self.setText = self.title.setText
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return