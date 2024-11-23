from core import *
from .saved_preset import SavedPreset
from widgets import HLine
from images import IMAGES

class Content(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 9, 9)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setObjectName("Content")
        
        self.header = QWidget(self)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(7, 0, 7, 0)
        
        self.header_name = QLabel(self.header, text="Name")
        self.header_name.setObjectName("PresetsHeaderName")
        
        self.header_edited = QLabel(self.header)
        self.header_edited_pixmap = QPixmap(IMAGES["pencil"]).scaledToWidth(24, Qt.TransformationMode.SmoothTransformation)
        self.header_edited.setPixmap(self.header_edited_pixmap)
        self.header_edited.setFixedSize(75, self.header_edited_pixmap.height())
        self.header_edited.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.header_layout.addWidget(self.header_name)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.header_edited)
        
        self.horizontal_line = HLine(self, h=2)
        self.horizontal_line.setObjectName("DivLine")
        
        self.presets_list = QWidget(self)
        self.presets_list_layout = QVBoxLayout(self.presets_list)
        self.presets_list_layout.setContentsMargins(0, 0, 0, 0)
        self.presets_list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self._layout.addWidget(self.header)
        self._layout.addWidget(self.horizontal_line)
        self._layout.addWidget(self.presets_list)
        
        self.load_presets()
        
        Globals.SIGNAL_MANAGER.presetsChanged.connect(self.load_presets)
    
    def reset_presets(self) -> None:
        for i in reversed(range(self.presets_list_layout.count())):
            if self.presets_list_layout.itemAt(i).widget() is not None:
                widget = self.presets_list_layout.itemAt(i).widget()
                self.presets_list_layout.removeWidget(widget)
                widget.deleteLater()
    
    def load_presets(self) -> None:
        self.reset_presets()
        presets_list = read_presets()
        self.saved_presets = []
        for preset in presets_list:
            saved_preset = SavedPreset(self, preset)
            self.presets_list_layout.addWidget(saved_preset)
            self.saved_presets.append(saved_preset)