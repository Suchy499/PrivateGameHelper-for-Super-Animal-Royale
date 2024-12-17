from core import *
from widgets import SettingsComboBox, HLine, KeybindEdit, LabeledToggle, FlowLayout, LabeledSlider, Button
from images import IMAGES

class PageSettings(QWidget):
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
        
        self.display_label = QLabel(self, text="Display")
        self.display_label.setContentsMargins(0, 0, 0, 15)
        self.display_label.setObjectName("PregameHeaderName")
        
        self.display_mode = SettingsComboBox(self, "Display Mode", "DisplayMode")
        self.display_mode.setContentsMargins(10, 0, 0, 15)
        self.overlay_position = SettingsComboBox(self, "Overlay Position", "OverlayPosition")
        self.overlay_position.setContentsMargins(10, 0, 0, 15)
        
        if self.window().metaObject().className() == "Overlay":
            self.close_container = QWidget(self)
            self.close_layout = QHBoxLayout(self.close_container)
            self.close_layout.setContentsMargins(10, 0, 0, 15)
            self.close_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.close_pixmap = QPixmap(IMAGES["close"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
            self.close_button = Button(self, "  Close app", self.close_pixmap, w=120)
            self.close_button.clicked.connect(QApplication.exit)
            self.close_layout.addWidget(self.close_button)
        
        self.display_hline = HLine(self, h=self.line_height)
        self.display_hline.setObjectName("DivLine")
        self.display_hline.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        
        self.keybinds_label = QLabel(self, text="Keybinds")
        self.keybinds_label.setContentsMargins(0, 0, 0, 15)
        self.keybinds_label.setObjectName("PregameHeaderName")
        
        self.stop_commands_label = QLabel("Abort sending commands", self)
        self.stop_commands_label.setContentsMargins(10, 0, 0, 0)
        self.stop_commands_label.setObjectName("HostIDLabel")
        self.stop_commands = KeybindEdit(self, "Abort", "Alt+Shift+Q", 211)
        self.stop_commands.setContentsMargins(10, 0, 0, 15)
        
        self.keybinds_hline = HLine(self, h=self.line_height)
        self.keybinds_hline.setObjectName("DivLine")
        self.keybinds_hline.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        
        self.other_label = QLabel(self, text="Other")
        self.other_label.setContentsMargins(0, 0, 0, 15)
        self.other_label.setObjectName("PregameHeaderName")
        
        self.other_container = QWidget(self)
        self.other_layout = QHBoxLayout(self.other_container)
        self.other_layout.setContentsMargins(10, 0, 0, 15)
        self.other_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.other_layout.setSpacing(40)
        
        self.enable_ocr = LabeledToggle(self, text="Enable OCR checks", default_state=True)
        self.enable_ocr.setContentsMargins(0, 15, 0, 0)
        self.enable_ocr.stateChanged.connect(self.ocr_enabled)
        self.enable_ocr.setToolTip(
            "OCR checks if your chatbox or pause menu is open before sending commands.\n"
            "This helps prevent unwanted inputs, however, it isn't perfect.\n"
            "If you're experiencing issues running certain commands, consider disabling this setting."
        )
        
        self.use_clipboard = LabeledToggle(self, text="Use Clipboard", default_state=True)
        self.use_clipboard.setContentsMargins(0, 15, 0, 0)
        self.use_clipboard.stateChanged.connect(self.clipboard_enabled)
        self.use_clipboard.setToolTip(
            "Use system clipboard to paste commands into SAR chat.\n"
            "Disabling this setting will significantly slow down the input process."
        )
        
        self.command_input_speed = LabeledSlider(
            self, 
            min_value=1,
            max_value=5,
            step=1, 
            default_value=3, 
            text="Command Input Speed", 
            text_type="int",
            enum=CommandSpeed,
            width=290,
            value_text_width=70
        )
        self.command_input_speed.valueChanged.connect(self.command_speed_changed)
        
        self.other_layout.addWidget(self.enable_ocr)
        self.other_layout.addWidget(self.use_clipboard)
        self.other_layout.addWidget(self.command_input_speed)
        
        self.other_hline = HLine(self, h=self.line_height)
        self.other_hline.setObjectName("DivLine")
        self.other_hline.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        
        self.themes_label = QLabel(self, text="Themes")
        self.themes_label.setContentsMargins(0, 0, 0, 15)
        self.themes_label.setObjectName("PregameHeaderName")
        
        self.app_theme_label = QLabel("App theme", self)
        self.app_theme_label.setContentsMargins(10, 0, 0, 0)
        self.app_theme_label.setObjectName("HostIDLabel")
        
        self.app_themes_container = QWidget(self)
        self.app_themes_container.setContentsMargins(10, 0, 0, 0)
        self.app_themes_container.setObjectName("ThemesContainer")
        self.app_themes_layout = FlowLayout(self.app_themes_container)
        self.app_themes_layout.setContentsMargins(0, 0, 0, 0)
        self.app_themes_layout.setSpacing(20)
        
        self.purple_theme = QRadioButton(self.app_themes_container)
        self.purple_theme.setFixedSize(80, 80)
        self.purple_theme.setObjectName("ThemePurple")
        self.purple_theme.setToolTip("Purple")
        self.purple_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.purple_theme.clicked.connect(lambda: self.select_app_style(0))
        
        self.dark_theme = QRadioButton(self.app_themes_container)
        self.dark_theme.setFixedSize(80, 80)
        self.dark_theme.setObjectName("ThemeDark")
        self.dark_theme.setToolTip("Dark")
        self.dark_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dark_theme.clicked.connect(lambda: self.select_app_style(1))
        
        self.blue_theme = QRadioButton(self.app_themes_container)
        self.blue_theme.setFixedSize(80, 80)
        self.blue_theme.setObjectName("ThemeBlue")
        self.blue_theme.setToolTip("Blue")
        self.blue_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.blue_theme.clicked.connect(lambda: self.select_app_style(2))
        
        self.purple_sky_theme = QRadioButton(self.app_themes_container)
        self.purple_sky_theme.setFixedSize(80, 80)
        self.purple_sky_theme.setObjectName("ThemePurpleSky")
        self.purple_sky_theme.setToolTip("Purple Sky")
        self.purple_sky_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.purple_sky_theme.clicked.connect(lambda: self.select_app_style(3))
        
        self.cotton_candy_theme = QRadioButton(self.app_themes_container)
        self.cotton_candy_theme.setFixedSize(80, 80)
        self.cotton_candy_theme.setObjectName("ThemeCottonCandy")
        self.cotton_candy_theme.setToolTip("Cotton Candy")
        self.cotton_candy_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cotton_candy_theme.clicked.connect(lambda: self.select_app_style(4))
        
        self.aqua_theme = QRadioButton(self.app_themes_container)
        self.aqua_theme.setFixedSize(80, 80)
        self.aqua_theme.setObjectName("ThemeAqua")
        self.aqua_theme.setToolTip("Aqua")
        self.aqua_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.aqua_theme.clicked.connect(lambda: self.select_app_style(5))
        
        self.nebula_theme = QRadioButton(self.app_themes_container)
        self.nebula_theme.setFixedSize(80, 80)
        self.nebula_theme.setObjectName("ThemeNebula")
        self.nebula_theme.setToolTip("Nebula")
        self.nebula_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nebula_theme.clicked.connect(lambda: self.select_app_style(6))
        
        self.void_theme = QRadioButton(self.app_themes_container)
        self.void_theme.setFixedSize(80, 80)
        self.void_theme.setObjectName("ThemeVoid")
        self.void_theme.setToolTip("Void")
        self.void_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.void_theme.clicked.connect(lambda: self.select_app_style(7))
        
        self.sunrise_theme = QRadioButton(self.app_themes_container)
        self.sunrise_theme.setFixedSize(80, 80)
        self.sunrise_theme.setObjectName("ThemeSunrise")
        self.sunrise_theme.setToolTip("Sunrise")
        self.sunrise_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sunrise_theme.clicked.connect(lambda: self.select_app_style(8))
        
        self.vaporwave_theme = QRadioButton(self.app_themes_container)
        self.vaporwave_theme.setFixedSize(80, 80)
        self.vaporwave_theme.setObjectName("ThemeVaporwave")
        self.vaporwave_theme.setToolTip("Vaporwave")
        self.vaporwave_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.vaporwave_theme.clicked.connect(lambda: self.select_app_style(9))
        
        self.black_and_white_theme = QRadioButton(self.app_themes_container)
        self.black_and_white_theme.setFixedSize(80, 80)
        self.black_and_white_theme.setObjectName("ThemeBlackAndWhite")
        self.black_and_white_theme.setToolTip("Black And White")
        self.black_and_white_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.black_and_white_theme.clicked.connect(lambda: self.select_app_style(10))
        
        self.app_themes_layout.addWidget(self.purple_theme)
        self.app_themes_layout.addWidget(self.dark_theme)
        self.app_themes_layout.addWidget(self.blue_theme)
        self.app_themes_layout.addWidget(self.purple_sky_theme)
        self.app_themes_layout.addWidget(self.cotton_candy_theme)
        self.app_themes_layout.addWidget(self.aqua_theme)
        self.app_themes_layout.addWidget(self.nebula_theme)
        self.app_themes_layout.addWidget(self.void_theme)
        self.app_themes_layout.addWidget(self.sunrise_theme)
        self.app_themes_layout.addWidget(self.vaporwave_theme)
        self.app_themes_layout.addWidget(self.black_and_white_theme)
        
        self.overlay_theme_label = QLabel("Overlay theme", self)
        self.overlay_theme_label.setContentsMargins(10, 15, 0, 0)
        self.overlay_theme_label.setObjectName("HostIDLabel")
        
        self.overlay_themes_container = QWidget(self)
        self.overlay_themes_container.setContentsMargins(10, 0, 0, 0)
        self.overlay_themes_container.setObjectName("ThemesContainer")
        self.overlay_themes_layout = FlowLayout(self.overlay_themes_container)
        self.overlay_themes_layout.setContentsMargins(0, 0, 0, 0)
        self.overlay_themes_layout.setSpacing(20)
        
        self.overlay_purple_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_purple_theme.setFixedSize(80, 80)
        self.overlay_purple_theme.setObjectName("ThemePurple")
        self.overlay_purple_theme.setToolTip("Purple")
        self.overlay_purple_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_purple_theme.clicked.connect(lambda: self.select_overlay_style(0))
        
        self.overlay_dark_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_dark_theme.setFixedSize(80, 80)
        self.overlay_dark_theme.setObjectName("ThemeDark")
        self.overlay_dark_theme.setToolTip("Dark")
        self.overlay_dark_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_dark_theme.clicked.connect(lambda: self.select_overlay_style(1))
        
        self.overlay_blue_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_blue_theme.setFixedSize(80, 80)
        self.overlay_blue_theme.setObjectName("ThemeBlue")
        self.overlay_blue_theme.setToolTip("Blue")
        self.overlay_blue_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_blue_theme.clicked.connect(lambda: self.select_overlay_style(2))
        
        self.overlay_purple_sky_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_purple_sky_theme.setFixedSize(80, 80)
        self.overlay_purple_sky_theme.setObjectName("ThemePurpleSky")
        self.overlay_purple_sky_theme.setToolTip("Purple Sky")
        self.overlay_purple_sky_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_purple_sky_theme.clicked.connect(lambda: self.select_overlay_style(3))
        
        self.overlay_cotton_candy_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_cotton_candy_theme.setFixedSize(80, 80)
        self.overlay_cotton_candy_theme.setObjectName("ThemeCottonCandy")
        self.overlay_cotton_candy_theme.setToolTip("Cotton Candy")
        self.overlay_cotton_candy_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_cotton_candy_theme.clicked.connect(lambda: self.select_overlay_style(4))
        
        self.overlay_aqua_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_aqua_theme.setFixedSize(80, 80)
        self.overlay_aqua_theme.setObjectName("ThemeAqua")
        self.overlay_aqua_theme.setToolTip("Aqua")
        self.overlay_aqua_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_aqua_theme.clicked.connect(lambda: self.select_overlay_style(5))
        
        self.overlay_nebula_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_nebula_theme.setFixedSize(80, 80)
        self.overlay_nebula_theme.setObjectName("ThemeNebula")
        self.overlay_nebula_theme.setToolTip("Nebula")
        self.overlay_nebula_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_nebula_theme.clicked.connect(lambda: self.select_overlay_style(6))
        
        self.overlay_void_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_void_theme.setFixedSize(80, 80)
        self.overlay_void_theme.setObjectName("ThemeVoid")
        self.overlay_void_theme.setToolTip("Void")
        self.overlay_void_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_void_theme.clicked.connect(lambda: self.select_overlay_style(7))
        
        self.overlay_sunrise_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_sunrise_theme.setFixedSize(80, 80)
        self.overlay_sunrise_theme.setObjectName("ThemeSunrise")
        self.overlay_sunrise_theme.setToolTip("Sunrise")
        self.overlay_sunrise_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_sunrise_theme.clicked.connect(lambda: self.select_overlay_style(8))
        
        self.overlay_vaporwave_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_vaporwave_theme.setFixedSize(80, 80)
        self.overlay_vaporwave_theme.setObjectName("ThemeVaporwave")
        self.overlay_vaporwave_theme.setToolTip("Vaporwave")
        self.overlay_vaporwave_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_vaporwave_theme.clicked.connect(lambda: self.select_overlay_style(9))
        
        self.overlay_black_and_white_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_black_and_white_theme.setFixedSize(80, 80)
        self.overlay_black_and_white_theme.setObjectName("ThemeBlackAndWhite")
        self.overlay_black_and_white_theme.setToolTip("Black And White")
        self.overlay_black_and_white_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_black_and_white_theme.clicked.connect(lambda: self.select_overlay_style(10))
        
        self.overlay_themes_layout.addWidget(self.overlay_purple_theme)
        self.overlay_themes_layout.addWidget(self.overlay_dark_theme)
        self.overlay_themes_layout.addWidget(self.overlay_blue_theme)
        self.overlay_themes_layout.addWidget(self.overlay_purple_sky_theme)
        self.overlay_themes_layout.addWidget(self.overlay_cotton_candy_theme)
        self.overlay_themes_layout.addWidget(self.overlay_aqua_theme)
        self.overlay_themes_layout.addWidget(self.overlay_nebula_theme)
        self.overlay_themes_layout.addWidget(self.overlay_void_theme)
        self.overlay_themes_layout.addWidget(self.overlay_sunrise_theme)
        self.overlay_themes_layout.addWidget(self.overlay_vaporwave_theme)
        self.overlay_themes_layout.addWidget(self.overlay_black_and_white_theme)
        
        self.app_icon_label = QLabel("Icon", self)
        self.app_icon_label.setContentsMargins(10, 15, 0, 0)
        self.app_icon_label.setObjectName("HostIDLabel")
        
        self.app_icon_container = QWidget(self)
        self.app_icon_container.setContentsMargins(10, 0, 0, 0)
        self.app_icon_layout = FlowLayout(self.app_icon_container)
        self.app_icon_layout.setContentsMargins(0, 0, 0, 0)
        self.app_icon_layout.setSpacing(20)
        
        self.icons = []
        self.icon_images = [value for key, value in IMAGES.items() if "icon" in key]
        for i, image in enumerate(self.icon_images):
            icon = QRadioButton(self.app_icon_container)
            icon.setFixedSize(80, 80)
            icon.setStyleSheet(f"""
                QRadioButton::indicator {{
                    width: 76px;
                    height: 76px;
                    border: 2px solid red;
                    border-radius: 9px;
                    image: url({image});
                }}

                QRadioButton::indicator:checked {{
                    border: 2px solid green;
                }}
            """)
            icon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            icon.clicked.connect(partial(self.select_app_icon, i))
            self.app_icon_layout.addWidget(icon)
            self.icons.append(icon)
        
        self.content_layout.addWidget(self.display_label)
        self.content_layout.addWidget(self.display_mode)
        self.content_layout.addWidget(self.overlay_position)
        if self.window().metaObject().className() == "Overlay":
            self.content_layout.addWidget(self.close_container)
        self.content_layout.addWidget(self.display_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.keybinds_label)
        self.content_layout.addWidget(self.stop_commands_label)
        self.content_layout.addWidget(self.stop_commands)
        self.content_layout.addWidget(self.keybinds_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.other_label)
        self.content_layout.addWidget(self.other_container)
        self.content_layout.addWidget(self.other_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.themes_label)
        self.content_layout.addWidget(self.app_theme_label)
        self.content_layout.addWidget(self.app_themes_container)
        self.content_layout.addWidget(self.overlay_theme_label)
        self.content_layout.addWidget(self.overlay_themes_container)
        self.content_layout.addWidget(self.app_icon_label)
        self.content_layout.addWidget(self.app_icon_container)
        
        self.ocr_sync()
        self.clipboard_sync()
        self.command_speed_sync()
        self.change_app_style()
        self.change_overlay_style()
        self.change_app_icon()
        
        glb.SIGNAL_MANAGER.settingChanged.connect(self.ocr_sync)
        glb.SIGNAL_MANAGER.settingChanged.connect(self.clipboard_sync)
        glb.SIGNAL_MANAGER.settingChanged.connect(self.command_speed_sync)
        glb.SIGNAL_MANAGER.appStyleChanged.connect(self.change_app_style)
        glb.SIGNAL_MANAGER.overlayStyleChanged.connect(self.change_overlay_style)
        glb.SIGNAL_MANAGER.appIconChanged.connect(self.change_app_icon)
        
    def ocr_enabled(self, state: bool) -> None:
        glb.SETTINGS.setValue("OcrEnabled", 1 if state else 0)
        glb.SIGNAL_MANAGER.settingChanged.emit()
    
    def ocr_sync(self) -> None:
        self.enable_ocr.setChecked(bool(glb.SETTINGS.value("OcrEnabled", 1)))
    
    def clipboard_enabled(self, state: bool) -> None:
        glb.SETTINGS.setValue("ClipboardEnabled", 1 if state else 0)
        glb.SIGNAL_MANAGER.settingChanged.emit()
        
    def clipboard_sync(self) -> None:
        self.use_clipboard.setChecked(bool(glb.SETTINGS.value("ClipboardEnabled", 1)))
    
    def command_speed_changed(self, speed: int) -> None:
        glb.SETTINGS.setValue("CommandSpeed", speed)
        glb.KEY_DELAY = 0.025 * (6 - speed)
        glb.SIGNAL_MANAGER.settingChanged.emit()
    
    def command_speed_sync(self) -> None:
        self.command_input_speed.setValue(glb.SETTINGS.value("CommandSpeed", 4))
    
    def select_app_style(self, index: int) -> None:
        glb.SETTINGS.setValue("AppStyle", index)
        glb.SIGNAL_MANAGER.appStyleChanged.emit()
        if self.window().metaObject().className() == "Overlay":
            open_window("Super Animal Royale")
    
    def change_app_style(self) -> None:
        match glb.SETTINGS.value("AppStyle", 0):
            case 0:
                self.purple_theme.setChecked(True)
            case 1:
                self.dark_theme.setChecked(True)
            case 2:
                self.blue_theme.setChecked(True)
            case 3:
                self.purple_sky_theme.setChecked(True)
            case 4:
                self.cotton_candy_theme.setChecked(True)
            case 5:
                self.aqua_theme.setChecked(True)
            case 6:
                self.nebula_theme.setChecked(True)
            case 7:
                self.void_theme.setChecked(True)
            case 8:
                self.sunrise_theme.setChecked(True)
            case 9:
                self.vaporwave_theme.setChecked(True)
            case 10:
                self.black_and_white_theme.setChecked(True)
    
    def select_overlay_style(self, index: int) -> None:
        glb.SETTINGS.setValue("OverlayStyle", index)
        glb.SIGNAL_MANAGER.overlayStyleChanged.emit()
        if self.window().metaObject().className() == "Overlay":
            open_window("Super Animal Royale")
    
    def change_overlay_style(self) -> None:
        match glb.SETTINGS.value("OverlayStyle", 0):
            case 0:
                self.overlay_purple_theme.setChecked(True)
            case 1:
                self.overlay_dark_theme.setChecked(True)
            case 2:
                self.overlay_blue_theme.setChecked(True)
            case 3:
                self.overlay_purple_sky_theme.setChecked(True)
            case 4:
                self.overlay_cotton_candy_theme.setChecked(True)
            case 5:
                self.overlay_aqua_theme.setChecked(True)
            case 6:
                self.overlay_nebula_theme.setChecked(True)
            case 7:
                self.overlay_void_theme.setChecked(True)
            case 8:
                self.overlay_sunrise_theme.setChecked(True)
            case 9:
                self.overlay_vaporwave_theme.setChecked(True)
            case 10:
                self.overlay_black_and_white_theme.setChecked(True)
                
    def select_app_icon(self, index: int) -> None:
        glb.SETTINGS.setValue("AppIcon", index)
        glb.SIGNAL_MANAGER.appIconChanged.emit()
        if self.window().metaObject().className() == "Overlay":
            open_window("Super Animal Royale")
    
    def change_app_icon(self) -> None:
        self.icons[glb.SETTINGS.value("AppIcon", 0)].setChecked(True)