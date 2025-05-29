from core import *
from typing import Literal
from widgets import VLine
from images import IMAGES

class Notification(QFrame):
    def __init__(
        self,
        parent: QWidget | None = None,
        w: int = 500,
        h: int = 40,
        notif_type: Literal["NotifInfo", "NotifWarning", "NotifSuccess", "NotifFail"] = "NotifInfo"
    ):
        super().__init__(parent)
        self._parent = parent
        self.setFixedSize(w, h)
        self.setObjectName("NotifWidget")
        self.notification_layout = QHBoxLayout(self)
        self.notification_layout.setContentsMargins(0, 0, 0, 0)
        self.notification_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)
        self.setVisible(False)
        self.connected = 0
        
        match notif_type:
            case "NotifInfo":
                self.pixmap = QPixmap(IMAGES["info"])
            case "NotifWarning":
                self.pixmap = QPixmap(IMAGES["warning"])
            case "NotifSuccess":
                self.pixmap = QPixmap(IMAGES["success"])
            case "NotifFail":
                self.pixmap = QPixmap(IMAGES["fail"])
        self.pixmap = self.pixmap.scaledToWidth(16, Qt.TransformationMode.SmoothTransformation)
        
        self.icon = QLabel(self)
        self.icon.setPixmap(self.pixmap)
        self.icon.setFixedSize(self.pixmap.size())
        self.vline = VLine(self, w=2)
        self.vline.setObjectName("DivLine")
        self.notif_text = QLabel(self)
        self.notif_text.setObjectName(notif_type)
        
        self._parent.showEvent = self._showEvent
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hide_popup)
        
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(200)
        
        self.notification_layout.addWidget(self.icon)
        self.notification_layout.addWidget(self.vline)
        self.notification_layout.addWidget(self.notif_text)
    
    def setText(self, text: str) -> None:
        return self.notif_text.setText(text)
    
    def setType(self, notif_type: Literal["NotifInfo", "NotifWarning", "NotifSuccess", "NotifFail"]):
        match notif_type:
            case "NotifInfo":
                self.pixmap = QPixmap(IMAGES["info"])
            case "NotifWarning":
                self.pixmap = QPixmap(IMAGES["warning"])
            case "NotifSuccess":
                self.pixmap = QPixmap(IMAGES["success"])
            case "NotifFail":
                self.pixmap = QPixmap(IMAGES["fail"])
        self.pixmap = self.pixmap.scaledToWidth(16, Qt.TransformationMode.SmoothTransformation)
        self.icon.setPixmap(self.pixmap)
        self.notif_text.setObjectName(notif_type)
    
    def updatePosition(self):
        _notif_x: int = (self._parent.width() // 2) - (self.width() // 2)
        _notif_y: int = self._parent.height() - self.height() - 10
        self.move(_notif_x, _notif_y)
    
    def _showEvent(self, event):
        self.updatePosition()
        return super().showEvent(event)
    
    def mouseReleaseEvent(self, event):
        self.hide_popup()
        return super().mouseReleaseEvent(event)
    
    def play_animation(self):
        self.raise_()
        self.setVisible(True)
        self.timer.stop()
        self.animation.stop()
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        if self.connected == 1:
            self.animation.finished.disconnect()
        self.animation.finished.connect(lambda: self.timer.start(5000))
        self.connected = 1
        self.animation.start()
    
    def hide_popup(self):
        self.timer.stop()
        self.animation.stop()
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.finished.disconnect()
        self.animation.finished.connect(lambda: self.setVisible(False))
        self.animation.start()
    
    def send_notification(
        self, 
        text: str = "", 
        notif_type: Literal["NotifInfo", "NotifWarning", "NotifSuccess", "NotifFail"] = "NotifInfo"
    ):
        self.setText(text)
        self.setType(notif_type)
        self.setStyleSheet(self.styleSheet())
        self.play_animation()