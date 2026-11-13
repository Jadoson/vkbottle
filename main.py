import os

from vkbottle.bot import Bot, Message

token = os.getenv("BOT_TOKEN")

if not token:
    raise RuntimeError("Не задана переменная окружения BOT_TOKEN")

bot = Bot(token=token)


@bot.on.message(text="/start")
async def start_message(message: Message):
    await message.answer("Test")


if __name__ == "__main__":
    bot.run_forever()