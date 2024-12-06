from core.qt_core import *
from .button import Button
from widgets.hline import HLine
from images import IMAGES

class Sidebar(QFrame):
    def __init__(
        self,
        parent: QWidget | None = None
    ):
        super().__init__(parent)
        
        self._max_width = 160
        self._min_width = 61
        self.setObjectName("Sidebar")
        self.setMaximumSize(self._max_width, 9999)
        self.setMinimumSize(self._min_width, 0)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(5, 8, 5, 8)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.hide_pixmap = QPixmap(IMAGES["left_arrow"]).scaledToWidth(13, Qt.TransformationMode.SmoothTransformation)
        self.show_pixmap = QPixmap(IMAGES["right_arrow"]).scaledToWidth(13, Qt.TransformationMode.SmoothTransformation)
        self.expand_button = QPushButton(text="    Hide", parent=self)
        self.expand_button.setObjectName("SidebarButton")
        self.expand_button.setFixedHeight(30)
        self.expand_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.expand_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.expand_button.setIcon(self.hide_pixmap)
        self.expand_button.setIconSize(self.hide_pixmap.size())
        self.expand_button.clicked.connect(self.toggle_animation)
        
        self.hide_line = HLine(self, h=1)
        self.hide_line.setObjectName("SidebarLine")
        
        self._layout.addWidget(self.expand_button)
        self._layout.addWidget(self.hide_line)
        
        self.animation = QPropertyAnimation(self, b"maximumWidth")
    
    def toggle_animation(self) -> None:
        self.animation.stop()
        if self.width() == self._min_width:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._max_width)
            self.expand_button.setIcon(self.hide_pixmap)
        else:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._min_width)
            self.expand_button.setIcon(self.show_pixmap)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.animation.setDuration(500)
        self.animation.start()
        
    def setup_buttons(self, btn_list: list[dict]) -> None:
        self.buttons = {}
        for index, btn in enumerate(btn_list):
            if btn["show_top"]:
                if btn["category"] != btn_list[index-1]["category"] and index > 0:
                    line = HLine(self, h=1)
                    line.setObjectName("SidebarLine")
                    self._layout.addWidget(line)
                button = Button(self, btn["icon"], btn["text"], btn["page"])
                if btn["active"]:
                    button.select()
                self._layout.addWidget(button)
                self.buttons[btn["text"]] = button
        self._layout.addStretch()
        for index, btn in enumerate(btn_list):
            if not btn["show_top"]:
                button = Button(self, btn["icon"], btn["text"], btn["page"])
                if btn["active"]:
                    button.select()
                self._layout.addWidget(button)
                self.buttons[btn["text"]] = button
                try:
                    if btn["category"] != btn_list[index+1]["category"]:
                        line = HLine(self, h=1)
                        line.setObjectName("SidebarLine")
                        self._layout.addWidget(line)
                except IndexError:
                    pass
        
    def deselect_all(self) -> None:
        for btn in self.buttons.values():
            btn.deselect()
    