from core import *
from typing import Literal

class WeaponSelect(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None,
        icon: QPixmap | None = None,
        weapon_id: int = 0,
        team: Literal["a", "b"] = "a",
        fixed_size: QSize = QSize(100, 100),
    ):
        super().__init__(parent=parent)
        self.weapon_id = weapon_id
        self.selected = True
        self.fixed_size = fixed_size
        self.team = team
        _icon_size = self.fixed_size.width() - 10, self.fixed_size.height() - 10
        self.pixmap_icon = icon.scaled(*_icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.pixmap_icon_dim = icon.scaled(*_icon_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.mask = self.pixmap_icon_dim.mask()
        
        p = QPainter(self.pixmap_icon_dim)
        p.setPen(QColor(0, 0, 0, 192))
        p.drawPixmap(self.pixmap_icon_dim.rect(), self.mask, self.mask.rect())
        p.end()
        self.setIcon(self.pixmap_icon)
        self.setIconSize(self.pixmap_icon.size())
        self.setContentsMargins(5, 5, 5, 5)
        self.setFixedSize(self.fixed_size)
        self.setObjectName("WeaponButton")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(self.on_click)
        glb.SIGNAL_MANAGER.weaponSelected.connect(self.change_state)
        glb.SIGNAL_MANAGER.weaponSelectedAll.connect(self.selected_all)
    
    def on_click(self) -> None:
        self.selected = not self.selected
        match self.team:
            case "a":
                glb.DUELS_A_WEAPONS[self.weapon_id] = self.selected
            case "b":
                glb.DUELS_B_WEAPONS[self.weapon_id] = self.selected
        glb.SIGNAL_MANAGER.weaponSelected.emit(self.weapon_id)
    
    def change_state(self, weapon_id: int) -> None:
        if weapon_id != self.weapon_id:
            return
        match self.team:
            case "a":
                self.selected = glb.DUELS_A_WEAPONS[self.weapon_id]
            case "b":
                self.selected = glb.DUELS_B_WEAPONS[self.weapon_id]
        self.setIcon(self.pixmap_icon if self.selected else self.pixmap_icon_dim)
    
    def selected_all(self, team: str, selected: bool) -> None:
        if self.team != team:
            return
        self.selected = selected
        match self.team:
            case "a":
                glb.DUELS_A_WEAPONS[self.weapon_id] = self.selected
            case "b":
                glb.DUELS_B_WEAPONS[self.weapon_id] = self.selected
        self.setIcon(self.pixmap_icon if self.selected else self.pixmap_icon_dim)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return