from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Reg_func import *

class RegWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/register_window.ui', self)
        self.register_button.clicked.connect(self.register_but)


    def register_but(self):
        name = self.name_le_reg.text()
        login = self.login_le_reg.text()
        password = self.password_le_reg.text()

        if check_already(login):
            QMessageBox.warning(self, "RegisterError", "Login is already")
            raise RegisterError

        if insert_reg_db(name, login, password):
            QMessageBox.information(self, "OK", "You are good")
            con.commit()
            self.close()
