import asyncio 
import os
import sqlite3

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    CallbackQuery,
    inline_keyboard_markup,
    InlineKeyboardButton
)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(
    bot, storage=MemoryStorage()
)

conn = sqlite3.connect("notes.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        title text NOT NULL,
        text text NOT NULL
    )
""")
conn.commit()

class AddNote(StatesGroup):
    title = State()
    text = State()

class EditNote(StatesGroup):
    note_id = State()
    text = State()


def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="➕ Добавить заметку",
                    callback_data="add_note"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📝 Мои заметки",
                    callback_data="my_notes"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✏️ Изменить заметку",
                    callback_data="edit_note"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🗑 Удалить заметку",
                    callback_data="delete_note"
                )
            ]
        ]
    )

@dp.message(F.text == "/start")
async def start_cmd(message: Message):

    await message.answer(
        "📝<b> МОИ ЗАМЕТКИ <b>\n\n"
        "Здесь ты можешь создавать и хранить свои заметки.",
        reply_markup=main_menu()
    )

@dp.callback_query(F.data == "add_note")
async def add_note_start(
    callback: CallBackQuery,
    state: FSMContext,
):

    await callback.answer()

    await callback.message.answer(
        "Добавляем новую заметку.\n\n"
        "Напишите название заметки"
    )

    await state.set_state(AddNote.title)

@dp.message(AddNote.title)
async def get_note_title(
    message: Message,
    state: FSMContext,
):
    await state.update_data(
        title=message.text
    )

    await message.answer(
        "Теперь напишите текст заметки:"
    )

    await state.set_state(AddNote.text)

@dp.message(AddNote.text)
async def get_note_text(
    message: Message,
    state: FSMContext
):
    data = await state.get_data()

    title = data["title"]
    text = message.text

    telegram_id = message.from_user.id

    cur.execute(
        """
        INSERT INTO notes
        (telegram_id, title, text)
        VALUES (?, ?, ?)
        """,
        (telegram_id, title, text)
    )
    conn.commit()

    await state.clear()

    await message.answer(
        "Заметка сохранена!\n\n"
        "f<b>{title}<b>\n"
        "{text}",
        reply_markup=main_menu()
    )

@dp.callback_query(F.data == "my_notes")
async def my_notes(callback: CallbackQuery)

    telegram_id = callback.from_user.id

    cur.execute(
        """
        SELECT id, title, text
        FROM notes
        WHERE telegram_id = ?
        """,
    )

    notes = cur.fetchall()

    if not notes:

        await callback.answer()

        await callback.message.answer(
            "У вас пока нет заметок."
            reply_markup=main_menu()
        )

        return

    text = "<b> Ваши заметки. <b>\n\n "

    for note in notes:

        note_id, title, note_text = note

        text += (
            f"ID: {note_id}\n"
            f"<b>{title}<b>\n"
            f"{note_text}\n"
            "---------------\n"
        )

    await callback.answer()

    await callback.message.answer(
        text,
        reply_markup = main_menu()
    )

@dp.callback_query(F.data == "edit_note")
async def edit_note_start(
    callback: CallbackQuery,
    state: FSMContext,
):

    telegram_id callback.from_user.id

    cur.execute(
        """
        SELECT id, title
        FROM notes 
        WHERE telegram_id = ?
        """
        (telegram_id,)
    )

    notes = cur.fetchall()

    if not notes:

        await callbcak.answer("У вас нет заметок.")
        return

    buttnos = []

    for note_id, title in notes:

        buttons.append([
            InlineKeyboardButton(
                text=f"{title}",
                callback_data=f"edit:{note_id}"
            )
        ])

        keyboard = InlineKeyboardMarkup(
            inline_keyboard = buttons
        )

        await callback.message.answer(
            "Выберите заметку, которую хотите изменить.",
            reply_markup=keyboard
        )