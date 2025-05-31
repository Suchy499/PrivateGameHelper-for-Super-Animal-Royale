from core import *
from widgets import ClickableLabel, Button
from images import IMAGES
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.figure import Figure
import os
import json
from pyfonts import load_font
from collections import namedtuple

class Canvas(FigureCanvas):
    def __init__(self, tournament_id: str, chart_name: str):
        fig = Figure(figsize=(16, 9), tight_layout=True)
        self.axes = fig.add_subplot()
        self.tournament_id = tournament_id
        self.chart_name = chart_name
        super().__init__(fig)
    
    def save_chart(self) -> None:
        if not self.window().metaObject().className() == "MainWindow":
            return
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
        participants_path = os.path.join(tournament_path, "participants.json")
        
        if not os.path.exists(participants_path):
            return
        
        with open(participants_path, "r", encoding="UTF-8", newline="") as f:
            data = json.load(f)
            
            try:
                if not data["rounds"] or not data["players"]:
                    return
            except:
                return
            
            participants = data["players"]

            PlayerTuple = namedtuple("PlayerTuple", ["name", "kills", "score", "placements"])
            
            players: list[PlayerTuple] = []

            for participant in participants:
                if len(participant["rounds_played"]) == 0:
                    continue
                
                if type(participant["name"]) == list:
                    name = ", ".join(participant["name"])
                else:
                    name = participant["name"]
                    
                if len(name) > 10:
                    name = f"{name[:8]}.."

                player_kills = 0
                player_score = 0
                player_placements = []
                
                for played_round in participant["rounds_played"]:
                    player_kills += played_round["kills"]
                    player_score += played_round["score"]
                    player_placements.append(played_round["placement"])
                
                players.append(PlayerTuple(name, player_kills, player_score, player_placements))
        
        rubik_font_bold = load_font(
            font_url="https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/blob/main/src/styles/fonts/Rubik-Bold.ttf?raw=true"
        )
        
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
        
        players.sort(key=lambda player: player.score, reverse=True)
        
        player_names, _, player_scores, _ = zip(*players)
        
        self.canvas_dict["score"].axes.spines["left"].set_color("white")
        self.canvas_dict["score"].axes.spines["left"].set_linewidth(1)
        self.canvas_dict["score"].axes.spines["bottom"].set_color("white")
        self.canvas_dict["score"].axes.spines["bottom"].set_linewidth(1)
        self.canvas_dict["score"].axes.bar(player_names, player_scores)
        self.canvas_dict["score"].axes.set_xticks(x, player_names, rotation=45, fontsize=8, ha="right", rotation_mode="anchor")
        self.canvas_dict["score"].axes.set_xmargin(0.01)
        self.canvas_dict["score"].axes.set_title(metadata["name"], font=rubik_font_bold, fontsize=20)
        self.canvas_dict["score"].axes.set_ylabel("Score", font=rubik_font_bold, fontsize=20)
        self.canvas_dict["score"].save_chart()
        
        players.sort(key=lambda player: player.kills, reverse=True)
        
        player_names, player_kills, _, _ = zip(*players)
        
        self.canvas_dict["kills"].axes.spines["left"].set_color("white")
        self.canvas_dict["kills"].axes.spines["left"].set_linewidth(1)
        self.canvas_dict["kills"].axes.spines["bottom"].set_color("white")
        self.canvas_dict["kills"].axes.spines["bottom"].set_linewidth(1)
        self.canvas_dict["kills"].axes.bar(player_names, player_kills)
        self.canvas_dict["kills"].axes.set_xticks(x, player_names, rotation=45, fontsize=8, ha="right", rotation_mode="anchor")
        self.canvas_dict["kills"].axes.set_xmargin(0.01)
        self.canvas_dict["kills"].axes.set_title(metadata["name"], font=rubik_font_bold, fontsize=20)
        self.canvas_dict["kills"].axes.set_ylabel("Kills", font=rubik_font_bold, fontsize=20)
        self.canvas_dict["kills"].save_chart()
        
        
        players.sort(key=lambda player: sum(player.placements)/len(player.placements))
        
        player_names, player_kills, _, player_placements  = zip(*players)
        
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
