import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties

# Инициализация бота с новым способом установки parse_mode
bot = Bot(
    token=os.getenv("BOT_TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)
dp = Dispatcher()

# Партнёрская ссылка и промокод
link = "https://app.lbxinfo.org/goto/raf2?rid=16981019"
promo = "GIFT"

@dp.message(Command("start"))
async def send_welcome(message: Message):
    # Создание клавиатуры
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Как получить акции?")]],
        resize_keyboard=True
    )
    await message.answer(
        "Привет! Я помогу тебе получить акции Tesla, Google и других компаний до $200 в подарок!",
        reply_markup=kb
    )

@dp.message(lambda msg: msg.text == "Как получить акции?")
async def explain_steps(message: Message):
    await message.answer(
        f"Все просто:\n"
        f"1. Перейди по ссылке: {link}\n"
        f"2. Зарегистрируйся\n"
        f"3. Введи промокод: *{promo}*\n"
        f"4. Пополни счёт на любую сумму\n\n"
        f"После этого ты получишь случайную акцию до *$200* на счёт!\n\n"
        f"Удачи в инвестициях!"
    )

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
