from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from db.api import *

class S(StatesGroup):
    ada = State()

def create_handlers(dp: Dispatcher):
    dp.register_message_handler(register_user, commands=["register"], state=S.ada)

async def register_user(msg: types.Message, state: FSMContext):
    await msg.answer("email: ")
    await state.set_state(sc=msg.text)
