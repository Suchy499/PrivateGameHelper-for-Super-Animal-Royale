from core import *
from .player import Player
from widgets import HLine, ClickableLabel
from images import IMAGES

class Teams(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(9, 9, 9, 22)
        _layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        
        self.header = QWidget(self)
        self.header_layout = QGridLayout(self.header)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setHorizontalSpacing(30)
        self.header_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.team_a_label = QLabel(self.header, text="Team A")
        self.team_a_label.setObjectName("PlayersHeaderName")
        self.team_a_label.setContentsMargins(9, 0, 0, 0)
        
        self.spectators_label = QLabel(self.header, text="Spectators")
        self.spectators_label.setObjectName("PlayersHeaderName")
        self.spectators_label.setContentsMargins(9, 0, 0, 0)
        
        self.team_b_container = QWidget(self.header)
        self.team_b_container_layout = QHBoxLayout(self.team_b_container)
        self.team_b_container_layout.setContentsMargins(9, 0, 9, 0)
        
        self.team_b_label = QLabel(self.header, text="Team B")
        self.team_b_label.setObjectName("PlayersHeaderName")
        
        self.refresh_button = ClickableLabel(self)
        self.refresh_button.setToolTip("Refresh")
        self.refresh_button_icon = QPixmap(IMAGES["refresh"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        self.refresh_button.setPixmap(self.refresh_button_icon)
        self.refresh_button.setFixedSize(self.refresh_button_icon.width() + 9, self.refresh_button_icon.height() + 9)
        self.refresh_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.refresh_button.setContentsMargins(0, 0, 0, 0)
        self.refresh_button.clicked.connect(read_players)
        self.refresh_button.setObjectName("PlayersHeaderRefresh")
        
        self.team_b_container_layout.addWidget(self.team_b_label)
        self.team_b_container_layout.addWidget(self.refresh_button)
        
        self.team_a_hline = HLine(self.header, h=self.line_height)
        self.team_a_hline.setObjectName("DivLine")
        
        self.spectators_hline = HLine(self.header, h=self.line_height)
        self.spectators_hline.setObjectName("DivLine")
        
        self.team_b_hline = HLine(self.header, h=self.line_height)
        self.team_b_hline.setObjectName("DivLine")
        
        self.header_layout.addWidget(self.team_a_label, 0, 0)
        self.header_layout.addWidget(self.spectators_label, 0, 1)
        self.header_layout.addWidget(self.team_b_container, 0, 2)
        self.header_layout.addWidget(self.team_a_hline, 1, 0)
        self.header_layout.addWidget(self.spectators_hline, 1, 1)
        self.header_layout.addWidget(self.team_b_hline, 1, 2)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        
        self.scroll_layout = QHBoxLayout(self.content_area)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(30)
        
        self.team_a_players = QWidget(self.content_area)
        self.team_a_players_layout = QVBoxLayout(self.team_a_players)
        self.team_a_players_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.spectators_players = QWidget(self.content_area)
        self.spectators_players_layout = QVBoxLayout(self.spectators_players)
        self.spectators_players_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.team_b_players = QWidget(self.content_area)
        self.team_b_players_layout = QVBoxLayout(self.team_b_players)
        self.team_b_players_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.scroll_layout.addWidget(self.team_a_players)
        self.scroll_layout.addWidget(self.spectators_players)
        self.scroll_layout.addWidget(self.team_b_players)
        
        self.set_columns_width()
        
        _layout.addWidget(self.header)
        _layout.addWidget(self.scroll_area)
    
        global_vars.SIGNAL_MANAGER.playersRefreshed.connect(self.load_players)
        global_vars.SIGNAL_MANAGER.playerChangedTeams.connect(self.load_players)
        
    def reset_players(self) -> None:
        for i in reversed(range(self.team_a_players_layout.count())):
            if self.team_a_players_layout.itemAt(i).widget() is not None:
                widget = self.team_a_players_layout.itemAt(i).widget()
                self.team_a_players_layout.removeWidget(widget)
                widget.deleteLater()
                
        for i in reversed(range(self.spectators_players_layout.count())):
            if self.spectators_players_layout.itemAt(i).widget() is not None:
                widget = self.spectators_players_layout.itemAt(i).widget()
                self.spectators_players_layout.removeWidget(widget)
                widget.deleteLater()
        
        for i in reversed(range(self.team_b_players_layout.count())):
            if self.team_b_players_layout.itemAt(i).widget() is not None:
                widget = self.team_b_players_layout.itemAt(i).widget()
                self.team_b_players_layout.removeWidget(widget)
                widget.deleteLater()
    
    def load_players(self) -> None:
        self.reset_players()
        self.saved_players = []
        for player_item in global_vars.PLAYER_LIST:
            player_object = Player(player_item, self)
            match player_item.team:
                case 0:
                    self.team_a_players_layout.addWidget(player_object)
                case 1:
                    self.spectators_players_layout.addWidget(player_object)
                case 2:
                    self.team_b_players_layout.addWidget(player_object)
            self.saved_players.append(player_object)
    
    def resizeEvent(self, event):
        self.set_columns_width()
        return super().resizeEvent(event)
    
    def set_columns_width(self) -> None:
        scroll_width = self.scroll_area.width()
        spacing = self.scroll_layout.spacing()
        col_width = (scroll_width - spacing * 2) / 3
        self.team_a_players.setFixedWidth(col_width)
        self.spectators_players.setFixedWidth(col_width)
        self.team_b_players.setFixedWidth(col_width)