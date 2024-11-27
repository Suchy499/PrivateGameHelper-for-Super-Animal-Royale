from core.qt_core import *
from widgets import EquipmentButton, HLine
from images import IMAGES

class Equipables(QWidget):
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
        
        self.powerups_label = QLabel(self.content_area, text="Powerups")
        self.powerups_label.setContentsMargins(0, 0, 0, 15)
        self.powerups_label.setObjectName("ItemsHeaderName")
        
        self.powerups_container = QWidget(self.content_area)
        self.powerups_container_layout = QGridLayout(self.powerups_container)
        self.powerups_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.powerups_container_layout.setContentsMargins(10, 0, 0, 0)
        self.powerups_container_layout.setSpacing(15)
        
        self.claw_boots_button = EquipmentButton(self, QPixmap(IMAGES["claw_boots"]), 70, "claw_boots")
        self.banana_forker_button = EquipmentButton(self, QPixmap(IMAGES["banana_forker"]), 70, "banana_forker")
        self.ninja_boots_button = EquipmentButton(self, QPixmap(IMAGES["ninja_boots"]), 70, "ninja_boots")
        self.snorkel_button = EquipmentButton(self, QPixmap(IMAGES["snorkel"]), 70, "snorkel")
        self.cupgrade_button = EquipmentButton(self, QPixmap(IMAGES["cupgrade"]), 70, "cupgrade")
        self.bandolier_button = EquipmentButton(self, QPixmap(IMAGES["bandolier"]), 70, "bandolier")
        self.impossible_tape_button = EquipmentButton(self, QPixmap(IMAGES["impossible_tape"]), 70, "impossible_tape")
        
        self.powerups_container_layout.addWidget(self.claw_boots_button, 0, 0)
        self.powerups_container_layout.addWidget(self.banana_forker_button, 0, 1)
        self.powerups_container_layout.addWidget(self.ninja_boots_button, 0, 2)
        self.powerups_container_layout.addWidget(self.snorkel_button, 0, 3)
        self.powerups_container_layout.addWidget(self.cupgrade_button, 1, 0)
        self.powerups_container_layout.addWidget(self.bandolier_button, 1, 1)
        self.powerups_container_layout.addWidget(self.impossible_tape_button, 1, 2)
        
        self.powerups_hline = HLine(self, h=self.line_width)
        self.powerups_hline.setObjectName("DivLine")
        
        self.armor_label = QLabel(self.content_area, text="Armor")
        self.armor_label.setContentsMargins(0, 0, 0, 15)
        self.armor_label.setObjectName("ItemsHeaderName")
        
        self.armor_container = QWidget(self.content_area)
        self.armor_container_layout = QGridLayout(self.armor_container)
        self.armor_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.armor_container_layout.setContentsMargins(10, 0, 0, 0)
        self.armor_container_layout.setSpacing(15)
        
        self.armor1_button = EquipmentButton(self.powerups_container, QPixmap(IMAGES["armor1"]), 100, "armor1")
        self.armor2_button = EquipmentButton(self.powerups_container, QPixmap(IMAGES["armor2"]), 100, "armor2")
        self.armor3_button = EquipmentButton(self.powerups_container, QPixmap(IMAGES["armor3"]), 100, "armor3")
        
        self.armor_container_layout.addWidget(self.armor1_button, 0, 0)
        self.armor_container_layout.addWidget(self.armor2_button, 0, 1)
        self.armor_container_layout.addWidget(self.armor3_button, 0, 2)
        
        self._layout.addWidget(self.powerups_label)
        self._layout.addWidget(self.powerups_container)
        self._layout.addWidget(self.powerups_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.armor_label)
        self._layout.addWidget(self.armor_container)