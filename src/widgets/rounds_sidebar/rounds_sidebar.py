from core import *
from .button import Button

class RoundsSidebar(QWidget):
    pageSelected = Signal(object)
    
    def __init__(
        self,
        parent: QWidget | None = None,
    ):
        super().__init__(parent)
            
        self.setObjectName("Sidebar")
        self.setFixedWidth(160)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        
        self.sidebar_layout = QVBoxLayout(self)
        self.sidebar_layout.setContentsMargins(5, 8, 5, 8)
        self.sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        
        self.buttons: list[Button] = []
        
    def add_button(self, btn: dict) -> None:
        button = Button(self, btn["icon"], btn["text"], btn["page"])
        button.clicked.connect(lambda: self.select_page(btn["page"]))
        if "active" in btn:
            button.select()
        if "insert_at" in btn:
            self.sidebar_layout.insertWidget(btn["insert_at"], button)
        else:
            self.sidebar_layout.addWidget(button)
        self.buttons.append(button)
    
    def get_btn_by_page(self, page: QWidget) -> None:
        for btn in self.buttons:
            if page == btn.page:
                return btn
    
    def remove_button(self, btn: Button) -> None:
        self.buttons.remove(btn)
        self.sidebar_layout.removeWidget(btn)
        btn.deleteLater()
        
    def deselect_all(self) -> None:
        for btn in self.buttons:
            btn.deselect()
    
    def select_page(self, page: QWidget) -> None:
        btn = self.get_btn_by_page(page)
        self.deselect_all()
        btn.select()
        self.pageSelected.emit(page)
    
    def keyPressEvent(self, arg__1):
        return

    def keyReleaseEvent(self, e):
        return