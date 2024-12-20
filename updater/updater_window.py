from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QScrollArea, QFrame, QPushButton, QLabel, QApplication
from PySide6.QtCore import Qt, QSettings, QThread, QObject, Signal
from PySide6.QtGui import QIcon
import rc_images
from title_bar import UpdaterTitleBar
from progress_bar import ProgressBar
import os
import sys
import shutil
from typing import Literal, Callable
from packaging.version import Version
import requests
from github_release_downloader import GitHubRepo, get_assets, download_assets
import re
import pathlib
from zipfile import ZipFile
import subprocess

try:
    from ctypes import windll
    myappid = 'suchy499.privategamehelperupdater.v2'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class SignalManager(QObject):
    buttonStateChanged = Signal(bool)
    buttonTextChanged = Signal(str)
    buttonCallbackChanged = Signal(object)
    textPrinted = Signal(str, str)
    progressUpdated = Signal(int)

SIGNAL_MANAGER = SignalManager()

class UpdaterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setObjectName("MainWindow")
        self.setFixedSize(500, 250)
        self.setWindowTitle("Private Game Helper - Updater")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(":/images/updater.png"))
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setStyleSheet("""
            #MainWindowContent {
                background: qlineargradient(spread:pad, x1:0.471591, y1:1, x2:0.915, y2:0, stop:0 #161733, stop:1 #332757);
                border-radius: 20px;
                border: 2px solid #332757;
            }
            
            #UpdaterTitleBar {
                background: rgba(0, 0, 0, 20);
            }
            
            #Title {
                font-family: Rubik;
                font-weight: bold;
                font-size: 13px;
                color: white;
                text-align: center;
            }
            
            QProgressBar {
                background: rgba(255, 255, 255, 0.15);
                border: 2px solid rgb(38, 63, 112);
                border-radius: 8px;
                text-align: center;
                font-family: Rubik;
                font-weight: bold;
                font-size: 13px;
                color: white;
            }

            QProgressBar::chunk {
                width: 6px;
                background: rgb(86, 138, 242);
                margin: 1px 3px 1px 3px;
                border-radius: 3px;
            }
            
            #ScrollArea {
                background: rgba(0, 0, 0, 0.3);
                border-radius: 8px;
            }
            
            #Content {
                background: transparent;
            }

            #Button {
                background: rgb(56, 91, 161);
                border: 2px solid rgb(38, 63, 112);
                font-family: Rubik;
                font-weight: bold;
                font-size: 13px;
                color: white;
                text-align: center;
                border-radius: 8px;
            }

            #Button:hover {
                background: rgb(47, 77, 137);
            }

            #Button:pressed {
                background: rgb(38, 63, 112);
            }
            
            #ProgressText {
                font-family: Rubik;
                font-weight: bold;
                font-size: 11px;
            }
            
            #ProgressText[color="white"] {
                color: white;
            }
            
            #ProgressText[color="green"] {
                color: green;
            }
            
            #ProgressText[color="red"] {
                color: red;
            }
            
            QScrollBar:vertical {
                border: none;
                background: rgba(0, 0, 0, 0);
                width: 14px;
                margin: 15px 0 15px 0;
                border-radius: 0px;
            }

            QScrollBar::handle:vertical {	
                background-color: rgba(129, 126, 120, 0.4);
                min-height: 30px;
                border-radius: 7px;
            }

            QScrollBar::handle:vertical:hover{	
                background-color: rgba(129, 126, 120, 1);
            }

            QScrollBar::handle:vertical:pressed {	
                background-color: rgba(129, 126, 120, 1);
            }

            QScrollBar::sub-line:vertical {
                border: none;
                background-color: rgba(129, 126, 120, 0.4);
                height: 15px;
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:vertical:hover {	
                background-color: rgba(129, 126, 120, 1);
            }

            QScrollBar::sub-line:vertical:pressed {	
                background-color: rgba(129, 126, 120, 1);
            }

            QScrollBar::add-line:vertical {
                border: none;
                background-color: rgba(129, 126, 120, 0.4);
                height: 15px;
                border-bottom-left-radius: 7px;
                border-bottom-right-radius: 7px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::add-line:vertical:hover {	
                background-color: rgba(129, 126, 120, 1);
            }

            QScrollBar::add-line:vertical:pressed {	
                background-color: rgba(129, 126, 120, 1);
            }

            QScrollBar::up-arrow:vertical, 
            QScrollBar::down-arrow:vertical {
                background: none;
            }

            QScrollBar::add-page:vertical, 
            QScrollBar::sub-page:vertical {
                background: none;
            }

        """)
        
        self.content = QWidget(self)
        self.content.setObjectName("MainWindowContent")
        self.setCentralWidget(self.content)
        self.window_layout = QVBoxLayout(self.content)
        self.window_layout.setContentsMargins(0, 0, 0, 0)
        self.window_layout.setSpacing(0)
        self.window_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.title_bar = UpdaterTitleBar(self)
        self.window_layout.addWidget(self.title_bar)
        
        self.updater_container = QWidget(self)
        self.updater_layout = QVBoxLayout(self.updater_container)
        self.window_layout.addWidget(self.updater_container)
        
        self.progress_bar = ProgressBar(self)
        self.updater_layout.addWidget(self.progress_bar)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.progress_description = QWidget(self)
        self.progress_description.setObjectName("Content")
        self.progress_description_layout = QVBoxLayout(self.progress_description)
        self.progress_description_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.progress_description_layout.setDirection(QVBoxLayout.Direction.TopToBottom)
        self.scroll_area.setWidget(self.progress_description)
        self.updater_layout.addWidget(self.scroll_area)
        
        self.button = QPushButton("Waiting to start", self)
        self.button.setObjectName("Button")
        self.button.setFixedHeight(32)
        self.button.setDisabled(True)
        self.updater_layout.addWidget(self.button)
    
        SIGNAL_MANAGER.buttonStateChanged.connect(self.button.setEnabled)
        SIGNAL_MANAGER.buttonTextChanged.connect(self.button.setText)
        SIGNAL_MANAGER.textPrinted.connect(self.print_text)
        SIGNAL_MANAGER.progressUpdated.connect(self.progress_bar.update_bar)
        SIGNAL_MANAGER.buttonCallbackChanged.connect(self.change_button_callback)
        
        self.update_thread = UpdateThread(self)
        
    def print_text(self, text: str, color: Literal["white", "green", "red"] = "white") -> None:
        step_label = QLabel(text, self)
        step_label.setObjectName("ProgressText")
        step_label.setProperty("color", color)
        self.progress_description_layout.addWidget(step_label)
    
    def change_button_callback(self, callback: Callable) -> None:
        try:
            self.button.clicked.disconnect()
        except:
            pass
        self.button.clicked.connect(callback)

class UpdateThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.SETTINGS = QSettings("Suchy499", "Private Game Helper")
        self.zip_path = None
        self.root_dir = os.path.dirname(sys.executable)
        self.backup_dir = os.path.join(self.root_dir, "backup")
        self.excluded_files = ["backup", "updater.exe", "unins000.dat", "unins000.exe"]
        
        self.current_version = self.SETTINGS.value("CurrentVersion", None)
        self.latest_version = self.get_latest_version()
    
    def run(self):
        self.update_app()
        
    def get_latest_version(self) -> int | str:
        try:
            latest_release = requests.get("https://api.github.com/repos/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/releases/latest").json()
            if "message" in latest_release:
                raise requests.exceptions.RequestException("API rate limit reached.")
        except requests.exceptions.ConnectionError:
            return 0
        except requests.exceptions.RequestException as e:
            return 1
        
        return latest_release["tag_name"]
    
    def check_version(self) -> bool:
        self.add_label("Checking current version...")
        self.update_bar(10)
        if self.current_version:
            self.add_label(f"Current version: {self.current_version}")
        else:
            self.add_label("Current version: Not found")
        self.add_label("Checking latest version...")
        self.update_bar(10)
        match self.latest_version:
            case 0:
                self.add_label("FAIL: Could not retrieve latest version. Check your internet connection", "red")
                return False
            case 1:
                self.add_label("FAIL: Could not retrieve latest version. API rate limit reached", "red")
                return False
            case _:
                self.add_label(f"Latest version: {self.latest_version}")
                return True
    
    def create_backup(self) -> bool:
        try:
            os.mkdir(self.backup_dir)
        except FileExistsError:
            shutil.rmtree(self.backup_dir)
            os.mkdir(self.backup_dir)
        self.add_label("Creating backup...")
        self.update_bar(10)
        for each_file in os.listdir(self.root_dir):
            if each_file not in self.excluded_files:
                shutil.move(os.path.join(self.root_dir, each_file), os.path.join(self.backup_dir, each_file))
        self.update_bar(10)
        self.add_label("Backup created")
        return True

    def download_update(self) -> bool:
        self.add_label("Downloading the update...")
        self.update_bar(10)
        try:
            assets = get_assets(
                GitHubRepo("Suchy499", "PrivateGameHelper-for-Super-Animal-Royale"),
                tag_name=self.latest_version,
                assets_mask=re.compile(r"private-game-helper-v(?:\d+\.)*\d+-windows-x86-64-portable\.zip"),
            )
            download_assets(assets, pathlib.Path(self.root_dir))
            for each_file in os.listdir(self.root_dir):
                if re.match(r"private-game-helper-v(?:\d+\.)*\d+-windows-x86-64-portable\.zip", each_file):
                    self.zip_path = os.path.join(self.root_dir, each_file)
            if self.zip_path is None:
                raise FileNotFoundError("Downloaded update not found")
        except:
            self.add_label("FAIL: Could not download the update", "red")
            return False
        self.update_bar(20)
        self.add_label("Update downloaded")
        return True
    
    def extract_zip(self) -> bool:
        self.add_label("Extracting the update...")
        self.update_bar(10)
        try:
            with ZipFile(self.zip_path) as zip_file:
                for each_file in zip_file.namelist():
                    if "updater.exe" not in each_file:
                        zip_file.extract(each_file, self.root_dir)
        except:
            self.add_label("FAIL: Could not extract the update", "red")
            return False
        os.remove(self.zip_path)
        self.zip_path = None
        self.update_bar(20)
        self.add_label("Update extracted")
        return True
    
    def restore_backup(self) -> None:
        for each_file in os.listdir(self.root_dir):
            if each_file not in self.excluded_files:
                try:
                    shutil.rmtree(os.path.join(self.root_dir, each_file))
                except NotADirectoryError:
                    os.remove(os.path.join(self.root_dir, each_file))
                
        for each_file in os.listdir(self.backup_dir):
            shutil.move(os.path.join(self.backup_dir, each_file), os.path.join(self.root_dir, each_file))
        shutil.rmtree(self.backup_dir)
    
    def add_label(self, text: str, color: Literal["white", "green", "red"] = "white") -> None:
        SIGNAL_MANAGER.textPrinted.emit(text, color)
    
    def update_bar(self, increment: int) -> None:
        SIGNAL_MANAGER.progressUpdated.emit(increment)
    
    def change_button_state(self, state: bool) -> None:
        SIGNAL_MANAGER.buttonStateChanged.emit(state)
        
    def change_button_text(self, text: str) -> None:
        SIGNAL_MANAGER.buttonTextChanged.emit(text)
    
    def change_button_callback(self, callback: Callable) -> None:
        SIGNAL_MANAGER.buttonCallbackChanged.emit(callback)
    
    def update_app(self) -> None:
        os.chdir(os.path.dirname(self.root_dir))
        self.change_button_text("Update in progress...")
        if not self.check_version():
            self.change_button_text("Close updater")
            self.change_button_state(True)
            self.change_button_callback(QApplication.exit)
            return
        if Version(self.current_version) >= Version(self.latest_version):
            self.add_label("You are up to date!", "green")
            self.change_button_text("Close updater")
            self.change_button_state(True)
            self.change_button_callback(QApplication.exit)
            return
        if not self.create_backup():
            self.change_button_text("Close updater")
            self.change_button_state(True)
            self.change_button_callback(QApplication.exit)
            return
        if not self.download_update():
            self.restore_backup()
            self.change_button_text("Close updater")
            self.change_button_state(True)
            self.change_button_callback(QApplication.exit)
            return
        if not self.extract_zip():
            self.restore_backup()
            self.change_button_text("Close updater")
            self.change_button_state(True)
            self.change_button_callback(QApplication.exit)
            return
        self.change_button_text("Open Private Game Helper")
        self.change_button_state(True)
        self.change_button_callback(self.open_pgh)
        self.add_label("SUCCESS: Update complete!", "green")
        
    def open_pgh(self) -> None:
        subprocess.Popen([os.path.join(self.root_dir, "Private Game Helper.exe")], creationflags=subprocess.CREATE_NEW_CONSOLE)
        QApplication.exit()