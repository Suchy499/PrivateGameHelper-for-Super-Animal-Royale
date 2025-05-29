from core import *
from .tournament_list import TournamentList
from .tournament_page import TournamentPage

class PageTournaments(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.tournament_list = TournamentList(self)
        
        self.addWidget(self.tournament_list)
        
        glb.SIGNAL_MANAGER.tournamentCreated.connect(self.add_tournament)
        glb.SIGNAL_MANAGER.tournamentCreated.connect(self.open_tournament)
        glb.SIGNAL_MANAGER.tournamentOpened.connect(self.open_tournament)
        glb.SIGNAL_MANAGER.tournamentClosed.connect(lambda: self.setCurrentWidget(self.tournament_list))
        glb.SIGNAL_MANAGER.tournamentDeleted.connect(self.delete_tournament)
        
        self.tournament_pages: dict[str, QWidget] = {}
    
    def add_tournament(self, tournament_id: str) -> None:
        self.tournament_pages[tournament_id] = TournamentPage(self, tournament_id)
        self.addWidget(self.tournament_pages[tournament_id])
    
    def open_tournament(self, tournament_id: str) -> None:
        if tournament_id not in self.tournament_pages:
            self.add_tournament(tournament_id)
        self.setCurrentWidget(self.tournament_pages[tournament_id])
    
    def delete_tournament(self, tournament_id: str) -> None:
        self.tournament_pages.pop(tournament_id).deleteLater()
        self.setCurrentWidget(self.tournament_list)