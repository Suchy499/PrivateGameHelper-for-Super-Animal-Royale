from PySide6.QtWidgets import QFrame, QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import Qt

class UpdaterTitleBar(QFrame):
    def __init__(
        self, 
        parent: QWidget | None = None
    ):
        super().__init__(parent)
        
        self.setFixedHeight(32)
        self.setObjectName("UpdaterTitleBar")
        self.initial_pos = None
        
        self.titlebar_layout = QHBoxLayout(self)
        self.titlebar_layout.setContentsMargins(20, 0, 9, 0)
        self.titlebar_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        self.title = QLabel(self, text=self.window().windowTitle())
        self.title.setObjectName("Title")
        self.titlebar_layout.addWidget(self.title)
        
        self.setText = self.title.setText
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.initial_pos is not None:
            delta = event.position().toPoint() - self.initial_pos
            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y(),
            )
        super().mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.initial_pos = None
        super().mouseReleaseEvent(event)
        event.accept()