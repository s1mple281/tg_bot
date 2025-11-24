import asyncio

if __name__ == "__main__":
    asyncio.run(main())
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import random

TOKEN = "8346970854:AAE5o0f7orJ4wNySnDDuuLjwsaggXiRDw9E"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Answers list ---
answers = [
    "Да, однозначно! 🔥",
    "Нет 😢",
    "Шансы хорошие 😎",
    "50/50 🤷‍♂️",
    "Лучше не спрашивай… 😶",
    "Определённо да! 💫",
    "Определённо нет! 👎",
    "Звёзды говорят — да ✨",
    "Звёзды молчат… 😐",
    "Скорее да, чем нет 😉",
    "Скорее нет 😬",
]

# --- Keyboard ---
def main_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text="🔮 Предсказание")
    kb.button(text="🎲 Шанс")
    kb.button(text="❤️ Любовь")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🔮 Привет! Я *Гадалка 3000*."
        "Задай мне вопрос или выбери действие ниже:",
        reply_markup=main_keyboard()
    )

# --- Normal prediction ---
async def prediction(message: types.Message):
    await message.answer("Думаю… 🤔")
    await asyncio.sleep(1)
    await message.answer("Смотрю в будущее… 🔮✨")
    await asyncio.sleep(1)
    await message.answer(random.choice(answers))

# --- Chance command ---
@dp.message(Command("chance"))
async def chance_cmd(message: types.Message):
    percent = random.randint(1, 100)
    await message.answer(f"🎲 Шанс этого: *{percent}%*")

# --- Love compatibility ---
@dp.message(Command("love"))
async def love_cmd(message: types.Message):
    args = message.text.split()
    if len(args) < 3:
        return await message.answer("Используй: /love имя1 имя2")

    percent = random.randint(1, 100)
    await message.answer(f"❤️ Совместимость *{args[1]}* и *{args[2]}*: {percent}%")

# --- Buttons handler ---
@dp.message()
async def all_messages(message: types.Message):
    text = message.text.lower()

    if text == "🔮 предсказание":
        return await prediction(message)

    if text == "🎲 шанс":
        percent = random.randint(1, 100)
        return await message.answer(f"🎲 Шанс: {percent}%")

    if text == "❤️ любовь":
        return await message.answer("Используй команду: /love имя1 имя2")

    # If user asks any question → prediction
    if "?" in text:
        return await prediction(message)

    # Default fallback
    return await prediction(message)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
# Waiting for user confirmation to insert full code.




