# import asyncio
# import sqlite3

# import os
# from dotenv import load_dotenv

# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message

# load_dotenv()

# TOKEN = os.getenv("BOT_TOKEN")

# if not TOKEN:
#     raise ValueError("BOT_TOKEN Не найден в .env")

# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# connection = sqlite3.connect("school.db")
# cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         telegram_id INTEGER,
#         name TEXT NOT NULL
#     )
# """)


# connection.commit()

# @dp.message(F.text == "/start")
# async def start(message: Message):
#     await message.answer(
#         "Привет! Как тебя зовут?"
#     )

# @dp.message()
# async def save_student(message: Message):
#     name = message.text
#     cursor.execute(
#         """
#         INSERT INTO stundets(telegram_id, name)
#         VALUES (?, ?)
#         """,
#         (message.from_user.id, name)
#     )

#     connection.commit()

#     await message.answer(
#         f"Приятно познакомиться {name} !"
#         f"Я сохранил тебя в базу данных."
#     )

# async def main():
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())



import asyncio
import os
import sqlite3

from dotenv import load_dotenv


from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN Not find in .env")

bot = Bot(token = TOKEN)
dp = Dispatcher()

conn = sqlite3.connect("students_db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )
""")

conn.commit()

@dp.message(F.text == "/start")

async def start(message: Message):

    telegram_id = message.from_user.id 
    name = message.from_user.first_name

    cur.execute(
        """
        SELECT * FROM students
        WHERE telegram_id = ?
        """,
        (telegram_id,)
    )

    student = cur.fetchone()

    if student:
        await message.answer(
            f"С возвращением, {name} ! \n\n"
            f"Ты уже есть в базе данных. \n\n"
            f"Команды: \n"
            f"/me - мой профиль \n"
            f"/students - список студентов"
        )

    else:
        cur.execute(
            """
            INSERT INTO students (telegram_id, name)
            VALUES (?, ?)
            """,
            (telegram_id, name)
        )

    conn.commit()

    await message.answer(
        f"Привет {name} !\n\n"
        f"Ты зарегистрирован и сохранен в базе данных. \n\n"
        f"Команды \n"
        f"/me - мой профиль. \n"
        f"/students - список студентов."
    )

@dp.message(F.text == "/me")
async def my_profile(message: Message):
    telegram_id = message.from_user.id

    cur.execute(
        """
        SELECT id, name, age, city
        FROM students 
        WHERE telegram_id = ?
        """,
        (telegram_id,)
    ) 

    student = cur.fetchone()

    if not student:
        await message.answer(
            "❌ Ты еще не зарегистрирован. \n"
            "Напиши /start"
        )
        return

    student_id, name, age, city = student

    age = age if age else "Не указан"
    cite = city if city else "Не указан"

    await message.answer(
        f"Твой профиль \n\n"
        f"ID: {student_id} \n"
        f"Имя: {name} \n"
        f"Возраст {age} \n"
        f"Город: {city}"
    )

@dp.message(F.text == "/students")
async def students(message: Message):
    cur.execute(
        """
        SELECT id, name, age, city
        FROM students
        """
    )

    students_list = cur.fetchall()

    if not students_list:
        await message.answer("В базе пока нет студентов.")
        return


    text = "Студенты: \n\n"

    for student in students_list:
        student_id, name, age, city = student

        text += (
            "ID: {student_id}\n"
            "Имя: {name}\n"
            "Возраст: {age}\n"
            "Город: {city}"
        )

        await message.answer(text)

@dp.message(F.text == "/help")
async def help_command(message: Message):
    await message.answer(
        "Команды бота \n\n"
        "/start - регистрация \n"
        "/students - студенты \n"
        "/help - помощь"
    )

@dp.message()
async def unknown(message: Message):
    await message.answer(
        "Я не знаю такую команды \n\n"
        "Используй /help"
    )


async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())


    finally:
        conn.close()
