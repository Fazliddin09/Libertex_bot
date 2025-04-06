import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

link = "https://app.lbxinfo.org/goto/raf2?rid=16981019"
promo = "GIFT"

@dp.message(commands=['start'])
async def send_welcome(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("Как получить акции?"))
    await message.answer(
        "Привет! Я помогу тебе получить акции Tesla, Google и других компаний до $200 в подарок!",
        reply_markup=kb
    )

@dp.message(lambda message: message.text == "Как получить акции?")
async def explain_steps(message: types.Message):
    await message.answer(
        f"Все просто:\n"
        f"1. Перейди по ссылке: {link}\n"
        f"2. Зарегистрируйся\n"
        f"3. Введи промокод: *{promo}*\n"
        f"4. Пополни счёт на любую сумму\n\n"
        f"После этого ты получишь случайную акцию до *$200* на счёт!\n\n"
        f"Удачи в инвестициях!",
        parse_mode="Markdown"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
