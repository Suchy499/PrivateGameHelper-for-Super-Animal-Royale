from core.qt_core import *
import styles

class Button(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None, 
        icon: str | None = None,
        text: str = "",
        page: QWidget | None = None
    ):
        super().__init__(parent)
        self.icon = icon
        self.text = text
        self.page = page
        
        self.setObjectName("SidebarButton")
        self.setFixedHeight(30)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if self.icon is not None:
            self.icon_pixmap = QPixmap(self.icon).scaledToWidth(13, Qt.TransformationMode.SmoothTransformation)
            self.setIcon(self.icon_pixmap)
            self.setIconSize(self.icon_pixmap.size())
        self.setText(f"    {self.text}")
        self.clicked.connect(self.select)
        
    def select(self) -> None:
        self.parentWidget().deselect_all()
        self.setObjectName("SidebarButtonActive")
        self.setStyleSheet(styles.default_style)
        if self.page:
            self.page.parentWidget().setCurrentWidget(self.page)
        
    def deselect(self) -> None:
        self.setObjectName("SidebarButton")
        self.setStyleSheet(styles.default_style)