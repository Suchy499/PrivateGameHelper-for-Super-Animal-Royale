from core import *
from widgets import RoundsSidebar, VLine, HLine, Button, Popup
from images import IMAGES
import pyperclip
from dataclasses import fields, asdict
import csv
import re

class Rounds(QWidget):
    def __init__(self, parent, tournament_id: str):
        super().__init__(parent)
        
        self.tournament_id = tournament_id
        
        self.page_layout = QHBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.rounds_list = RoundsSidebar(self)
        self.rounds_list.setObjectName("Content")
        self.scroll_area.setWidget(self.rounds_list)
        self.scroll_area.setFixedWidth(self.rounds_list.width())
        self.scroll_area.setContentsMargins(0, 0, 0, 0)
        
        self.dividing_line = VLine(self)
        
        self.rounds_widget = QStackedWidget(self)
        
        self.rounds: list[SavedRound] = []
        
        self.new_round_page = NewRound(self, self.tournament_id)
        self.rounds_widget.addWidget(self.new_round_page)
        
        self.page_layout.addWidget(self.scroll_area)
        self.page_layout.addWidget(self.dividing_line)
        self.page_layout.addWidget(self.rounds_widget)
        
        new_round_btn = {
            "icon": IMAGES["add"],
            "text": "New Round",
            "page": self.new_round_page,
        }
        
        self.rounds_list.add_button(new_round_btn)
        
        self.load_rounds()
        self.rounds_list.select_page(self.new_round_page)
        
        self.rounds_list.pageSelected.connect(self.rounds_widget.setCurrentWidget)
        glb.SIGNAL_MANAGER.roundSaved.connect(self.add_round)
        glb.SIGNAL_MANAGER.tournamentUpdated.connect(self.update_scoring)
    
    def add_round(self, tournament_id: str, round_id: int) -> None:
        if tournament_id != self.tournament_id:
            return
        saved_round = SavedRound(self, tournament_id, round_id)
        saved_round.roundDeleted.connect(self.delete_round)
        self.rounds_widget.addWidget(saved_round)
        self.rounds.append(saved_round)
        btn = {
            "icon": None,
            "text": f"Round {round_id}",
            "page": saved_round,
            "insert_at": 0 if not self.rounds_list.buttons else len(self.rounds_list.buttons) - 1
        }
        self.rounds_list.add_button(btn)
    
    def load_rounds(self) -> None:
        rounds_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "participants.json")
        if not os.path.exists(rounds_path):
            return
        with open(rounds_path, "r") as f:
            data = json.load(f)
        for round_id in data["rounds"]:
            self.add_round(self.tournament_id, round_id)
    
    def delete_round(self, round_widget: QWidget) -> None:
        self.rounds.remove(round_widget)
        self.rounds_widget.removeWidget(round_widget)
        self.rounds_list.remove_button(self.rounds_list.get_btn_by_page(round_widget))
        self.rounds_list.select_page(self.new_round_page)
        glb.SIGNAL_MANAGER.roundDeleted.emit(self.tournament_id)
    
    def update_scoring(self, tournament_id: str):
        if tournament_id != self.tournament_id:
            return
        
        for saved_round in self.rounds:
            saved_round.update_scoring(self.tournament_id)
        
        self.new_round_page.update_scores(self.tournament_id)
        
        glb.SIGNAL_MANAGER.scoresUpdated.emit(self.tournament_id)

