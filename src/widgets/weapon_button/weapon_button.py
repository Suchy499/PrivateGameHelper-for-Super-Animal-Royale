from core import *

class WeaponButton(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None,
        icon: QPixmap | None = None,
        size: QSize = QSize(100, 100),
        weapon_id: int | None = None
    ):
        super().__init__(parent=parent)
        self.weapon_id = weapon_id
        _icon_size = size.width() - 10, size.height() - 10
        self.pixmap_icon = icon.scaled(*_icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.setIcon(self.pixmap_icon)
        self.setIconSize(self.pixmap_icon.size())
        self.setContentsMargins(5, 5, 5, 5)
        self.setFixedSize(size)
        self.setObjectName("WeaponButton")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(lambda: spawn_weapon(self.weapon_id))
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return