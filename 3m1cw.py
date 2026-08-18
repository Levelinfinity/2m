import asyncio 

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import CallbackQuery

TOKEN = "8851227121:AAGfqlBKlAj2SjdwrkDOQ7_L_r1p7OsHJ-4"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🐍 Python",
                    callback_data="python"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🗄 SQL",
                    callback_data="sql"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🐧 Linux",
                    callback_data="linux"
                )
            ]
        ]
    )

    await message.answer(
        "🧠Выберите тему:",
        reply_markup=keyboard
    )


@dp.callback_query(F.data == "python")
async def answer_python(callback: CallbackQuery):

    await callback.message.answer(
        "🐍 Python - один из самых популярных,\nпростых в освоении и универсальных\n языков программирования в мире."
    )


@dp.callback_query(F.data == "sql")
async def answer_sql(callback: CallbackQuery):

    await callback.message.answer(
        "🗄 SQL - Это язык программирования\nдля управления данными в реляционных базах данных."
    )

@dp.callback_query(F.data == "linux")
async def answer_linux(callback: CallbackQuery):

    await callback.message.answer(
        "🐧 Linux - это бесплатная операционная система с открытым исходным кодом,\n которая работает на базе одноимённого ядра."
    )


async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
