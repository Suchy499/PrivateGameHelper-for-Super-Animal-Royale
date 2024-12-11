from core import *
from .content import Content
from images import IMAGES
from widgets import HLine, ClickableLabel, Button

class PagePlayers(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(9, 9, 9, 22)
        
        self.header = QWidget(self)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(10, 0, 10, 0)
        
        self.header_name = QLabel(self.header, text="Players")
        self.header_name.setObjectName("PlayersHeaderName")
        
        self.header_refresh = ClickableLabel(self)
        self.header_refresh.setToolTip("Refresh")
        self.header_refresh_icon = QPixmap(IMAGES["refresh"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        self.header_refresh.setPixmap(self.header_refresh_icon)
        self.header_refresh.setFixedSize(self.header_refresh_icon.width() + 9, self.header_refresh_icon.height() + 9)
        self.header_refresh.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_refresh.setContentsMargins(0, 0, 0, 0)
        self.header_refresh.clicked.connect(read_players)
        self.header_refresh.setObjectName("PlayersHeaderRefresh")
        
        self.header_layout.addWidget(self.header_name)
        self.header_layout.addWidget(self.header_refresh, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.horizontal_line = HLine(self, h=2)
        self.horizontal_line.setObjectName("DivLine")
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = Content(self)
        self.scroll_area.setWidget(self.content_area)
        
        self.horizontal_line2 = HLine(self, h=2)
        self.horizontal_line2.setObjectName("DivLine")
        
        self.buttons = QWidget(self)
        self.buttons_layout = QHBoxLayout(self.buttons)
        self.buttons_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.buttons_layout.setContentsMargins(9, 9, 9, 0)
        self.buttons_layout.setSpacing(10)
        self.button_admin = Button(self.buttons, "Admin")
        self.button_god = Button(self.buttons, "God")
        self.button_kill = Button(self.buttons, "Kill")
        self.button_ghost = Button(self.buttons, "Ghost")
        self.button_kick = Button(self.buttons, "Kick")
        self.button_getpos = Button(self.buttons, "Position")
        self.button_saw = Button(self.buttons, "S.A.W")
        self.button_rebel = Button(self.buttons, "Rebel")
        self.button_infect = Button(self.buttons, "Infect")
        self.button_admin.clicked.connect(lambda: send_player_command("admin"))
        self.button_god.clicked.connect(lambda: send_player_command("god"))
        self.button_kill.clicked.connect(lambda: send_player_command("kill"))
        self.button_ghost.clicked.connect(lambda: send_player_command("ghost"))
        self.button_kick.clicked.connect(lambda: send_player_command("kick"))
        self.button_getpos.clicked.connect(lambda: send_player_command("getpos"))
        self.button_saw.clicked.connect(lambda: send_player_command("saw"))
        self.button_rebel.clicked.connect(lambda: send_player_command("rebel"))
        self.button_infect.clicked.connect(lambda: send_player_command("infect"))
        self.buttons_layout.addWidget(self.button_admin)
        self.buttons_layout.addWidget(self.button_god)
        self.buttons_layout.addWidget(self.button_kill)
        self.buttons_layout.addWidget(self.button_ghost)
        self.buttons_layout.addWidget(self.button_kick)
        self.buttons_layout.addWidget(self.button_getpos)
        self.buttons_layout.addWidget(self.button_saw)
        self.buttons_layout.addWidget(self.button_rebel)
        self.buttons_layout.addWidget(self.button_infect)
        
        self.button_admin.setToolTip(
            "Makes the selected player a \"helper admin\" which allows them to use all of the admin commands except the kick command on the primary admin.\n"
            "Repeating the command on the same player will revoke their helper admin status."
        )
        
        self.button_god.setToolTip(
            "Gives the selected player god-mode, making them immune to player damage.\n"
            "Selecting all will enable god-mode for all players."
        )
        
        self.button_kill.setToolTip(
            "Kills the selected player. Selecting all will kill all players.\n"
            "Only works on players who have finished parachuting."
        )
        
        self.button_ghost.setToolTip(
            "Turns the selected player into a spectator ghost.\n"
            "Can be ran in the lobby, or in-game after death only."
        )
        
        self.button_kick.setToolTip(
            "Kicks the selected player from the game.\n"
            "Player cannot rejoin until next match."
        )
        
        self.button_getpos.setToolTip(
            "Displays position of the selected player."
        )
        
        self.button_saw.setToolTip(
            "In SvR, changes the team of the selected player to S.A.W. Security Forces."
        )
        
        self.button_rebel.setToolTip(
            "In SvR, changes the team of the selected player to Super Animal Super Resistance."
        )
        
        self.button_infect.setToolTip(
            "In The Bwoking Dead, infects the selected player."
        )
        
        _layout.addWidget(self.header)
        _layout.addWidget(self.horizontal_line)
        _layout.addWidget(self.scroll_area)
        _layout.addWidget(self.horizontal_line2)
        _layout.addWidget(self.buttons)
        