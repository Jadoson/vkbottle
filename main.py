import os
import asyncio

from vkbottle.bot import Bot, Message

token = os.getenv("BOT_TOKEN")

if not token:
    raise RuntimeError("Не задана переменная окружения BOT_TOKEN")

bot = Bot(token=token)


@bot.on.message(text="/start")
async def start_message(message: Message):
    await message.answer("Test")


if __name__ == "__main__":
    asyncio.run(bot.run_polling())