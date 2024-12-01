from core.qt_core import *
from .toggle import Toggle

class LabeledToggle(QWidget):
    def __init__(
        self,
        parent: QWidget | None = None,
        width: int = 200,
        bg_color: str = "#595b5e", 
        circle_color: str = "#DDD",
        active_color: str = "#00BCFF",
        animation_curve: QEasingCurve = QEasingCurve.OutSine,
        animation_duration: int = 250,
        text: str = "",
        default_state: bool = False
    ):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        self._width = width
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color
        self._animation_curve = animation_curve
        self._animation_duration = animation_duration
        self._text = text
        self._default_state = default_state
        
        self.setFixedWidth(self._width)
        
        self.toggle = Toggle(
            parent = self,
            bg_color = self._bg_color,
            circle_color = self._circle_color,
            active_color = self._active_color,
            animation_curve = self._animation_curve,
            animation_duration = self._animation_duration
        )
        
        self.label = QLabel(self, text=self._text)
        layout.addWidget(self.toggle)
        layout.addSpacing(10)
        layout.addWidget(self.label)
        self.setChecked(self._default_state)
        self.stateChanged = self.toggle.stateChanged
        self.setObjectName("LabeledToggle")
    
    def isChecked(self) -> bool:
        return self.toggle.isChecked()
    
    def setChecked(self, arg__1: bool) -> None:
        self.toggle.setChecked(arg__1)
    
    def setObjectName(self, name) -> None:
        self.label.setObjectName(name)
    