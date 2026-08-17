import asyncio
import os 
import sqlite3

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message   
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN not found in .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()

connection = sqlite3.connect("baza.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        name TEXT NOT NULL,
        surname TEXT,
        age INTEGER,
        city TEXT,
        street TEXT,
        phone TEXT
    )
""")
connection.commit()

class RegisterState(StatesGroup):
    name = State()
    surname = State()
    age = State()
    city = State()
    street = State()
    phone = State()


@dp.message(F.text == "/start")
async def start_cmd(message: Message, state: FSMContext):
    telegram_id = message.from_user.id
    
    cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
    user = cursor.fetchone()
    
    if user:
        await message.answer(f"Привет, {user[2]}! Ты уже есть в базе данных. Используй /me для просмотра профиля.")
    else:
        await message.answer("Привет! Давай пройдем регистрацию.\n\nВведи своё имя:")
        await state.set_state(RegisterState.name)


@dp.message(RegisterState.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введи свою фамилию:")
    await state.set_state(RegisterState.surname)


@dp.message(RegisterState.surname)
async def process_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer("Введи свой возраст:")
    await state.set_state(RegisterState.age)


@dp.message(RegisterState.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введи возраст цифрами:")
        return
    
    await state.update_data(age=int(message.text))
    await message.answer("Введи свой город:")
    await state.set_state(RegisterState.city)


@dp.message(RegisterState.city)
async def process_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer("Введи свою улицу:")
    await state.set_state(RegisterState.street)


@dp.message(RegisterState.street)
async def process_street(message: Message, state: FSMContext):
    await state.update_data(street=message.text)
    await message.answer("Введи свой номер телефона:")
    await state.set_state(RegisterState.phone)


@dp.message(RegisterState.phone)
async def process_phone(message: Message, state: FSMContext):
    data = await state.get_data()
    telegram_id = message.from_user.id
    
    cursor.execute("""
        INSERT OR IGNORE INTO users (telegram_id, name, surname, age, city, street, phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        telegram_id,
        data['name'],
        data['surname'],
        data['age'],
        data['city'],
        data['street'],
        message.text
    ))
    connection.commit()
    
    await state.clear()
    await message.answer("🎉 Регистрация успешно завершена! Теперь тебе доступны команды /me и /users.")


@dp.message(F.text == "/me")
async def me_cmd(message: Message):
    telegram_id = message.from_user.id
    cursor.execute("""
        SELECT name, surname, age, city, street, phone 
        FROM users WHERE telegram_id = ?
    """, (telegram_id,))
    user = cursor.fetchone()
    
    if user:
        name, surname, age, city, street, phone = user
        await message.answer(
            f"👤 Твой профиль:\n\n"
            f"• Имя: {name}\n"
            f"• Фамилия: {surname}\n"
            f"• Возраст: {age}\n"
            f"🏙 Город: {city}\n"
            f"📍 Улица: {street}\n"
            f"📞 Телефон: {phone}"
        )
    else:
        await message.answer("Тебя нет в базе. Напиши /start для регистрации.")


@dp.message(F.text == "/users")
async def users_cmd(message: Message):
    cursor.execute("""
        SELECT telegram_id, name, surname, age, city, street, phone 
        FROM users
    """)
    users = cursor.fetchall()
    
    if not users:
        await message.answer("В базе данных пока нет пользователей.")
        return
    
    text = "📋 Список всех пользователей:\n\n"
    for u in users:
        text += f"👤 {u[1]} {u[2]} ({u[3]} лет)\n  📍 г. {u[4]}, ул. {u[5]}\n  📞 {u[6]}\n  🆔 Telegram ID: `{u[0]}`\n\n"
    
    await message.answer(text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())