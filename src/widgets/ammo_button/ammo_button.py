from core import *

class AmmoButton(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None,
        icon: QPixmap | None = None,
        width: int = 55,
        ammo_id: int = 0
    ):
        super().__init__(parent=parent)
        self.parent_widget = parent
        self.ammo_id = ammo_id
        _icon_width = width - 10
        self.pixmap_icon = icon.scaledToWidth(_icon_width, Qt.TransformationMode.SmoothTransformation)
        self.setIcon(self.pixmap_icon)
        self.setIconSize(self.pixmap_icon.size())
        self.setContentsMargins(5, 5, 5, 5)
        self.setFixedSize(width, width)
        self.setObjectName("AmmoButton")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(self.spawn_ammo)
    
    def spawn_ammo(self) -> None:
        ammo_amount = self.parent_widget.ammo_amount.value()
        spawn_ammo(ammo_amount, self.ammo_id)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return