class NewRound(QWidget):
    def __init__(self, parent, tournament_id: str):
        super().__init__(parent)
        
        self.tournament_id = tournament_id
        
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0, 0, 0, 0)
        
        self.table_labels = QWidget(self)
        self.table_labels.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.table_labels_layout = QGridLayout(self.table_labels)
        self.table_labels_layout.setContentsMargins(9, 9, 16, 9)
        self.table_labels_layout.setSpacing(0)
        
        self.ranking_label = QLabel(self, text="RANKING")
        self.ranking_label.setObjectName("PresetNameLabel")
        self.ranking_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.player_name_label = QLabel(self, text="PLAYER NAME")
        self.player_name_label.setObjectName("PresetNameLabel")
        self.player_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.kills_label = QLabel(self, text="KILLS")
        self.kills_label.setObjectName("PresetNameLabel")
        self.kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.kill_points_label = QLabel(self, text="KILL\nPOINTS")
        self.kill_points_label.setObjectName("PresetNameLabel")
        self.kill_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.placement_points_label = QLabel(self, text="PLACEMENT\nPOINTS")
        self.placement_points_label.setObjectName("PresetNameLabel")
        self.placement_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.total_points_label = QLabel(self, text="TOTAL\nPOINTS")
        self.total_points_label.setObjectName("PresetNameLabel")
        self.total_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.table_labels_layout.addWidget(self.ranking_label, 0, 0)
        self.table_labels_layout.addWidget(self.player_name_label, 0, 1, 1, 3)
        self.table_labels_layout.addWidget(self.kills_label, 0, 4)
        self.table_labels_layout.addWidget(self.kill_points_label, 0, 5)
        self.table_labels_layout.addWidget(self.placement_points_label, 0, 6)
        self.table_labels_layout.addWidget(self.total_points_label, 0, 7)
        
        self.hline = HLine(self, h=2)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.stats_widget = QWidget(self)
        self.stats_widget.setObjectName("Content")
        self.scroll_area.setWidget(self.stats_widget)
        self.stats_layout = QGridLayout(self.stats_widget)
        self.stats_layout.setContentsMargins(9, 0, 9, 9)
        self.stats_layout.setSpacing(0)
        
        self.buttons_container = QWidget(self)
        self.buttons_layout = QHBoxLayout(self.buttons_container)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buttons_layout.setSpacing(20)
        
        self.paste_button = Button(self, "Paste scores")
        self.paste_button.setToolTip("Use /getplayers at the end of a game to copy the scores to your clipboard")
        self.paste_button.clicked.connect(self.paste_scores)
        
        self.confirm_button = Button(self, "Confirm")
        self.confirm_button.clicked.connect(self.confirm_round)
        
        self.clear_button = Button(self, "Clear", btn_style="ButtonDelete")
        self.clear_button.clicked.connect(self.clear_round)
        
        self.buttons_layout.addWidget(self.paste_button)
        self.buttons_layout.addWidget(self.confirm_button)
        self.buttons_layout.addWidget(self.clear_button)
        
        self.page_layout.addWidget(self.table_labels, alignment=Qt.AlignmentFlag.AlignTop)
        self.page_layout.addWidget(self.hline, alignment=Qt.AlignmentFlag.AlignTop)
        self.page_layout.addWidget(self.scroll_area)
        self.page_layout.addWidget(self.buttons_container, alignment=Qt.AlignmentFlag.AlignBottom)
        
        self.player_list: list[Player] = []
        self.leaderboard: dict[str, dict[str, Any]] = {}
    
    def get_scoring(self, tournament_id: str) -> dict:
        try:
            tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", tournament_id)
            with open(os.path.join(tournament_path, "scoring.json"), "r") as f:
                return json.load(f)
        except:
            send_notification("Could not load scoring.", "NotifFail")
            
    def get_metadata(self) -> dict:
        try:
            tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
            with open(os.path.join(tournament_path, "metadata.json"), "r") as f:
                return json.load(f)
        except:
            send_notification("Could not load metadata.", "NotifFail")
    
    def get_players_list(self) -> list[Player]:
        try:
            clipboard: list[str] = pyperclip.paste().strip().split("\n")
            clipboard.pop(0)
            player_list: list[Player] = []
            for player in clipboard:
                player_data = player.split("\t")
                player_id = int(player_data.pop(0))
                placement = int(player_data.pop())
                kills = int(player_data.pop())
                team_id = int(player_data.pop())
                squad_id = int(player_data.pop())
                playfab_id = player_data.pop()
                name = "".join(player_data)
                if placement > 0:
                    player_list.append(Player(player_id, name, playfab_id, squad_id, team_id, kills, placement))
            return sorted(player_list, key=lambda player: player.placement)
        except ValueError:
            send_notification("Invalid player list. Try again", "NotifFail")
            return []
        except IndexError:
            send_notification("Invalid player list. Try again", "NotifFail")
            return []
    
    def save_round_file(self, player_list: list[Player]) -> int:
        rounds_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "Rounds")
        
        if not os.path.exists(rounds_path):
            os.makedirs(rounds_path)
            
        files: list[str] = os.listdir(rounds_path)
        rounds: list[int] = []
        
        for round_file in files:
            if re.match(r"^\d+\.csv$", round_file):
                rounds.append(int(os.path.splitext(round_file)[0]))
                
        new_round_id = 1 if len(rounds) == 0 else max(rounds) + 1
        with open(os.path.join(rounds_path, f"{new_round_id}.csv"), "w", encoding="UTF-8", newline="") as f:
            header = [fld.name for fld in fields(Player)]
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            for player in player_list:
                csv_writer.writerow(list(asdict(player).values()))

        return new_round_id
    
    def save_round_scores(self, leaderboard: dict, round_id: int) -> None:
        scores_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "participants.json")
        scores: list = []
        
        if os.path.exists(scores_path):
            with open(scores_path, "r") as f:
                data = json.load(f)
            data["rounds"].append(round_id)
            scores = data["players"]
        else:
            data = {
                "rounds": [round_id],
                "players": []
            }
        
        for playfab_id, player in leaderboard.items():
            for saved_player in scores:
                if type(saved_player["playfab_id"]) == str:
                    saved_player["playfab_id"] = {saved_player["playfab_id"]}
                
                if type(playfab_id) == str:
                    playfab_id = {playfab_id}
                
                if playfab_id.issubset(saved_player["playfab_id"]):
                    saved_player["rounds_played"].append(
                        {
                            "id": round_id,
                            "kills": player["kills"],
                            "placement": player["placement"],
                            "kill_points": player["kill_points"],
                            "placement_points": player["placement_points"],
                            "score": player["score"]
                        }
                    )
                    break
            else:
                if type(playfab_id) in (frozenset, set):
                    playfab_id = list(playfab_id)
                elif type(playfab_id) == str:
                    playfab_id = [playfab_id]
                scores.append(
                    {
                        "playfab_id": playfab_id,
                        "name": player["name"],
                        "rounds_played": [
                            {
                                "id": round_id,
                                "kills": player["kills"],
                                "placement": player["placement"],
                                "kill_points": player["kill_points"],
                                "placement_points": player["placement_points"],
                                "score": player["score"]
                            }
                        ]
                    }
                )
        
        data["players"] = scores
        
        with open(scores_path, "w") as f:
            json.dump(data, f, indent=4)
    
    def calculate_scores(self) -> dict[str, dict[str, int | float | str]]:
        scoring = self.get_scoring(self.tournament_id)
        metadata = self.get_metadata()
        
        leaderboard: dict[str, dict[str, Any]] = {}
        
        player_list = self.player_list
        
        if metadata["mode"] != "Solo":
            squad_dict = {}
            
            for player in self.player_list:
                if player.squad_id not in squad_dict:
                    squad_dict[player.squad_id] = {
                        "playfab_id": set(),
                        "name": [],
                        "kills": 0,
                        "placement": player.placement
                    }
                    
                squad_dict[player.squad_id]["playfab_id"].add(player.playfab_id)
                squad_dict[player.squad_id]["name"].append(player.name)
                squad_dict[player.squad_id]["kills"] += player.kills
            
            player_list: list[Player] = []
            for squad_id, squad in squad_dict.items():
                player_list.append(Player(0, squad["name"], frozenset(squad["playfab_id"]), squad_id, 0, squad["kills"], squad["placement"]))
            
            player_list.sort(key=lambda team: team.placement)
            
            for ranking, team in enumerate(player_list):
                team.placement = ranking + 1
        
        max_kills = max([player.kills for player in player_list])
        kill_leaders = frozenset([player.playfab_id for player in player_list if player.kills == max_kills])
        
        for player in player_list:
            kill_points = 0
            placement_points = 0
            
            for placement_range in scoring["placement_ranges"]:
                if int(player.placement) >= placement_range["from"] and int(player.placement) <= placement_range["to"]:
                    placement_points = placement_range["points"]
                    break
            
            if not scoring["static_kill_points"]:
                for placement_range in scoring["placement_ranges"]:
                    if int(player.placement) >= placement_range["from"] and int(player.placement) <= placement_range["to"]:
                        if scoring["kill_cap"] > 0 and int(player.kills) > scoring["kill_cap"]:
                            kill_points = scoring["kill_cap"] * placement_range["placement_kill_points"]
                        else:
                            kill_points = int(player.kills) * placement_range["placement_kill_points"]
            else:
                if scoring["kill_cap"] > 0 and int(player.kills) > scoring["kill_cap"]:
                    kill_points = scoring["kill_cap"] * scoring["kill_points"]
                else:
                    kill_points = int(player.kills) * scoring["kill_points"]
            
            if player.playfab_id in kill_leaders:
                kill_points += scoring["kill_leader_game"]
            
            total_points = placement_points + kill_points
            
            leaderboard[player.playfab_id] = {
                "name": player.name,
                "kills": int(player.kills),
                "placement": int(player.placement),
                "kill_points": round(kill_points, 1),
                "placement_points": round(placement_points, 1),
                "score": round(total_points, 1)
            }
            
        return leaderboard
    
    def display_leaderboard(self, leaderboard: dict[str, dict[str, Any]]) -> None:
        for index, player in enumerate(leaderboard.values()):
            if type(player["name"]) == list:
                display_name = ""
                for name in player["name"]:
                    if len(name) > 22:
                        display_name += f"{name[:20]}...\n"
                    else:
                        display_name += f"{name}\n"
                display_name = display_name.strip()
            else:
                if len(player["name"]) > 26:
                    display_name = f"{player["name"][:24]}..."
                else:
                    display_name = player["name"]
            
            ranking_label = QLabel(self, text=str(player["placement"]))
            ranking_label.setObjectName("LeaderboardLabel")
            ranking_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            name_label = QLabel(self, text=display_name)
            name_label.setObjectName("LeaderboardLabel")
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
            
            kills_label = QLabel(self, text=str(player["kills"]))
            kills_label.setObjectName("LeaderboardLabel")
            kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            kill_points_label = QLabel(self, text=str(player["kill_points"]))
            kill_points_label.setObjectName("LeaderboardLabel")
            kill_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            placement_points_label = QLabel(self, text=str(player["placement_points"]))
            placement_points_label.setObjectName("LeaderboardLabel")
            placement_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            total_points_label = QLabel(self, text=str(player["score"]))
            total_points_label.setObjectName("LeaderboardLabel")
            total_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            row_index = self.stats_layout.rowCount()

            match player["placement"]:
                case 1:
                    ranking_label.setStyleSheet("background: #EFBF04")
                    name_label.setStyleSheet("background: #EFBF04")
                    kills_label.setStyleSheet("background: #EFBF04")
                    kill_points_label.setStyleSheet("background: #EFBF04")
                    placement_points_label.setStyleSheet("background: #EFBF04")
                    total_points_label.setStyleSheet("background: #EFBF04")
                case 2:
                    ranking_label.setStyleSheet("background: #C4C4C4")
                    name_label.setStyleSheet("background: #C4C4C4")
                    kills_label.setStyleSheet("background: #C4C4C4")
                    kill_points_label.setStyleSheet("background: #C4C4C4")
                    placement_points_label.setStyleSheet("background: #C4C4C4")
                    total_points_label.setStyleSheet("background: #C4C4C4")
                case 3:
                    ranking_label.setStyleSheet("background: #CE8946")
                    name_label.setStyleSheet("background: #CE8946")
                    kills_label.setStyleSheet("background: #CE8946")
                    kill_points_label.setStyleSheet("background: #CE8946")
                    placement_points_label.setStyleSheet("background: #CE8946")
                    total_points_label.setStyleSheet("background: #CE8946")
            
            self.stats_layout.addWidget(ranking_label, row_index, 0)
            self.stats_layout.addWidget(name_label, row_index, 1, 1, 3)
            self.stats_layout.addWidget(kills_label, row_index, 4)
            self.stats_layout.addWidget(kill_points_label, row_index, 5)
            self.stats_layout.addWidget(placement_points_label, row_index, 6)
            self.stats_layout.addWidget(total_points_label, row_index, 7)
            
            if index < len(leaderboard) - 1:
                div_line = HLine(self, h=1)
                div_line.setObjectName("DivLine")
                div_line.setContentsMargins(0, 0, 0, 0)
                row_index += 1
                self.stats_layout.addWidget(div_line, row_index, 0, 1, 8)
    
    def paste_scores(self) -> None:
        self.player_list = self.get_players_list()
        if not self.player_list:
            return
        
        self.clear_layout()
        self.leaderboard = self.calculate_scores()
        self.display_leaderboard(self.leaderboard)
    
    def update_scores(self, tournament_id: str) -> None:
        if tournament_id != self.tournament_id:
            return
        if not self.player_list:
            return
        
        self.clear_layout()
        self.leaderboard = self.calculate_scores()
        self.display_leaderboard(self.leaderboard)
    
    def clear_layout(self) -> None:
        while self.stats_layout.count():
            child = self.stats_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def clear_round(self) -> None:
        self.clear_layout()
        self.player_list.clear()
        self.leaderboard.clear()

    def confirm_round(self) -> None:
        if self.player_list:
            new_round_id = self.save_round_file(self.player_list)
            self.save_round_scores(self.leaderboard, new_round_id)
            glb.SIGNAL_MANAGER.roundSaved.emit(self.tournament_id, new_round_id)
            self.clear_round()
            send_notification("Round saved!", "NotifSuccess")
        else:
            send_notification("To save a round, you must first paste the scroes", "NotifFail")

