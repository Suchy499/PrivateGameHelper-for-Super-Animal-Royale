from core.qt_core import *
from images import IMAGES

class TitleBar(QFrame):
    def __init__(
        self, 
        parent: QWidget | None = None
    ):
        super().__init__(parent)
        
        self.setFixedHeight(32)
        self.setObjectName("TitleBar")
        self.initial_pos = None
        
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(20, 0, 9, 0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        self.title = QLabel(self, text=self.window().windowTitle())
        self.title.setObjectName("Title")
        self.minimize_button = QToolButton(self)
        self.minimize_button.setObjectName("TitleButton")
        self.minimize_pixmap = QPixmap(IMAGES["minimize"]).scaledToHeight(24, Qt.TransformationMode.SmoothTransformation)
        self.minimize_button.setIcon(self.minimize_pixmap)
        self.minimize_button.setFixedSize(self.minimize_pixmap.size())
        self.minimize_button.clicked.connect(self.window().showMinimized)
        self.maximize_button = QToolButton(self)
        self.maximize_button.setObjectName("TitleButton")
        self.maximize_pixmap = QPixmap(IMAGES["maximize"]).scaledToHeight(24, Qt.TransformationMode.SmoothTransformation)
        self.maximize_button.setIcon(self.maximize_pixmap)
        self.maximize_button.setFixedSize(self.maximize_pixmap.size())
        self.maximize_button.clicked.connect(self.window().showMaximized)
        self.normal_button = QToolButton(self)
        self.normal_button.setObjectName("TitleButton")
        self.normal_pixmap = QPixmap(IMAGES["normal"]).scaledToHeight(24, Qt.TransformationMode.SmoothTransformation)
        self.normal_button.setIcon(self.normal_pixmap)
        self.normal_button.setFixedSize(self.normal_pixmap.size())
        self.normal_button.clicked.connect(self.window().showNormal)
        self.normal_button.setVisible(False)
        self.close_button = QToolButton(self)
        self.close_button.setObjectName("TitleButtonClose")
        self.close_pixmap = QPixmap(IMAGES["close"]).scaledToHeight(24, Qt.TransformationMode.SmoothTransformation)
        self.close_button.setIcon(self.close_pixmap)
        self.close_button.setFixedSize(self.close_pixmap.size())
        self.close_button.clicked.connect(self.window().close)
        self._layout.addWidget(self.title)
        self._layout.addStretch()
        self._layout.addWidget(self.minimize_button)
        self._layout.addWidget(self.maximize_button)
        self._layout.addWidget(self.normal_button)
        self._layout.addWidget(self.close_button)
        
        self.window().windowTitleChanged.connect(lambda: self.title.setText(self.window().windowTitle()))
        
    def window_state_changed(self, state):
        if state == Qt.WindowState.WindowMaximized:
            self.normal_button.setVisible(True)
            self.maximize_button.setVisible(False)
        else:
            self.normal_button.setVisible(False)
            self.maximize_button.setVisible(True)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
            self.window_state_changed(self.windowState())
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
    