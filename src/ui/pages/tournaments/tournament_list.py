from core import *
from widgets import HLine, ClickableLabel
from images import IMAGES

class TournamentList(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        
        self.header = QWidget(self)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(10, 0, 0, 0)
        
        self.header_name = QLabel(self.header, text="Tournaments")
        self.header_name.setObjectName("PresetsHeaderName")
        
        self.header_new = ClickableLabel(self.header)
        self.header_new.setContentsMargins(0, 0, 0, 0)
        self.header_new.setToolTip("New")
        self.header_new_pixmap = QPixmap(IMAGES["add"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        self.header_new.setPixmap(self.header_new_pixmap)
        self.header_new.setFixedSize(self.header_new_pixmap.width() + 9, self.header_new_pixmap.height() + 9)
        self.header_new.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_new.setObjectName("PlayersHeaderRefresh")
        self.header_new.setContentsMargins(0, 0, 0, 0)
        self.header_new.clicked.connect(create_tournament)
        
        self.header_layout.addWidget(self.header_name)
        self.header_layout.addWidget(self.header_new, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.horizontal_line = HLine(self, h=2)
        self.horizontal_line.setObjectName("DivLine")
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(0, 0, 9, 9)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        
        self.page_layout.addWidget(self.header)
        self.page_layout.addWidget(self.horizontal_line)
        self.page_layout.addWidget(self.scroll_area)
        
        self.load_tournaments()
        
        glb.SIGNAL_MANAGER.tournamentCreated.connect(self.load_tournaments)
        glb.SIGNAL_MANAGER.tournamentDeleted.connect(self.load_tournaments)
        
    def reset_tournaments(self) -> None:
        for i in reversed(range(self.content_layout.count())):
            if self.content_layout.itemAt(i).widget() is not None:
                widget = self.content_layout.itemAt(i).widget()
                self.content_layout.removeWidget(widget)
                widget.deleteLater()
    
    def load_tournaments(self) -> None:
        self.reset_tournaments()
        tournament_ids: list[str] = []
        tournament_list: list[tuple[str, str]] = []
        tournaments_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments")
        try:
            for tournament_id in os.listdir(tournaments_path):
                tournament_ids.append(tournament_id)
        except FileNotFoundError:
            return
        for tournament_id in tournament_ids:
            try:
                with open(os.path.join(tournaments_path, tournament_id, "metadata.json"), "r") as f:
                    tournament_metadata = json.load(f)
                    tournament_list.append((tournament_id, tournament_metadata["name"]))
            except:
                pass
        tournament_list.sort(key=lambda tup: tup[1])
        for tournament_id, tournament_name in tournament_list:
            saved_tournament = SavedTournament(self, tournament_id, tournament_name)
            self.content_layout.addWidget(saved_tournament)

class SavedTournament(QWidget):
    def __init__(self, parent, tournament_id: str, name: str):
        super().__init__(parent)
        self.tournament_id = tournament_id
        self.name = name
        
        self.tournament_layout = QHBoxLayout(self)
        self.tournament_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tournament_layout.setContentsMargins(7, 10, 7, 10)
        
        self.name_label = ClickableLabel(self, self.name)
        self.name_label.setObjectName("SavedPresetName")
        self.name_label.clicked.connect(lambda: glb.SIGNAL_MANAGER.tournamentOpened.emit(self.tournament_id))
        
        self.tournament_layout.addWidget(self.name_label)
        
        glb.SIGNAL_MANAGER.tournamentUpdated.connect(self.update_name)
    
    def update_name(self, tournament_id: str) -> None:
        if tournament_id != self.tournament_id:
            return
        
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", tournament_id)
        with open(os.path.join(tournament_path, "metadata.json"), "r") as f:
            tournament_metadata = json.load(f)
            
        self.name = tournament_metadata["name"]
        self.name_label.setText(self.name)