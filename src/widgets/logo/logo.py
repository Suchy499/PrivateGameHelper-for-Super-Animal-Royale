from core import *
from images import IMAGES

class Logo(QWidget):
    def __init__(
        self,
        parent: QWidget | None = None,
        h: int = 256
    ):
        super().__init__(parent)
        
        _layout = QHBoxLayout(self)
        _layout.setContentsMargins(0, 0, 0, 0)
        _layout.setSpacing(10)
        
        self.icon = QPixmap(IMAGES[f"icon_{glb.SETTINGS.value("AppIcon", 0)}"]).scaledToHeight(h, Qt.TransformationMode.SmoothTransformation)
        self.icon_label = QLabel(self)
        self.icon_label.setPixmap(self.icon)
        self.icon_label.setFixedSize(self.icon.size())
        
        self.name_container = QWidget(self)
        self.name_layout = QVBoxLayout(self.name_container)
        self.name_layout.setContentsMargins(0, 0, 0, 0)
        self.name_container.setStyleSheet(f"""
            QLabel {{
                font-size: {int(self.icon.height()/3)}px;
                font-family: Rubik;
                font-weight: bold;
                color: white;
            }}
        """)
        self.name_label_1 = QLabel(self.name_container, text="Private")
        self.name_label_2 = QLabel(self.name_container, text="Game")
        self.name_label_3 = QLabel(self.name_container, text="Helper")
        self.name_container.setFixedHeight(self.icon.height())
        self.name_layout.addWidget(self.name_label_1, alignment=Qt.AlignmentFlag.AlignTop)
        self.name_layout.addWidget(self.name_label_2, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.name_layout.addWidget(self.name_label_3, alignment=Qt.AlignmentFlag.AlignBottom)
        
        _layout.addWidget(self.icon_label)
        _layout.addWidget(self.name_container)
    
        glb.SIGNAL_MANAGER.appIconChanged.connect(self.update_icon)
    
    def update_icon(self) -> None:
        self.icon_label.setPixmap(QPixmap(IMAGES[f"icon_{glb.SETTINGS.value("AppIcon", 0)}"]))