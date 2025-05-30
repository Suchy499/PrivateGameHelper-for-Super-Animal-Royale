from core import *
from images import IMAGES
from widgets import Button, HLine
import os
import json
import discord
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pyfonts import load_font
from itertools import batched
from datetime import datetime
from plottable import Table, ColumnDefinition

class PageDiscord(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        self.title_label = QLabel(self, text="Discord Integration for Tournaments")
        self.title_label.setObjectName("PresetsHeaderName")
        self.title_label.setContentsMargins(9, 0, 0, 0)
        self.page_layout.addWidget(self.title_label)
        
        self.hline_1 = HLine(self, h=2)
        self.hline_1.setObjectName("DivLine")
        self.page_layout.addWidget(self.hline_1)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        self.page_layout.addWidget(self.scroll_area)
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        
        self.desc_1 = QLabel(
            "Private Game Helper can use a discord webhook to send the graphs for selected tourneys in a specific channel,\n"
            "while keeping them updated in real time!\n\n"
            "Setup:\n"
            "1) Navigate to your Server's Settings",
            self
        )
        self.desc_1.setObjectName("HostIDLabel")
        self.desc_1.setContentsMargins(9, 10, 0, 0)
        
        self.screenshot_1 = QLabel(self)
        self.screenshot_1.setPixmap(QPixmap(IMAGES["webhook_setup_0"]).scaledToWidth(200, Qt.TransformationMode.SmoothTransformation))
        self.screenshot_1.setContentsMargins(9, 0, 0, 0)
        
        self.desc_2 = QLabel(
            "\n2) Scroll down to the Apps section and open Integrations",
            self
        )
        self.desc_2.setObjectName("HostIDLabel")
        self.desc_2.setContentsMargins(9, 0, 0, 0)
        
        self.screenshot_2 = QLabel(self)
        self.screenshot_2.setPixmap(QPixmap(IMAGES["webhook_setup_1"]).scaledToWidth(200, Qt.TransformationMode.SmoothTransformation))
        self.screenshot_2.setContentsMargins(9, 0, 0, 0)
        
        self.desc_3 = QLabel(
            "\n3) Create a new webhook",
            self
        )
        self.desc_3.setObjectName("HostIDLabel")
        self.desc_3.setContentsMargins(9, 0, 0, 0)
        
        self.screenshot_3 = QLabel(self)
        self.screenshot_3.setPixmap(QPixmap(IMAGES["webhook_setup_2"]).scaledToWidth(400, Qt.TransformationMode.SmoothTransformation))
        self.screenshot_3.setContentsMargins(9, 0, 0, 0)
        
        self.desc_4 = QLabel(
            "\n4) Give your webhook a name, optionally an avatar and select which channel the leaderboards should be posted to.\n"
            "Save your settings, then copy the webhook's URL",
            self
        )
        self.desc_4.setObjectName("HostIDLabel")
        self.desc_4.setContentsMargins(9, 0, 0, 0)
        
        self.screenshot_4 = QLabel(self)
        self.screenshot_4.setPixmap(QPixmap(IMAGES["webhook_setup_3"]).scaledToWidth(400, Qt.TransformationMode.SmoothTransformation))
        self.screenshot_4.setContentsMargins(9, 0, 0, 0)
        
        self.desc_5 = QLabel(
            "\n5) Paste the URL into the input box below and press Save\n",
            self
        )
        self.desc_5.setObjectName("HostIDLabel")
        self.desc_5.setContentsMargins(9, 0, 0, 0)
        
        self.webhooks_widget = QWidget(self)
        self.webhooks_layout = QGridLayout(self.webhooks_widget)
        self.webhooks_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.webhooks_layout.setContentsMargins(9, 0, 0, 0)
        
        self.webhooks: list[QLineEdit] = []
        
        self.create_first_line_edit()
            
        self.buttons_widget = QWidget(self)
        self.buttons_layout = QHBoxLayout(self.buttons_widget)
        self.buttons_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.buttons_layout.setContentsMargins(9, 0, 0, 0)
            
        add_icon = QPixmap(IMAGES["add"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.add_button = Button(self, "Add", add_icon)
        self.add_button.clicked.connect(self.create_line_edit)
        self.buttons_layout.addWidget(self.add_button)
        
        save_icon = QPixmap(IMAGES["save"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.save_button = Button(self, "Save", save_icon)
        self.save_button.clicked.connect(self.save_webhooks)
        self.buttons_layout.addWidget(self.save_button)
        
        self.content_layout.addWidget(self.desc_1)
        self.content_layout.addWidget(self.screenshot_1)
        self.content_layout.addWidget(self.desc_2)
        self.content_layout.addWidget(self.screenshot_2)
        self.content_layout.addWidget(self.desc_3)
        self.content_layout.addWidget(self.screenshot_3)
        self.content_layout.addWidget(self.desc_4)
        self.content_layout.addWidget(self.screenshot_4)
        self.content_layout.addWidget(self.desc_5)
        self.content_layout.addWidget(self.webhooks_widget)
        self.content_layout.addWidget(self.buttons_widget)
        
        self.load_webhooks()
        
        if self.window().metaObject().className() == "MainWindow":
            glb.SIGNAL_MANAGER.graphsUpdated.connect(self.send_messages)
        
        glb.SIGNAL_MANAGER.webhooksSaved.connect(self.load_webhooks)
        
    def save_webhooks(self) -> None:
        pgh_documents_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper")
        if not os.path.exists(pgh_documents_path):
            os.makedirs(pgh_documents_path)
        
        webhooks: list[str] = []
        
        for webhook in self.webhooks:
            if webhook.text() != "":
                webhooks.append(webhook.text())
        
        glb.WEBHOOKS = webhooks
        
        try:
            with open(os.path.join(pgh_documents_path, "discord.json"), "w") as f:
                json.dump(webhooks, f, indent=4)
            send_notification("Discord webhooks connected!", "NotifSuccess")
        except:
            send_notification("Could not save webhooks", "NotifFail")
        
        glb.SIGNAL_MANAGER.webhooksSaved.emit()
    
    def load_webhooks(self) -> None:
        webhooks_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "discord.json")
        if not os.path.exists(webhooks_path):
            return
        
        for _ in range(self.webhooks_layout.count()):
            widget = self.webhooks_layout.takeAt(0).widget()
            widget.deleteLater()
        self.webhooks.clear()

        self.create_first_line_edit()
        
        with open(webhooks_path, "r") as f:
            glb.WEBHOOKS = json.load(f)
        
        for index, webhook in enumerate(glb.WEBHOOKS):
            if index != 0:
                self.create_line_edit()
            self.webhooks[index].setText(webhook)
    
    def create_first_line_edit(self) -> None:
        webhook_line_edit = QLineEdit(self)
        webhook_line_edit.setObjectName("LineEdit")
        webhook_line_edit.setFixedWidth(600)
        webhook_line_edit.setPlaceholderText("Webhook URL")
        webhook_line_edit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.webhooks.append(webhook_line_edit)
        self.webhooks_layout.addWidget(webhook_line_edit, 0, 0)
        
        remove_icon = QPixmap(IMAGES["trash"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        webhook_clear_button = Button(self, "Clear", remove_icon, btn_style="ButtonDelete")
        webhook_clear_button.clicked.connect(webhook_line_edit.clear)
        self.webhooks_layout.addWidget(webhook_clear_button, 0, 1)
    
    def create_line_edit(self) -> None:
        webhook_line_edit = QLineEdit(self)
        webhook_line_edit.setObjectName("LineEdit")
        webhook_line_edit.setFixedWidth(600)
        webhook_line_edit.setPlaceholderText("Webhook URL")
        webhook_line_edit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        remove_icon = QPixmap(IMAGES["trash"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        webhook_remove_button = Button(self, "Remove", remove_icon, btn_style="ButtonDelete")
        webhook_remove_button.clicked.connect(lambda: self.webhooks.remove(webhook_line_edit))
        webhook_remove_button.clicked.connect(webhook_line_edit.deleteLater)
        webhook_remove_button.clicked.connect(webhook_remove_button.deleteLater)
        self.webhooks.append(webhook_line_edit)
        self.webhooks_layout.addWidget(webhook_line_edit, self.webhooks_layout.rowCount(), 0)
        self.webhooks_layout.addWidget(webhook_remove_button, self.webhooks_layout.rowCount()-1, 1)
    
    def create_webhooks(self) -> list[discord.SyncWebhook]:
        if not glb.WEBHOOKS:
            return
        
        webhooks: list[discord.SyncWebhook] = []
        
        for webhook_url in glb.WEBHOOKS:
            try:
                webhooks.append(discord.SyncWebhook.from_url(webhook_url))
            except ValueError:
                pass
        
        return webhooks
    
    def send_messages(self, tournament_id: str) -> None:
        webhooks = self.create_webhooks()
        
        if not webhooks:
            return
        
        webhook_messages: dict[int, dict[str, int]] = {}
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", tournament_id)
        tournament_messages_path = os.path.join(tournament_path, "discord_messages.json")
        
        metadata_path = os.path.join(tournament_path, "metadata.json")
        
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
        
        if not metadata["discord"]:
            return
        
        self.create_tables(tournament_id)
        leaderboard_files = self.get_tables(tournament_id)
        graphs_files = self.get_graphs(tournament_id)
        
        if not leaderboard_files:
            return
        
        if not graphs_files:
            return
        
        if not os.path.exists(tournament_messages_path):
            for webhook in webhooks:
                webhook_messages[webhook.id] = {}
                
                leaderboard_embeds, leaderboard_pngs = self.get_leaderboard_embeds(tournament_id, leaderboard_files)
                try:
                    leaderboard_message = webhook.send("", wait=True, embeds=leaderboard_embeds, files=leaderboard_pngs)
                    webhook_messages[webhook.id]["leaderboard_message"] = leaderboard_message.id
                except:
                    pass
                
                graphs_embeds, graphs_pngs = self.get_graphs_embeds(tournament_id, graphs_files)
                try:
                    graphs_message = webhook.send("", wait=True, embeds=graphs_embeds, files=graphs_pngs)
                    webhook_messages[webhook.id]["graphs_message"] = graphs_message.id
                except:
                    pass
            
            with open(tournament_messages_path, "w") as f:
                json.dump(webhook_messages, f, indent=4)
        else:
            with open(tournament_messages_path, "r") as f:
                tournament_messages = json.load(f)
            
            for webhook in webhooks:
                webhook_messages[webhook.id] = {}
                leaderboard_embeds, leaderboard_pngs = self.get_leaderboard_embeds(tournament_id, leaderboard_files)
                graphs_embeds, graphs_pngs = self.get_graphs_embeds(tournament_id, graphs_files)
                if str(webhook.id) in tournament_messages:
                    try:
                        leaderboard_message = webhook.fetch_message(tournament_messages[str(webhook.id)]["leaderboard_message"])
                        leaderboard_message.edit(embeds=leaderboard_embeds, attachments=leaderboard_pngs)
                        webhook_messages[webhook.id]["leaderboard_message"] = leaderboard_message.id
                    except:
                        try:
                            leaderboard_message = webhook.send("", wait=True, embeds=leaderboard_embeds, files=leaderboard_pngs)
                            webhook_messages[webhook.id]["leaderboard_message"] = leaderboard_message.id
                        except:
                            pass

                    try:
                        graphs_message = webhook.fetch_message(tournament_messages[str(webhook.id)]["graphs_message"])
                        graphs_message.edit(embeds=graphs_embeds, attachments=graphs_pngs)
                        webhook_messages[webhook.id]["graphs_message"] = graphs_message.id
                    except:
                        try:
                            graphs_message = webhook.send("", wait=True, embeds=graphs_embeds, files=graphs_pngs)
                            webhook_messages[webhook.id]["graphs_message"] = graphs_message.id
                        except:
                            pass
                        
                else:
                    try:
                        leaderboard_message = webhook.send("", wait=True, embeds=leaderboard_embeds, files=leaderboard_pngs)
                        webhook_messages[webhook.id]["leaderboard_message"] = leaderboard_message.id
                    except:
                        pass
                    
                    try:
                        graphs_message = webhook.send("", wait=True, embeds=graphs_embeds, files=graphs_pngs)
                        webhook_messages[webhook.id]["graphs_message"] = graphs_message.id
                    except:
                        pass
            
            with open(tournament_messages_path, "w") as f:
                json.dump(webhook_messages, f, indent=4)
    
    def get_leaderboard_embeds(self, tournament_id: str, leaderboard_files: list[str]) -> tuple[list[discord.Embed], list[discord.File]]:
        metadata = self.get_metadata(tournament_id)
        embeds: list[discord.Embed] = []
        pngs: list[discord.File] = []
        for index, table in enumerate(leaderboard_files):
            table_file = discord.File(table, os.path.basename(table))
            if len(leaderboard_files) == 1:
                embed = discord.Embed(title=f"{metadata["name"]} Leaderboard", type="image", timestamp=datetime.now())
            elif index == 0:
                embed = discord.Embed(title=f"{metadata["name"]} Leaderboard", type="image")
            elif index == len(leaderboard_files) - 1:
                embed = discord.Embed(type="image", timestamp=datetime.now())
            else:
                embed = discord.Embed(type="image")
            if len(leaderboard_files) > 1:
                embed.set_footer(text=f"Page {index + 1}/{len(leaderboard_files)}")
            embed.set_image(url=f"attachment://{os.path.basename(table)}")
            embeds.append(embed)
            pngs.append(table_file)
        
        return (embeds, pngs)

    def get_graphs_embeds(self, tournament_id: str, graphs_files: list[str]) -> tuple[list[discord.Embed], list[discord.File]]:
        metadata = self.get_metadata(tournament_id)
        embeds: list[discord.Embed] = []
        pngs: list[discord.File] = []
        for index, graph in enumerate(graphs_files):
            graph_file = discord.File(graph, os.path.basename(graph))
            if index == 0:
                embed = discord.Embed(title=f"{metadata["name"]} Graphs", type="image")
            elif index == len(graphs_files) - 1:
                embed = discord.Embed(type="image", timestamp=datetime.now())
                embed.set_footer(text="Private Game Helper", icon_url="https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/blob/main/src/images/images/icon_0.png?raw=true")
            else:
                embed = discord.Embed(type="image")
            embed.set_image(url=f"attachment://{os.path.basename(graph)}")
            embeds.append(embed)
            pngs.append(graph_file)
            
        return (embeds, pngs)
    
    def get_metadata(self, tournament_id: str) -> dict:
        try:
            tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", tournament_id)
            with open(os.path.join(tournament_path, "metadata.json"), "r") as f:
                return json.load(f)
        except:
            send_notification("Could not load metadata.", "NotifFail")
    
    def create_tables(self, tournament_id: str) -> None:
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", tournament_id)
        tournament_leaderboard_path = os.path.join(tournament_path, "leaderboard.csv")
        tournament_tables_path = os.path.join(tournament_path, "Tables")
        
        if not os.path.exists(tournament_leaderboard_path):
            return
        
        if not os.path.exists(tournament_tables_path):
            os.makedirs(tournament_tables_path)

        leaderboard_data: list[list] = [] 
        
        rubik_font = load_font(
            font_url="https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/blob/main/src/styles/fonts/Rubik-Regular.ttf?raw=true"
        )
        
        rubik_font_bold = load_font(
            font_url="https://github.com/Suchy499/PrivateGameHelper-for-Super-Animal-Royale/blob/main/src/styles/fonts/Rubik-Bold.ttf?raw=true"
        )
        
        fm.fontManager.addfont(rubik_font.get_file())
        fm.fontManager.addfont(rubik_font_bold.get_file())
        
        plt.rcParams["font.family"] = ["Rubik", "Arial", "DejaVu Sans", "Microsoft YaHei"]
        plt.rcParams["text.color"] = "white"
        plt.rcParams["font.size"] = 20

        fig, ax = plt.subplots()
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        
        with open(tournament_leaderboard_path, "r", newline="", encoding="UTF-8") as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 0:
                    leaderboard_header = ["Ranking", "Name", "Games\nPlayed", "Wins", "Kills", "Average\nPlacement", "Average\nKills", "Most Kills\nin a Match", "Score"]
                    continue
                
                if len(row[1]) > 30:
                    row[1] = f"{row[1][:29]}.."
                    
                ranking_change = int(row.pop())
                
                gap = "   " if int(row[0]) <= 9 else "  "
                    
                match ranking_change:
                    case -1:
                        row[0] = f"↑{gap}{row[0]}"
                    case 0:
                        row[0] = f"-{gap}{row[0]}"
                    case 1:
                        row[0] = f"↓{gap}{row[0]}"
                        
                leaderboard_data.append(row)
            leaderboard_batches = batched(leaderboard_data, 19)
            
        if leaderboard_data:
            for table_file in os.listdir(tournament_tables_path):
                os.remove(os.path.join(tournament_tables_path, table_file))
            for index, batch in enumerate(leaderboard_batches):
                ax.clear()
                data = pd.DataFrame(batch, columns=leaderboard_header)
                data = data.set_index("Ranking")
                col_defs = [
                    ColumnDefinition(
                        name="Ranking",
                        textprops={"ha": "center"},
                        width=0.5,
                    ),
                    ColumnDefinition(
                        name="Name",
                        textprops={"ha": "center", "weight": "bold"},
                        width=2,
                    ),
                    ColumnDefinition(
                        name="Games\nPlayed",
                        textprops={"ha": "center"},
                        width=0.5,
                    ),
                    ColumnDefinition(
                        name="Wins",
                        textprops={"ha": "center"},
                        width=0.5,
                    ),
                    ColumnDefinition(
                        name="Kills",
                        textprops={"ha": "center"},
                        width=0.5,
                    ),
                    ColumnDefinition(
                        name="Average\nPlacement",
                        textprops={"ha": "center"},
                        width=0.5,
                    ),
                    ColumnDefinition(
                        name="Average\nKills",
                        textprops={"ha": "center"},
                        width=0.5,
                    ),
                    ColumnDefinition(
                        name="Most Kills\nin a Match",
                        textprops={"ha": "center"},
                        width=0.5,
                    ),
                    ColumnDefinition(
                        name="Score",
                        textprops={"ha": "center"},
                        width=0.5,
                    ),
                ]
                tab = Table(data, column_definitions=col_defs)
                fig.set_figheight(len(batch)+1)
                fig.set_figwidth(20)
                fig.tight_layout()
                plt.savefig(os.path.join(tournament_tables_path, f"{index}.png"), dpi=200, bbox_inches="tight")
    
    def get_tables(self, tournament_id: str) -> list[str]:
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", tournament_id)
        tournament_tables_path = os.path.join(tournament_path, "Tables")
        if not os.path.exists(tournament_tables_path):
            return
        
        tables_paths: list[str] = []
        for table in os.listdir(tournament_tables_path):
            tables_paths.append(os.path.join(tournament_tables_path, table))
        return tables_paths
    
    def get_graphs(self, tournament_id: str) -> list[str]:
        tournament_path = os.path.join(os.environ["USERPROFILE"], "Documents", "Private Game Helper", "Tournaments", tournament_id)
        tournament_graphs_path = os.path.join(tournament_path, "Graphs")
        if not os.path.exists(tournament_graphs_path):
            return
        
        graphs_paths: list[str] = []
        for graph in os.listdir(tournament_graphs_path):
            graphs_paths.append(os.path.join(tournament_graphs_path, graph))
        return graphs_paths