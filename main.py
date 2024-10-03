# nuitka-project: --standalone
# nuitka-project: --enable-plugin=pyside6

import sys
from PySide6.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec())
