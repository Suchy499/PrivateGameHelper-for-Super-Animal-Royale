from core import *
from widgets import SettingsComboBox, HLine, KeybindEdit, LabeledToggle, FlowLayout
from images import IMAGES

class PageSettings(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(9, 9, 9, 22)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        _layout.addWidget(self.scroll_area)
        
        self._layout = QVBoxLayout(self.content_area)
        self._layout.setContentsMargins(0, 0, 9, 0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        
        self.display_label = QLabel(self, text="Display")
        self.display_label.setContentsMargins(0, 0, 0, 15)
        self.display_label.setObjectName("PregameHeaderName")
        
        self.display_mode = SettingsComboBox(self, "Display Mode", "DisplayMode")
        self.display_mode.setContentsMargins(10, 0, 0, 15)
        self.overlay_position = SettingsComboBox(self, "Overlay Position", "OverlayPosition")
        self.overlay_position.setContentsMargins(10, 0, 0, 15)
        
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
        self.enable_ocr.stateChanged.connect(self.ocr_enabled)
        self.enable_ocr.setToolTip(
            "OCR checks if your chatbox or pause menu is open before sending commands.\n"
            "This helps prevent unwanted inputs, however, it isn't perfect.\n"
            "If you're experiencing issues running certain commands, consider disabling this setting."
        )
        
        self.use_clipboard = LabeledToggle(self, text="Use Clipboard", default_state=True)
        self.use_clipboard.stateChanged.connect(self.clipboard_enabled)
        self.use_clipboard.setToolTip(
            "Use system clipboard to paste commands into SAR chat.\n"
            "Disabling this setting will significantly slow down the input process."
        )
        
        self.other_layout.addWidget(self.enable_ocr)
        self.other_layout.addWidget(self.use_clipboard)
        
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
        
        self.blue_theme = QRadioButton(self.app_themes_container)
        self.blue_theme.setFixedSize(80, 80)
        self.blue_theme.setObjectName("ThemeBlue")
        self.blue_theme.setToolTip("Blue")
        self.blue_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.blue_theme.clicked.connect(lambda: self.select_app_style(1))
        
        self.app_themes_layout.addWidget(self.purple_theme)
        self.app_themes_layout.addWidget(self.blue_theme)
        
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
        self.overlay_purple_theme.setObjectName("ThemeOverlayPurple")
        self.overlay_purple_theme.setToolTip("Purple")
        self.overlay_purple_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_purple_theme.clicked.connect(lambda: self.select_overlay_style(0))
        
        self.overlay_dark_theme = QRadioButton(self.overlay_themes_container)
        self.overlay_dark_theme.setFixedSize(80, 80)
        self.overlay_dark_theme.setObjectName("ThemeOverlayDark")
        self.overlay_dark_theme.setToolTip("Dark")
        self.overlay_dark_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.overlay_dark_theme.clicked.connect(lambda: self.select_overlay_style(1))
        
        self.overlay_themes_layout.addWidget(self.overlay_purple_theme)
        self.overlay_themes_layout.addWidget(self.overlay_dark_theme)
        
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
        
        self._layout.addWidget(self.display_label)
        self._layout.addWidget(self.display_mode)
        self._layout.addWidget(self.overlay_position)
        self._layout.addWidget(self.display_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.keybinds_label)
        self._layout.addWidget(self.stop_commands_label)
        self._layout.addWidget(self.stop_commands)
        self._layout.addWidget(self.keybinds_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.other_label)
        self._layout.addWidget(self.other_container)
        self._layout.addWidget(self.other_hline)
        self._layout.addSpacing(10)
        self._layout.addWidget(self.themes_label)
        self._layout.addWidget(self.app_theme_label)
        self._layout.addWidget(self.app_themes_container)
        self._layout.addWidget(self.overlay_theme_label)
        self._layout.addWidget(self.overlay_themes_container)
        self._layout.addWidget(self.app_icon_label)
        self._layout.addWidget(self.app_icon_container)
        
        self.ocr_sync()
        self.clipboard_sync()
        self.change_app_style()
        self.change_overlay_style()
        self.change_app_icon()
        
        glb.SIGNAL_MANAGER.settingChanged.connect(self.ocr_sync)
        glb.SIGNAL_MANAGER.settingChanged.connect(self.clipboard_sync)
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
    
    def select_app_style(self, index: int) -> None:
        glb.SETTINGS.setValue("AppStyle", index)
        glb.SIGNAL_MANAGER.appStyleChanged.emit()
    
    def change_app_style(self) -> None:
        match glb.SETTINGS.value("AppStyle", 0):
            case 0:
                self.purple_theme.setChecked(True)
            case 1:
                self.blue_theme.setChecked(True)
    
    def select_overlay_style(self, index: int) -> None:
        glb.SETTINGS.setValue("OverlayStyle", index)
        glb.SIGNAL_MANAGER.overlayStyleChanged.emit()
    
    def change_overlay_style(self) -> None:
        match glb.SETTINGS.value("OverlayStyle", 0):
            case 0:
                self.overlay_purple_theme.setChecked(True)
            case 1:
                self.overlay_dark_theme.setChecked(True)
                
    def select_app_icon(self, index: int) -> None:
        glb.SETTINGS.setValue("AppIcon", index)
        glb.SIGNAL_MANAGER.appIconChanged.emit()
    
    def change_app_icon(self) -> None:
        self.icons[glb.SETTINGS.value("AppIcon", 0)].setChecked(True)