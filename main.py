import logging
import os

from handlers.index import *
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from db.index import *

load_dotenv() # Loading .env

logging.basicConfig(level=logging.INFO) # Setting configuration

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

connect_db() # Connection to database
create_handlers(dp) # Initializing all handlers

if __name__ == "__main__": # Starting long polling
    executor.start_polling(dp)