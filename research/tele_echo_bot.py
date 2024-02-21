import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
API_Token = os.getenv("Token")
print(API_Token)
print("a")
#configure logging
logging.basicConfig(level=logging.INFO)

#initialise and dispatcher
bot = Bot(token=API_Token)
dp = Dispatcher(bot)   # help to make the connection with telegram

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message) :
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.reply("Hi\nI am chatbot!\npowered by aiogram")

@dp.message_handler()
async def echo(message: types.Message) :
    """
    This will return echo
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(message.text)

if __name__ =="__main__":
    executor.start_polling(dp, skip_updates =True)



