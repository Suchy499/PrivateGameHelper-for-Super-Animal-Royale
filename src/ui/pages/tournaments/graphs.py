from core import *
from widgets import ClickableLabel, Button
from images import IMAGES
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.figure import Figure
import os
import json
import csv
from pyfonts import load_font

class Canvas(FigureCanvas):
    def __init__(self, tournament_id: str, chart_name: str):
        fig = Figure(figsize=(16, 9), tight_layout=True)
        self.axes = fig.add_subplot()
        self.tournament_id = tournament_id
        self.chart_name = chart_name
        super().__init__(fig)
    
    def save_chart(self) -> None:
        graphs_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "Graphs")
        if not os.path.isdir(graphs_path):
            os.makedirs(graphs_path)
        self.figure.savefig(os.path.join(graphs_path, self.chart_name))
        
class Graphs(QWidget):
    def __init__(self, parent, tournament_id: str):
        super().__init__(parent)
        
        self.tournament_id = tournament_id
        
        rubik_font = load_font(
            font_url="https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/blob/main/src/styles/fonts/Rubik-Regular.ttf?raw=true"
            
        )
        plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
        
        fm.fontManager.addfont(rubik_font.get_file())
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0, 0, 0, 0)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.graph_widget = QStackedWidget(self)
        self.graph_widget.setObjectName("GraphWidget")
        self.graph_widget.setFixedSize(800, 360)
        
        self.canvas_dict = {
            "score": Canvas(self.tournament_id, "score"),
            "kills": Canvas(self.tournament_id, "kills"),
            "average_placement": Canvas(self.tournament_id, "average_placement")
        }
        
        for canvas in self.canvas_dict.values():
            self.graph_widget.addWidget(canvas)
        
        self.controls_widget = QWidget(self)
        self.controls_layout = QHBoxLayout(self.controls_widget)
        self.controls_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.left_icon = QPixmap(IMAGES["left_arrow"])
        self.left_button = ClickableLabel(self)
        self.left_button.setPixmap(self.left_icon)
        self.left_button.setObjectName("TeamsButton")
        self.left_button.setFixedSize(self.left_icon.width() + 20, self.left_icon.height() + 20)
        self.left_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_button.clicked.connect(lambda: self.change_chart(-1))
        
        self.graph_label = QLabel(self, text="SCORE")
        self.graph_label.setObjectName("LeaderboardLabel")
        self.graph_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.graph_label.setFixedWidth(400)
        
        self.right_icon = QPixmap(IMAGES["right_arrow"])
        self.right_button = ClickableLabel(self)
        self.right_button.setPixmap(self.right_icon)
        self.right_button.setObjectName("TeamsButton")
        self.right_button.setFixedSize(self.right_icon.width() + 20, self.right_icon.height() + 20)
        self.right_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right_button.clicked.connect(lambda: self.change_chart(1))
        
        self.controls_layout.addWidget(self.left_button)
        self.controls_layout.addWidget(self.graph_label)
        self.controls_layout.addWidget(self.right_button)
        
        self.open_folder_button = Button(self, "Open Graphs Folder", w=210)
        self.open_folder_button.clicked.connect(self.open_folder)
        
        self.page_layout.addStretch()
        self.page_layout.addWidget(self.graph_widget)
        self.page_layout.addStretch()
        self.page_layout.addWidget(self.controls_widget)
        self.page_layout.addWidget(self.open_folder_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        glb.SIGNAL_MANAGER.leaderboardUpdated.connect(self.update_charts)
        
        self.plot_charts(self.tournament_id)
    
    def open_folder(self) -> None:
        graphs_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "Graphs")
        if not os.path.isdir(graphs_path):
            os.makedirs(graphs_path)
        os.startfile(graphs_path)
    
    def change_chart(self, index_change: int) -> None:
        new_index = self.graph_widget.currentIndex() + index_change
        if new_index < 0:
            self.graph_widget.setCurrentIndex(self.graph_widget.count() - 1)
        elif new_index >= self.graph_widget.count():
            self.graph_widget.setCurrentIndex(0)
        else:
            self.graph_widget.setCurrentIndex(new_index)
        self.graph_label.setText(list(self.canvas_dict.keys())[list(self.canvas_dict.values()).index(self.graph_widget.currentWidget())].upper().replace("_", " "))
    
    def get_rounds(self) -> list[str]:
        rounds_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id, "Rounds")
        if not os.path.exists(rounds_path):
            os.makedirs(rounds_path)
        files: list[str] = os.listdir(rounds_path)
        round_files: list[str] = []
        rounds: list[int] = []
        for round_file in files:
            if re.match(r"^\d+\.csv$", round_file):
                rounds.append(int(os.path.splitext(round_file)[0]))
        rounds.sort()
        for round_id in rounds:
            round_file = f"{round_id}.csv"
            round_files.append(os.path.join(rounds_path, round_file))
        return round_files
    
    def get_metadata(self) -> dict:
        try:
            tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
            with open(os.path.join(tournament_path, "metadata.json"), "r") as f:
                return json.load(f)
        except:
            send_notification("Could not load metadata.", "NotifFail")
    
    def plot_charts(self, tournament_id: str) -> None:
        if tournament_id != self.tournament_id:
            return
        metadata = self.get_metadata()
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", self.tournament_id)
        leaderboard_path = os.path.join(tournament_path, "leaderboard.csv")
        if not os.path.exists(leaderboard_path):
            return
        with open(leaderboard_path, "r", encoding="UTF-8", newline="") as f:
            leaderboard_csv_reader = csv.reader(f)

            players = []
            scores = []
            kills_list: list[tuple] = []

            for row in leaderboard_csv_reader:
                if row[0] == "ranking":
                    continue
                if len(row[1]) > 10:
                    name = f"{row[1][:8]}.."
                else:
                    name = row[1]
                players.append(name)
                scores.append(round(float(row[8]), 1))
                kills_list.append((name, int(row[4])))
            
            kills_list.sort(key=lambda player: player[1], reverse=True)
        
        rubik_font_bold = load_font(
            font_url="https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/blob/main/src/styles/fonts/Rubik-Bold.ttf?raw=true"
        )
        
        try:
            kill_list_players, kill_list_values = zip(*kills_list)
        except ValueError:
            return
        
        plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
        plt.rcParams["text.color"] = "white"
        plt.rcParams["xtick.major.size"] = 4
        plt.rcParams["font.family"] = ["Rubik", "Arial", "DejaVu Sans", "Microsoft YaHei"]
        plt.rcParams["font.size"] = 10
        
        for _ in range(self.graph_widget.count()):
            widget = self.graph_widget.widget(0)
            self.graph_widget.removeWidget(widget)
            widget.deleteLater()
        
        self.canvas_dict = {
            "score": Canvas(self.tournament_id, "score"),
            "kills": Canvas(self.tournament_id, "kills"),
            "average_placement": Canvas(self.tournament_id, "average_placement")
        }
        
        for canvas in self.canvas_dict.values():
            self.graph_widget.addWidget(canvas)
            
        self.graph_label.setText("SCORE")
        
        x = range(len(players))
        self.canvas_dict["score"].axes.spines["left"].set_color("white")
        self.canvas_dict["score"].axes.spines["left"].set_linewidth(1)
        self.canvas_dict["score"].axes.spines["bottom"].set_color("white")
        self.canvas_dict["score"].axes.spines["bottom"].set_linewidth(1)
        self.canvas_dict["score"].axes.bar(players, scores)
        self.canvas_dict["score"].axes.set_xticks(x, players, rotation=45, fontsize=8, ha="right", rotation_mode="anchor")
        self.canvas_dict["score"].axes.set_xmargin(0.01)
        self.canvas_dict["score"].axes.set_title(metadata["name"], font=rubik_font_bold, fontsize=20)
        self.canvas_dict["score"].axes.set_ylabel("Score", font=rubik_font_bold, fontsize=20)
        self.canvas_dict["score"].save_chart()
        
        x = range(len(kills_list))
        self.canvas_dict["kills"].axes.spines["left"].set_color("white")
        self.canvas_dict["kills"].axes.spines["left"].set_linewidth(1)
        self.canvas_dict["kills"].axes.spines["bottom"].set_color("white")
        self.canvas_dict["kills"].axes.spines["bottom"].set_linewidth(1)
        self.canvas_dict["kills"].axes.bar(kill_list_players, kill_list_values)
        self.canvas_dict["kills"].axes.set_xticks(x, kill_list_players, rotation=45, fontsize=8, ha="right", rotation_mode="anchor")
        self.canvas_dict["kills"].axes.set_xmargin(0.01)
        self.canvas_dict["kills"].axes.set_title(metadata["name"], font=rubik_font_bold, fontsize=20)
        self.canvas_dict["kills"].axes.set_ylabel("Kills", font=rubik_font_bold, fontsize=20)
        self.canvas_dict["kills"].save_chart()
        
        player_data: dict[dict] = {}
        for round_file in self.get_rounds():
            with open(round_file, "r", encoding="UTF-8", newline="") as f:
                csv_reader = csv.reader(f)
                player_list: list[list] = []
                for row in csv_reader:
                    if row[0] == "player_id":
                        continue
                    player_list.append(row)
                
                if metadata["mode"] != "Solo":
                    squad_dict = {}
                    for row in player_list:
                        player_id, name, playfab_id, squad_id, team_id, kills, placement = int(row[0]), row[1], row[2], int(row[3]), int(row[4]), int(row[5]), int(row[6])
                        
                        if squad_id not in squad_dict:
                            squad_dict[squad_id] = {
                                "playfab_id": set(),
                                "name": [],
                                "placement": placement
                            }
                            
                        squad_dict[squad_id]["playfab_id"].add(playfab_id)
                        squad_dict[squad_id]["name"].append(name)
                    player_list = list(squad_dict.values())
                    player_list.sort(key=lambda team: team["placement"])
                    for ranking, team in enumerate(player_list):
                        team["placement"] = ranking + 1
                    
                for row in player_list:
                    if metadata["mode"] == "Solo":
                        player_id, name, playfab_id, squad_id, team_id, kills, placement = int(row[0]), row[1], row[2], int(row[3]), int(row[4]), int(row[5]), int(row[6])
                    else:
                        playfab_id, name, placement = frozenset(row["playfab_id"]), ";".join(row["name"]), row["placement"]
                    
                    if metadata["mode"] != "Solo":
                        for playfab_id_set in player_data.keys():
                            if playfab_id.issubset(playfab_id_set):
                                playfab_id = playfab_id_set
                                break
                    
                    if playfab_id not in player_data:
                        if len(name) > 10:
                            display_name = f"{name[:8]}.."
                        else:
                            display_name = name
                        player_data[playfab_id] = {
                            "name": display_name,
                            "placements": []
                        }
                    
                    player_data[playfab_id]["placements"].append(placement)
        player_list = list(player_data.values())
        player_list.sort(key=lambda player: sum(player["placements"])/len(player["placements"]))
        player_names: list[str] = []
        player_placements: list[list] = []
        for player in player_list:
            player_names.append(player["name"])
            player_placements.append(player["placements"])
        
        self.canvas_dict["average_placement"].axes.boxplot(
            player_placements, 
            capprops={"color":"white"},
            boxprops={"color":"white"},
            whiskerprops={"color":"white"},
            flierprops={"color":"white", "markeredgecolor":"white", "marker":"x"}
        )
        self.canvas_dict["average_placement"].axes.spines["left"].set_color("white")
        self.canvas_dict["average_placement"].axes.spines["left"].set_linewidth(1)
        self.canvas_dict["average_placement"].axes.spines["bottom"].set_color("white")
        self.canvas_dict["average_placement"].axes.spines["bottom"].set_linewidth(1)
        self.canvas_dict["average_placement"].axes.set_yticks(range(1, max([max(sublist) for sublist in player_placements]), 10))
        self.canvas_dict["average_placement"].axes.set_xticklabels(player_names, rotation=45, fontsize=8, ha="right", rotation_mode="anchor")
        self.canvas_dict["average_placement"].axes.set_xmargin(0.01)
        self.canvas_dict["average_placement"].axes.set_title(metadata["name"], font=rubik_font_bold, fontsize=20)
        self.canvas_dict["average_placement"].axes.set_ylabel("Average Placement", font=rubik_font_bold, fontsize=20)
        self.canvas_dict["average_placement"].axes.invert_yaxis()
        self.canvas_dict["average_placement"].save_chart()
    
    def update_charts(self, tournament_id: str) -> None:
        if tournament_id != self.tournament_id:
            return
        self.plot_charts(tournament_id)
        if self.window().metaObject().className() == "MainWindow":
            glb.SIGNAL_MANAGER.graphsUpdated.emit(tournament_id)

    def resizeEvent(self, event):
        self.graph_widget.setFixedSize(self.width()-self.width()/10, self.height()-self.height()/5)
        return super().resizeEvent(event)
