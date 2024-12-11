from core import *
from images import IMAGES
from widgets import HLine
import webbrowser

class PageAbout(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(9, 9, 9, 22)
        self.line_height = 2
        self.icon_size = QSize(60, 60)
        self.button_size = QSize(self.icon_size.width()+20, self.icon_size.height()+20)
        
        self.description_container = QWidget(self)
        self.description_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.description_layout = QVBoxLayout(self.description_container)
        self.description_layout.setContentsMargins(10, 9, 0, 9)
        self.description_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.description_layout.setSpacing(30)
        
        self.title_container = QWidget(self)
        self.title_layout = QVBoxLayout(self.title_container)
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.title = QLabel("Private Game Helper", self)
        self.title.setObjectName("TitleLabel")
        
        self.made_by = QLabel("Made by Suchy499", self)
        self.made_by.setObjectName("HostIDLabel")
        
        self.title_layout.addWidget(self.title)
        self.title_layout.addWidget(self.made_by)
        
        self.coffee_container = QWidget(self)
        self.coffee_layout = QVBoxLayout(self.coffee_container)
        self.coffee_layout.setContentsMargins(0, 0, 0, 0)
        self.coffee_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.coffee = QLabel(
            "This is a passion project of mine, which I have poured hundreds of hours into.\n"
            "So if you found this project useful, it would mean a world to me if you considered supporting through ko-fi.\n"
            "Thank you <3", 
            self
        )
        self.coffee.setObjectName("HostIDLabel")
        
        self.kofi_icon = QPixmap(IMAGES["ko-fi"]).scaled(self.icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.kofi = QPushButton(self, icon=self.kofi_icon)
        self.kofi.setIconSize(self.kofi_icon.size())
        self.kofi.setFixedSize(self.button_size)
        self.kofi.setContentsMargins(10, 10, 10, 10)
        self.kofi.setObjectName("WeaponButton")
        self.kofi.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.kofi.clicked.connect(lambda: webbrowser.open("https://ko-fi.com/suchy499"))
        self.kofi.setToolTip("Ko-fi")
        
        self.coffee_layout.addWidget(self.coffee)
        self.coffee_layout.addWidget(self.kofi)
        
        self.socials_container = QWidget(self)
        self.socials_layout = QGridLayout(self.socials_container)
        self.socials_layout.setContentsMargins(0, 0, 0, 0)
        self.socials_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.socials_layout.setHorizontalSpacing(20)
        self.socials = QLabel("You can also find me on these socials!", self)
        self.socials.setObjectName("HostIDLabel")
        
        self.discord_icon = QPixmap(IMAGES["discord"]).scaled(self.icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.discord = QPushButton(self, icon=self.discord_icon)
        self.discord.setIconSize(self.discord_icon.size())
        self.discord.setFixedSize(self.button_size)
        self.discord.setContentsMargins(10, 10, 10, 10)
        self.discord.setObjectName("WeaponButton")
        self.discord.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.discord.clicked.connect(lambda: webbrowser.open("https://discord.com/users/484740625137139733"))
        self.discord.setToolTip("Discord")
        
        self.twitter_icon = QPixmap(IMAGES["twitter"]).scaled(self.icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.twitter = QPushButton(self, icon=self.twitter_icon)
        self.twitter.setIconSize(self.twitter_icon.size())
        self.twitter.setFixedSize(self.button_size)
        self.twitter.setContentsMargins(10, 10, 10, 10)
        self.twitter.setObjectName("WeaponButton")
        self.twitter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.twitter.clicked.connect(lambda: webbrowser.open("https://twitter.com/Suchy4992"))
        self.twitter.setToolTip("Twitter")
        
        self.github_icon = QPixmap(IMAGES["github"]).scaled(self.icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.github = QPushButton(self, icon=self.github_icon)
        self.github.setIconSize(self.github_icon.size())
        self.github.setFixedSize(self.button_size)
        self.github.setContentsMargins(10, 10, 10, 10)
        self.github.setObjectName("WeaponButton")
        self.github.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.github.clicked.connect(lambda: webbrowser.open("https://github.com/Suchy499"))
        self.github.setToolTip("Github")
        
        self.twitch_icon = QPixmap(IMAGES["twitch"]).scaled(self.icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.twitch = QPushButton(self, icon=self.twitch_icon)
        self.twitch.setIconSize(self.twitch_icon.size())
        self.twitch.setFixedSize(self.button_size)
        self.twitch.setContentsMargins(10, 10, 10, 10)
        self.twitch.setObjectName("WeaponButton")
        self.twitch.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.twitch.clicked.connect(lambda: webbrowser.open("https://www.twitch.tv/suchy4992"))
        self.twitch.setToolTip("Twitch")
        
        self.socials_layout.addWidget(self.socials, 0, 0, 1, 4)
        self.socials_layout.addWidget(self.discord, 1, 0, 1, 1)
        self.socials_layout.addWidget(self.twitter, 1, 1, 1, 1)
        self.socials_layout.addWidget(self.github, 1, 2, 1, 1)
        self.socials_layout.addWidget(self.twitch, 1, 3, 1, 1)
        
        self.description_layout.addWidget(self.title_container)
        self.description_layout.addWidget(self.coffee_container)
        self.description_layout.addWidget(self.socials_container)
        
        self.disclaimer_container = QWidget(self)
        self.disclaimer_layout = QVBoxLayout(self.disclaimer_container)
        self.disclaimer_layout.setContentsMargins(0, 0, 0, 0)
        self.disclaimer_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.hline = HLine(self, h=self.line_height)
        self.hline.setObjectName("DivLine")
        
        self.disclaimer_label = QLabel("Disclaimer", self)
        self.disclaimer_label.setObjectName("ItemsHeaderName")
        
        self.disclaimer_text = QLabel(
            "Assets used in this project come from the Official Super Animal Royale Wiki.\n"
            "Super Animal Royale is a trademark owned by Pixile Studios. This project is not associated with Pixile Studios in any form."
        )
        self.disclaimer_text.setObjectName("HostIDLabel")
        self.disclaimer_text.setContentsMargins(10, 0, 0, 0)
        
        self.disclaimer_layout.addWidget(self.hline)
        self.disclaimer_layout.addSpacing(10)
        self.disclaimer_layout.addWidget(self.disclaimer_label)
        self.disclaimer_layout.addWidget(self.disclaimer_text)
        
        _layout.addWidget(self.description_container)
        _layout.addWidget(self.disclaimer_container)