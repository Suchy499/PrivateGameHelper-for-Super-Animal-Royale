from core.qt_core import *
from dataclasses import dataclass
import time
from typing import Optional
import win32gui
from enum import Enum

class WorkThread(QThread):
    QUEUE: list = []
    def run(self):
        while True:
            try:
                command = self.QUEUE[0]
                self.QUEUE.pop(0)
                command()
            except IndexError:
                break
            
class OverlayThread(QThread):
    def __init__(self, parent: QWidget, name: str):
        super().__init__(parent)
        self.name = name
        self.overlay = parent
        
    def run(self):
        last_size: tuple[int, int, int, int] = (0, 0, 0, 0)
        while True:
            time.sleep(0.5)
            if (size := self.get_window_size(self.name)) is None:
                break
            if size != last_size:
                last_size = size
                self.overlay.setGeometry(*size)
    
    def get_window_size(self, name) -> Optional[tuple[int, int, int, int]]:
        if hwnd := win32gui.FindWindow(None, name):
            x, y, right, bottom = win32gui.GetWindowRect(hwnd)
            width = right - x
            height = bottom - y
            return x, y, width, height
        return None


class SignalManager(QObject):
    pageChanged = Signal(QWidget, str)
    presetOpened = Signal(dict, str)
    presetDeleted = Signal()
    presetEdited = Signal()
    presetSaved = Signal()
    presetRestored = Signal(dict)
    presetNameChanged = Signal(str)
    presetSettingChanged = Signal()
    playersRefreshed = Signal()
    playerSelected = Signal()
    raritySelected = Signal()
    duelsMapSelected = Signal(str)
    dodgeballMapSelected = Signal(str)
    playerChangedTeams = Signal()
    weaponSelected = Signal(int)
    weaponSelectedAll = Signal(str, bool)
    hostIdChanged = Signal(int)
    duelsSettingChanged = Signal(str, bool)
    dodgeballSettingChanged = Signal(str, bool)
    dodgeballDamageChanged = Signal(float)
    overlayClosed = Signal()
    settingChanged = Signal()
    appStyleChanged = Signal()
    overlayStyleChanged = Signal()
    appIconChanged = Signal()
    coordinatesChanged = Signal(str)
    tournamentCreated = Signal(str)
    tournamentDeleted = Signal(str)
    tournamentNameChanged = Signal(str)
    tournamentModeChanged = Signal(str)
    tournamentDateTimeChanged = Signal(int)
    tournamentUpdated = Signal(str)
    tournamentOpened = Signal(str)
    tournamentClosed = Signal()
    killPointsToggled = Signal(bool, str)
    roundSaved = Signal(str, int)
    roundDeleted = Signal(str)
    notificationSent = Signal(str, str)
    leaderboardUpdated = Signal(str)
    graphsUpdated = Signal(str)
    webhooksSaved = Signal()
    scoresUpdated = Signal(str)

@dataclass
class PlayerItem:
    player_id: int
    name: str
    team: int = 1
    
@dataclass
class Player:
    player_id: int
    name: str
    playfab_id: str
    squad_id: int
    team_id: int
    kills: int
    placement: int
    
class CommandSpeed(Enum):
    VERY_SLOW = 1
    SLOW = 2
    NORMAL = 3
    FAST = 4
    VERY_FAST = 5