from core import *

class EquipmentButton(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None,
        icon: QPixmap | None = None,
        width: int = 55,
        equipment_type: str = ""
    ):
        super().__init__(parent=parent)
        self.equipment_type = equipment_type
        _icon_width = width - 10
        self.pixmap_icon = icon.scaledToWidth(_icon_width, Qt.TransformationMode.SmoothTransformation)
        self.setIcon(self.pixmap_icon)
        self.setIconSize(self.pixmap_icon.size())
        self.setContentsMargins(5, 5, 5, 5)
        self.setFixedSize(width, width)
        self.setObjectName("EquipmentButton")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(self.spawn_equipment)
    
    def spawn_equipment(self) -> None:
        match self.equipment_type:
            case "claw_boots":
                command = "util0"
            case "banana_forker":
                command = "util1"
            case "ninja_boots":
                command = "util2"
            case "snorkel":
                command = "util3"
            case "cupgrade":
                command = "util4"
            case "bandolier":
                command = "util5"
            case "impossible_tape":
                command = "util6"
            case "armor1":
                command = "armor1"
            case "armor2":
                command = "armor2"
            case "armor3":
                command = "armor3"
            case "emu":
                command = "emu"
            case "hamball":
                command = "hamball"
        spawn_equipment(command)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return