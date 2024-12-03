from core import *
from images import IMAGES

class Player(QWidget):
    def __init__(
        self,
        playerItem: PlayerItem,
        parent: QWidget | None = None,
    ):
        super().__init__(parent)
        
        self.player_item = playerItem
        self.index = global_vars.PLAYER_LIST.index(playerItem)
        
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(7, 10, 7, 10)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.name_label = QLabel(self.player_item.name, self)
        self.name_label.setObjectName("PlayerNameTeams")
        
        if self.player_item.team == 2 or self.player_item.team == 1:
            self.left_icon = QPixmap(IMAGES["left_arrow"])
            self.left_button = QPushButton(self)
            self.left_button.setContentsMargins(10, 10, 10, 10)
            self.left_button.setIcon(self.left_icon)
            self.left_button.setFixedSize(self.left_icon.width()+10, self.left_icon.height()+10)
            self.left_button.setObjectName("TeamsButton")
            self.left_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.left_button.clicked.connect(self.move_left)
            self._layout.addWidget(self.left_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self._layout.addStretch()
        self._layout.addWidget(self.name_label)
        self._layout.addStretch()
        if self.player_item.team == 0 or self.player_item.team == 1:
            self.right_icon = QPixmap(IMAGES["right_arrow"])
            self.right_button = QPushButton(self)
            self.right_button.setContentsMargins(10, 10, 10, 10)
            self.right_button.setIcon(self.right_icon)
            self.right_button.setFixedSize(self.right_icon.width()+10, self.right_icon.height()+10)
            self.right_button.setObjectName("TeamsButton")
            self.right_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.right_button.clicked.connect(self.move_right)
            self._layout.addWidget(self.right_button, alignment=Qt.AlignmentFlag.AlignRight)
        
    def move_left(self) -> None:
        global_vars.PLAYER_LIST[self.index].team -= 1
        global_vars.SIGNAL_MANAGER.playerChangedTeams.emit()
    
    def move_right(self) -> None:
        global_vars.PLAYER_LIST[self.index].team += 1
        global_vars.SIGNAL_MANAGER.playerChangedTeams.emit()