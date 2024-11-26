from core import *
from .player import Player

class Content(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 9, 9)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setObjectName("Content")

        Globals.SIGNAL_MANAGER.playersRefreshed.connect(self.load_players)
        Globals.SIGNAL_MANAGER.playerSelected.connect(self.load_players)
        
    def reset_players(self) -> None:
        for i in reversed(range(self._layout.count())):
            if self._layout.itemAt(i).widget() is not None:
                widget = self._layout.itemAt(i).widget()
                self._layout.removeWidget(widget)
                widget.deleteLater()
    
    def load_players(self) -> None:
        self.reset_players()
        self.saved_players = []
        for player_item in Globals.PLAYER_LIST:
            player_object = Player(player_item, self)
            self._layout.addWidget(player_object)
            self.saved_players.append(player_object)