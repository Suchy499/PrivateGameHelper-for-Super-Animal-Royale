from core.qt_core import *
from widgets import NavBar
from .settings import Settings
from .teams import Teams
from .keybinds import Keybinds

class PageDodgeball(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(9, 9, 9, 22)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._layout.setSpacing(15)
        self.setObjectName("Content")
        
        self.navbar = NavBar(self)
        self.pages = QStackedWidget(self)
        self.settings_page = Settings(self.pages)
        self.teams_page = Teams(self.pages)
        self.keybinds_page = Keybinds(self.pages)
        self.pages.addWidget(self.settings_page)
        self.pages.addWidget(self.teams_page)
        self.pages.addWidget(self.keybinds_page)
        
        _btn_list = [
            {
                "text": "Settings",
                "page": self.settings_page,
                "active": True
            },
            {
                "text": "Teams",
                "page": self.teams_page,
                "active": False
            },
            {
                "text": "Keybinds",
                "page": self.keybinds_page,
                "active": False
            },
        ]
        
        self.navbar.setup_buttons(_btn_list)
        self._layout.addWidget(self.navbar)
        self._layout.addWidget(self.pages)