from core import *
from styles import Style
from typing import Literal

class Button(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None, 
        icon: str | None = None,
        text: str = "",
        page: QWidget | None = None,
        style_name: Literal["SidebarButton", "OverlayButton"] = "SidebarButton",
        orientation: Qt.Orientation = Qt.Orientation.Vertical
    ):
        super().__init__(parent)
        self.icon = icon
        self.text = text
        self.page = page
        self.style_name = style_name
        
        self.setObjectName(self.style_name)
        if orientation == Qt.Orientation.Vertical:
            self.setFixedHeight(30)
            self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        else:
            self.setFixedWidth(39)
            self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        
        if self.style_name == "OverlayButton":
            self.overlay = get_main_overlay()
        else:
            self.overlay = None
            
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if self.icon is not None:
            self.icon_pixmap = QPixmap(self.icon).scaledToWidth(13, Qt.TransformationMode.SmoothTransformation)
            self.setIcon(self.icon_pixmap)
            self.setIconSize(self.icon_pixmap.size())
        if self.text != "":
            self.setText(f"     {self.text}")
        self.clicked.connect(lambda: glb.SIGNAL_MANAGER.pageChanged.emit(self.page, self.style_name))
    
        glb.SIGNAL_MANAGER.pageChanged.connect(self.recieve_signal)
        glb.SIGNAL_MANAGER.presetOpened.connect(self.open_preset)
        glb.SIGNAL_MANAGER.appStyleChanged.connect(self.style_changed)
        glb.SIGNAL_MANAGER.overlayStyleChanged.connect(self.style_changed)
    
    def recieve_signal(self, page, parent) -> None:
        if page.metaObject().className() == self.page.metaObject().className():
            self.select(parent)
    
    def open_preset(self, preset, parent) -> None:
        if self.page.metaObject().className() == "PagePregame":
            self.select(parent)
    
    def select(self, parent) -> None:
        if self.overlay and not self.overlay.isVisible() and parent == "SidebarButton":
            return
        self.parentWidget().deselect_all()
        self.setProperty("selected", "True")
        self.style_changed()
        if self.page and self.page.parentWidget().currentWidget() != self.page:
            self.page.parentWidget().setCurrentWidget(self.page)
        if self.overlay and not self.overlay.isVisible() and parent == "OverlayButton":
            self.overlay.setVisible(True)
        if self.overlay and self.overlay.isVisible() and parent == "OverlayButton":
            open_window("Super Animal Royale")
        
    def deselect(self) -> None:
        self.setProperty("selected", "False")
        self.style_changed()
    
    def style_changed(self) -> None:
        if self.style_name == "SidebarButton":
            self.setStyleSheet(Style.getValue(glb.SETTINGS.value("AppStyle", 0)))
        elif self.style_name == "OverlayButton":
            self.setStyleSheet(Style.getValue(glb.SETTINGS.value("OverlayStyle", 0)))
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return