from core import *
from images import IMAGES
from widgets import NavBar, ClickableLabel
from .settings import Settings
from .scoring import Scoring
from .leaderboard import Leaderboard
from .rounds import Rounds
from .graphs import  Graphs

class TournamentPage(QWidget):
    def __init__(self, parent, tournament_id: str):
        super().__init__(parent)
        
        self.tournament_id = tournament_id
        
        self.page_layout = QGridLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.page_layout.setSpacing(15)
        self.setObjectName("Content")
        
        self.navbar = NavBar(self)
        
        self.back_icon = QPixmap(IMAGES["back_arrow"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        self.back_button = ClickableLabel(self)
        self.back_button.setPixmap(self.back_icon)
        self.back_button.setFixedSize(self.back_icon.width() + 9, self.back_icon.height() + 9)
        self.back_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.back_button.setContentsMargins(0, 0, 0, 0)
        self.back_button.setToolTip("Go back")
        self.back_button.setObjectName("PlayersHeaderRefresh")
        self.back_button.clicked.connect(glb.SIGNAL_MANAGER.tournamentClosed.emit)
        
        self.pages = QStackedWidget(self)
        self.pages.setContentsMargins(0, 0, 0, 0)
        
        self.settings_page = Settings(self.pages, self.tournament_id)
        self.scoring_page = Scoring(self.pages, self.tournament_id)
        self.leaderboard_page = Leaderboard(self.pages, self.tournament_id)
        self.rounds_page = Rounds(self.pages, self.tournament_id)
        self.graphs_page = Graphs(self.pages, self.tournament_id)
        
        self.pages.addWidget(self.settings_page)
        self.pages.addWidget(self.scoring_page)
        self.pages.addWidget(self.leaderboard_page)
        self.pages.addWidget(self.rounds_page)
        self.pages.addWidget(self.graphs_page)
        
        _btn_list = [
            {
                "text": "Settings",
                "page": self.settings_page,
                "active": True
            },
            {
                "text": "Scoring",
                "page": self.scoring_page,
                "active": False
            },
            {
                "text": "Leaderboard",
                "page": self.leaderboard_page,
                "active": False
            },
            {
                "text": "Rounds",
                "page": self.rounds_page,
                "active": False
            },
            {
                "text": "Graphs",
                "page": self.graphs_page,
                "active": False
            },
        ]
        
        self.navbar.setup_buttons(_btn_list)
        self.page_layout.addWidget(self.navbar, 0, 0)
        self.page_layout.addWidget(self.back_button, 0, 1)
        self.page_layout.addWidget(self.pages, 1, 0, 1, 2)