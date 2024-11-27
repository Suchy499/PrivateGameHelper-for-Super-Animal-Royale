from core.qt_core import *
from widgets import EquipmentButton
from images import IMAGES

class Vehicles(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(0, 0, 0, 0)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        _layout.addWidget(self.scroll_area)
        
        self._layout = QVBoxLayout(self.content_area)
        self._layout.setContentsMargins(0, 0, 9, 0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_width = 2
        
        self.vehicles_label = QLabel(self.content_area, text="Vehicles")
        self.vehicles_label.setContentsMargins(0, 0, 0, 15)
        self.vehicles_label.setObjectName("ItemsHeaderName")
        
        self.vehicles_container = QWidget(self.content_area)
        self.vehicles_container_layout = QGridLayout(self.vehicles_container)
        self.vehicles_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.vehicles_container_layout.setContentsMargins(10, 0, 0, 0)
        self.vehicles_container_layout.setSpacing(15)
        
        self.emu_button = EquipmentButton(self.vehicles_container, QPixmap(IMAGES["emu"]), 200, "emu")
        self.hamball_button = EquipmentButton(self.vehicles_container, QPixmap(IMAGES["hamball"]), 200, "hamball")
        
        self.vehicles_container_layout.addWidget(self.emu_button, 0, 0)
        self.vehicles_container_layout.addWidget(self.hamball_button, 0, 1)
        
        self._layout.addWidget(self.vehicles_label)
        self._layout.addWidget(self.vehicles_container)