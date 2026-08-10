# from aiogram import Bot, Dispatcher
# from aiogram.enums import ParseMode
# from aiogram.client.default import DefaultBotProperties
# import asyncio

# TOKEN = "8851227121:AAGfqlBKlAj2SjdwrkDOQ7_L_r1p7OsHJ-4"

# bot = Bot(
#     token=TOKEN,
#     default=DefaultBotProperties(parse_mode=ParseMode.HTML)
# )

# dp = Dispatcher()

# async def main():
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())

# from aiogram import Bot, Dispatcher, F
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.types import Message
# import asyncio

# TOKEN = "8851227121:AAGfqlBKlAj2SjdwrkDOQ7_L_r1p7OsHJ-4"

# bot = Bot(
#     token=TOKEN,
#     default=DefaultBotProperties(parse_mode=ParseMode.HTML)
# )

# dp = Dispatcher(bot)

# @dp.message(F.text == " Привет")
# async def hello(message: Message):
#     await message.answer("Привет-я твой телеграм-бот!")

# @dp.message(F.text == "Как дела?")
# async def how_are_you(message: Message):
#     await message.answer("Отлично, у тебя как?")

# @dp.message()
# async def unknown(message: Message):
#     await message.answer("Я пока не понимаю эту команду.")

# async def main():
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     asyncio.run(main())

from aiogram import Bot, Dispatcher, F
import random
from datetime import datetime
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

TOKEN = "8851227121:AAGfqlBKlAj2SjdwrkDOQ7_L_r1p7OsHJ-4"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

@dp.message((F.text == "Привет") | (F.text == "привет"))
async def hello(message: Message):
    await message.answer("Привет! Я телеграм-бот!")

@dp.message((F.text == "Как дела?") | (F.text == "как дела?") | (F.text.lower() == "Как дела" ) | (F.text.lower() == "как дела"))
async def how_are_you(message: Message):
    await message.answer("Отлично, у тебя как?")

@dp.message(
    (F.text == "Кто ты") 
    | (F.text == "Кто ты?") 
    | (F.text == "кто ты") 
    | (F.text == "кто ты?")
)
async def who_are_you(message: Message):
    await message.answer("Я - телеграм-бот, созданный на Python!")

@dp.message(
      (F.text.lower() == "пока")
      | (F.text.lower() == "до свидания")
      | (F.text.lower() == "давай")
  )
async def bye(message: Message):
    await message.answer("Пока!")

@dp.message(
    (F.text.lower() == "орел или решка")
    | (F.text.lower() == "подбрось монетку")
    | (F.text.lower() == "монетка")
)
async def flip_coin(message: Message):
  # Случайным образом выбираем один из двух вариантов
  result = random.choice(["Орел", "Решка"])
  await message.answer(f" <b>{result}</b>!")

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("Привет! Я телеграм-бот! \nНапиши команду /help чтобы узнать подробнее.")
@dp.message(Command("about"))
async def about_cmd(message: Message):
    await message.answer("Я учебный бот, созданный на языке <b>Python</b>")

@dp.message(Command("time"))
async def time_cmd(message: Message):
    now = datetime.now().strftime("%H:%M:%S")
    await message.answer(f"Текущее время: <b>{now}</b>")

@dp.message(Command("dice"))
async def dice_cmd(message: Message):
  await message.answer_dice()
    
@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "Я понимаю фразы:\n"
        " Привет\n"
        " Как дела?\n"
        " Кто ты?\n"
        " Пока\n"
        " Подбрось монетку\n\n"
        "Команды:\n"
        "/start\n"
        "/help\n"
        "/dice\n"
        "/about\n"
        "/time"
    )

@dp.message()
async def unknown(message: Message):
    await message.answer("Я пока не понимаю эту команду, Напиши /help чтобы узнать на что я могу отвечать.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())