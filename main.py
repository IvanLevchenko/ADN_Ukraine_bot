import logging
from aiogram import executor
from db.index import *
from handlers.index import create_handlers
from bot_connection import dp

logging.basicConfig(level=logging.INFO) # Setting configuration

connect_db() # Connection to database
create_handlers(dp) # Initializing all handlers

if __name__ == "__main__": # Starting long polling
    executor.start_polling(dp, skip_updates=True)

