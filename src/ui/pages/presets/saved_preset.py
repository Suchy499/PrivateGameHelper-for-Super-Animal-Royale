from core import *
from widgets import ClickableLabel
import datetime

class SavedPreset(QWidget):
    def __init__(
        self,
        parent,
        preset: dict
    ):
        super().__init__(parent)
        self.preset = preset
        self.id = self.preset["preset_id"]
        self.name = self.preset["name"]
        self.last_edited = self.preset["last_edited"]
        
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(7, 10, 7, 10)
        
        self.name_label = ClickableLabel(self, self.name)
        self.name_label.setObjectName("SavedPresetName")
        if glb.ACTIVE_PRESET == self.id:
            self.name_label.setProperty("selected", "True")
        else:
            self.name_label.setProperty("selected", "False")
        self.name_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.name_label.clicked.connect(self.set_active)
        
        self.last_edited_label = QLabel(self, text=self.get_relative_time(self.last_edited))
        self.last_edited_label.setFixedWidth(75)
        self.last_edited_label.setObjectName("SavedPresetEdited")
        self.last_edited_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self._layout.addWidget(self.name_label)
        self._layout.addStretch()
        self._layout.addWidget(self.last_edited_label)
        
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update)
        self.update_timer.start(1000)
    
    def update(self) -> None:
        self.last_edited_label.setText(self.get_relative_time(self.last_edited))
        
    def get_relative_time(self, timestamp: float | None) -> str:
        if timestamp is None:
            return "Not played"
        
        now = datetime.datetime.now()
        past = datetime.datetime.fromtimestamp(timestamp)
        delta = now - past
        
        seconds = int(delta.total_seconds())
        minutes = seconds//60
        hours = minutes//60
        days = delta.days
        
        if seconds < 60:
            relative_time = f"{seconds}s ago"
        elif minutes < 60:
            relative_time = f"{minutes}m ago"
        elif hours < 24:
            relative_time = f"{hours}h ago"
        else:
            relative_time = f"{days}d ago"
        
        return relative_time

    def set_active(self):
        glb.ACTIVE_PRESET = self.id
        match self.window().metaObject().className():
            case "MainWindow":
                parent = "SidebarButton"
            case "Overlay":
                parent = "OverlayButton"
        glb.SIGNAL_MANAGER.presetOpened.emit(self.preset, parent)