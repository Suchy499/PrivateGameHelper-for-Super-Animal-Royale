from core.qt_core import *
from .content import Content
from widgets import HLine
from images import IMAGES

class Presets(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(9, 9, 9, 22)
        
        self.header = QWidget(self)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(10, 0, 40, 0)
        
        self.header_name = QLabel(self.header, text="Name")
        self.header_name.setObjectName("PresetsHeaderName")
        
        self.header_edited = QLabel(self.header)
        self.header_edited_pixmap = QPixmap(IMAGES["pencil"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        self.header_edited.setPixmap(self.header_edited_pixmap)
        self.header_edited.setFixedSize(self.header_edited_pixmap.size())
        self.header_edited.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.header_layout.addWidget(self.header_name)
        self.header_layout.addWidget(self.header_edited, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.horizontal_line = HLine(self, h=2)
        self.horizontal_line.setObjectName("DivLine")
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = Content(self)
        self.scroll_area.setWidget(self.content_area)
        
        _layout.addWidget(self.header)
        _layout.addWidget(self.horizontal_line)
        _layout.addWidget(self.scroll_area)
        