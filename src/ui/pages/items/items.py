from core.qt_core import *
from .weapons import Weapons
from .consumables import Consumables
from .equipables import Equipables
from .vehicles import Vehicles
from widgets import NavBar

class PageItems(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(9, 9, 9, 22)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._layout.setSpacing(15)
        self.setObjectName("Content")
        
        self.navbar = NavBar(self)
        self.pages = QStackedWidget(self)
        self.weapons_page = Weapons(self.pages)
        self.consumables_page = Consumables(self.pages)
        self.equipables_page = Equipables(self.pages)
        self.vehicles_page = Vehicles(self.pages)
        self.pages.addWidget(self.weapons_page)
        self.pages.addWidget(self.consumables_page)
        self.pages.addWidget(self.equipables_page)
        self.pages.addWidget(self.vehicles_page)
        
        _btn_list = [
            {
                "text": "Weapons",
                "page": self.weapons_page,
                "active": True
            },
            {
                "text": "Consumables",
                "page": self.consumables_page,
                "active": False
            },
            {
                "text": "Equipables",
                "page": self.equipables_page,
                "active": False
            },
            {
                "text": "Vehicles",
                "page": self.vehicles_page,
                "active": False
            },
        ]
        
        self.navbar.setup_buttons(_btn_list)
        self._layout.addWidget(self.navbar)
        self._layout.addWidget(self.pages)