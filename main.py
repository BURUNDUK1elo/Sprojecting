import sys
import traceback

import PyQt6
from PyQt6.QtWidgets import QApplication
from Auth import *


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Error:", tb)


def main():
    app = QApplication(sys.argv)
    sys.excepthook = excepthook

    AuthWin = AuthWindow()
    AuthWin.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
