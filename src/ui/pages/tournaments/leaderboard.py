from core import *
from widgets import HLine
from images import IMAGES
import os
import csv
import json

class Leaderboard(QWidget):
    def __init__(self, parent, tournament_id: str):
        super().__init__(parent)
        
        self.tournament_id = tournament_id
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0, 0, 0, 0)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
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
        
        self.games_played = QLabel(self, text="GAMES\nPLAYED")
        self.games_played.setObjectName("PresetNameLabel")
        self.games_played.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.wins_label = QLabel(self, text="WINS")
        self.wins_label.setObjectName("PresetNameLabel")
        self.wins_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.kills_label = QLabel(self, text="KILLS")
        self.kills_label.setObjectName("PresetNameLabel")
        self.kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.average_placement_label = QLabel(self, text="AVERAGE\nPLACEMENT")
        self.average_placement_label.setObjectName("PresetNameLabel")
        self.average_placement_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.average_kills_label = QLabel(self, text="AVERAGE\nKILLS")
        self.average_kills_label.setObjectName("PresetNameLabel")
        self.average_kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.most_kills_label = QLabel(self, text="MOST KILLS\nIN A MATCH")
        self.most_kills_label.setObjectName("PresetNameLabel")
        self.most_kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.score_label = QLabel(self, text="SCORE")
        self.score_label.setObjectName("PresetNameLabel")
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.table_labels_layout.addWidget(self.ranking_label, 0, 0)
        self.table_labels_layout.addWidget(self.player_name_label, 0, 1, 1, 3)
        self.table_labels_layout.addWidget(self.games_played, 0, 4)
        self.table_labels_layout.addWidget(self.wins_label, 0, 5)
        self.table_labels_layout.addWidget(self.kills_label, 0, 6)
        self.table_labels_layout.addWidget(self.average_placement_label, 0, 7)
        self.table_labels_layout.addWidget(self.average_kills_label, 0, 8)
        self.table_labels_layout.addWidget(self.most_kills_label, 0, 9)
        self.table_labels_layout.addWidget(self.score_label, 0, 10)
        
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
        
        self.page_layout.addWidget(self.table_labels)
        self.page_layout.addWidget(self.hline)
        self.page_layout.addWidget(self.scroll_area)
        
        leaderboard = self.calculate_leaderboard()
        self.display_leaderboard(leaderboard)
        
        glb.SIGNAL_MANAGER.scoresUpdated.connect(self.update_leaderboard)
        glb.SIGNAL_MANAGER.roundSaved.connect(self.update_leaderboard)
        glb.SIGNAL_MANAGER.roundDeleted.connect(self.update_leaderboard)
        
    def get_participants(self) -> dict:
        try:
            participants_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "participants.json")
            with open(participants_path, "r") as f:
                return json.load(f)
        except:
            return
        
    def get_scoring(self) -> dict:
        try:
            scoring_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "scoring.json")
            with open(scoring_path, "r") as f:
                return json.load(f)
        except:
            return

    def calculate_leaderboard(self) -> list[dict]:
        participants = self.get_participants()
        scoring = self.get_scoring()
        
        if not participants:
            return
        
        if not scoring:
            return
        
        try:
            secondary_sorting_condition = scoring["tiebreaker"]
        except KeyError:
            secondary_sorting_condition = 0
        
        rounds = participants["rounds"]
        players = participants["players"]
        
        leaderboard: list[dict] = []
        
        for pid, player in enumerate(players):
            leaderboard.append(
                {
                    "id": pid,
                    "ranking": 0,
                    "name": player["name"],
                    "games_played": 0,
                    "wins": 0,
                    "kills": 0,
                    "total_placement": 0,
                    "average_placement": 0,
                    "average_kills": 0,
                    "most_kills": 0,
                    "score": 0,
                    "ranking_change": 0
                }
            )
        
        for i, round_id in enumerate(rounds):
            if len(rounds) >= 2 and i == len(rounds) - 1:
                match secondary_sorting_condition:
                    case 0:
                        leaderboard_prev = sorted(leaderboard, key=lambda player: (player["score"], player["kills"]), reverse=True)
                    case 1:
                        leaderboard_prev = sorted(leaderboard, key=lambda player: (player["score"], (player["kills"]/player["games_played"]) if player["games_played"] > 0 else 0), reverse=True)
                    case 2:
                        leaderboard_prev = sorted(leaderboard, key=lambda player: (player["score"], -(player["total_placement"]/player["games_played"]) if player["games_played"] > 0 else 0), reverse=True)
                    case 3:
                        leaderboard_prev = sorted(leaderboard, key=lambda player: (player["score"], player["wins"]), reverse=True)
                
                for j, player in enumerate(leaderboard_prev):
                    leaderboard[player["id"]]["ranking"] = j + 1
                
            for k, player in enumerate(players):
                for played_round in player["rounds_played"]:
                    if round_id != played_round["id"]:
                        continue
                    
                    leaderboard[k]["games_played"] += 1
                    if played_round["placement"] == 1:
                        leaderboard[k]["wins"] += 1
                    leaderboard[k]["kills"] += played_round["kills"]
                    leaderboard[k]["total_placement"] += played_round["placement"]
                    if leaderboard[k]["most_kills"] < played_round["kills"]:
                        leaderboard[k]["most_kills"] = played_round["kills"]
                    leaderboard[k]["score"] += played_round["score"]
            
            if len(rounds) >= 2 and i == len(rounds) - 1:
                match secondary_sorting_condition:
                    case 0:
                        leaderboard.sort(key=lambda player: (player["score"], player["kills"]), reverse=True)
                    case 1:
                        leaderboard.sort(key=lambda player: (player["score"], (player["kills"]/player["games_played"]) if player["games_played"] > 0 else 0), reverse=True)
                    case 2:
                        leaderboard.sort(key=lambda player: (player["score"], -(player["total_placement"]/player["games_played"]) if player["games_played"] > 0 else 0), reverse=True)
                    case 3:
                        leaderboard.sort(key=lambda player: (player["score"], player["wins"]), reverse=True)
                        
                for l, player in enumerate(leaderboard):
                    if player["ranking"] > l + 1:
                        player["ranking_change"] = -1
                        
                    if player["ranking"] < l + 1:
                        player["ranking_change"] = 1
                        
                    player["ranking"] = l + 1
                    
                    if player["games_played"] > 0:
                        player["average_kills"] = round(player["kills"] / player["games_played"], 1)
                        player["average_placement"] = round(player["total_placement"] / player["games_played"], 1)
                        
            elif len(rounds) == 1:
                match secondary_sorting_condition:
                    case 0:
                        leaderboard.sort(key=lambda player: (player["score"], player["kills"]), reverse=True)
                    case 1:
                        leaderboard.sort(key=lambda player: (player["score"], (player["kills"]/player["games_played"]) if player["games_played"] > 0 else 0), reverse=True)
                    case 2:
                        leaderboard.sort(key=lambda player: (player["score"], -(player["total_placement"]/player["games_played"]) if player["games_played"] > 0 else 0), reverse=True)
                    case 3:
                        leaderboard.sort(key=lambda player: (player["score"], player["wins"]), reverse=True)
                
                for m, player in enumerate(leaderboard):
                    player["ranking"] = m + 1
                    
                    if player["games_played"] > 0:
                        player["average_kills"] = round(player["kills"] / player["games_played"], 1)
                        player["average_placement"] = round(player["total_placement"] / player["games_played"], 1)
        
        leaderboard = [player for player in leaderboard if player["games_played"] > 0]
        
        return leaderboard
        
    def display_leaderboard(self, leaderboard: list[dict]) -> None:
        if not leaderboard:
            return
        
        for index, player in enumerate(leaderboard):
            ranking_label = QWidget(self)
            ranking_layout = QHBoxLayout(ranking_label)
            ranking_layout.setContentsMargins(0, 0, 0, 0)
            ranking_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            ranking_change = QLabel(self)
            
            match player["ranking_change"]:
                case -1:
                    ranking_change_icon = QPixmap(IMAGES["ranking_gain"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
                case 1:
                    ranking_change_icon = QPixmap(IMAGES["ranking_drop"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
                case _:
                    ranking_change_icon = QPixmap(IMAGES["ranking_no_change"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
                    
            ranking_change.setPixmap(ranking_change_icon)
            ranking_change.setFixedSize(ranking_change_icon.size())
            ranking_change.setContentsMargins(0, 0, 0, 0)
            
            ranking_text = QLabel(self, text=str(player["ranking"]))
            ranking_text.setObjectName("LeaderboardLabel")
            ranking_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            if index < 9:
                ranking_layout.setSpacing(20)
            
            ranking_layout.addWidget(ranking_change)
            ranking_layout.addWidget(ranking_text)
            
            if type(player["name"]) == str:
                if len(player["name"]) > 22:
                    display_name = f"{player["name"][:20]}..."
                else:
                    display_name = player["name"]
            else:
                display_name = ""
                for name in player["name"]:
                    if len(name) > 22:
                        display_name += f"{name[:20]}...\n"
                    else:
                        display_name += f"{name}\n"
                display_name = display_name.strip()
            
            name_label = QLabel(self, text=display_name)
            name_label.setObjectName("LeaderboardLabel")
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
            
            games_played_label = QLabel(self, text=str(player["games_played"]))
            games_played_label.setObjectName("LeaderboardLabel")
            games_played_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            wins_label = QLabel(self, text=str(player["wins"]))
            wins_label.setObjectName("LeaderboardLabel")
            wins_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            kills_label = QLabel(self, text=str(player["kills"]))
            kills_label.setObjectName("LeaderboardLabel")
            kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            average_placement_label = QLabel(self, text=str(player["average_placement"]))
            average_placement_label.setObjectName("LeaderboardLabel")
            average_placement_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            average_kills_label = QLabel(self, text=str(player["average_kills"]))
            average_kills_label.setObjectName("LeaderboardLabel")
            average_kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            most_kills_label = QLabel(self, text=str(player["most_kills"]))
            most_kills_label.setObjectName("LeaderboardLabel")
            most_kills_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            score_label = QLabel(self, text=str(player["score"]))
            score_label.setObjectName("LeaderboardLabel")
            score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            row_index = self.stats_layout.rowCount()

            match player["ranking"]:
                case 1:
                    ranking_label.setStyleSheet("background: #EFBF04")
                    name_label.setStyleSheet("background: #EFBF04")
                    games_played_label.setStyleSheet("background: #EFBF04")
                    wins_label.setStyleSheet("background: #EFBF04")
                    kills_label.setStyleSheet("background: #EFBF04")
                    average_placement_label.setStyleSheet("background: #EFBF04")
                    average_kills_label.setStyleSheet("background: #EFBF04")
                    most_kills_label.setStyleSheet("background: #EFBF04")
                    score_label.setStyleSheet("background: #EFBF04")
                case 2:
                    ranking_label.setStyleSheet("background: #C4C4C4")
                    name_label.setStyleSheet("background: #C4C4C4")
                    games_played_label.setStyleSheet("background: #C4C4C4")
                    wins_label.setStyleSheet("background: #C4C4C4")
                    kills_label.setStyleSheet("background: #C4C4C4")
                    average_placement_label.setStyleSheet("background: #C4C4C4")
                    average_kills_label.setStyleSheet("background: #C4C4C4")
                    most_kills_label.setStyleSheet("background: #C4C4C4")
                    score_label.setStyleSheet("background: #C4C4C4")
                case 3:
                    ranking_label.setStyleSheet("background: #CE8946")
                    name_label.setStyleSheet("background: #CE8946")
                    games_played_label.setStyleSheet("background: #CE8946")
                    wins_label.setStyleSheet("background: #CE8946")
                    kills_label.setStyleSheet("background: #CE8946")
                    average_placement_label.setStyleSheet("background: #CE8946")
                    average_kills_label.setStyleSheet("background: #CE8946")
                    most_kills_label.setStyleSheet("background: #CE8946")
                    score_label.setStyleSheet("background: #CE8946")
            
            self.stats_layout.addWidget(ranking_label, row_index, 0)
            self.stats_layout.addWidget(name_label, row_index, 1, 1, 3)
            self.stats_layout.addWidget(games_played_label, row_index, 4)
            self.stats_layout.addWidget(wins_label, row_index, 5)
            self.stats_layout.addWidget(kills_label, row_index, 6)
            self.stats_layout.addWidget(average_placement_label, row_index, 7)
            self.stats_layout.addWidget(average_kills_label, row_index, 8)
            self.stats_layout.addWidget(most_kills_label, row_index, 9)
            self.stats_layout.addWidget(score_label, row_index, 10)
            
            if index < len(leaderboard) - 1:
                div_line = HLine(self, h=1)
                div_line.setObjectName("DivLine")
                div_line.setContentsMargins(0, 0, 0, 0)
                row_index += 1
                self.stats_layout.addWidget(div_line, row_index, 0, 1, 11)
    
    def save_leaderboard_file(self, player_data: list[dict]) -> None:
        if not player_data:
            return
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
        with open(os.path.join(tournament_path, "leaderboard.csv"), "w", encoding="UTF-8", newline="") as f:
            csv_writer = csv.writer(f)
            csv_header = ["ranking", "name", "games_played", "wins", "kills", "average_placement", "average_kills", "most_kills", "score", "ranking_change"]
            csv_writer.writerow(csv_header)
            for player in player_data:
                placement = player["ranking"]
                if type(player["name"]) == list:
                    name = ";".join(player["name"])
                else:
                    name = player["name"]
                games_played = player["games_played"]
                wins = player["wins"]
                kills = player["kills"]
                average_placement = player["average_placement"]
                average_kills = player["average_kills"]
                most_kills = player["most_kills"]
                score = player["score"]
                ranking_change = player["ranking_change"]
                row = [placement, name, games_played, wins, kills, average_placement, average_kills, most_kills, score, ranking_change]
                csv_writer.writerow(row)
    
    def clear_leaderboard(self) -> None:
        while self.stats_layout.count():
            child = self.stats_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def update_leaderboard(self, tournament_id: str) -> None:
        if tournament_id != self.tournament_id:
            return
        self.clear_leaderboard()
        player_data = self.calculate_leaderboard()
        if not player_data:
            send_notification("Could not load participants", "NotifFail")
        self.display_leaderboard(player_data)
        self.save_leaderboard_file(player_data)
        if self.window().metaObject().className() == "MainWindow":
            glb.SIGNAL_MANAGER.leaderboardUpdated.emit(tournament_id)