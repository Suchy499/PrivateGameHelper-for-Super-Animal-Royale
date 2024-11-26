from core.qt_core import *
from images import IMAGES

class PageHome(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.setContentsMargins(9, 9, 9, 9)
        
        self.icon = QPixmap(IMAGES["icon"])
        self.icon_label = QLabel(self)
        self.icon_label.setPixmap(self.icon)
        self.icon_label.setMinimumSize(self.icon.size())
        self.icon_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label = QLabel(self, text="Private Game Helper")
        self.name_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.setObjectName("NameLabel")
        
        _layout.addWidget(self.icon_label)
        _layout.addWidget(self.name_label)