class SavedRound(QWidget):
    roundDeleted = Signal(object)
    def __init__(self, parent, tournament_id: str, round_id: int):
        super().__init__(parent)
        
        self.tournament_id = tournament_id
        self.round_id = round_id
        
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0, 0, 0, 0)
        
        self.table_labels = QWidget(self)
        self.table_labels.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.table_labels_layout = QGridLayout(self.table_labels)
        self.table_labels_layout.setContentsMargins(9, 9, 16, 9)
        self.table_labels_layout.setSpacing(0)
        
        self.ranking_label = QLabel(self, text="RANKING")
        self.ranking_label.setObjectName("PresetNameLabel")
        self.ranking_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.player_name_label = QLabel(self, text="PLAYER NAME")
        self.player_name_label.setObjectName("PresetNameLabel")
        self.player_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.kills_label = QLabel(self, text="KILLS")
        self.kills_label.setObjectName("PresetNameLabel")
        self.kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.kill_points_label = QLabel(self, text="KILL\nPOINTS")
        self.kill_points_label.setObjectName("PresetNameLabel")
        self.kill_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.placement_points_label = QLabel(self, text="PLACEMENT\nPOINTS")
        self.placement_points_label.setObjectName("PresetNameLabel")
        self.placement_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.total_points_label = QLabel(self, text="TOTAL\nPOINTS")
        self.total_points_label.setObjectName("PresetNameLabel")
        self.total_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.table_labels_layout.addWidget(self.ranking_label, 0, 0)
        self.table_labels_layout.addWidget(self.player_name_label, 0, 1, 1, 3)
        self.table_labels_layout.addWidget(self.kills_label, 0, 4)
        self.table_labels_layout.addWidget(self.kill_points_label, 0, 5)
        self.table_labels_layout.addWidget(self.placement_points_label, 0, 6)
        self.table_labels_layout.addWidget(self.total_points_label, 0, 7)
        
        self.hline = HLine(self, h=2)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.stats_widget = QWidget(self)
        self.stats_widget.setObjectName("Content")
        self.scroll_area.setWidget(self.stats_widget)
        self.stats_layout = QGridLayout(self.stats_widget)
        self.stats_layout.setContentsMargins(9, 0, 9, 9)
        self.stats_layout.setSpacing(0)
        
        self.delete_button = Button(self, "Delete Round", btn_style="ButtonDelete", w=300)
        
        self.page_layout.addWidget(self.table_labels, alignment=Qt.AlignmentFlag.AlignTop)
        self.page_layout.addWidget(self.hline, alignment=Qt.AlignmentFlag.AlignTop)
        self.page_layout.addWidget(self.scroll_area)
        self.page_layout.addWidget(self.delete_button, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        
        self.confirm_popup = Popup(
            self, 
            "Confirm", 
            "Are you sure you want to\ndelete this round?",
            300,
            150,
            Button(None, "Cancel", btn_style="ButtonDelete"),
            Button(None, "Delete", btn_style="ButtonDefault")
        )
        
        self.confirm_popup.buttons[0].clicked.connect(self.confirm_popup.hide)
        self.confirm_popup.buttons[1].clicked.connect(self.delete_round)

        self.confirm_popup.hide()
        
        self.delete_button.clicked.connect(self.open_popup)
        
        leaderboard = self.load_round(self.round_id)
        self.display_round(leaderboard)
        
    def get_scoring(self, tournament_id: str) -> dict:
        try:
            tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", tournament_id)
            with open(os.path.join(tournament_path, "scoring.json"), "r") as f:
                return json.load(f)
        except:
            send_notification("Could not load scoring.", "NotifFail")
            
    def get_metadata(self) -> dict:
        try:
            tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
            with open(os.path.join(tournament_path, "metadata.json"), "r") as f:
                return json.load(f)
        except:
            send_notification("Could not load metadata.", "NotifFail")
            
    def clear_round(self) -> None:
        while self.stats_layout.count():
            child = self.stats_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def load_round(self, round_id: int) -> None:
        scores_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "participants.json")
        
        with open(scores_path, "r") as f:
            data = json.load(f)
        
        leaderboard = []
        
        for participant in data["players"]:
            for round_played in participant["rounds_played"]:
                if not round_played["id"] == round_id:
                    continue
                
                if type(participant["name"]) != str:
                    display_name = ""
                    for name in participant["name"]:
                        if len(name) > 22:
                            display_name += f"{name[:20]}...\n"
                        else:
                            display_name += f"{name}\n"
                    display_name = display_name.strip()
                else:
                    display_name = participant["name"]
                
                leaderboard.append({
                    "playfab_id": tuple(participant["playfab_id"]),
                    "name": display_name,
                    "kills": round_played["kills"],
                    "placement": round_played["placement"],
                    "kill_points": round_played["kill_points"],
                    "placement_points": round_played["placement_points"],
                    "score": round_played["score"]
                })
        
        leaderboard.sort(key=lambda player: player["placement"])
        
        return leaderboard
        
    def display_round(self, leaderboard: list[dict]):
        for index, player in enumerate(leaderboard):
            ranking_label = QLabel(self, text=str(player["placement"]))
            ranking_label.setObjectName("LeaderboardLabel")
            ranking_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            name_label = QLabel(self, text=player["name"])
            name_label.setObjectName("LeaderboardLabel")
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
            
            kills_label = QLabel(self, text=str(player["kills"]))
            kills_label.setObjectName("LeaderboardLabel")
            kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            kill_points_label = QLabel(self, text=str(player["kill_points"]))
            kill_points_label.setObjectName("LeaderboardLabel")
            kill_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            placement_points_label = QLabel(self, text=str(player["placement_points"]))
            placement_points_label.setObjectName("LeaderboardLabel")
            placement_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            total_points_label = QLabel(self, text=str(player["score"]))
            total_points_label.setObjectName("LeaderboardLabel")
            total_points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            row_index = self.stats_layout.rowCount()

            match int(player["placement"]):
                case 1:
                    ranking_label.setStyleSheet("background: #EFBF04")
                    name_label.setStyleSheet("background: #EFBF04")
                    kills_label.setStyleSheet("background: #EFBF04")
                    kill_points_label.setStyleSheet("background: #EFBF04")
                    placement_points_label.setStyleSheet("background: #EFBF04")
                    total_points_label.setStyleSheet("background: #EFBF04")
                case 2:
                    ranking_label.setStyleSheet("background: #C4C4C4")
                    name_label.setStyleSheet("background: #C4C4C4")
                    kills_label.setStyleSheet("background: #C4C4C4")
                    kill_points_label.setStyleSheet("background: #C4C4C4")
                    placement_points_label.setStyleSheet("background: #C4C4C4")
                    total_points_label.setStyleSheet("background: #C4C4C4")
                case 3:
                    ranking_label.setStyleSheet("background: #CE8946")
                    name_label.setStyleSheet("background: #CE8946")
                    kills_label.setStyleSheet("background: #CE8946")
                    kill_points_label.setStyleSheet("background: #CE8946")
                    placement_points_label.setStyleSheet("background: #CE8946")
                    total_points_label.setStyleSheet("background: #CE8946")
            
            self.stats_layout.addWidget(ranking_label, row_index, 0)
            self.stats_layout.addWidget(name_label, row_index, 1, 1, 3)
            self.stats_layout.addWidget(kills_label, row_index, 4)
            self.stats_layout.addWidget(kill_points_label, row_index, 5)
            self.stats_layout.addWidget(placement_points_label, row_index, 6)
            self.stats_layout.addWidget(total_points_label, row_index, 7)
            
            if index < len(leaderboard) - 1:
                div_line = HLine(self, h=1)
                div_line.setObjectName("DivLine")
                div_line.setContentsMargins(0, 0, 0, 0)
                row_index += 1
                self.stats_layout.addWidget(div_line, row_index, 0, 1, 8)
    
    def save_round_scores(self, leaderboard: dict, round_id: int) -> None:
        scores_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "participants.json")
        
        if not os.path.exists(scores_path):
            return
        
        with open(scores_path, "r") as f:
            data = json.load(f)
            
        scores = data["players"]
        
        for player in leaderboard:
            for saved_player in scores:
                if player["playfab_id"] != tuple(saved_player["playfab_id"]):
                    continue
                
                for played_round in saved_player["rounds_played"]:
                    if int(played_round["id"]) != round_id:
                        continue
                    
                    played_round["kill_points"] = player["kill_points"]
                    played_round["placement_points"] = player["placement_points"]
                    played_round["score"] = player["score"]
        
        data["players"] = scores
        
        with open(scores_path, "w") as f:
            json.dump(data, f, indent=4)
    
    def update_scoring(self, tournament_id: str):
        if tournament_id != self.tournament_id:
            return
        
        self.clear_round()
        
        scoring = self.get_scoring(self.tournament_id)
        leaderboard = self.load_round(self.round_id)
        
        if not leaderboard:
            return

        max_kills = max([player["kills"] for player in leaderboard])
        kill_leaders = frozenset([player["playfab_id"] for player in leaderboard if player["kills"] == max_kills])
        
        for player in leaderboard:
            kill_points = 0
            placement_points = 0
            
            for placement_range in scoring["placement_ranges"]:
                if int(player["placement"]) >= placement_range["from"] and int(player["placement"]) <= placement_range["to"]:
                    placement_points = placement_range["points"]
                    break
            
            if not scoring["static_kill_points"]:
                for placement_range in scoring["placement_ranges"]:
                    if int(player["placement"]) >= placement_range["from"] and int(player["placement"]) <= placement_range["to"]:
                        if scoring["kill_cap"] > 0 and int(player["kills"]) > scoring["kill_cap"]:
                            kill_points = scoring["kill_cap"] * placement_range["placement_kill_points"]
                        else:
                            kill_points = int(player["kills"]) * placement_range["placement_kill_points"]
            else:
                if scoring["kill_cap"] > 0 and int(player["kills"]) > scoring["kill_cap"]:
                    kill_points = scoring["kill_cap"] * scoring["kill_points"]
                else:
                    kill_points = int(player["kills"]) * scoring["kill_points"]
            
            if player["playfab_id"] in kill_leaders:
                kill_points += scoring["kill_leader_game"]
            
            player["kill_points"] = kill_points
            player["placement_points"] = placement_points
            player["score"] = placement_points + kill_points
        
        self.save_round_scores(leaderboard, self.round_id)
        self.display_round(leaderboard)
    
    def delete_round(self) -> None:
        try:
            round_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "Rounds", f"{self.round_id}.csv")
            os.remove(round_path)
        except FileNotFoundError:
            send_notification("Could not delete round.", "NotifFail")
        
        scores_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "participants.json")
        
        if os.path.exists(scores_path):
            with open(scores_path, "r") as f:
                data = json.load(f)
            
            rounds: list[int] = data["rounds"]
            rounds.remove(self.round_id)
            scores = data["players"]
            
            for player in scores:
                for saved_round in player["rounds_played"]:
                    if saved_round["id"] == self.round_id:
                        player["rounds_played"].remove(saved_round)
                        break

            data = {
                "rounds": rounds,
                "players": scores
            }
            
            with open(scores_path, "w") as f:
                json.dump(data, f, indent=4)
                
        self.confirm_popup.hide()
        self.roundDeleted.emit(self)
    
    def open_popup(self) -> None:
        self.confirm_popup.setGeometry(
            (self.width()-self.confirm_popup.width())/2,
            (self.height()-self.confirm_popup.height())/2,
            self.confirm_popup.width(),
            self.confirm_popup.height()
        )
        self.confirm_popup.show()