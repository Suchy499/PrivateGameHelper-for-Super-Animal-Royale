from core import *
from .player import Player

class PlayersList(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.player_layout = QVBoxLayout(self)
        self.player_layout.setContentsMargins(0, 0, 9, 9)
        self.player_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setObjectName("Content")

        glb.SIGNAL_MANAGER.playersRefreshed.connect(self.load_players)
        glb.SIGNAL_MANAGER.playerSelected.connect(self.load_players)
        
    def reset_players(self) -> None:
        for i in reversed(range(self.player_layout.count())):
            if self.player_layout.itemAt(i).widget() is not None:
                widget = self.player_layout.itemAt(i).widget()
                self.player_layout.removeWidget(widget)
                widget.deleteLater()
    
    def load_players(self) -> None:
        self.reset_players()
        self.saved_players = []
        for player_item in glb.PLAYER_LIST:
            player_object = Player(player_item, self)
            self.player_layout.addWidget(player_object)
            self.saved_players.append(player_object)