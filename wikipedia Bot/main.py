import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia
API_TOKEN = 'YOUR TOKEN'
wikipedia.set_lang("en")
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi. I'll help you to look for info from wikipedia.Type what you wanna search...") 



@dp.message_handler()
async def wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('There is no info accourding to your search.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
