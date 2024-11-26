import hashlib
import sqlite3

from Errors import *
from funcs import hash_arg

from main import *

con = sqlite3.connect("db/main.sqlite")
cur = con.cursor()

#НЕ УБИВАЙТЕ МЕНЯ ЗА ЭТУ ФУНКЦИЮ)))))))))))) ↓

def check_login(self):
    login = self.login_le.text()
    password = self.password_le.text()
    password_hashed = hash_arg(password)

    result = cur.execute("""SELECT * FROM table_main""").fetchall()

    for i in result:
        if i[2] == login and i[3] == password_hashed:
            return True
    return False
