from core import *
from styles import AppStyle
from images import IMAGES
from widgets import Sidebar, TitleBar, SizeGrip, Notification, UpdatePopup
from ui.pages import Pages
from ui.windows.overlay import Overlay

try:
    from ctypes import windll
    myappid = 'suchy499.privategamehelper.v2'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setObjectName("MainWindow")
        self.setMinimumSize(1265, 620)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setWindowTitle("Private Game Helper")
        self.setWindowIcon(QIcon(IMAGES[f"icon_{glb.SETTINGS.value("AppIcon", 0)}"]))
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setStyleSheet(AppStyle.getValue(glb.SETTINGS.value("AppStyle", 0)))
        
        self.content = QWidget(self)
        self.content.setObjectName("MainWindowContent")
        self.setCentralWidget(self.content)
        _layout = QGridLayout(self.content)
        _layout.setContentsMargins(0, 0, 0, 0)
        _layout.setSpacing(0)
        
        self.notif = Notification(self.content)
        self.update_popup = UpdatePopup(self.content)
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
        
        self.overlay = Overlay()
        self.overlay.show()
        update_hotkeys()
        
        self.tray_icon = QSystemTrayIcon(self.windowIcon(), self)
        self.tray_icon.setToolTip("Private Game Helper")
        
        self.tray_menu = QMenu("Tray Menu")
        self.tray_menu.addAction("Open App", self.open_app)
        self.tray_menu.addAction("Exit", QApplication.exit)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()
        
        glb.SIGNAL_MANAGER.settingChanged.connect(self.change_display_mode)
        glb.SIGNAL_MANAGER.appStyleChanged.connect(self.update_style)
        glb.SIGNAL_MANAGER.appIconChanged.connect(self.update_icon)
        
    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            self.title_bar.window_state_changed(self.windowState())
        super().changeEvent(event)
        event.accept()
    
    def moveEvent(self, event):
        self.title_bar.window_state_changed(self.windowState())
        return super().moveEvent(event)
    
    def resizeEvent(self, event):
        self.left_grip.setGeometry(-5, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 5, 10, 10, self.height())
        self.top_grip.setGeometry(5, -5, self.width() - 15, 10)
        self.bottom_grip.setGeometry(5, self.height() - 5, self.width() - 10, 10)
        self.top_left_grip.setGeometry(-5, -5, 15, 15)
        self.top_right_grip.setGeometry(self.width() - 10, -5, 15, 15)
        self.bottom_left_grip.setGeometry(-5, self.height() - 10, 15, 15)
        self.bottom_right_grip.setGeometry(self.width() - 10, self.height() - 10, 15, 15)
        self.notif.updatePosition()
        self.update_popup.updatePosition()
    
    def change_display_mode(self) -> None:
        match glb.SETTINGS.value("DisplayMode", 0):
            case 0:
                if not self.isVisible():
                    self.show()
                if not self.overlay.isVisible():
                    self.overlay.show()
            case 1:
                if not self.isVisible():
                    self.show()
                if self.overlay.isVisible():
                    self.overlay.hide()
            case 2:
                if self.isVisible():
                    self.hide()
                    self.tray_icon.showMessage("Private Game Helper", "Moved to Tray", msecs=5000)
                if not self.overlay.isVisible():
                    self.overlay.show()
    
    def update_style(self) -> None:
        self.setStyleSheet(AppStyle.getValue(glb.SETTINGS.value("AppStyle", 0)))
    
    def update_icon(self) -> None:
        self.setWindowIcon(QIcon(IMAGES[f"icon_{glb.SETTINGS.value("AppIcon", 0)}"]))
        self.tray_icon.setIcon(self.windowIcon())
    
    def open_app(self) -> None:
        match glb.SETTINGS.value("DisplayMode", 0):
            case 0:
                self.setWindowState(Qt.WindowState.WindowActive)
            case 1:
                self.setWindowState(Qt.WindowState.WindowActive)
            case 2:
                self.show()
                self.setWindowState(Qt.WindowState.WindowActive)