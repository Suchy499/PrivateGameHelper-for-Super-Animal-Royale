from core import *
import pyperclip

class MapWidget(QLabel):
    def __init__(
        self,
        parent: QWidget | None = None,
        p_map: QPixmap | None = None,
        initial_size: QSize | None = None
    ):
        super().__init__(parent=parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setMouseTracking(True)
        self._pixmap: QPixmap | None = p_map
        self.setStyleSheet("""
            border: 1px solid transparent;
        """)
        if initial_size:
            self._init_pixmap = self._pixmap.scaled(
                initial_size, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            )
            super().setPixmap(self._init_pixmap)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
    def scaledPixmap(self) -> QPixmap:
        scaled = self._pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        return scaled
    
    def setPixmap(self, pixmap: QPixmap) -> None:
        self._pixmap = pixmap
        super().setPixmap(pixmap)
    
    def resizeEvent(self, event) -> None:
        if self._pixmap is not None:
            super().setPixmap(self.scaledPixmap())
            self.setAlignment(Qt.AlignCenter)
    
    def mouseReleaseEvent(self, ev):
        x, y = self.get_coordinates(ev)
        match ev.button():
            case Qt.MouseButton.LeftButton:
                teleport_player(x, y)
            case Qt.MouseButton.RightButton:
                pyperclip.copy(f"{x} {y}")
                send_notification("Coordinates copied to clipboard")
                if self.window().metaObject().className() == "Overlay":
                    open_window("Super Animal Royale")
            case _:
                pass
        return super().mouseReleaseEvent(ev)
    
    def mouseMoveEvent(self, ev):
        x, y = self.get_coordinates(ev)
        QToolTip.showText(ev.globalPos(), f"{x} {y}", self, msecShowTime=0)
        return super().mouseMoveEvent(ev)
    
    def get_coordinates(self, ev: QMouseEvent) -> tuple[int, int]:
        width = self.width()
        scale = 4608 / width
        x = int(ev.position().x() * scale)
        y = int((width - ev.position().y()) * scale)
        return x, y
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return