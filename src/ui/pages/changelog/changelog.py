from core import *
from core._version import __version__
from widgets import HLine, Button
from packaging.version import Version
import requests

class PageChangelog(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height: int = 2
        
        self.changelog_label = QLabel("Changelog", self)
        self.changelog_label.setObjectName("PlayersHeaderName")
        self.changelog_label.setContentsMargins(9, 0, 0, 0)
        
        self.changelog_hline_top = HLine(self, h=self.line_height)
        self.changelog_hline_top.setObjectName("DivLine")
        
        self.changelog_hline_bottom = HLine(self, h=self.line_height)
        self.changelog_hline_bottom.setObjectName("DivLine")
        
        self.bottom_row_container = QWidget(self)
        self.bottom_row_layout = QHBoxLayout(self.bottom_row_container)
        self.bottom_row_layout.setContentsMargins(9, 0, 9, 0)
        
        self.current_version = QLabel(f"Current version: {__version__}", self)
        self.current_version.setObjectName("PlayersHeaderName")
        self.check_updates_button = Button(self, "Check for updates...", w=200)
        self.check_updates_button.clicked.connect(self.check_updates)
        
        self.bottom_row_layout.addWidget(self.current_version, alignment=Qt.AlignmentFlag.AlignLeft)
        self.bottom_row_layout.addWidget(self.check_updates_button, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_area.setWidget(self.content_area)
        
        self.page_layout.addWidget(self.changelog_label)
        self.page_layout.addWidget(self.changelog_hline_top)
        self.page_layout.addWidget(self.scroll_area)
        self.page_layout.addWidget(self.changelog_hline_bottom)
        self.page_layout.addSpacing(9)
        self.page_layout.addWidget(self.bottom_row_container)
        self.print_changelog()
        
        glb.SETTINGS.setValue("CurrentVersion", __version__)
    
    def get_response(self, api: str) -> dict:
        response = requests.get(api)
        return response.json()
    
    def print_changelog(self) -> None:
        try:
            releases = self.get_response("https://api.github.com/repos/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases")
            if "message" in releases:
                raise requests.exceptions.RequestException("API rate limit reached.")
        except requests.exceptions.ConnectionError:
            error_message = QLabel("Error retrieving changelog data.\nCheck your internet connection.", self)
            error_message.setObjectName("ItemsHeaderName")
            self.content_layout.addWidget(error_message)
            return
        except requests.exceptions.RequestException as e:
            error_message = QLabel(f"Error retrieving changelog data.\n{e}", self)
            error_message.setObjectName("ItemsHeaderName")
            self.content_layout.addWidget(error_message)
            return
        for i, release in enumerate(releases):
            content: list[str] = release["body"].split("\r\n")
            header_text: str = content[0].strip("*").removeprefix("Changelog: ")
            del content[:2]
            description_text = '\n'.join(content)
            
            header = QLabel(header_text, self)
            header.setObjectName("ItemsHeaderName")
            description = QLabel(description_text, self)
            description.setContentsMargins(20, 0, 0, 0)
            description.setObjectName("ChangelogDescription")
            self.content_layout.addWidget(header)
            self.content_layout.addWidget(description)
            if i < len(releases)-1:
                self.content_layout.addSpacing(30)
    
    def check_updates(self) -> None:
        latest_version = update_latest_version()
        if not latest_version:
            send_notification("Could not retrieve data", "NotifFail")
        elif Version(__version__) < Version(latest_version):
            show_update()
        else:
            send_notification("You are up to date!", "NotifSuccess")