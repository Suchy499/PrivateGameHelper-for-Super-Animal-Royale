from core import *
from .settings import Settings
from .spawn_rates import SpawnRates
from .general import General
from widgets import NavBar

class PagePregame(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.page_layout.setSpacing(15)
        self.setObjectName("Content")
        
        self.navbar = NavBar(self)
        self.pages = QStackedWidget(self)
        self.general_page = General(self.pages)
        self.settings_page = Settings(self.pages)
        self.spawn_rates_page = SpawnRates(self.pages)
        self.pages.addWidget(self.general_page)
        self.pages.addWidget(self.settings_page)
        self.pages.addWidget(self.spawn_rates_page)
        
        _btn_list = [
            {
                "text": "General",
                "page": self.general_page,
                "active": True
            },
            {
                "text": "Settings",
                "page": self.settings_page,
                "active": False
            },
            {
                "text": "Spawn Rates",
                "page": self.spawn_rates_page,
                "active": False
            },
        ]
        
        self.navbar.setup_buttons(_btn_list)
        self.page_layout.addWidget(self.navbar)
        self.page_layout.addWidget(self.pages)
        
        glb.SIGNAL_MANAGER.presetOpened.connect(self.load_settings)
        glb.SIGNAL_MANAGER.presetRestored.connect(self.reset_settings)
        
    def load_settings(self, preset: dict) -> None:
        self.general_page.load_settings(preset)
        self.settings_page.load_settings(preset["settings"])
        self.spawn_rates_page.load_settings(preset["settings"]["gun_weights"])
        glb.PREGAME_SETTINGS["preset_id"] = preset["preset_id"]
        glb.PREGAME_SETTINGS["last_edited"] = preset["last_edited"]
    
    def reset_settings(self, preset: dict) -> None:
        self.general_page.reset_settings()
        self.settings_page.load_settings(preset["settings"])
        self.spawn_rates_page.load_settings(preset["settings"]["gun_weights"])
        glb.PREGAME_SETTINGS["preset_id"] = preset["preset_id"]
        glb.PREGAME_SETTINGS["last_edited"] = preset["last_edited"]