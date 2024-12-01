from core.qt_core import *
from dataclasses import dataclass

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

class SignalManager(QObject):
    presetOpened = Signal(dict)
    presetsChanged = Signal()
    presetRestored = Signal(dict)
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

@dataclass
class PlayerItem:
    player_id: int
    name: str
    team: int = 1