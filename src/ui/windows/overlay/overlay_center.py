from core import *
from ui.pages import Pages
from widgets import Notification, UpdatePopup, OverlayTitleBar, DebugConsole
import sys

class OverlayCenter(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setObjectName("Overlay")
        self.setProperty("side", "center")
        self.setVisible(False)
        
        self.overlay_layout = QVBoxLayout(self)
        self.overlay_layout.setContentsMargins(0, 0, 0, 0)
        self.overlay_layout.setSpacing(0)
        
        self.notif = Notification(self)
        self.update_popup = UpdatePopup(self)
        self.title_bar = OverlayTitleBar(self)
        self.pages = Pages(self)
        self.overlay_layout.addWidget(self.title_bar)
        self.overlay_layout.addWidget(self.pages)
        
        self.pages.currentChanged.connect(self.set_title)
        self.title_bar.close_button.clicked.connect(self.close_overlay)
        glb.SIGNAL_MANAGER.notificationSent.connect(self.notif.send_notification)
        
        self.debug_console = DebugConsole(self)
        self.debug_console.setGeometry(10, 10, self.width()-20, self.height()-20)
        self.debug_console.setVisible(False)
        
    def resizeEvent(self, event):
        self.notif.updatePosition()
        self.update_popup.updatePosition()
        self.debug_console.setGeometry(10, 10, self.width()-20, self.height()-20)
        return super().resizeEvent(event)

    def set_title(self, index: int) -> None:
        widget_name = self.pages.widget(index).metaObject().className()
        self.title_bar.setText(f"Private Game Helper - {widget_name.removeprefix("Page")}")
    
    def close_overlay(self) -> None:
        self.setVisible(False)
        open_window("Super Animal Royale")
        glb.SIGNAL_MANAGER.overlayClosed.emit()
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return
    
    def open_console(self) -> None:
        self.debug_console.setVisible(not self.debug_console.isVisible())