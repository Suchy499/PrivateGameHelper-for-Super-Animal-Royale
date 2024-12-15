from core.qt_core import *
from images import IMAGES
from widgets import OverlaySidebar

class OverlayBottom(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setFixedSize(1000, 81)
        
        self.container = QWidget(self)
        self.container.setFixedSize(self.size())
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)
        
        self.button_container = QWidget(self)
        self.button_container.setFixedSize(80, 40)
        
        self.expand_button = QPushButton(self.button_container)
        self.expand_button.setGeometry(0, 16, self.button_container.width(), self.button_container.height())
        self.expand_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.expand_button.setObjectName("OverlayExpandButton")
        self.expand_button.setProperty("side", "bottom")
        self.top_arrow = QPixmap(IMAGES["top_arrow"])
        self.down_arrow = QPixmap(IMAGES["down_arrow"])
        self.expand_button.setIcon(self.down_arrow)
        self.expand_button.clicked.connect(self.toggle_animation)
        
        self.expand_button.keyPressEvent = self.keyPressEvent
        self.expand_button.keyReleaseEvent = self.keyReleaseEvent
        
        self.overlay_content = QFrame(self)
        self.overlay_content.setFixedSize(self.width(), self.height()-self.button_container.height())
        self.overlay_content.setObjectName("Overlay")
        self.overlay_content.setProperty("side", "bottom")
        self.overlay_content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.overlay_layout = QHBoxLayout(self.overlay_content)
        self.overlay_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = OverlaySidebar(self, Qt.Orientation.Horizontal)
        self.overlay_layout.addWidget(self.sidebar)
        
        self.container_layout.addWidget(self.button_container, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.container_layout.addWidget(self.overlay_content)
        
        self.animation = QPropertyAnimation(self.container, b"pos")
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.animation.setDuration(1500)
        
    def toggle_animation(self) -> None:
        self.animation.stop()
        if self.container.y() == 0:
            self.animation.setEndValue(QPoint(0, self.overlay_content.height()))
            self.expand_button.setIcon(self.top_arrow)
        else:
            self.animation.setEndValue(QPoint(0, 0))
            self.expand_button.setIcon(self.down_arrow)
        self.animation.setDuration(500)
        self.animation.start()
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return