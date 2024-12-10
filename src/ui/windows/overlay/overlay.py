from core import *
from styles import OverlayStyle
from .overlay_right import OverlayRight
from .overlay_left import OverlayLeft
from .overlay_top import OverlayTop
from .overlay_bottom import OverlayBottom
from .overlay_center import OverlayCenter
from images import IMAGES
import win32gui
from typing import Optional
import win32con

class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Private Game Helper Overlay")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.SplashScreen, True)
        self.setStyleSheet(OverlayStyle.getValue(glb.SETTINGS.value("OverlayStyle", 0)))
        
        self.layout_ = QGridLayout(self)
        self.layout_.setContentsMargins(0, 0, 0, 0)
        self.layout_.setSpacing(0)
        
        self.top_overlay_container = QWidget(self)
        self.top_overlay_container_layout = QVBoxLayout(self.top_overlay_container)
        self.top_overlay_container_layout.setContentsMargins(0, 0, 0, 0)
        self.top_overlay_container_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.top_overlay = OverlayTop(self.top_overlay_container)
        self.top_overlay_container_layout.addWidget(self.top_overlay)
        self.top_overlay_container.setMaximumSize(self.top_overlay.size())
        self.top_overlay_container.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        
        self.right_overlay_container = QWidget(self)
        self.right_overlay_container_layout = QVBoxLayout(self.right_overlay_container)
        self.right_overlay_container_layout.setContentsMargins(0, 0, 0, 0)
        self.right_overlay_container_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.right_overlay = OverlayRight(self.right_overlay_container)
        self.right_overlay_container_layout.addWidget(self.right_overlay)
        self.right_overlay_container.setMaximumSize(self.right_overlay.size())
        self.right_overlay_container.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        
        self.bottom_overlay_container = QWidget(self)
        self.bottom_overlay_container_layout = QVBoxLayout(self.bottom_overlay_container)
        self.bottom_overlay_container_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_overlay_container_layout.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.bottom_overlay = OverlayBottom(self.bottom_overlay_container)
        self.bottom_overlay_container_layout.addWidget(self.bottom_overlay)
        self.bottom_overlay_container.setMaximumSize(self.bottom_overlay.size())
        self.bottom_overlay_container.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        
        self.left_overlay_container = QWidget(self)
        self.left_overlay_container_layout = QVBoxLayout(self.left_overlay_container)
        self.left_overlay_container_layout.setContentsMargins(0, 0, 0, 0)
        self.left_overlay_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.left_overlay = OverlayLeft(self.left_overlay_container)
        self.left_overlay_container_layout.addWidget(self.left_overlay)
        self.left_overlay_container.setMaximumSize(self.left_overlay.size())
        self.left_overlay_container.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        
        self.center_overlay_container = QWidget(self)
        self.center_overlay_container_layout = QVBoxLayout(self.center_overlay_container)
        self.center_overlay_container_layout.setContentsMargins(0, 0, 0, 0)
        self.center_overlay = OverlayCenter(self)
        self.center_overlay_container_layout.addWidget(self.center_overlay)
        
        self.layout_.addWidget(self.top_overlay_container, 0, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.layout_.addWidget(self.right_overlay_container, 1, 2, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout_.addWidget(self.bottom_overlay_container, 2, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.layout_.addWidget(self.left_overlay_container, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout_.addWidget(self.center_overlay_container, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.resize_timer = QTimer(self)
        self.resize_timer.timeout.connect(self.updateRect)
        self.resize_timer.start(16)
        
        _btn_list = [
            {
                "icon": IMAGES["home"],
                "text": "",
                "category": "home",
                "show_top": True,
                "page": self.center_overlay.pages.home_page,
                "active": False,
            },
            {
                "icon": IMAGES["presets"],
                "text": "",
                "category": "pregame_setup",
                "show_top": True,
                "page": self.center_overlay.pages.presets_page,
                "active": False,
            },
            {
                "icon": IMAGES["pregame"],
                "text": "",
                "category": "pregame_setup",
                "show_top": True,
                "page": self.center_overlay.pages.pregame_page,
                "active": False,
            },
            {
                "icon": IMAGES["players"],
                "text": "",
                "category": "players",
                "show_top": True,
                "page": self.center_overlay.pages.players_page,
                "active": False,
            },
            {
                "icon": IMAGES["teleport"],
                "text": "",
                "category": "players",
                "show_top": True,
                "page": self.center_overlay.pages.teleport_page,
                "active": False,
            },
            {
                "icon": IMAGES["banana"],
                "text": "",
                "category": "commands",
                "show_top": True,
                "page": self.center_overlay.pages.items_page,
                "active": False,
            },
            {
                "icon": IMAGES["commands"],
                "text": "",
                "category": "commands",
                "show_top": True,
                "page": self.center_overlay.pages.commands_page,
                "active": False,
            },
            {
                "icon": IMAGES["duels"],
                "text": "",
                "category": "gamemodes",
                "show_top": True,
                "page": self.center_overlay.pages.duels_page,
                "active": False,
            },
            {
                "icon": IMAGES["dodgeball"],
                "text": "",
                "category": "gamemodes",
                "show_top": True,
                "page": self.center_overlay.pages.dodgeball_page,
                "active": False,
            },
            {
                "icon": IMAGES["changelog"],
                "text": "",
                "category": "info",
                "show_top": False,
                "page": self.center_overlay.pages.changelog_page,
                "active": False,
            },
            {
                "icon": IMAGES["info"],
                "text": "",
                "category": "info",
                "show_top": False,
                "page": self.center_overlay.pages.about_page,
                "active": False,
            },
            {
                "icon": IMAGES["settings"],
                "text": "",
                "category": "settings",
                "show_top": False,
                "page": self.center_overlay.pages.settings_page,
                "active": False,
            },
        ]
        
        self.right_overlay.sidebar.setup_buttons(_btn_list)
        self.left_overlay.sidebar.setup_buttons(_btn_list)
        self.top_overlay.sidebar.setup_buttons(_btn_list)
        self.bottom_overlay.sidebar.setup_buttons(_btn_list)
        
        self.select_position()
        glb.SIGNAL_MANAGER.settingChanged.connect(self.select_position)
        glb.SIGNAL_MANAGER.overlayStyleChanged.connect(self.update_style)
    
    def resizeEvent(self, event):
        center_w = self.width() // 1.5
        center_h = self.height() // 1.5
        self.center_overlay_container.setFixedSize(center_w, center_h)
        return super().resizeEvent(event)
    
    def get_window_size(self, name) -> Optional[tuple[int, int, int, int]]:
        if hwnd := win32gui.FindWindow(None, name):
            x, y, w, h = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            return hwnd, x, y, w, h
        return None
    
    def updateRect(self):
        if window := self.get_window_size("Super Animal Royale"):
            hwnd, x, y, w, h = window
            if win32gui.GetWindowLong(self.handle, win32con.GWL_HWNDPARENT) != hwnd:
                win32gui.SetWindowLong(self.handle, win32con.GWL_HWNDPARENT, hwnd)
            self.setGeometry(x, y, w, h)
            if glb.SETTINGS.value("DisplayMode", 0) != 1:
                self.setVisible(True)
        else:
            self.setVisible(False)
    
    def showEvent(self, event):
        self.handle = win32gui.FindWindow(None, "Private Game Helper Overlay")
        return super().showEvent(event)

    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return
    
    def select_position(self):
        match glb.SETTINGS.value("OverlayPosition", 0):
            case 0:
                self.right_overlay.setVisible(True)
                self.bottom_overlay.setVisible(False)
                self.left_overlay.setVisible(False)
                self.top_overlay.setVisible(False)
            case 1:
                self.right_overlay.setVisible(False)
                self.bottom_overlay.setVisible(False)
                self.left_overlay.setVisible(True)
                self.top_overlay.setVisible(False)
            case 2:
                self.right_overlay.setVisible(False)
                self.bottom_overlay.setVisible(True)
                self.left_overlay.setVisible(False)
                self.top_overlay.setVisible(False)
            case 3:
                self.right_overlay.setVisible(False)
                self.bottom_overlay.setVisible(False)
                self.left_overlay.setVisible(False)
                self.top_overlay.setVisible(True)
                
    def update_style(self) -> None:
        self.setStyleSheet(OverlayStyle.getValue(glb.SETTINGS.value("OverlayStyle", 0)))