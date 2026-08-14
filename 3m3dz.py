import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
                    callback_data="q1_python"
                )
            ],
            [
                InlineKeyboardButton(
                    text="☕️ Java",
                    callback_data="q1_java"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚡️ C++",
                    callback_data="q1_cpp"
                )
            ]
        ]
    )

    await message.answer(
        "🧠 Викторина: \n\n"
        "Вопрос 1 из 3:\nНа каком языке написан фреймворк Django?",
        reply_markup=keyboard
    )


@dp.callback_query(F.data == "q1_python")
async def q1_correct(callback: CallbackQuery):
    await callback.answer("Правильно! 🎉")
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➡️ Следующий вопрос", callback_data="next_q2")]
        ]
    )
    
    await callback.message.answer(
        "✅ Верно! Django написан на Python.",
        reply_markup=keyboard
    )


@dp.callback_query(F.data.in_({"q1_java", "q1_cpp"}))
async def q1_wrong(callback: CallbackQuery):
    await callback.answer("Неправильно ❌")
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➡️ Следующий вопрос", callback_data="next_q2")]
        ]
    )
    
    await callback.message.answer(
        "❌ Неправильно. Django написан на Python.",
        reply_markup=keyboard
    )


@dp.callback_query(F.data == "next_q2")
async def question_2(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🐧 Linux", callback_data="q2_linux")],
            [InlineKeyboardButton(text="🪟 Windows", callback_data="q2_windows")],
            [InlineKeyboardButton(text="🍏 macOS", callback_data="q2_macos")]
        ]
    )
    
    await callback.message.answer(
        "Вопрос 2 из 3:\nКакая операционная система является полностью открытой (Open Source) и создана Линусом Торвальдсом?",
        reply_markup=keyboard
    )


@dp.callback_query(F.data == "q2_linux")
async def q2_correct(callback: CallbackQuery):
    await callback.answer("Правильно! 🎉")
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➡️ Следующий вопрос", callback_data="next_q3")]
        ]
    )
    
    await callback.message.answer(
        "✅ Верно! Это Linux.",
        reply_markup=keyboard
    )


@dp.callback_query(F.data.in_({"q2_windows", "q2_macos"}))
async def q2_wrong(callback: CallbackQuery):
    await callback.answer("Неправильно ❌")
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➡️ Следующий вопрос", callback_data="next_q3")]
        ]
    )
    
    await callback.message.answer(
        "❌ Неправильно. Правильный ответ: Linux.",
        reply_markup=keyboard
    )


@dp.callback_query(F.data == "next_q3")
async def question_3(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🌐 HTML", callback_data="q3_html")],
            [InlineKeyboardButton(text="🗄 SQL", callback_data="q3_sql")],
            [InlineKeyboardButton(text="🎨 CSS", callback_data="q3_css")]
        ]
    )
    
    await callback.message.answer(
        "Вопрос 3 из 3:\nКакой язык используется для управления и запросов в реляционных базах данных?",
        reply_markup=keyboard
    )


@dp.callback_query(F.data == "q3_sql")
async def q3_correct(callback: CallbackQuery):
    await callback.answer("Правильно! 🎉")
    
    await callback.message.answer(
        "✅ Верно! Это SQL.\n\n"
        "🏆 Поздравляем! Вы прошли викторину до конца!\n"
        "Нажмите /start, чтобы пройти её снова."
    )


@dp.callback_query(F.data.in_({"q3_html", "q3_css"}))
async def q3_wrong(callback: CallbackQuery):
    await callback.answer("Неправильно ❌")
    
    await callback.message.answer(
        "❌ Неправильно. Правильный ответ: SQL.\n\n"
        "🏁 Викторина завершена!\n"
        "Нажмите /start, чтобы попробовать ещё раз."
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())