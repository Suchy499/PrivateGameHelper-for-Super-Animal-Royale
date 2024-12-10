import sys
from core.qt_core import *
from ui.windows import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    main_window.change_display_mode()
    sys.exit(app.exec())
