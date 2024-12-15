from core import *
from .button import Button
from widgets.hline import HLine
from widgets.vline import VLine

class OverlaySidebar(QFrame):
    def __init__(
        self,
        parent: QWidget | None = None,
        orientation: Qt.Orientation = Qt.Orientation.Vertical,
    ):
        super().__init__(parent)
        self.orientation = orientation
        
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        if self.orientation == Qt.Orientation.Vertical:
            self.sidebar_layout = QVBoxLayout(self)
            self.sidebar_layout.setContentsMargins(5, 8, 5, 8)
            self.sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        else:
            self.sidebar_layout = QHBoxLayout(self)
            self.sidebar_layout.setContentsMargins(8, 5, 8, 5)
            self.sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        self.buttons = []
        
        glb.SIGNAL_MANAGER.overlayClosed.connect(self.deselect_all)
        
    def setup_buttons(self, btn_list: list[dict]) -> None:
        for index, btn in enumerate(btn_list):
            if btn["show_top"]:
                if btn["category"] != btn_list[index-1]["category"] and index > 0:
                    line = HLine(self, h=1) if self.orientation == Qt.Orientation.Vertical else VLine(self, w=1)
                    line.setObjectName("SidebarLine")
                    self.sidebar_layout.addWidget(line)
                button = Button(self, btn["icon"], "", btn["page"], f"OverlayButton", self.orientation)
                button.setToolTip(btn["tooltip"])
                if btn["active"]:
                    button.select("OverlayButton")
                self.sidebar_layout.addWidget(button)
                self.buttons.append(button)
        self.sidebar_layout.addStretch()
        for index, btn in enumerate(btn_list):
            if not btn["show_top"]:
                button = Button(self, btn["icon"], "", btn["page"], f"OverlayButton", self.orientation)
                button.setToolTip(btn["tooltip"])
                if btn["active"]:
                    button.select("OverlayButton")
                self.sidebar_layout.addWidget(button)
                self.buttons.append(button)
                try:
                    if btn["category"] != btn_list[index+1]["category"]:
                        line = HLine(self, h=1) if self.orientation == Qt.Orientation.Vertical else VLine(self, w=1)
                        line.setObjectName("SidebarLine")
                        self.sidebar_layout.addWidget(line)
                except IndexError:
                    pass
        
    def deselect_all(self) -> None:
        for btn in self.buttons:
            btn.deselect()
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return