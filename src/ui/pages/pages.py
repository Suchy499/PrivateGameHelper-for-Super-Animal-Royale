from core import *
from .home import PageHome
from .presets import PagePresets
from .pregame import PagePregame
from .players import PagePlayers
from .teleport import PageTeleport
from .items import PageItems
from .commands import PageCommands
from .duels import PageDuels
from .dodgeball import PageDodgeball
from .changelog import PageChangelog
from .about import PageAbout
from .settings import PageSettings

class Pages(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.home_page = PageHome(self)
        self.presets_page = PagePresets(self)
        self.pregame_page = PagePregame(self)
        self.players_page = PagePlayers(self)
        self.teleport_page = PageTeleport(self)
        self.items_page = PageItems(self)
        self.commands_page = PageCommands(self)
        self.duels_page = PageDuels(self)
        self.dodgeball_page = PageDodgeball(self)
        self.changelog_page = PageChangelog(self)
        self.about_page = PageAbout(self)
        self.settings_page = PageSettings(self)
        
        self.addWidget(self.home_page)
        self.addWidget(self.presets_page)
        self.addWidget(self.pregame_page)
        self.addWidget(self.players_page)
        self.addWidget(self.teleport_page)
        self.addWidget(self.items_page)
        self.addWidget(self.commands_page)
        self.addWidget(self.duels_page)
        self.addWidget(self.dodgeball_page)
        self.addWidget(self.changelog_page)
        self.addWidget(self.about_page)
        self.addWidget(self.settings_page)
        