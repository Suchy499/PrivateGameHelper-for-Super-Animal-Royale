from core import *
from widgets import HLine, WeaponSelect, ClickableLabel
from images import IMAGES

class Weapons(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(0, 0, 0, 0)
        _layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.label = QLabel("Weapon Selection")
        self.label.setObjectName("ItemsHeaderName")
        
        self.header = QWidget(self)
        self.header_layout = QGridLayout(self.header)
        self.header_layout.setContentsMargins(9, 9, 19, 0)
        self.header_layout.setHorizontalSpacing(50)
        self.header_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        self.deselect_icon = QPixmap(IMAGES["deselect_all"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        self.select_icon = QPixmap(IMAGES["select_all"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        
        self.team_a_container = QWidget(self.header)
        self.team_a_container_layout = QHBoxLayout(self.team_a_container)
        self.team_a_container_layout.setContentsMargins(9, 0, 9, 0)
        
        self.team_a_label = QLabel(self.header, text="Team A")
        self.team_a_label.setObjectName("PlayersHeaderName")
        
        self.team_a_deselect_button = ClickableLabel(self)
        self.team_a_deselect_button.setToolTip("Disable all")
        self.team_a_deselect_button.setPixmap(self.deselect_icon)
        self.team_a_deselect_button.setFixedSize(self.deselect_icon.width() + 9, self.deselect_icon.height() + 9)
        self.team_a_deselect_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.team_a_deselect_button.setContentsMargins(0, 0, 0, 0)
        self.team_a_deselect_button.setObjectName("PlayersHeaderRefresh")
        self.team_a_deselect_button.clicked.connect(lambda: glb.SIGNAL_MANAGER.weaponSelectedAll.emit("a", False))
        
        self.team_a_select_button = ClickableLabel(self)
        self.team_a_select_button.setToolTip("Enable all")
        self.team_a_select_button.setPixmap(self.select_icon)
        self.team_a_select_button.setFixedSize(self.select_icon.width() + 9, self.select_icon.height() + 9)
        self.team_a_select_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.team_a_select_button.setContentsMargins(0, 0, 0, 0)
        self.team_a_select_button.setObjectName("PlayersHeaderRefresh")
        self.team_a_select_button.clicked.connect(lambda: glb.SIGNAL_MANAGER.weaponSelectedAll.emit("a", True))
        
        self.team_a_container_layout.addWidget(self.team_a_label)
        self.team_a_container_layout.addStretch()
        self.team_a_container_layout.addWidget(self.team_a_deselect_button)
        self.team_a_container_layout.addWidget(self.team_a_select_button)
        
        self.team_b_container = QWidget(self.header)
        self.team_b_container_layout = QHBoxLayout(self.team_b_container)
        self.team_b_container_layout.setContentsMargins(9, 0, 9, 0)
        
        self.team_b_label = QLabel(self.header, text="Team B")
        self.team_b_label.setObjectName("PlayersHeaderName")
        
        self.team_b_deselect_button = ClickableLabel(self)
        self.team_b_deselect_button.setToolTip("Disable all")
        self.team_b_deselect_button.setPixmap(self.deselect_icon)
        self.team_b_deselect_button.setFixedSize(self.deselect_icon.width() + 9, self.deselect_icon.height() + 9)
        self.team_b_deselect_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.team_b_deselect_button.setContentsMargins(0, 0, 0, 0)
        self.team_b_deselect_button.setObjectName("PlayersHeaderRefresh")
        self.team_b_deselect_button.clicked.connect(lambda: glb.SIGNAL_MANAGER.weaponSelectedAll.emit("b", False))
        
        self.team_b_select_button = ClickableLabel(self)
        self.team_b_select_button.setToolTip("Enable all")
        self.team_b_select_button.setPixmap(self.select_icon)
        self.team_b_select_button.setFixedSize(self.select_icon.width() + 9, self.select_icon.height() + 9)
        self.team_b_select_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.team_b_select_button.setContentsMargins(0, 0, 0, 0)
        self.team_b_select_button.setObjectName("PlayersHeaderRefresh")
        self.team_b_select_button.clicked.connect(lambda: glb.SIGNAL_MANAGER.weaponSelectedAll.emit("b", True))
        
        self.team_b_container_layout.addWidget(self.team_b_label)
        self.team_b_container_layout.addStretch()
        self.team_b_container_layout.addWidget(self.team_b_deselect_button)
        self.team_b_container_layout.addWidget(self.team_b_select_button)
        
        self.team_a_hline = HLine(self.header, h=self.line_height)
        self.team_a_hline.setObjectName("DivLine")
        
        self.team_b_hline = HLine(self.header, h=self.line_height)
        self.team_b_hline.setObjectName("DivLine")
        
        self.header_layout.addWidget(self.team_a_container, 0, 0)
        self.header_layout.addWidget(self.team_b_container, 0, 1)
        self.header_layout.addWidget(self.team_a_hline, 1, 0)
        self.header_layout.addWidget(self.team_b_hline, 1, 1)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        
        self.scroll_layout = QHBoxLayout(self.content_area)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(50)
        
        self.team_a_players = QWidget(self.content_area)
        self.team_a_players_layout = QGridLayout(self.team_a_players)
        self.team_a_players_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.team_a_players_layout.setContentsMargins(9, 9, 9, 9)
        
        self.team_b_players = QWidget(self.content_area)
        self.team_b_players_layout = QGridLayout(self.team_b_players)
        self.team_b_players_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.team_b_players_layout.setContentsMargins(9, 9, 19, 9)
        
        self.scroll_layout.addWidget(self.team_a_players)
        self.scroll_layout.addWidget(self.team_b_players)
        
        self.set_columns_width()
        
        _buttons_a = [
            WeaponSelect(self.content_area, QPixmap(IMAGES["pistol_color"]), 0, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["dualies_color"]), 1, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["magnum_color"]), 2, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["deagle_color"]), 3, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["silenced_pistol_color"]), 4, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["shotgun_color"]), 5, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["jag7_color"]), 6, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["smg_color"]), 7, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["tommy_gun_color"]), 8, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["ak_color"]), 9, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["m16_color"]), 10, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["dart_gun_color"]), 11, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["dartfly_gun_color"]), 12, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["hunting_rifle_color"]), 13, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["sniper_color"]), 14, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["superite_laser_color"]), 15, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["minigun_color"]), 16, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["bow_color"]), 17, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["sparrow_launcher_color"]), 18, "a"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["bcg_color"]), 19, "a"),
        ]
        
        _buttons_b = [
            WeaponSelect(self.content_area, QPixmap(IMAGES["pistol_color"]), 0, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["dualies_color"]), 1, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["magnum_color"]), 2, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["deagle_color"]), 3, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["silenced_pistol_color"]), 4, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["shotgun_color"]), 5, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["jag7_color"]), 6, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["smg_color"]), 7, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["tommy_gun_color"]), 8, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["ak_color"]), 9, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["m16_color"]), 10, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["dart_gun_color"]), 11, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["dartfly_gun_color"]), 12, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["hunting_rifle_color"]), 13, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["sniper_color"]), 14, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["superite_laser_color"]), 15, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["minigun_color"]), 16, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["bow_color"]), 17, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["sparrow_launcher_color"]), 18, "b"),
            WeaponSelect(self.content_area, QPixmap(IMAGES["bcg_color"]), 19, "b"),
        ]
        
        _layout.addWidget(self.label)
        _layout.addWidget(self.header)
        _layout.addWidget(self.scroll_area)
        for index, button in enumerate(_buttons_a):
            row = index // 4
            col = index % 4
            button_container = QWidget(self.content_area)
            button_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            button_layout = QHBoxLayout(button_container)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            button_layout.addWidget(button)
            self.team_a_players_layout.addWidget(button_container, row, col)
            
        for index, button in enumerate(_buttons_b):
            row = index // 4
            col = index % 4
            button_container = QWidget(self.content_area)
            button_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            button_layout = QHBoxLayout(button_container)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            button_layout.addWidget(button)
            self.team_b_players_layout.addWidget(button_container, row, col)
        
    def resizeEvent(self, event):
        self.set_columns_width()
        return super().resizeEvent(event)
    
    def set_columns_width(self) -> None:
        scroll_width = self.scroll_area.width()
        spacing = self.scroll_layout.spacing()
        col_width = (scroll_width - spacing) / 2
        self.team_a_players.setFixedWidth(col_width)
        self.team_b_players.setFixedWidth(col_width)