from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox

from Auth_func import *
from Errors import *
from Main_Window import *
from main import *
from Reg_Window import *


class AuthWindow(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('ui/auth_window.ui', self)
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def register(self):
        self.reg_window = RegWindow()
        self.reg_window.show()

        # ...

    def login(self):
        if not check_login(self):
            QMessageBox.warning(self, "ErrorLogin", "Login is incorrect")
            raise LoginError
        QMessageBox.information(self, "Login", "Sure")
        self.open_main_window()



    def open_main_window(self):
        self.main_window = MainWindow()
        self.close()
        self.main_window.show()
