from core import *
from typing import Literal

class RarityButton(QPushButton):
    def __init__(
        self,
        parent: QWidget | None = None,
        rarity: Literal["Common", "Uncommon", "Rare", "Epic", "Legendary"] = "Common",
        selected: bool = False
    ):
        super().__init__(parent=parent, text=rarity)
        self.rarity = rarity
        match self.rarity:
            case "Common":
                self.rarity_id = 0
            case "Uncommon":
                self.rarity_id = 1
            case "Rare":
                self.rarity_id = 2
            case "Epic":
                self.rarity_id = 3
            case "Legendary":
                self.rarity_id = 4
        self.setFixedSize(100, 25)
        if selected or glb.SELECTED_RARITY == self.rarity_id:
            self.select()
        
        self.setObjectName("RarityButton")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(self.select)
        
        glb.SIGNAL_MANAGER.raritySelected.connect(self.on_rarity_selected)
        
        match self.rarity:
            case "Common":
                self._bg_color = "#292d2f"
                self._border_color = "#181b1b"
                self._hover_color = "#33383a"
                self._hover_border = "#1f2223"
            case "Uncommon":
                self._bg_color = "#366400"
                self._border_color = "#214000"
                self._hover_color = "#437900"
                self._hover_border = "#294e00"
            case "Rare":
                self._bg_color = "#005f83"
                self._border_color = "#003d55"
                self._hover_color = "#00739d"
                self._hover_border = "#004a67"
            case "Epic":
                self._bg_color = "#4b0a6c"
                self._border_color = "#2f0445"
                self._hover_color = "#5b0f83"
                self._hover_border = "#3a0655"
            case "Legendary":
                self._bg_color = "#7a5400"
                self._border_color = "#4f3500"
                self._hover_color = "#936600"
                self._hover_border = "#604100"
        self._color = "#aaaaaa"
        
        self.setStyleSheet(f"""
            #RarityButton {{
                background: {self._bg_color};
                border: 3px solid {self._border_color};
                border-radius: 8px;
                color: {self._color};
                font-weight: bold;
                font-family: Aptos;
            }}
            
            #RarityButton:hover {{
                background: {self._hover_color};
                border: 3px solid {self._hover_border};
            }}
            
            #RarityButtonSelected {{
                background: {self._bg_color};
                border: 3px solid {self._border_color};
                border-radius: 8px;
                color: {self._color};
                font-weight: bold;
                font-family: Aptos;
            }}
        """)
    
    def select(self) -> None:
        glb.SELECTED_RARITY = self.rarity_id
        glb.SIGNAL_MANAGER.raritySelected.emit()
    
    def on_rarity_selected(self) -> None:
        if glb.SELECTED_RARITY == self.rarity_id:
            self.setObjectName("RarityButtonSelected")
            match self.rarity:
                case "Common":
                    self._bg_color = "#43494b"
                    self._border_color = "#292d2f"
                case "Uncommon":
                    self._bg_color = "#569900"
                    self._border_color = "#366400"
                case "Rare":
                    self._bg_color = "#0092c6"
                    self._border_color = "#005f83"
                case "Epic":
                    self._bg_color = "#7416a5"
                    self._border_color = "#4b0a6c"
                case "Legendary":
                    self._bg_color = "#b98200"
                    self._border_color = "#7a5400"
            self._color = "white"
        else:
            self.setObjectName("RarityButton")
            match self.rarity:
                case "Common":
                    self._bg_color = "#292d2f"
                    self._border_color = "#181b1b"
                    self._hover_color = "#33383a"
                    self._hover_border = "#1f2223"
                case "Uncommon":
                    self._bg_color = "#366400"
                    self._border_color = "#214000"
                    self._hover_color = "#437900"
                    self._hover_border = "#294e00"
                case "Rare":
                    self._bg_color = "#005f83"
                    self._border_color = "#003d55"
                    self._hover_color = "#00739d"
                    self._hover_border = "#004a67"
                case "Epic":
                    self._bg_color = "#4b0a6c"
                    self._border_color = "#2f0445"
                    self._hover_color = "#5b0f83"
                    self._hover_border = "#3a0655"
                case "Legendary":
                    self._bg_color = "#7a5400"
                    self._border_color = "#4f3500"
                    self._hover_color = "#936600"
                    self._hover_border = "#604100"
            self._color = "#aaaaaa"
         
        self.setStyleSheet(f"""
            #RarityButton {{
                background: {self._bg_color};
                border: 3px solid {self._border_color};
                border-radius: 8px;
                color: {self._color};
                font-weight: bold;
                font-family: Aptos;
            }}
            
            #RarityButton:hover {{
                background: {self._hover_color};
                border: 3px solid {self._hover_border};
            }}
            
            #RarityButtonSelected {{
                background: {self._bg_color};
                border: 3px solid {self._border_color};
                border-radius: 8px;
                color: {self._color};
                font-weight: bold;
                font-family: Aptos;
            }}
        """)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return