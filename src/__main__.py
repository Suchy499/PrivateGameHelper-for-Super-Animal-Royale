import sys
from core.qt_core import *
from styles import rc_fonts
from ui.windows import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    QFontDatabase.addApplicationFont(":/fonts/Rubik-Regular.ttf")
    QFontDatabase.addApplicationFont(":/fonts/Rubik-Bold.ttf")
    QFontDatabase.addApplicationFont(":/fonts/Rubik-BoldItalic.ttf")
    QFontDatabase.addApplicationFont(":/fonts/Rubik-Italic.ttf")
    main_window = MainWindow()
    main_window.show()
    main_window.change_display_mode()
    sys.exit(app.exec())
