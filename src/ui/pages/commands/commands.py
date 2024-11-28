from core import *
from widgets import Button, HLine

class PageCommands(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(9, 9, 9, 22)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        _layout.addWidget(self.scroll_area)
        
        self._layout = QVBoxLayout(self.content_area)
        self._layout.setContentsMargins(0, 0, 9, 0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_width = 2
        
        self.info_label = QLabel(self.content_area, text="Information")
        self.info_label.setContentsMargins(0, 0, 0, 15)
        self.info_label.setObjectName("ItemsHeaderName")
        
        self.info_container = QWidget(self.content_area)
        self.info_container_layout = QHBoxLayout(self.info_container)
        self.info_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.info_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.getplayers_button = Button(self.info_container, "/getplayers", w=125, command="getplayers")
        self.score_button = Button(self.info_container, "/score", w=125, command="score")
        self.getpid_button = Button(self.info_container, "/getpid", w=125, command="getpid")
        
        self.info_container_layout.addWidget(self.getplayers_button)
        self.info_container_layout.addWidget(self.score_button)
        self.info_container_layout.addWidget(self.getpid_button)
        
        self.info_hline = HLine(self, h=self.line_width)
        self.info_hline.setObjectName("DivLine")
        
        self.environment_label = QLabel(self.content_area, text="Environment")
        self.environment_label.setContentsMargins(0, 0, 0, 15)
        self.environment_label.setObjectName("ItemsHeaderName")
        
        self.environment_container = QWidget(self.content_area)
        self.environment_container_layout = QHBoxLayout(self.environment_container)
        self.environment_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.environment_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.night_button = Button(self.environment_container, "/night", w=125, command="night")
        self.rain_button = Button(self.environment_container, "/rain", w=125, command="rain")
        self.rain_off_button = Button(self.environment_container, "/rainoff", w=125, command="rainoff")
        self.gas_start_button = Button(self.environment_container, "/gasstart", w=125, command="gasstart")
        
        self.environment_container_layout.addWidget(self.night_button)
        self.environment_container_layout.addWidget(self.rain_button)
        self.environment_container_layout.addWidget(self.rain_off_button)
        self.environment_container_layout.addWidget(self.gas_start_button)
        
        self.environment_hline = HLine(self, h=self.line_width)
        self.environment_hline.setObjectName("DivLine")
        
        self.svr_label = QLabel(self.content_area, text="S.A.W. vs Rebellion")
        self.svr_label.setContentsMargins(0, 0, 0, 15)
        self.svr_label.setObjectName("ItemsHeaderName")
        
        self.svr_container = QWidget(self.content_area)
        self.svr_container_layout = QHBoxLayout(self.svr_container)
        self.svr_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.svr_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.boss_button = Button(self.svr_container, "/boss", w=125, command="boss")
        self.no_boss_button = Button(self.svr_container, "/noboss", w=125, command="noboss")
        
        self.svr_container_layout.addWidget(self.boss_button)
        self.svr_container_layout.addWidget(self.no_boss_button)
        
        self.svr_hline = HLine(self, h=self.line_width)
        self.svr_hline.setObjectName("DivLine")
        
        self.mystery_label = QLabel(self.content_area, text="Mystery Mode")
        self.mystery_label.setContentsMargins(0, 0, 0, 15)
        self.mystery_label.setObjectName("ItemsHeaderName")
        
        self.mystery_container = QWidget(self.content_area)
        self.mystery_container_layout = QHBoxLayout(self.mystery_container)
        self.mystery_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.mystery_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.shotgun_sniper_button = Button(self.mystery_container, "Shotguns Snipers", w=125, command="mystery 0")
        self.wild_west_button = Button(self.mystery_container, "Wild West", w=125, command="mystery 1")
        self.slow_bullets_button = Button(self.mystery_container, "Slow Bullets", w=125, command="mystery 2")
        self.bananarama_button = Button(self.mystery_container, "Bananarama", w=125, command="mystery 3")
        self.handguns_only_button = Button(self.mystery_container, "Handguns Only", w=125, command="mystery 4")
        self.fast_bullets_button = Button(self.mystery_container, "Fast Bullets", w=125, command="mystery 5")
        self.one_hit_kill_button = Button(self.mystery_container, "One Hit Kill", w=125, command="mystery 6")
        
        self.mystery_container_layout.addWidget(self.shotgun_sniper_button)
        self.mystery_container_layout.addWidget(self.wild_west_button)
        self.mystery_container_layout.addWidget(self.slow_bullets_button)
        self.mystery_container_layout.addWidget(self.bananarama_button)
        self.mystery_container_layout.addWidget(self.handguns_only_button)
        self.mystery_container_layout.addWidget(self.fast_bullets_button)
        self.mystery_container_layout.addWidget(self.one_hit_kill_button)
        
        self.mystery_hline = HLine(self, h=self.line_width)
        self.mystery_hline.setObjectName("DivLine")
        
        self.misc_label = QLabel(self.content_area, text="Miscellaneous")
        self.misc_label.setContentsMargins(0, 0, 0, 15)
        self.misc_label.setObjectName("ItemsHeaderName")
        
        self.misc_container = QWidget(self.content_area)
        self.misc_container_layout = QHBoxLayout(self.misc_container)
        self.misc_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.misc_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.flight_button = Button(self.misc_container, "/flight", w=125, command="flight")
        self.soccer_button = Button(self.misc_container, "/soccer", w=125, command="soccer")
        
        self.misc_container_layout.addWidget(self.flight_button)
        self.misc_container_layout.addWidget(self.soccer_button)
        
        self._layout.addWidget(self.info_label)
        self._layout.addWidget(self.info_container)
        self._layout.addWidget(self.info_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.environment_label)
        self._layout.addWidget(self.environment_container)
        self._layout.addWidget(self.environment_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.svr_label)
        self._layout.addWidget(self.svr_container)
        self._layout.addWidget(self.svr_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.mystery_label)
        self._layout.addWidget(self.mystery_container)
        self._layout.addWidget(self.mystery_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.misc_label)
        self._layout.addWidget(self.misc_container)