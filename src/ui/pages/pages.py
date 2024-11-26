from core import *
from .home import PageHome
from .presets import PagePresets
from .pregame import PagePregame
from .players import PagePlayers
from .teleport import PageTeleport

class Pages(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.home_page = PageHome(self)
        self.presets_page = PagePresets(self)
        self.pregame_page = PagePregame(self)
        self.players_page = PagePlayers(self)
        self.teleport_page = PageTeleport(self)
        
        self.addWidget(self.home_page)
        self.addWidget(self.presets_page)
        self.addWidget(self.pregame_page)
        self.addWidget(self.players_page)
        self.addWidget(self.teleport_page)
        