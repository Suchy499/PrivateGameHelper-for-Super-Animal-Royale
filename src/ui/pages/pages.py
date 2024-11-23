from core import *
from .home import Home
from .presets import Presets
from .pregame import Pregame

class Pages(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.home_page = Home(self)
        self.presets_page = Presets(self)
        self.pregame_page = Pregame(self)
        
        self.addWidget(self.home_page)
        self.addWidget(self.presets_page)
        self.addWidget(self.pregame_page)
        