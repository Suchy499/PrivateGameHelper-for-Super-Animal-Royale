from core import *
from widgets import Logo

class PageHome(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QHBoxLayout(self)
        _layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _layout.setContentsMargins(9, 9, 9, 9)
        _layout.setSpacing(10)
        
        self.logo = Logo(self)
        
        _layout.addWidget(self.logo)
        