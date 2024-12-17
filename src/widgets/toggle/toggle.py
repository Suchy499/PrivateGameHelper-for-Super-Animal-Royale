from core import *
from styles import Style

class Toggle(QCheckBox):
    def __init__(
        self,
        parent: QWidget | None = None,
        width: int = 50,
        animation_curve: QEasingCurve = QEasingCurve.OutSine,
        animation_duration: int = 250,
        default_state: bool = False 
    ):
        super().__init__(parent)
        self.setFixedSize(width, 28)
        self.setObjectName("Toggle")
        self.setCursor(Qt.PointingHandCursor)
        self._default_state = default_state
        self._position = 4
        
        self.circle = QLabel(self)
        self.circle.setObjectName("ToggleCircle")
        self.circle.setGeometry(self._position, 3, 22, 22)
            
        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(animation_duration)
        self.animation.valueChanged.connect(self.move_circle)
        self.stateChanged.connect(self.setup_animation)
        self.setChecked(self._default_state)
        if self.window().metaObject().className() == "Overlay":
            self.clicked.connect(lambda: open_window("Super Animal Royale"))
        
        glb.SIGNAL_MANAGER.appStyleChanged.connect(self.style_changed)
        glb.SIGNAL_MANAGER.overlayStyleChanged.connect(self.style_changed)

    @Property(float)
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
        self.update()

    def setup_animation(self, state: bool):
        self.animation.stop()
        if state:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(4)
        self.animation.start()
    
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)
    
    def style_changed(self) -> None:
        if self.window().metaObject().className() == "MainWindow":
            self.setStyleSheet(Style.getValue(glb.SETTINGS.value("AppStyle", 0)))
        else:
            self.setStyleSheet(Style.getValue(glb.SETTINGS.value("OverlayStyle", 0)))
    
    def move_circle(self, value) -> None:
        self.circle.move(self._position, 3)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return