from core import *
from typing import Literal

class ThrowableButton(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None,
        icon: QPixmap | None = None,
        width: int = 55,
        throwable_type: Literal["banana", "nade", "zip"] = "banana"
    ):
        super().__init__(parent=parent)
        self.parent_widget = parent
        self.throwable_type = throwable_type
        _icon_width = width - 10
        self.pixmap_icon = icon.scaledToWidth(_icon_width, Qt.TransformationMode.SmoothTransformation)
        self.setIcon(self.pixmap_icon)
        self.setIconSize(self.pixmap_icon.size())
        self.setContentsMargins(5, 5, 5, 5)
        self.setFixedSize(width, width)
        self.setObjectName("ThrowableButton")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(self.spawn_throwables)
        
    def spawn_throwables(self) -> None:
        amount = self.parent_widget.throwables_amount.value()
        spawn_throwable(amount, self.throwable_type)