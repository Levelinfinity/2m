# Реляционные базы данных и типы соотношения таблиц. 
# Агрегационные функции(управление несколькими таблицами) и группировка данных. Вложенные запросы. Views.

# One To One (1:1)
# Одному пользователю соответствует один паспорт.
# One To Many (1:N)
# Самый популярный вид.
# Один пользователь может сделать много заказов
# Many To Many (M:N)
# Например:
# Студенты ↔️ Курсы
# Один студент может проходить много курсов.
# Один курс проходят много студентов.

import sqlite3

conn = sqlite3.connect("shohp.db")
cursor = conn.cursor()

cursor.execute("""
    create table if not exists users(
        id integer primary key autoincrement,
        name text,
        age integer
    )
""")

cursor.execute("""
    create table if not exists orders(
        id integer primary key autoincrement,
        user_id integer,
        product text,
        price integer,
        foreign key(user_id) references users(id)
    )
""")

# users = [
#     ("Bob", 20),
#     ("Alice", 21),
#     ("Tom", 22)
# ]

# cursor.executemany(
#     "insert into users(name, age) values (?, ?)",
#     users
# )

# orders = [
#     (1, "Phone Charger", 1000),
#     (1, "Charger Cabel", 500),
#     (2, "Hair Dryer", 6000),
#     (2, "Hair Utyg", 5000),
#     (3, "Toothpaste", 500),
#     (3, "Eyeglasses", 3500)
# ]

# cursor.executemany(
#     "insert into orders(user_id, product, price) values (?, ?, ?)",
#     orders
# )

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# INNER JOIN
# Покажем пользователей вместе с их заказами.
# LEFT JOIN
# Добавим пользователя без заказов

cursor.execute("""
    SELECT users.name,
            orders.product,
            orders.price
    FROM users
    INNER JOIN orders
    ON users.id = orders.user_id
""")

# cursor.execute("""
#     insert into users(name, age)
#     values("Sara", 25)
# """)

cursor.execute("""
    select users.name,
            orders.product
    from users
    left join orders
    on users.id = orders.user_id
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
    select count(*) from orders
""")

print(cursor.fetchall()[0])

cursor.execute("""
    select sum(price) from orders
""")

print(cursor.fetchall()[0])

cursor.execute("""
    select AVG(price) from orders
""")

avg_price = cursor.fetchone()[0]
print(avg_price)

cursor.execute("SELECT MIN(price) FROM orders")
min_price = cursor.fetchone()[0]
print(f"min {min_price}")

cursor.execute("SELECT MAX(price) FROM orders")
max_price = cursor.fetchone()[0]
print(f"max {max_price}")

cursor.execute("""
    select
        users.name,
        sum(orders.price)
    from users
    join orders
    on users.id = orders.user_id
    group by users.name
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
    select name
    from users
    where id = (
        select user_id from orders
        where price = (
            select max(price)
            from orders
        )
    )
""")

print(cursor.fetchone())



conn.commit()
conn.close()
