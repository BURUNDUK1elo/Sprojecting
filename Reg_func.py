import sqlite3

from funcs import hash_arg
from main import *

con = sqlite3.connect("db/main.sqlite")
cur = con.cursor()

def check_already(login):
    result = cur.execute("""SELECT * FROM table_main""").fetchall()

    for i in result:
        if i[2] == login:
            return True
    return False

def insert_reg_db(name, login, password):
    data = (name, login, hash_arg(password))
    sql_request = """INSERT INTO table_main(name, login, password) VALUES (?, ?, ?)"""
    cur.execute(sql_request, data)
    result = cur.execute("""SELECT * FROM table_main""").fetchall()
    return True