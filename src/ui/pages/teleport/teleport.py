from core import *
from .players_list import PlayersList
from images import IMAGES
from widgets import HLine, ClickableLabel, MapWidget, Button

class PageTeleport(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QHBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.page_layout.setSpacing(10)
        self.line_height = 2
        
        self.map_container = QWidget(self)
        self.map_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.map_container_layout = QGridLayout(self.map_container)
        self.map_container_layout.setContentsMargins(0, 0, 0, 0)
        self.map_container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.map_pixmap = QPixmap(IMAGES["sar_map"])
        self.map_image = MapWidget(self.map_container, self.map_pixmap, QSize(432, 432))
        
        self.lmb_container = QWidget(self.map_container)
        self.lmb_container_layout = QHBoxLayout(self.lmb_container)
        self.lmb_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.lmb_pixmap = QPixmap(IMAGES["mouse_lmb"]).scaledToWidth(16, Qt.TransformationMode.SmoothTransformation)
        self.lmb_image = QLabel(self.lmb_container)
        self.lmb_image.setPixmap(self.lmb_pixmap)
        self.lmb_label = QLabel("Teleport selected player", self.lmb_container)
        self.lmb_label.setObjectName("TeleportMouseTip")
        
        self.lmb_container_layout.addWidget(self.lmb_image)
        self.lmb_container_layout.addWidget(self.lmb_label)
        
        self.rmb_container = QWidget(self.map_container)
        self.rmb_container_layout = QHBoxLayout(self.rmb_container)
        self.rmb_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.rmb_pixmap = QPixmap(IMAGES["mouse_rmb"]).scaledToWidth(16, Qt.TransformationMode.SmoothTransformation)
        self.rmb_image = QLabel(self.rmb_container)
        self.rmb_image.setPixmap(self.rmb_pixmap)
        self.rmb_label = QLabel("Copy coordinates", self.rmb_container)
        self.rmb_label.setObjectName("TeleportMouseTip")
        
        self.rmb_container_layout.addWidget(self.rmb_image)
        self.rmb_container_layout.addWidget(self.rmb_label)
        
        self.or_container = QWidget(self)
        self.or_layout = QHBoxLayout(self.or_container)
        self.or_layout.setContentsMargins(0, 0, 0, 0)
        self.left_hline = HLine(self, h=self.line_height)
        self.left_hline.setObjectName("DivLine")
        self.right_hline = HLine(self, h=self.line_height)
        self.right_hline.setObjectName("DivLine")
        self.or_label = QLabel("OR", self)
        self.or_label.setFixedWidth(50)
        self.or_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.or_label.setObjectName("PlayersHeaderName")
        self.or_layout.addWidget(self.left_hline)
        self.or_layout.addWidget(self.or_label)
        self.or_layout.addWidget(self.right_hline)
        
        self.coordinates_label = QLabel(self, text="Coordinates")
        self.coordinates_label.setObjectName("HostIDLabel")
        self.coordinates_label.setContentsMargins(0, 0, 0, 0)
        
        self.coordinates_edit = QLineEdit(self)
        self.coordinates_edit.setFixedWidth(190)
        self.coordinates_edit.setObjectName("LineEdit")
        self.coordinates_edit.setContentsMargins(0, 0, 0, 0)
        self.coordinates_edit.setValidator(QRegularExpressionValidator(r"\d{1,4} \d{1,4}", self))
        self.coordinates_edit.textEdited.connect(lambda: glb.SIGNAL_MANAGER.coordinatesChanged.emit(self.coordinates_edit.text()))
        
        self.teleport_button = Button(self, "Teleport to coordinates", w=190)
        self.teleport_button.clicked.connect(self.teleport_to_coordinates)
        
        self.map_container_layout.addWidget(self.map_image, 0, 0, 1, 2)
        self.map_container_layout.addWidget(self.lmb_container, 1, 0, Qt.AlignmentFlag.AlignCenter)
        self.map_container_layout.addWidget(self.rmb_container, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.map_container_layout.addWidget(self.or_container, 2, 0, 1, 2)
        self.map_container_layout.addWidget(self.coordinates_label, 3, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        self.map_container_layout.addWidget(self.coordinates_edit, 4, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        self.map_container_layout.addWidget(self.teleport_button, 3, 1, 2, 1, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
        self.players_container = QWidget(self)
        self.players_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.players_container_layout = QVBoxLayout(self.players_container)
        self.players_container_layout.setContentsMargins(0, 0, 0, 0)
        self.players_container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.header = QWidget(self.players_container)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(10, 0, 10, 0)
        self.header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.header_name = QLabel(self.header, text="Players")
        self.header_name.setObjectName("PlayersHeaderName")
        
        self.header_all = ClickableLabel(self.header)
        self.header_all.setToolTip("Select All")
        self.header_all_icon = QPixmap(IMAGES["all"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        self.header_all.setPixmap(self.header_all_icon)
        self.header_all.setFixedSize(self.header_all_icon.width() + 9, self.header_all_icon.height() + 9)
        self.header_all.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_all.setContentsMargins(0, 0, 0, 0)
        self.header_all.clicked.connect(select_all_players)
        self.header_all.setObjectName("PlayersHeaderRefresh")
        
        self.header_refresh = ClickableLabel(self.header)
        self.header_refresh.setToolTip("Refresh")
        self.header_refresh_icon = QPixmap(IMAGES["refresh"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        self.header_refresh.setPixmap(self.header_refresh_icon)
        self.header_refresh.setFixedSize(self.header_refresh_icon.width() + 9, self.header_refresh_icon.height() + 9)
        self.header_refresh.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_refresh.setContentsMargins(0, 0, 0, 0)
        self.header_refresh.clicked.connect(read_players)
        self.header_refresh.setObjectName("PlayersHeaderRefresh")
        
        self.header_layout.addWidget(self.header_name)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.header_all)
        self.header_layout.addWidget(self.header_refresh)
        
        self.horizontal_line = HLine(self, h=self.line_height)
        self.horizontal_line.setObjectName("DivLine")
        
        self.scroll_area = QScrollArea(self.players_container)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = PlayersList(self.players_container)
        self.scroll_area.setWidget(self.content_area)
        
        self.players_container_layout.addWidget(self.header)
        self.players_container_layout.addWidget(self.horizontal_line)
        self.players_container_layout.addWidget(self.scroll_area)

        self.page_layout.addWidget(self.map_container)
        self.page_layout.addWidget(self.players_container)
        
        glb.SIGNAL_MANAGER.coordinatesChanged.connect(self.coordinates_edited)
        
    def resizeEvent(self, event):
        self.map_container.setMaximumWidth(self.width() // 2)
        return super().resizeEvent(event)
    
    def coordinates_edited(self, coordinates: str) -> None:
        self.coordinates_edit.setText(coordinates)
    
    def teleport_to_coordinates(self) -> None:
        try:
            x, y = self.coordinates_edit.text().split(" ")
            teleport_player(int(x), int(y))
        except ValueError:
            send_notification("Invalid coordinates", "NotifFail")