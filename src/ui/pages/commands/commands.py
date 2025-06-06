from core.qt_core import *
from widgets import Button, HLine

class PageCommands(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        self.page_layout.addWidget(self.scroll_area)
        
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(0, 0, 9, 0)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        
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
        
        self.getplayers_button.setToolTip(
            "Copies a list of all players in the match.\n"
            "After running the command, can be pasted into notepad.\n"
            "At the end of a match, you can use this command to grab the stats of the players."
        )
        
        self.score_button.setToolTip(
            "Copies the stats (placement, kills and time survived) of all players in the match.\n"
            "After running the command, can be pasted into notepad."
        )
        
        self.getpid_button.setToolTip(
            "Shows your in-game player id #."
        )
        
        self.info_container_layout.addWidget(self.getplayers_button)
        self.info_container_layout.addWidget(self.score_button)
        self.info_container_layout.addWidget(self.getpid_button)
        
        self.info_hline = HLine(self, h=self.line_height)
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
        
        self.night_button.setToolTip(
            "Toggles the night mode."
        )
        
        self.rain_button.setToolTip(
            "Forces a rain weather event."
        )
        
        self.rain_off_button.setToolTip(
            "Disables rain for entirity of a match.\n"
            "Won't work if it's already raining in-game."
        )
        
        self.gas_start_button.setToolTip(
            "Makes the first skunk gas timer start right away.\n"
            "(if in lobby, it just means it'll start right when the eagle starts)"
        )
        
        self.environment_container_layout.addWidget(self.night_button)
        self.environment_container_layout.addWidget(self.rain_button)
        self.environment_container_layout.addWidget(self.rain_off_button)
        self.environment_container_layout.addWidget(self.gas_start_button)
        
        self.environment_hline = HLine(self, h=self.line_height)
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
        
        self.boss_button.setToolTip(
            "Spawns a Giant Star-nosed Mole."
        )
        
        self.no_boss_button.setToolTip(
            "Toggle to enable or disable Giant Star-nosed Mole from arriving."
        )
        
        self.svr_container_layout.addWidget(self.boss_button)
        self.svr_container_layout.addWidget(self.no_boss_button)
        
        self.svr_hline = HLine(self, h=self.line_height)
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
        
        self.shotgun_sniper_button.setToolTip(
            "In Mystery Mode, selects the \"Shotguns & Snipers\" game mode."
        )
        
        self.wild_west_button.setToolTip(
            "In Mystery Mode, selects the \"Wild West\" game mode."
        )
        
        self.slow_bullets_button.setToolTip(
            "In Mystery Mode, selects the \"Slow Bullets\" game mode."
        )
        
        self.bananarama_button.setToolTip(
            "In Mystery Mode, selects the \"Bananarama\" game mode."
        )
        
        self.handguns_only_button.setToolTip(
            "In Mystery Mode, selects the \"Handguns Only\" game mode."
        )
        
        self.fast_bullets_button.setToolTip(
            "In Mystery Mode, selects the \"Fast Bullets\" game mode."
        )
        
        self.one_hit_kill_button.setToolTip(
            "In Mystery Mode, selects the \"One Hit Kill\" game mode."
        )
        
        self.mystery_container_layout.addWidget(self.shotgun_sniper_button)
        self.mystery_container_layout.addWidget(self.wild_west_button)
        self.mystery_container_layout.addWidget(self.slow_bullets_button)
        self.mystery_container_layout.addWidget(self.bananarama_button)
        self.mystery_container_layout.addWidget(self.handguns_only_button)
        self.mystery_container_layout.addWidget(self.fast_bullets_button)
        self.mystery_container_layout.addWidget(self.one_hit_kill_button)
        
        self.mystery_hline = HLine(self, h=self.line_height)
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
        
        self.flight_button.setToolTip(
            "Can be used to regenerate the Eagle flight path.\n"
            "Must run before the game timer has started."
        )
        
        self.soccer_button.setToolTip(
            "Spawns a Fox Ball (only 1 at a time)."
        )
        
        self.misc_container_layout.addWidget(self.flight_button)
        self.misc_container_layout.addWidget(self.soccer_button)
        
        self.content_layout.addWidget(self.info_label)
        self.content_layout.addWidget(self.info_container)
        self.content_layout.addWidget(self.info_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.environment_label)
        self.content_layout.addWidget(self.environment_container)
        self.content_layout.addWidget(self.environment_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.svr_label)
        self.content_layout.addWidget(self.svr_container)
        self.content_layout.addWidget(self.svr_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.mystery_label)
        self.content_layout.addWidget(self.mystery_container)
        self.content_layout.addWidget(self.mystery_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.misc_label)
        self.content_layout.addWidget(self.misc_container)