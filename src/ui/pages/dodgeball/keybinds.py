from core import *
from widgets import KeybindEdit, HLine

class Keybinds(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(0, 0, 0, 0)
        
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
        
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.content_layout.setContentsMargins(0, 0, 9, 0)
        self.line_height = 2
        
        self.spawn_nades_label = QLabel("Spawn Nades")
        self.spawn_nades_label.setContentsMargins(0, 0, 0, 15)
        self.spawn_nades_label.setObjectName("ItemsHeaderName")
        
        self.spawn_nades_container = QWidget(self)
        self.spawn_nades_layout = QGridLayout(self.spawn_nades_container)
        self.spawn_nades_layout.setContentsMargins(10, 0, 0, 0)
        self.spawn_nades_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        self.starting_left_label = QLabel("Left", self)
        self.starting_left_label.setContentsMargins(0, 0, 0, 0)
        self.starting_left_label.setObjectName("HostIDLabel")
        
        self.starting_right_label = QLabel("Right", self)
        self.starting_right_label.setContentsMargins(0, 0, 0, 0)
        self.starting_right_label.setObjectName("HostIDLabel")
        
        self.spawn_1_left_edit = KeybindEdit(self, "SpawnOneNadeLeft", "Ctrl+1")
        self.spawn_1_left_edit.setContentsMargins(0, 0, 0, 15)
        
        self.spawn_2_left_edit = KeybindEdit(self, "SpawnTwoNadesLeft", "Ctrl+2")
        self.spawn_2_left_edit.setContentsMargins(0, 0, 0, 15)
        
        self.spawn_3_left_edit = KeybindEdit(self, "SpawnThreeNadesLeft", "Ctrl+3")
        
        self.spawn_1_right_edit = KeybindEdit(self, "SpawnOneNadeRight", "Alt+1")
        self.spawn_1_right_edit.setContentsMargins(0, 0, 0, 15)
        
        self.spawn_2_right_edit = KeybindEdit(self, "SpawnTwoNadesRight", "Alt+2")
        self.spawn_2_right_edit.setContentsMargins(0, 0, 0, 15)
        
        self.spawn_3_right_edit = KeybindEdit(self, "SpawnThreeNadesRight", "Alt+3")
        
        self.label_1 = QLabel("1", self)
        self.label_1.setObjectName("HostIDLabel")
        self.label_1.setFixedWidth(150)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_1.setContentsMargins(0, 0, 0, 15)
        
        self.label_2 = QLabel("2", self)
        self.label_2.setObjectName("HostIDLabel")
        self.label_2.setFixedWidth(150)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setContentsMargins(0, 0, 0, 15)
        
        self.label_3 = QLabel("3", self)
        self.label_3.setObjectName("HostIDLabel")
        self.label_3.setFixedWidth(150)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.spawn_nades_layout.addWidget(self.starting_left_label, 0, 0)
        self.spawn_nades_layout.addWidget(self.starting_right_label, 0, 2)
        self.spawn_nades_layout.addWidget(self.spawn_1_left_edit, 1, 0)
        self.spawn_nades_layout.addWidget(self.spawn_2_left_edit, 2, 0)
        self.spawn_nades_layout.addWidget(self.spawn_3_left_edit, 3, 0)
        self.spawn_nades_layout.addWidget(self.spawn_1_right_edit, 1, 2)
        self.spawn_nades_layout.addWidget(self.spawn_2_right_edit, 2, 2)
        self.spawn_nades_layout.addWidget(self.spawn_3_right_edit, 3, 2)
        self.spawn_nades_layout.addWidget(self.label_1, 1, 1)
        self.spawn_nades_layout.addWidget(self.label_2, 2, 1)
        self.spawn_nades_layout.addWidget(self.label_3, 3, 1)
        
        self.spawn_nades_hline = HLine(self, h=self.line_height)
        self.spawn_nades_hline.setObjectName("DivLine")
        
        self.misc_label = QLabel("Miscellaneous")
        self.misc_label.setContentsMargins(0, 0, 0, 15)
        self.misc_label.setObjectName("ItemsHeaderName")
        
        self.spawn_single_nade_label = QLabel("Spawn single nade", self)
        self.spawn_single_nade_label.setContentsMargins(10, 0, 0, 0)
        self.spawn_single_nade_label.setObjectName("HostIDLabel")
        
        self.spawn_single_nade_edit = KeybindEdit(self, "SpawnSingleNade", "Ctrl+Y", 220)
        self.spawn_single_nade_edit.setContentsMargins(10, 0, 0, 15)
        
        self.ghost_host_label = QLabel("Ghost host", self)
        self.ghost_host_label.setContentsMargins(10, 0, 0, 0)
        self.ghost_host_label.setObjectName("HostIDLabel")
        
        self.ghost_host_edit = KeybindEdit(self, "GhostHost", "Ctrl+Shift+K", 220)
        self.ghost_host_edit.setContentsMargins(10, 0, 0, 15)
        
        self.spawn_hr_label = QLabel("Spawn hunting rifle and ziplines", self)
        self.spawn_hr_label.setContentsMargins(10, 0, 0, 0)
        self.spawn_hr_label.setObjectName("HostIDLabel")
        
        self.spawn_hr_edit = KeybindEdit(self, "SpawnHrAndZiplines", "Ctrl+Shift+S", 220)
        self.spawn_hr_edit.setContentsMargins(10, 0, 0, 15)
        
        self.content_layout.addWidget(self.spawn_nades_label)
        self.content_layout.addWidget(self.spawn_nades_container)
        self.content_layout.addSpacing(8)
        self.content_layout.addWidget(self.spawn_nades_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.misc_label)
        self.content_layout.addWidget(self.spawn_single_nade_label)
        self.content_layout.addWidget(self.spawn_single_nade_edit)
        self.content_layout.addWidget(self.ghost_host_label)
        self.content_layout.addWidget(self.ghost_host_edit)
        self.content_layout.addWidget(self.spawn_hr_label)
        self.content_layout.addWidget(self.spawn_hr_edit)
    