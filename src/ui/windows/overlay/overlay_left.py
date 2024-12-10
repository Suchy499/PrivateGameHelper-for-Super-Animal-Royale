from core.qt_core import *
from images import IMAGES
from widgets import OverlaySidebar

class OverlayLeft(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setFixedSize(90, 500)
        
        self.container = QWidget(self)
        self.container.setFixedSize(self.size())
        self.container_layout = QHBoxLayout(self.container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setDirection(QHBoxLayout.Direction.RightToLeft)
        self.container_layout.setSpacing(0)
        
        self.button_container = QWidget(self)
        self.button_container.setFixedSize(40, 80)
        
        self.expand_button = QPushButton(self.button_container)
        self.expand_button.setGeometry(-16, 0, self.button_container.width(), self.button_container.height())
        self.expand_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.expand_button.setObjectName("OverlayExpandButtonLeft")
        self.left_arrow = QPixmap(IMAGES["left_arrow"])
        self.right_arrow = QPixmap(IMAGES["right_arrow"])
        self.expand_button.setIcon(self.left_arrow)
        self.expand_button.clicked.connect(self.toggle_animation)
        
        self.expand_button.keyPressEvent = self.keyPressEvent
        self.expand_button.keyReleaseEvent = self.keyReleaseEvent
        
        self.overlay_content = QFrame(self)
        self.overlay_content.setFixedSize(self.width()-self.button_container.width(), self.height())
        self.overlay_content.setObjectName("OverlayLeft")
        self.overlay_content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout_ = QVBoxLayout(self.overlay_content)
        self.layout_.setContentsMargins(0, 0, 0, 0)
        self.sidebar = OverlaySidebar(self, Qt.Orientation.Vertical)
        self.layout_.addWidget(self.sidebar)
        
        self.container_layout.addWidget(self.button_container)
        self.container_layout.addWidget(self.overlay_content)
        
        self.animation = QPropertyAnimation(self.container, b"pos")
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.animation.setDuration(1500)
        
    def toggle_animation(self) -> None:
        self.animation.stop()
        if self.container.x() == 0:
            self.animation.setEndValue(QPoint(-self.overlay_content.width(), 0))
            self.expand_button.setIcon(self.right_arrow)
        else:
            self.animation.setEndValue(QPoint(0, 0))
            self.expand_button.setIcon(self.left_arrow)
        self.animation.setDuration(500)
        self.animation.start()
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return