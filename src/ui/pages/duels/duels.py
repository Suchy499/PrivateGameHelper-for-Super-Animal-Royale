from core.qt_core import *
from widgets import NavBar
from .settings import Settings
from .teams import Teams
from .weapons import Weapons

class PageDuels(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.page_layout.setSpacing(15)
        self.setObjectName("Content")
        
        self.navbar = NavBar(self)
        self.pages = QStackedWidget(self)
        self.settings_page = Settings(self.pages)
        self.teams_page = Teams(self.pages)
        self.weapons_page = Weapons(self.pages)
        self.pages.addWidget(self.settings_page)
        self.pages.addWidget(self.teams_page)
        self.pages.addWidget(self.weapons_page)
        
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
                "text": "Weapons",
                "page": self.weapons_page,
                "active": False
            },
        ]
        
        self.navbar.setup_buttons(_btn_list)
        self.page_layout.addWidget(self.navbar)
        self.page_layout.addWidget(self.pages)