from core import *
from typing import Literal

class HealingButton(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None,
        icon: QPixmap | None = None,
        width: int = 100,
        healing_type: Literal["juice", "tape"] = "juice"
    ):
        super().__init__(parent=parent)
        self.parent_widget = parent
        self.healing_type = healing_type
        _icon_width = width - 10
        self.pixmap_icon = icon.scaledToWidth(_icon_width, Qt.TransformationMode.SmoothTransformation)
        self.setIcon(self.pixmap_icon)
        self.setIconSize(self.pixmap_icon.size())
        self.setContentsMargins(5, 5, 5, 5)
        self.setFixedSize(width, width)
        self.setObjectName("HealingButton")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(self.spawn_healing)
    
    def spawn_healing(self) -> None:
        match self.healing_type:
            case "juice":
                amount = self.parent_widget.juice_amount.value()
            case "tape":
                amount = self.parent_widget.tape_amount.value()
        spawn_healing(amount, self.healing_type)
        