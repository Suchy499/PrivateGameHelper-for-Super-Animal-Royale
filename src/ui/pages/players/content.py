from core import *
from core.globals import *
from .player import Player

class Content(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.content_layout = QVBoxLayout(self)
        self.content_layout.setContentsMargins(0, 0, 9, 9)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setObjectName("Content")

        glb.SIGNAL_MANAGER.playersRefreshed.connect(self.load_players)
        glb.SIGNAL_MANAGER.playerSelected.connect(self.load_players)
        
    def reset_players(self) -> None:
        for i in reversed(range(self.content_layout.count())):
            if self.content_layout.itemAt(i).widget() is not None:
                widget = self.content_layout.itemAt(i).widget()
                self.content_layout.removeWidget(widget)
                widget.deleteLater()
    
    def load_players(self) -> None:
        self.reset_players()
        self.saved_players = []
        for player_item in glb.PLAYER_LIST:
            player_object = Player(player_item, self)
            self.content_layout.addWidget(player_object)
            self.saved_players.append(player_object)