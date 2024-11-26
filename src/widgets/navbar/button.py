from core.qt_core import *
from widgets.clickable_label import ClickableLabel
import styles

class Button(ClickableLabel):
    def __init__(
        self,
        parent: QWidget | None = None, 
        text: str = "",
        page: QWidget | None = None,
        w: int = 100,
        h: int = 30
    ):
        super().__init__(parent)
        self.text = text
        self.page = page
        self.w = w
        self.h = h
        
        self.setObjectName("NavbarButton")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setFixedSize(self.w, self.h)
        self.setText(self.text)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setContentsMargins(0, 0, 0, 0)
        self.clicked.connect(self.select)
        
    def select(self) -> None:
        self.parentWidget().deselect_all()
        self.setObjectName("NavbarButtonActive")
        self.setStyleSheet(styles.default_style)
        if self.page:
            self.page.parentWidget().setCurrentWidget(self.page)
        
    def deselect(self) -> None:
        self.setObjectName("NavbarButton")
        self.setStyleSheet(styles.default_style)