# Базы данных и СУБД. Работа с БД в Python. Основы SQL, создание таблиц и типы данных, CRUD операции
import sqlite3
  

#    crud system
# создать таблицу
# CREATE TABLE

# добавить данные 
# INSERT  create - c

# получить данные
# SELECT        read - r
 
# изменять
# UPDATE         update - u
# 
# удалить
# DELETE         delete - d
#  ТИПЫ ДАННЫХ
# INTEGER - целое число
# REAL - 
#
#

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
""")

cursor.execute(
    """
        insert into users(name, age)
        values (?, ?)
    """, ("Bob", 20)
)

users = [
    ("Alice", 20),
    ("Tom", 21),
    ("Jack", 22)
]

cursor.executemany(
    "insert into users(name, age) values (?, ?)",
    users
)

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute(
    """
        update users
        set age = ?
        where id = ?
    """, (30, 1)
)

cursor.execute("""
        delete from users
        where id = ?
    """,
    (1, ) 
)

conn.commit()
conn.close()