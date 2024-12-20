import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase
import rc_fonts
from updater_window import UpdaterWindow

if __name__ == "__main__":
    app = QApplication([])
    QFontDatabase.addApplicationFont(":/fonts/Rubik-Regular.ttf")
    QFontDatabase.addApplicationFont(":/fonts/Rubik-Bold.ttf")
    QFontDatabase.addApplicationFont(":/fonts/Rubik-BoldItalic.ttf")
    QFontDatabase.addApplicationFont(":/fonts/Rubik-Italic.ttf")
    window = UpdaterWindow()
    window.show()
    window.update_thread.start()
    sys.exit(app.exec())
    