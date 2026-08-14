import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from google import genai

BOT_TOKEN = ""
GEMINI_API_KEY = ""

gemini_client = genai.Client(api_key=GEMINI_API_KEY)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет! С чего начнем?")

@dp.message()
async def chat_handler(message: types.Message):
    # Показываем статус "печатает..." в чате
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    try:
        response = gemini_client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=message.text,
        )
        await message.answer(response.text)
    except Exception as e:
        logging.error(f"Ошибка Gemini API: {e}")
        await message.answer("Произошла ошибка при обращении к ИИ.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())