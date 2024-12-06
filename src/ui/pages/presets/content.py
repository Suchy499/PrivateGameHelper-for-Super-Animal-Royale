from core import *
from .saved_preset import SavedPreset

class Content(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 9, 9)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setObjectName("Content")
        
        self.load_presets()
        
        glb.SIGNAL_MANAGER.presetOpened.connect(self.load_presets)
        glb.SIGNAL_MANAGER.presetsChanged.connect(self.load_presets)
    
    def reset_presets(self) -> None:
        for i in reversed(range(self._layout.count())):
            if self._layout.itemAt(i).widget() is not None:
                widget = self._layout.itemAt(i).widget()
                self._layout.removeWidget(widget)
                widget.deleteLater()
    
    def load_presets(self) -> None:
        self.reset_presets()
        presets_list = read_presets()
        self.saved_presets = []
        for preset in presets_list:
            saved_preset = SavedPreset(self, preset)
            self._layout.addWidget(saved_preset)
            self.saved_presets.append(saved_preset)