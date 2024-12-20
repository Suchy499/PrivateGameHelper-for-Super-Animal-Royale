from PySide6.QtWidgets import QProgressBar
from PySide6.QtCore import QTimer

class ProgressBar(QProgressBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.ticks_left = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.increment_bar)
        self.update_bar(1)

    def update_bar(self, increment):
        self.ticks_left += increment
        if not self.timer.isActive():
            self.timer.start(20)
    
    def increment_bar(self) -> None:
        value = self.value() + 1
        self.setValue(value)
        self.ticks_left -= 1
            
        if value >= self.maximum():
            self.setValue(100)
            self.ticks_left = 0
            
        if self.ticks_left <= 0:
            self.timer.stop()