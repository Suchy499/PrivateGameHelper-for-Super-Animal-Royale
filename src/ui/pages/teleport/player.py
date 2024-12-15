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
        
        self.player_layout = QHBoxLayout(self)
        self.player_layout.setContentsMargins(7, 10, 7, 10)
        
        self.name_label = ClickableLabel(self, self.player_item.name)
        self.name_label.setObjectName("PlayerName")
        if glb.SELECTED_PLAYER_TELE == self.player_item or glb.SELECTED_PLAYER_TELE == "ALL":
            self.name_label.setProperty("selected", "True")
        else:
            self.name_label.setProperty("selected", "False")
        self.name_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.name_label.clicked.connect(self.set_active)
        
        self.player_layout.addWidget(self.name_label)
        self.player_layout.addStretch()
    
    def set_active(self):
        glb.SELECTED_PLAYER_TELE = self.player_item
        glb.SIGNAL_MANAGER.playerSelected.emit()