from core.qt_core import *
from .toggle import Toggle

class LabeledToggle(QWidget):
    def __init__(
        self,
        parent: QWidget | None = None,
        width: int = 200,
        animation_curve: QEasingCurve = QEasingCurve.OutSine,
        animation_duration: int = 250,
        text: str = "",
        default_state: bool = False
    ):
        super().__init__(parent)
        self.toggle_layout = QHBoxLayout(self)
        self.toggle_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.toggle_layout.setContentsMargins(0, 0, 0, 0)

        self._width = width
        self._animation_curve = animation_curve
        self._animation_duration = animation_duration
        self._text = text
        self._default_state = default_state
        
        self.setFixedWidth(self._width)
        
        self.toggle = Toggle(
            parent = self,
            animation_curve = self._animation_curve,
            animation_duration = self._animation_duration
        )
        
        self.label = QLabel(self, text=self._text)
        self.toggle_layout.addWidget(self.toggle)
        self.toggle_layout.addSpacing(10)
        self.toggle_layout.addWidget(self.label)
        self.setChecked(self._default_state)
        self.stateChanged = self.toggle.stateChanged
        self.setObjectName("LabeledToggle")
    
    def isChecked(self) -> bool:
        return self.toggle.isChecked()
    
    def setChecked(self, arg__1: bool) -> None:
        self.toggle.setChecked(arg__1)
    
    def setObjectName(self, name) -> None:
        self.label.setObjectName(name)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return
    
    def setToolTip(self, arg__1):
        self.toggle.setToolTip(arg__1)
        return super().setToolTip(arg__1)