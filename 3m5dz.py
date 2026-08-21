import asyncio
import sqlite3

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

TOKEN = "8851227121:AAGfqlBKlAj2SjdwrkDOQ7_L_r1p7OsHJ-4"

bot = Bot(token=TOKEN)
dp = Dispatcher()


def init_db():
  conn = sqlite3.connect("shopping_list.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity TEXT NOT NULL
        )
    """
  )
  conn.commit()
  conn.close()


init_db()


class AddItemState(StatesGroup):
  waiting_for_name = State()
  waiting_for_quantity = State()


def get_main_keyboard():
  return InlineKeyboardMarkup(
      inline_keyboard=[
          [InlineKeyboardButton(text="➕ Добавить товар", callback_data="add_item")],
          [InlineKeyboardButton(text="🛒 Мои товары", callback_data="list_items")],
          [
              InlineKeyboardButton(
                  text="🗑 Удалить товар", callback_data="delete_menu"
              )
          ],
      ]
  )


@dp.message(F.text == "/start")
async def start(message: Message):
  await message.answer(
      "🛒 Добро пожаловать в бот «Список покупок»!\nВыберите действие:",
      reply_markup=get_main_keyboard(),
  )


@dp.callback_query(F.data == "add_item")
async def start_add_item(callback: CallbackQuery, state: FSMContext):
  await callback.message.answer("Введите название товара:")
  await state.set_state(AddItemState.waiting_for_name)
  await callback.answer()


@dp.message(AddItemState.waiting_for_name)
async def process_item_name(message: Message, state: FSMContext):
  await state.update_data(name=message.text)
  await message.answer(
      "Введите количество (например: 2 шт, 1 кг или пачка):"
  )
  await state.set_state(AddItemState.waiting_for_quantity)


@dp.message(AddItemState.waiting_for_quantity)
async def process_item_quantity(message: Message, state: FSMContext):
  user_data = await state.get_data()
  name = user_data["name"]
  quantity = message.text

  conn = sqlite3.connect("shopping_list.db")
  cursor = conn.cursor()
  cursor.execute(
      "INSERT INTO items (name, quantity) VALUES (?, ?)", (name, quantity)
  )
  conn.commit()
  conn.close()

  await state.clear()
  await message.answer(
      f"✅ Товар **{name}** ({quantity}) успешно добавлен!",
      reply_markup=get_main_keyboard(),
      parse_mode="Markdown",
  )


@dp.callback_query(F.data == "list_items")
async def list_items(callback: CallbackQuery):
  conn = sqlite3.connect("shopping_list.db")
  cursor = conn.cursor()
  cursor.execute("SELECT id, name, quantity FROM items")
  items = cursor.fetchall()
  conn.close()

  if not items:
    await callback.message.answer(
        "🛒 Ваш список покупок пуст.", reply_markup=get_main_keyboard()
    )
    await callback.answer()
    return

  response = "🛒 **Ваш список покупок:**\n\n"
  for item in items:
    response += f"🆔 ID: {item[0]} | 📦 **{item[1]}** — {item[2]}\n"

  await callback.message.answer(
      response, reply_markup=get_main_keyboard(), parse_mode="Markdown"
  )
  await callback.answer()


@dp.callback_query(F.data == "delete_menu")
async def delete_menu(callback: CallbackQuery):
  conn = sqlite3.connect("shopping_list.db")
  cursor = conn.cursor()
  cursor.execute("SELECT id, name, quantity FROM items")
  items = cursor.fetchall()
  conn.close()

  if not items:
    await callback.message.answer(
        "🗑 Нечего удалять, список пуст.", reply_markup=get_main_keyboard()
    )
    await callback.answer()
    return

  keyboard_buttons = []
  for item in items:
    keyboard_buttons.append([
        InlineKeyboardButton(
            text=f"❌ Удалить: {item[1]} ({item[2]})",
            callback_data=f"del_{item[0]}",
        )
    ])

  keyboard_buttons.append(
      [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
  )

  keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

  await callback.message.answer(
      "Выберите товар, который хотите удалить:", reply_markup=keyboard
  )
  await callback.answer()


@dp.callback_query(F.data.startswith("del_"))
async def delete_item(callback: CallbackQuery):
  item_id = int(callback.data.split("_")[1])

  conn = sqlite3.connect("shopping_list.db")
  cursor = conn.cursor()
  cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
  conn.commit()
  conn.close()

  await callback.message.answer(
      "🗑 Товар успешно удален из списка!", reply_markup=get_main_keyboard()
  )
  await callback.answer()


@dp.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
  await callback.message.answer(
      "Главное меню:", reply_markup=get_main_keyboard()
  )
  await callback.answer()


async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())