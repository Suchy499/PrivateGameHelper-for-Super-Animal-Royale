from core.qt_core import *
from core._version import __version__
from widgets import Button
import requests
import webbrowser
from packaging.version import Version
from typing import Optional
import os
import subprocess
import sys

class UpdatePopup(QFrame):
    def __init__(
        self,
        parent: QWidget | None = None,
        w: int = 300,
        h: int = 150,
    ):
        super().__init__(parent)
        self._parent = parent
        self.setFixedSize(w, h)
        self.setObjectName("UpdatePopup")
        self.popup_layout = QGridLayout(self)
        self.popup_layout.setContentsMargins(0, 0, 0, 0)
        self.popup_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.latest_version: str = self.get_latest_version()
        if not self.latest_version or Version(__version__) >= Version(self.latest_version):
            self.setVisible(False)
        
        self.title_label = QLabel("Update available", self)
        self.title_label.setObjectName("PlayersHeaderName")
        
        self.current_version_label = QLabel(f"Current version: {__version__}")
        self.current_version_label.setObjectName("HostIDLabel")
        
        self.latest_version_label = QLabel(f"Latest version: {self.latest_version if self.latest_version else __version__}", self)
        self.latest_version_label.setObjectName("HostIDLabel")
        
        self.remind_button = Button(self, "Remind me later", w=125, btn_style="ButtonDelete")
        self.remind_button.clicked.connect(lambda: self.setVisible(False))
        self.update_button = Button(self, "Update", w=125)
        self.update_button.clicked.connect(self.update_pgh)
        
        self.popup_layout.addWidget(self.title_label, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.popup_layout.addWidget(self.current_version_label, 1, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.popup_layout.addWidget(self.latest_version_label, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.popup_layout.addWidget(self.remind_button, 3, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.popup_layout.addWidget(self.update_button, 3, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self._parent.showEvent = self._showEvent
    
    def updatePosition(self):
        _popup_x: int = (self._parent.width() // 2) - (self.width() // 2)
        _popup_y: int = (self._parent.height() // 2) - (self.height() // 2)
        self.move(_popup_x, _popup_y)
    
    def _showEvent(self, event):
        self.raise_()
        self.updatePosition()
        return super().showEvent(event)
    
    def get_latest_version(self) -> Optional[str]:
        try:
            response = requests.get("https://api.github.com/repos/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases/latest")
            return response.json()["tag_name"]
        except:
            return None
    
    def update_latest_version(self) -> None:
        self.latest_version = self.get_latest_version()
        self.latest_version_label.setText(f"Latest version: {self.latest_version if self.latest_version else __version__}")
    
    def update_pgh(self) -> None:
        root_dir = os.path.dirname(sys.executable)
        if "updater.exe" in os.listdir(root_dir):
            subprocess.Popen([os.path.join(root_dir, "updater.exe")], creationflags=subprocess.CREATE_NEW_CONSOLE)
            QApplication.exit()
            return
        webbrowser.open("https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases/latest")
        self.setVisible(False)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return