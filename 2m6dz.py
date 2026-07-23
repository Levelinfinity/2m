import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        address TEXT,
        phone TEXT,
        date TEXT
    )
""")

cursor.execute(
    """
        insert into users(name, age, address, phone, date)
        values (?, ?, ?, ?, ?)
    """, ("Bob", 26, "25 Lenin st.", "+996(777)77-77-77", "10.10.2000")
)

cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()
print(f"Все пользователи в базе: {all_users}")

cursor.execute(
    "UPDATE users SET address = ? WHERE id = ?", ("25 Alymbek Datka st.", 1)
)
cursor.execute("DELETE FROM users WHERE id = ?", (2,))

conn.commit()
conn.close()