from core import *
from images import IMAGES
from widgets import ClickableLabel

class Player(QWidget):
    def __init__(
        self,
        playerItem: PlayerItem,
        parent: QWidget | None = None,
    ):
        super().__init__(parent)
        
        self.player_item = playerItem
        self.index = glb.PLAYER_LIST.index(playerItem)
        
        self.player_layout = QHBoxLayout(self)
        self.player_layout.setContentsMargins(7, 10, 7, 10)
        self.player_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.name_label = ClickableLabel(self, self.player_item.name)
        self.name_label.setObjectName("PlayerNameTeams")
        self.name_label.clicked.connect(self.change_host)
        
        if self.player_item.team == 2 or self.player_item.team == 1:
            self.left_icon = QPixmap(IMAGES["left_arrow"])
            self.left_button = QPushButton(self)
            self.left_button.setContentsMargins(10, 10, 10, 10)
            self.left_button.setIcon(self.left_icon)
            self.left_button.setFixedSize(self.left_icon.width()+10, self.left_icon.height()+10)
            self.left_button.setObjectName("TeamsButton")
            self.left_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.left_button.clicked.connect(self.move_left)
            self.player_layout.addWidget(self.left_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.player_layout.addStretch()
        self.player_layout.addWidget(self.name_label)
        self.player_layout.addStretch()
        if self.player_item.team == 0 or self.player_item.team == 1:
            self.right_icon = QPixmap(IMAGES["right_arrow"])
            self.right_button = QPushButton(self)
            self.right_button.setContentsMargins(10, 10, 10, 10)
            self.right_button.setIcon(self.right_icon)
            self.right_button.setFixedSize(self.right_icon.width()+10, self.right_icon.height()+10)
            self.right_button.setObjectName("TeamsButton")
            self.right_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.right_button.clicked.connect(self.move_right)
            self.player_layout.addWidget(self.right_button, alignment=Qt.AlignmentFlag.AlignRight)
        
        if glb.HOST_ID == self.player_item.player_id:
            self.name_label.setProperty("selected", "True")
        else:
            self.name_label.setProperty("selected", "False")
            
        glb.SIGNAL_MANAGER.hostIdChanged.connect(self.host_changed)
        
    def change_host(self) -> None:
        glb.HOST_ID = self.player_item.player_id
        glb.SIGNAL_MANAGER.hostIdChanged.emit(self.player_item.player_id)
        if self.window().metaObject().className() == "Overlay":
            open_window("Super Animal Royale")
    
    def host_changed(self, host_id: int) -> None:
        if glb.HOST_ID == self.player_item.player_id:
            self.name_label.setProperty("selected", "True")
        else:
            self.name_label.setProperty("selected", "False")
        self.setStyleSheet(self.styleSheet())
        
    def move_left(self) -> None:
        glb.PLAYER_LIST[self.index].team -= 1
        glb.SIGNAL_MANAGER.playerChangedTeams.emit()
        if self.window().metaObject().className() == "Overlay":
            open_window("Super Animal Royale")
    
    def move_right(self) -> None:
        glb.PLAYER_LIST[self.index].team += 1
        glb.SIGNAL_MANAGER.playerChangedTeams.emit()
        if self.window().metaObject().className() == "Overlay":
            open_window("Super Animal Royale")