from core import *
import styles
from images import IMAGES
from widgets import Sidebar, TitleBar, SizeGrip
from ui.pages import Pages

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setObjectName("MainWindow")
        self.setMinimumSize(1265, 620)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setWindowTitle("Private Game Helper")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setStyleSheet(styles.default_style)
        
        global_vars.SIGNAL_MANAGER.presetOpened.connect(lambda: self.setActivePage(self.pages.pregame_page, "Pregame"))
        
        self.content = QWidget(self)
        self.content.setObjectName("MainWindowContent")
        self.setCentralWidget(self.content)
        _layout = QGridLayout(self.content)
        _layout.setContentsMargins(0, 0, 0, 0)
        _layout.setSpacing(0)
        
        self.title_bar = TitleBar(self.content)
        self.sidebar = Sidebar(self.content)
        self.pages = Pages(self.content)
        self.left_grip = SizeGrip(self, "left", True)
        self.right_grip = SizeGrip(self, "right", True)
        self.top_grip = SizeGrip(self, "top", True)
        self.bottom_grip = SizeGrip(self, "bottom", True)
        self.top_left_grip = SizeGrip(self, "top_left", True)
        self.top_right_grip = SizeGrip(self, "top_right", True)
        self.bottom_left_grip = SizeGrip(self, "bottom_left", True)
        self.bottom_right_grip = SizeGrip(self, "bottom_right", True)
        
        _btn_list = [
            {
                "icon": IMAGES["home"],
                "text": "Home",
                "category": "home",
                "show_top": True,
                "page": self.pages.home_page,
                "active": True,
            },
            {
                "icon": IMAGES["presets"],
                "text": "Presets",
                "category": "pregame_setup",
                "show_top": True,
                "page": self.pages.presets_page,
                "active": False,
            },
            {
                "icon": IMAGES["pregame"],
                "text": "Pregame",
                "category": "pregame_setup",
                "show_top": True,
                "page": self.pages.pregame_page,
                "active": False,
            },
            {
                "icon": IMAGES["players"],
                "text": "Players",
                "category": "players",
                "show_top": True,
                "page": self.pages.players_page,
                "active": False,
            },
            {
                "icon": IMAGES["teleport"],
                "text": "Teleport",
                "category": "players",
                "show_top": True,
                "page": self.pages.teleport_page,
                "active": False,
            },
            {
                "icon": IMAGES["banana"],
                "text": "Items",
                "category": "commands",
                "show_top": True,
                "page": self.pages.items_page,
                "active": False,
            },
            {
                "icon": IMAGES["commands"],
                "text": "Commands",
                "category": "commands",
                "show_top": True,
                "page": self.pages.commands_page,
                "active": False,
            },
            {
                "icon": IMAGES["duels"],
                "text": "Duels",
                "category": "gamemodes",
                "show_top": True,
                "page": self.pages.duels_page,
                "active": False,
            },
            {
                "icon": IMAGES["dodgeball"],
                "text": "Dodgeball",
                "category": "gamemodes",
                "show_top": True,
                "page": self.pages.dodgeball_page,
                "active": False,
            },
            {
                "icon": IMAGES["changelog"],
                "text": "Changelog",
                "category": "info",
                "show_top": False,
                "page": self.pages.changelog_page,
                "active": False,
            },
            {
                "icon": IMAGES["info"],
                "text": "About",
                "category": "info",
                "show_top": False,
                "page": self.pages.about_page,
                "active": False,
            },
            {
                "icon": IMAGES["settings"],
                "text": "Settings",
                "category": "settings",
                "show_top": False,
                "page": self.pages.settings_page,
                "active": False,
            },
        ]
        
        self.sidebar.setup_buttons(_btn_list)
        _layout.addWidget(self.title_bar, 0, 0, 1, -1)
        _layout.addWidget(self.sidebar, 1, 0)
        _layout.addWidget(self.pages, 1, 1)
    
    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            self.title_bar.window_state_changed(self.windowState())
        super().changeEvent(event)
        event.accept()
    
    def resizeEvent(self, event):
        self.left_grip.setGeometry(-5, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 5, 10, 10, self.height())
        self.top_grip.setGeometry(5, -5, self.width() - 15, 10)
        self.bottom_grip.setGeometry(5, self.height() - 5, self.width() - 10, 10)
        self.top_left_grip.setGeometry(-5, -5, 15, 15)
        self.top_right_grip.setGeometry(self.width() - 10, -5, 15, 15)
        self.bottom_left_grip.setGeometry(-5, self.height() - 10, 15, 15)
        self.bottom_right_grip.setGeometry(self.width() - 10, self.height() - 10, 15, 15)
    
    def setActivePage(self, page, btn_text):
        self.pages.setCurrentWidget(page)
        self.sidebar.buttons[btn_text].select()