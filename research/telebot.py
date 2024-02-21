from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import openai
import sys
from openai import OpenAI
client=OpenAI()

class Reference:
    '''
    A class to stor previously response from chatgpt API
    
    '''
    def __init__(self)-> None:
        self.response = ""  # it will save question here


load_dotenv()
OpenAI.api_key = os.getenv("OpenAI_API_KEY")



reference = Reference()
Token = os.getenv("Token")

#model name
MODEL_NAME = "gpt-3.5-turbo"
bot = Bot(token=Token)
dispatcher = Dispatcher(bot)   # help to make the connection with telegram

def clear_past():
    '''
    This function to clear the previous conversation and context
    '''
    reference.response=""

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message) :
    """
    This handler receives messages with `/start` command
    """
    await message.reply("Hi\nI am chatbot!\ncreated by Upasana. How can I assist you?")

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message) :
    """
    A handler to clear the previous conversation and context.
    """
    await message.reply("I have cleared the past conversation and context")

@dispatcher.message_handler(commands=['help'])
async def help(message: types.Message) :
    """
    This handler to display messages with `/start` command
    """
    help_command ="""
    Hi there, I'm ChatGPT Telegram bot created by Upasana ! Please follow these commands-
    /start - to start the conversation
    /clear- to clear the past conversation
    /help - to get this help menu
    I hope this help.:)

"""
    await message.reply(help_command)

@dispatcher.message_handler()
async def chatgpt(message: types.Message) :
    """
    A handler to process the user's input and genearte a response using ChatGPT API
    """
    print(f">>> USER: \n\t{message.text}")
    response = client.chat.completions.create(
        model = MODEL_NAME,
        messages= [
            {"role": "assistant", "content":reference.response}, # role assistant
            {"role": "user", "content":message.text}  # our query
            ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id =message.chat.id, text=reference.response)  


if __name__ =="__main__":
    executor.start_polling(dispatcher, skip_updates =True)

