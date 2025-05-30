from core import *
from images import IMAGES
from widgets import Button, TournamentComboBox, ClickableLabel, Popup, LabeledToggle
import json
import shutil
from zipfile import ZipFile

class Settings(QWidget):
    def __init__(self, parent, tournament_id: str):
        super().__init__(parent)
        
        self.tournament_id = tournament_id
        self.line_height = 2
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(9, 0, 0, 0)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.settings_label = QLabel(self, text="Settings")
        self.settings_label.setContentsMargins(-9, 0, 0, 15)
        self.settings_label.setObjectName("PregameHeaderName")
        
        self.name_label = QLabel(self, text="Tournament name")
        self.name_label.setObjectName("PresetNameLabel")
        self.name_label.setContentsMargins(0, 0, 0, 0)
        
        self.name_edit = QLineEdit(self)
        self.name_edit.setFixedWidth(221)
        self.name_edit.setObjectName("LineEdit")
        self.name_edit.setContentsMargins(0, 0, 0, 10)
        self.name_edit.setText("Untitled")
        self.name_edit.textEdited.connect(self.name_edit.setText)
        
        self.mode_combobox = TournamentComboBox(self, "Game mode", 221)
        self.mode_combobox.addItems([
            "Solo",
            "Duo",
            "Squad"
        ])
        
        self.datetime_label = QLabel(self, text="Date and time")
        self.datetime_label.setObjectName("PresetNameLabel")
        self.datetime_label.setContentsMargins(0, 10, 0, 0)
        
        self.datetime_container = QWidget(self)
        self.datetime_container_layout = QHBoxLayout(self.datetime_container)
        self.datetime_container_layout.setContentsMargins(0, 0, 0, 0)
        self.datetime_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.datetime_edit = QDateTimeEdit(self)
        self.datetime_edit.setFixedWidth(221)
        self.datetime_edit.setObjectName("LineEdit")
        self.datetime_edit.setContentsMargins(0, 0, 0, 10)
        self.datetime_edit.setCalendarPopup(True)
        self.datetime_edit.setStyleSheet(f"""
            #LineEdit::down-arrow {{
                image: url(:/images/down_arrow.png);
                width: 10px;
            }}
            #LineEdit::drop-down {{
                padding-right: 10px;
                border: none;
            }}
        """)
        self.datetime_edit.calendarWidget().setFixedSize(300, 200)
        self.datetime_edit.dateTimeChanged.connect(self.datetime_edit.setDateTime)
        
        self.copy_to_clipboard = ClickableLabel(self)
        self.copy_to_clipboard.setContentsMargins(0, 0, 0, 0)
        self.copy_to_clipboard.setToolTip("Copy Discord Timestamp")
        self.clipboard_pixmap = QPixmap(IMAGES["clipboard"]).scaledToWidth(15, Qt.TransformationMode.SmoothTransformation)
        self.copy_to_clipboard.setPixmap(self.clipboard_pixmap)
        self.copy_to_clipboard.setFixedSize(self.clipboard_pixmap.width() + 9, self.clipboard_pixmap.height() + 9)
        self.copy_to_clipboard.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.copy_to_clipboard.setObjectName("PlayersHeaderRefresh")
        self.copy_to_clipboard.setContentsMargins(0, 0, 0, 0)
        self.copy_to_clipboard.clicked.connect(self.copy_timestamp)
        
        self.datetime_container_layout.addWidget(self.datetime_edit)
        self.datetime_container_layout.addWidget(self.copy_to_clipboard)
        
        self.discord_integration_toggle = LabeledToggle(self, text="Discord Integration", default_state=True)
        
        self.settings_buttons = QWidget(self)
        self.settings_buttons_layout = QHBoxLayout(self.settings_buttons)
        self.settings_buttons_layout.setContentsMargins(0, 0, 0, 9)
        self.settings_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.settings_buttons_layout.setSpacing(10)
        
        self.save_icon = QPixmap(IMAGES["pencil"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.save_button = Button(self.settings_buttons, " Save", self.save_icon)
        self.settings_buttons_layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_settings)
        
        self.delete_icon = QPixmap(IMAGES["trash"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.delete_button = Button(self.settings_buttons, " Delete", self.delete_icon, btn_style="ButtonDelete")
        
        self.settings_buttons_layout.addWidget(self.delete_button)
        
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        self.file_dialog.setNameFilter("Zip archive (*.zip)")
        self.file_dialog.fileSelected.connect(self.export_csvs)
        
        self.export_button = Button(self, "Export to CSVs", w=210)
        self.export_button.clicked.connect(self.file_dialog.exec)
        
        self.page_layout.addWidget(self.settings_label)
        self.page_layout.addWidget(self.name_label)
        self.page_layout.addWidget(self.name_edit)
        self.page_layout.addWidget(self.mode_combobox)
        self.page_layout.addWidget(self.datetime_label)
        self.page_layout.addWidget(self.datetime_container)
        self.page_layout.addSpacing(10)
        self.page_layout.addWidget(self.discord_integration_toggle)
        self.page_layout.addSpacing(10)
        self.page_layout.addWidget(self.settings_buttons)
        self.page_layout.addWidget(self.export_button)
        
        self.confirm_popup = Popup(
            self, 
            "Confirm", 
            "Are you sure you want to\ndelete this tournament?",
            300,
            150,
            Button(None, "Cancel", btn_style="ButtonDelete"),
            Button(None, "Delete", btn_style="ButtonDefault")
        )
        
        self.confirm_popup.buttons[0].clicked.connect(self.confirm_popup.hide)
        self.confirm_popup.buttons[1].clicked.connect(self.delete_tournament)

        self.confirm_popup.hide()
        
        self.delete_button.clicked.connect(self.open_popup)
        
        glb.SIGNAL_MANAGER.tournamentUpdated.connect(self.load_settings)
        
        self.load_settings(self.tournament_id)
    
    def copy_timestamp(self) -> None:
        pyperclip.copy(f"<t:{self.datetime_edit.dateTime().toSecsSinceEpoch()}:F>")
        send_notification("Timestamp copied to clipboard!", "NotifSuccess")
    
    def save_settings(self) -> None:
        try:
            tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
            tournament_metadata = {
                "name": self.name_edit.text(),
                "mode": self.mode_combobox.currentText(),
                "starts_at": self.datetime_edit.dateTime().toSecsSinceEpoch(),
                "discord": self.discord_integration_toggle.isChecked()
            }
            with open(os.path.join(tournament_path, "metadata.json"), "w") as f:
                json.dump(tournament_metadata, f, indent=4)
            glb.SIGNAL_MANAGER.tournamentUpdated.emit(self.tournament_id)
            send_notification("Settings have been saved!", "NotifSuccess")
        except Exception as e:
            send_notification("Something went wrong. Try again", "NotifFail")
            print(e)
    
    def load_settings(self, tournament_id: str) -> None:
        if tournament_id != self.tournament_id:
            return
        
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
        with open(os.path.join(tournament_path, "metadata.json"), "r") as f:
            tournament_metadata = json.load(f)
        
        self.name_edit.setText(tournament_metadata["name"])
        self.mode_combobox.setCurrentText(tournament_metadata["mode"])
        if not tournament_metadata["starts_at"]:
            self.datetime_edit.setDateTime(QDateTime.currentDateTime())
        else:
            self.datetime_edit.setDateTime(QDateTime.fromSecsSinceEpoch(tournament_metadata["starts_at"]))
        if tournament_metadata["discord"]:
            self.discord_integration_toggle.setChecked(True)
        else:
            self.discord_integration_toggle.setChecked(False)
    
    def delete_tournament(self) -> None:
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
        shutil.rmtree(tournament_path)
        self.confirm_popup.hide()
        glb.SIGNAL_MANAGER.tournamentDeleted.emit(self.tournament_id)
    
    def get_rounds(self) -> list[str]:
        rounds_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "Rounds")
        if not os.path.exists(rounds_path):
            os.makedirs(rounds_path)
        files: list[str] = os.listdir(rounds_path)
        round_files: list[str] = []
        for round_file in files:
            if re.match(r"^\d+\.csv$", round_file):
                round_files.append(os.path.join(rounds_path, round_file))
        return round_files
    
    def export_csvs(self, file: str) -> None:
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
        leaderboard_path = os.path.join(tournament_path, "leaderboard.csv")
        rounds = self.get_rounds()
        if not os.path.exists(leaderboard_path) and not rounds:
            send_notification("No files to export.", "NotifFail")
            return
        with ZipFile(file, "w") as zip_file:
            if os.path.exists(leaderboard_path):
                zip_file.write(leaderboard_path, os.path.basename(leaderboard_path))
            for round_file in rounds:
                zip_file.write(round_file, os.path.basename(round_file))
    
    def open_popup(self) -> None:
        self.confirm_popup.setGeometry(
            (self.width()-self.confirm_popup.width())/2,
            (self.height()-self.confirm_popup.height())/2,
            self.confirm_popup.width(),
            self.confirm_popup.height()
        )
        self.confirm_popup.show()