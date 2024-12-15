from core import *
from .saved_preset import SavedPreset

class Content(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.content_layout = QVBoxLayout(self)
        self.content_layout.setContentsMargins(0, 0, 9, 9)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setObjectName("Content")
        
        self.load_presets()
        
        glb.SIGNAL_MANAGER.presetOpened.connect(self.load_presets)
        glb.SIGNAL_MANAGER.presetDeleted.connect(self.load_presets)
        glb.SIGNAL_MANAGER.presetEdited.connect(self.load_presets)
        glb.SIGNAL_MANAGER.presetSaved.connect(self.load_presets)
        glb.SIGNAL_MANAGER.appStyleChanged.connect(self.load_presets)
        glb.SIGNAL_MANAGER.overlayStyleChanged.connect(self.load_presets)
    
    def reset_presets(self) -> None:
        for i in reversed(range(self.content_layout.count())):
            if self.content_layout.itemAt(i).widget() is not None:
                widget = self.content_layout.itemAt(i).widget()
                self.content_layout.removeWidget(widget)
                widget.deleteLater()
    
    def load_presets(self) -> None:
        self.reset_presets()
        presets_list = read_presets()
        self.saved_presets = []
        for preset in presets_list:
            saved_preset = SavedPreset(self, preset)
            self.content_layout.addWidget(saved_preset)
            self.saved_presets.append(saved_preset)