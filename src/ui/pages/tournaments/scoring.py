from core import *
from widgets import VLine, Toggle, Button, SettingsComboBox
from images import IMAGES

class Scoring(QWidget):
    def __init__(self, parent, tournament_id: str):
        super().__init__(parent)
        
        self.tournament_id = tournament_id
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(9, 0, 9, 0)
        
        self.scoring_widget = QWidget(self)
        self.page_layout = QHBoxLayout(self.scoring_widget)
        self.page_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(self.scoring_widget)
        
        self.left_widget = QWidget(self)
        self.left_widget.setFixedWidth(400)
        self.vline = VLine(self)
        self.right_widget = QWidget(self)
        
        self.left_widget_layout = QVBoxLayout(self.left_widget)
        self.right_widget_layout = QVBoxLayout(self.right_widget)
        
        self.left_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.right_widget_layout.setContentsMargins(9, 0, 0, 0)
        
        self.left_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.right_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.page_layout.addWidget(self.left_widget)
        self.page_layout.addWidget(self.vline)
        self.page_layout.addWidget(self.right_widget)
        
        self.kills_label = QLabel(self, text="Kills")
        self.kills_label.setContentsMargins(-9, 0, 0, 15)
        self.kills_label.setObjectName("PregameHeaderName")
        
        self.placement_label = QLabel(self, text="Placement")
        self.placement_label.setContentsMargins(-9, 0, 0, 15)
        self.placement_label.setObjectName("PregameHeaderName")
        
        self.left_widget_layout.addWidget(self.kills_label)
        self.right_widget_layout.addWidget(self.placement_label)
        
        # LEFT WIDGET
        
        self.static_kill_points_label = QLabel(self, text="Static kill points")
        self.static_kill_points_label.setObjectName("PresetNameLabel")
        self.static_kill_points_label.setContentsMargins(0, 0, 0, 0)
        self.static_kill_points_label.setToolTip("If enabled, all kills will be worth the same amount of points regardless of placement")
        
        self.static_kill_points_toggle = Toggle(self, default_state=True)
        self.static_kill_points_toggle.stateChanged.connect(lambda: glb.SIGNAL_MANAGER.killPointsToggled.emit(self.static_kill_points_toggle.isChecked(), self.tournament_id))
        self.static_kill_points_toggle.setToolTip("If enabled, all kills will be worth the same amount of points regardless of placement")
        
        self.kill_points_label = QLabel(self, text="Points per kill")
        self.kill_points_label.setObjectName("PresetNameLabel")
        self.kill_points_label.setContentsMargins(0, 15, 0, 0)
        
        self.kill_points_spinbox = QDoubleSpinBox(self)
        self.kill_points_spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.kill_points_spinbox.setFixedWidth(221)
        self.kill_points_spinbox.setObjectName("LineEdit")
        self.kill_points_spinbox.setContentsMargins(0, 0, 0, 10)
        self.kill_points_spinbox.setDecimals(1)
        self.kill_points_spinbox.setMaximum(999.9)
        
        self.kill_leader_game_label = QLabel(self, text="Points for most kills in a game")
        self.kill_leader_game_label.setObjectName("PresetNameLabel")
        self.kill_leader_game_label.setContentsMargins(0, 15, 0, 0)
        
        self.kill_leader_game_spinbox = QDoubleSpinBox(self)
        self.kill_leader_game_spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.kill_leader_game_spinbox.setFixedWidth(221)
        self.kill_leader_game_spinbox.setObjectName("LineEdit")
        self.kill_leader_game_spinbox.setContentsMargins(0, 0, 0, 10)
        self.kill_leader_game_spinbox.setDecimals(1)
        self.kill_leader_game_spinbox.setMaximum(999.9)
        
        self.kill_leader_tournament_label = QLabel(self, text="Points for most kills in the tournament")
        self.kill_leader_tournament_label.setObjectName("PresetNameLabel")
        self.kill_leader_tournament_label.setContentsMargins(0, 15, 0, 0)
        
        self.kill_leader_tournament_spinbox = QDoubleSpinBox(self)
        self.kill_leader_tournament_spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.kill_leader_tournament_spinbox.setFixedWidth(221)
        self.kill_leader_tournament_spinbox.setObjectName("LineEdit")
        self.kill_leader_tournament_spinbox.setContentsMargins(0, 0, 0, 10)
        self.kill_leader_tournament_spinbox.setDecimals(1)
        self.kill_leader_tournament_spinbox.setMaximum(999.9)
        
        self.kill_cap_label = QLabel(self, text="Max number of kills that get awarded points (0 - No Limit)")
        self.kill_cap_label.setObjectName("PresetNameLabel")
        self.kill_cap_label.setContentsMargins(0, 15, 0, 0)
        
        self.kill_cap_spinbox = QSpinBox(self)
        self.kill_cap_spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.kill_cap_spinbox.setFixedWidth(221)
        self.kill_cap_spinbox.setObjectName("LineEdit")
        self.kill_cap_spinbox.setContentsMargins(0, 0, 0, 10)
        self.kill_cap_spinbox.setMinimum(0)
        self.kill_cap_spinbox.setMaximum(999)
        
        self.kill_leader_tiebreaker = SettingsComboBox(self, "Kill Leader Tiebreaker", w=220)
        self.kill_leader_tiebreaker.addItems(["All", "Highest Placed", "Lowest Placed"])
        self.kill_leader_tiebreaker.setToolTip("Changes which players get awarded points for most kills in case of a tie")
        
        self.tiebreaker = SettingsComboBox(self, "Tiebreaker", w=220)
        self.tiebreaker.addItems(["Kills", "Average Kills", "Average Placement", "Wins"])
        self.tiebreaker.setToolTip("Changes the value according to which players are ordered in the leaderboard in case of a tie")
        
        self.left_widget_layout.addWidget(self.static_kill_points_label)
        self.left_widget_layout.addWidget(self.static_kill_points_toggle)
        self.left_widget_layout.addWidget(self.kill_points_label)
        self.left_widget_layout.addWidget(self.kill_points_spinbox)
        self.left_widget_layout.addWidget(self.kill_leader_game_label)
        self.left_widget_layout.addWidget(self.kill_leader_game_spinbox)
        self.left_widget_layout.addWidget(self.kill_leader_tournament_label)
        self.left_widget_layout.addWidget(self.kill_leader_tournament_spinbox)
        self.left_widget_layout.addWidget(self.kill_cap_label)
        self.left_widget_layout.addWidget(self.kill_cap_spinbox)
        self.left_widget_layout.addSpacing(10)
        self.left_widget_layout.addWidget(self.kill_leader_tiebreaker)
        self.left_widget_layout.addSpacing(10)
        self.left_widget_layout.addWidget(self.tiebreaker)
        
        # RIGHT WIDGET
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.placement_container = QWidget(self)
        self.scroll_area.setWidget(self.placement_container)
        self.placement_container.setObjectName("Content")
        self.right_widget_layout.addWidget(self.scroll_area)
        
        self.placement_layout = QVBoxLayout(self.placement_container)
        self.placement_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.placement_labels = PlacementLabels(self)
        self.placement_layout.addWidget(self.placement_labels)
        
        self.placement_array: list[TournamentRange] = []
            
        self.new_icon = QPixmap(IMAGES["add"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.new_button = Button(self, " Add Range", self.new_icon, 120, btn_style="ButtonDefault")
        self.new_button.clicked.connect(self.add_range)
        self.placement_layout.addWidget(self.new_button)
        
        self.save_icon = QPixmap(IMAGES["pencil"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.save_button = Button(self, " Save", self.save_icon, w=120)
        self.save_button.clicked.connect(self.save_scoring)
        self.main_layout.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignRight)
        
        glb.SIGNAL_MANAGER.killPointsToggled.connect(self.toggle_static_kill_points)
        glb.SIGNAL_MANAGER.tournamentUpdated.connect(self.load_scoring)
        
        self.load_scoring(self.tournament_id)
    
    def add_range(
        self,
        from_: int | None = None,
        to: int | None = None,
        points: int = 0,
        kill_points: int = 0,
        allow_deletion: bool = True
    ) -> None:
        new_range = TournamentRange(self, allow_deletion)
        if allow_deletion:
            new_range.delete_button.clicked.connect(lambda: self.delete_range(new_range))
        self.placement_layout.insertWidget(self.placement_layout.count()-1, new_range)
        self.placement_array.append(new_range)
        previous_to = self.placement_array[self.placement_array.index(new_range)-1].to
        
        if to:
            new_range.to = to
        else:
            new_range.to = previous_to + 1
        
        if from_:
            new_range.from_ = from_
        else:
            new_range.from_ = previous_to + 1
        
        new_range.placement_points = points
        new_range.placement_kills = kill_points
        
        if self.static_kill_points_toggle.isChecked():
            new_range.placement_kill_points_spinbox.setVisible(False)
        else:
            new_range.placement_kill_points_spinbox.setVisible(True)
    
    def delete_range(self, range_object: object) -> None:
        self.placement_array.remove(range_object)
        range_object.deleteLater()
    
    def clear_ranges(self) -> None:
        for placement_range in reversed(self.placement_array):
            self.delete_range(placement_range)
        
    def toggle_static_kill_points(self, enabled: bool, tournament_id: str) -> None:
        if tournament_id != self.tournament_id:
            return
        if enabled:
            self.kill_points_spinbox.setEnabled(True)
            self.placement_labels.placement_kill_points_label.setVisible(False)
            for placement_range in self.placement_array:
                placement_range.placement_kill_points_spinbox.setVisible(False)
        else:
            self.kill_points_spinbox.setEnabled(False)
            self.placement_labels.placement_kill_points_label.setVisible(True)
            for placement_range in self.placement_array:
                placement_range.placement_kill_points_spinbox.setVisible(True)
    
    def load_scoring(self, tournament_id: str) -> None:
        if tournament_id != self.tournament_id:
            return
        
        self.clear_ranges()
        
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
        with open(os.path.join(tournament_path, "scoring.json"), "r") as f:
            tournament_scoring = json.load(f)
        
        self.static_kill_points_toggle.setChecked(tournament_scoring["static_kill_points"])
        self.kill_points_spinbox.setValue(tournament_scoring["kill_points"])
        self.kill_leader_game_spinbox.setValue(tournament_scoring["kill_leader_game"])
        self.kill_leader_tournament_spinbox.setValue(tournament_scoring["kill_leader_tournament"])
        self.kill_cap_spinbox.setValue(tournament_scoring["kill_cap"])
        for index, placement_range in enumerate(tournament_scoring["placement_ranges"]):
            from_, to, points, kill_points, allow_deletion = placement_range["from"], placement_range["to"], placement_range["points"], placement_range["placement_kill_points"], True
            if index == 0:
                allow_deletion = False
            self.add_range(from_, to, points, kill_points, allow_deletion)
        
        if self.static_kill_points_toggle.isChecked():
            self.kill_points_spinbox.setEnabled(True)
            self.placement_labels.placement_kill_points_label.setVisible(False)
            for placement_range in self.placement_array:
                placement_range.placement_kill_points_spinbox.setVisible(False)
        else:
            self.kill_points_spinbox.setEnabled(False)
            self.placement_labels.placement_kill_points_label.setVisible(True)
            for placement_range in self.placement_array:
                placement_range.placement_kill_points_spinbox.setVisible(True)
        
        try:
            self.kill_leader_tiebreaker.combobox.setCurrentIndex(tournament_scoring["kill_leader_tiebreaker"])
        except KeyError:
            self.kill_leader_tiebreaker.combobox.setCurrentIndex(0)
            
        try:
            self.tiebreaker.combobox.setCurrentIndex(tournament_scoring["tiebreaker"])
        except KeyError:
            self.tiebreaker.combobox.setCurrentIndex(0)
    
    def save_scoring(self) -> None:
        try:
            tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
            placement_ranges = []
            for placement_range in self.placement_array:
                range_data = {
                    "from": placement_range.from_,
                    "to": placement_range.to,
                    "points": placement_range.placement_points,
                    "placement_kill_points": placement_range.placement_kills
                }
                placement_ranges.append(range_data)
            tournament_scoring = {
                "static_kill_points": self.static_kill_points_toggle.isChecked(),
                "kill_points": self.kill_points_spinbox.value(),
                "kill_leader_game": self.kill_leader_game_spinbox.value(),
                "kill_leader_tournament": self.kill_leader_tournament_spinbox.value(),
                "kill_leader_tiebreaker": self.kill_leader_tiebreaker.combobox.currentIndex(),
                "kill_cap": self.kill_cap_spinbox.value(),
                "tiebreaker": self.tiebreaker.combobox.currentIndex(),
                "placement_ranges": placement_ranges
            }
            with open(os.path.join(tournament_path, "scoring.json"), "w") as f:
                json.dump(tournament_scoring, f, indent=4)
            glb.SIGNAL_MANAGER.tournamentUpdated.emit(self.tournament_id)
            send_notification("Scoring has been saved!", "NotifSuccess")
        except Exception as e:
            send_notification("Could not save scoring. Try again", "NotifFail")
            print(e)

class PlacementLabels(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.range_layout = QHBoxLayout(self)
        self.range_layout.setContentsMargins(0, 0, 0, 0)
        self.range_layout.setSpacing(20)
        
        self.from_label = QLabel(self, text="From")
        self.from_label.setObjectName("PresetNameLabel")
        self.from_label.setContentsMargins(0, 0, 0, 0)
        self.from_label.setFixedWidth(70)
        
        self.to_label = QLabel(self, text="To")
        self.to_label.setObjectName("PresetNameLabel")
        self.to_label.setContentsMargins(0, 0, 0, 0)
        self.to_label.setFixedWidth(70)
        
        self.placement_points_label = QLabel(self, text="Points")
        self.placement_points_label.setObjectName("PresetNameLabel")
        self.placement_points_label.setContentsMargins(0, 0, 0, 0)
        self.placement_points_label.setFixedWidth(70)
        
        self.placement_kill_points_label = QLabel(self, text="Kill points")
        self.placement_kill_points_label.setObjectName("PresetNameLabel")
        self.placement_kill_points_label.setContentsMargins(0, 0, 0, 0)
        self.placement_kill_points_label.setFixedWidth(70)
        
        self.delete_label = QLabel(self, text="")
        self.delete_label.setObjectName("PresetNameLabel")
        self.delete_label.setContentsMargins(0, 0, 0, 0)
        self.delete_label.setFixedWidth(100)
        
        self.range_layout.addWidget(self.from_label)
        self.range_layout.addSpacing(40)
        self.range_layout.addWidget(self.to_label)
        self.range_layout.addSpacing(40)
        self.range_layout.addWidget(self.placement_points_label)
        self.range_layout.addWidget(self.placement_kill_points_label)
        self.range_layout.addWidget(self.delete_label)

class TournamentRange(QWidget):
    def __init__(self, parent, allow_deletion: bool = True):
        super().__init__(parent)
        
        self.allow_deletion = allow_deletion
        
        self.range_layout = QHBoxLayout(self)
        self.range_layout.setContentsMargins(0, 0, 0, 0)
        self.range_layout.setSpacing(20)
        
        self.from_spinbox = QSpinBox(self)
        self.from_spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.from_spinbox.setFixedSize(70, 30)
        self.from_spinbox.setObjectName("LineEdit")
        self.from_spinbox.setContentsMargins(0, 0, 0, 0)
        self.from_spinbox.setMinimum(0)
        self.from_minimum = 1
        self.from_maximum = 64
        self.from_spinbox.valueChanged.connect(self.validate_range)
        
        self.dash_label = QLabel(self, text="-")
        self.dash_label.setObjectName("PresetNameLabel")
        self.dash_label.setContentsMargins(0, 0, 0, 0)
        self.dash_label.setFixedWidth(20)
        self.dash_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.to_spinbox = QSpinBox(self)
        self.to_spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.to_spinbox.setFixedSize(70, 30)
        self.to_spinbox.setObjectName("LineEdit")
        self.to_spinbox.setContentsMargins(0, 0, 0, 0)
        self.to_spinbox.setMinimum(0)
        self.to_minimum = 1
        self.to_maximum = 64
        self.to_spinbox.valueChanged.connect(self.validate_range)
        
        self.arrow_label = QLabel(self, text="->")
        self.arrow_label.setObjectName("PresetNameLabel")
        self.arrow_label.setContentsMargins(0, 0, 0, 0)
        self.arrow_label.setFixedWidth(20)
        self.arrow_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.placement_points_spinbox = QDoubleSpinBox(self)
        self.placement_points_spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.placement_points_spinbox.setFixedSize(70, 30)
        self.placement_points_spinbox.setObjectName("LineEdit")
        self.placement_points_spinbox.setContentsMargins(0, 0, 0, 0)
        self.placement_points_spinbox.setDecimals(1)
        self.placement_points_spinbox.setMaximum(999.9)
        
        self.placement_kill_points_spinbox = QDoubleSpinBox(self)
        self.placement_kill_points_spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.placement_kill_points_spinbox.setFixedSize(70, 30)
        self.placement_kill_points_spinbox.setObjectName("LineEdit")
        self.placement_kill_points_spinbox.setContentsMargins(0, 0, 0, 0)
        self.placement_kill_points_spinbox.setDecimals(1)
        self.placement_kill_points_spinbox.setMaximum(999.9)
        
        if allow_deletion:
            self.delete_icon = QPixmap(IMAGES["trash"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
            self.delete_button = Button(self, "Remove", self.delete_icon, btn_style="ButtonDelete")
        else:
            self.delete_button = QLabel(self, text="")
            self.delete_button.setObjectName("PresetNameLabel")
            self.delete_button.setContentsMargins(0, 0, 0, 0)
            self.delete_button.setFixedWidth(100)
        
        self.range_layout.addWidget(self.from_spinbox)
        self.range_layout.addWidget(self.dash_label)
        self.range_layout.addWidget(self.to_spinbox)
        self.range_layout.addWidget(self.arrow_label)
        self.range_layout.addWidget(self.placement_points_spinbox)
        self.range_layout.addWidget(self.placement_kill_points_spinbox)
        self.range_layout.addWidget(self.delete_button)
    
    @property
    def from_(self) -> int:
        return self.from_spinbox.value()
    
    @from_.setter
    def from_(self, value: int) -> None:
        self.from_spinbox.setValue(value)
    
    @property
    def to(self) -> int:
        return self.to_spinbox.value()
    
    @to.setter
    def to(self, value: int) -> None:
        self.to_spinbox.setValue(value)
    
    @property
    def placement_points(self) -> int:
        return self.placement_points_spinbox.value()

    @placement_points.setter
    def placement_points(self, value: int) -> None:
        self.placement_points_spinbox.setValue(value)
    
    @property
    def placement_kills(self) -> int:
        return self.placement_kill_points_spinbox.value()
    
    @placement_kills.setter
    def placement_kills(self, value: int) -> None:
        self.placement_kill_points_spinbox.setValue(value)
    
    @property
    def from_minimum(self) -> int:
        return self.from_spinbox.minimum()
    
    @from_minimum.setter
    def from_minimum(self, value: int) -> None:
        self.from_spinbox.setMinimum(value)
        
    @property
    def from_maximum(self) -> int:
        return self.from_spinbox.maximum()
    
    @from_maximum.setter
    def from_maximum(self, value: int) -> None:
        self.from_spinbox.setMaximum(value)
        
    @property
    def to_minimum(self) -> int:
        return self.to_spinbox.minimum()
    
    @to_minimum.setter
    def to_minimum(self, value: int) -> None:
        self.to_spinbox.setMinimum(value)
        
    @property
    def to_maximum(self) -> int:
        return self.to_spinbox.maximum()
    
    @to_maximum.setter
    def to_maximum(self, value: int) -> None:
        self.to_spinbox.setMaximum(value)
    
    def validate_range(self, value: int) -> None:
        if self.from_ > self.to:
            self.to = self.from_
        self.to_minimum = self.from_