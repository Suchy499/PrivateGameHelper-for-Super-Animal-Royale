from core.qt_core import *
from images import IMAGES
from typing import Literal

class LabeledSlider(QWidget):
    def __init__(
        self, 
        parent: QWidget | None = None, 
        orientation: Qt.Orientation = Qt.Orientation.Horizontal,
        min_value: float | int = 0, 
        max_value: float | int = 10.0, 
        step: float | int = 0.1, 
        default_value: float | int = 1.0, 
        text: str = "",
        text_type: Literal["float", "int"] = "float",
        icon: str = "",
        width: int = 200
    ):
        super().__init__(parent)
        self.orientation = orientation
        self.step = step
        self.min_value = min_value / self.step
        self.max_value = max_value / self.step
        self.default_value = default_value / self.step
        self.text = text
        self.type = text_type
        try:
            self.icon = QPixmap(IMAGES[icon]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        except KeyError:
            self.icon = ""
        self._width = width
        
        self.setFixedWidth(self._width)
        self.labeled_slider_layout = QGridLayout(self)
        self.labeled_slider_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.labeled_slider_layout.setContentsMargins(0, 0, 20, 0)
        
        self.label = QLabel(self, text=self.text)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.label.setObjectName("SliderLabel")
        self.slider = QSlider(self.orientation, self)
        self.slider.wheelEvent = self.wheelEvent
        self.slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slider.setObjectName("Slider")
        self.slider.setRange(int(self.min_value), int(self.max_value))
        self.slider.setSingleStep(1)
        self.slider.setPageStep(2)
        self.slider.setTracking(True)
        self.slider.setValue(int(self.default_value))
        self.slider.setFixedWidth(self._width-60)
        self.slider.valueChanged.connect(self._update_value)
        if self.type == "float":
            self.slider_value_label = QLabel(self, text=f"{(self.default_value * self.step):.1f}")
        else:
            self.slider_value_label = QLabel(self, text=str(int(self.default_value * self.step)))
        self.slider_value_label.setObjectName("SliderValue")
        self.slider_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slider_value_label.setFixedWidth(30)
        self.icon_label = QLabel(self)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_label.setFixedWidth(30)
        if self.icon != "":
            self.icon_label.setPixmap(self.icon)
        
        self.labeled_slider_layout.addWidget(self.label, 0, 0)
        self.labeled_slider_layout.addWidget(self.icon_label, 0, 1)
        self.labeled_slider_layout.addWidget(self.slider, 1, 0)
        self.labeled_slider_layout.addWidget(self.slider_value_label, 1, 1)
        
        self.valueChanged = self.slider.valueChanged
    
    def _update_value(self) -> None:
        if self.type == "float":
            self.slider_value_label.setText(f"{(self.slider.value() * self.step):.1f}")
        else:
            self.slider_value_label.setText(str(int(self.slider.value() * self.step)))
    
    def value(self) -> float:
        return round(self.slider.value() * self.step, 1)
    
    def setValue(self, value: float | int) -> None:
        if self.type == float:
            self.slider.setValue(round((value / self.step), 1))
        else:
            self.slider.setValue(round(value / self.step))
    
    def wheelEvent(self, event):
        return

    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return