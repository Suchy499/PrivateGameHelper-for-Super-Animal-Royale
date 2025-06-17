from core import *
from widgets import Button
import sys

class DebugConsole(QFrame):
    def __init__(
        self,
        parent: QWidget | None = None,
        old_stream = None
    ):
        super().__init__(parent)
        self.setObjectName("ConsoleWidget")
        
        self.old_stream = old_stream
        
        self.console_layout = QVBoxLayout(self)
        self.console_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.scroll_area.setWidget(self.content_area)
        
        self.console_layout.addWidget(self.scroll_area)
        
        self.console_output = QLabel(self)
        self.console_output.setObjectName("ConsoleOutput")
        self.console_output.setAlignment(Qt.AlignmentFlag.AlignBottom)
        
        self.content_layout.addWidget(self.console_output)
        
        self.buttons_widget = QWidget(self)
        self.buttons_layout = QHBoxLayout(self.buttons_widget)
        
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        self.file_dialog.setNameFilter("Text file (*.txt)")
        self.file_dialog.fileSelected.connect(self.save)
        
        self.save_button = Button(self, "Save log", size_policy="Expanding")
        self.save_button.setFixedHeight(30)
        self.clear_button = Button(self, "Clear console", btn_style="ButtonDelete", size_policy="Expanding")
        self.clear_button.setFixedHeight(30)
        self.save_button.clicked.connect(self.file_dialog.exec)
        self.clear_button.clicked.connect(self.clear)
        
        self.buttons_layout.addWidget(self.save_button)
        self.buttons_layout.addWidget(self.clear_button)
        
        self.console_layout.addWidget(self.buttons_widget)
        
        glb.SIGNAL_MANAGER.consoleUpdated.connect(self.console_output.setText)
    
    def write(self, text) -> None:
        output_text = f"{self.console_output.text()}{str(text)}"
        self.console_output.setText(output_text)
        glb.SIGNAL_MANAGER.consoleUpdated.emit(output_text)
        if self.old_stream:
            self.old_stream.write(text)
    
    def flush(self, text) -> None:
        output_text = f"{self.console_output.text()}{str(text)}"
        self.console_output.setText(output_text)
        glb.SIGNAL_MANAGER.consoleUpdated.emit(output_text)
        if self.old_stream:
            self.old_stream.flush()
    
    def clear(self) -> None:
        self.console_output.clear()
        glb.SIGNAL_MANAGER.consoleUpdated.emit("")
    
    def save(self, path) -> None:
        try:
            with open(path, "w") as f:
                f.write(self.console_output.text())
        except Exception as e:
            print(e)