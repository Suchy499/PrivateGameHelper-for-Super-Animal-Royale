from core import *
from .home import Home
from .presets import Presets
from .pregame import Pregame
from .players import Players

class Pages(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.home_page = Home(self)
        self.presets_page = Presets(self)
        self.pregame_page = Pregame(self)
        self.players_page = Players(self)
        
        self.addWidget(self.home_page)
        self.addWidget(self.presets_page)
        self.addWidget(self.pregame_page)
        self.addWidget(self.players_page)
        