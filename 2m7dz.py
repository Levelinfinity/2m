import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
    create table if not exists orders(
        id integer primary key autoincrement,
        user_id integer,
        product text,
        price integer
    )
""")

# orders = [
#     (1, "IPhone", 1000),
#     (1, "Airpods", 200),
#     (2, "Laptop", 1500),
#     (2, "Mouse", 50),
#     (3, "Keyboard", 120)
# ]

# cursor.executemany(
#     "insert into orders(user_id, product, price) values (?, ?, ?)",
#     orders
# )

cursor.execute("""
    create view expensive_orders as
    select * from orders
    where price > 500
""")

cursor.execute("select * from expensive_orders")
for row in cursor.fetchall():
    print(row)

cursor.execute(
    """
        insert into orders(user_id, product, price)
        values (?, ?, ?)
    """, (1, "MacBook", 2500)
)

cursor.execute("select * from expensive_orders")

for row in cursor.fetchall():
    print(row)

cursor.execute("drop view expensive_orders")

try:
    cursor.execute("select * from expensive_orders")
except Exception as e:
    print(e)

conn.commit()
conn.close()