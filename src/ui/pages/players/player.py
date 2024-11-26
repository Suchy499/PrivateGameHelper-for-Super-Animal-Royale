from core import *
from widgets import ClickableLabel

class Player(QWidget):
    def __init__(
        self,
        playerItem: PlayerItem,
        parent: QWidget | None = None,
    ):
        super().__init__(parent)
        
        self.player_item = playerItem
        
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(7, 10, 7, 10)
        
        self.name_label = ClickableLabel(self, self.player_item.name)
        if Globals.SELECTED_PLAYER == self.player_item:
            self.name_label.setObjectName("PlayerNameSelected")
        else:
            self.name_label.setObjectName("PlayerName")
        self.name_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.name_label.clicked.connect(self.set_active)
        
        self._layout.addWidget(self.name_label)
        self._layout.addStretch()
    
    def set_active(self):
        Globals.SELECTED_PLAYER = self.player_item
        Globals.SIGNAL_MANAGER.playerSelected.emit()