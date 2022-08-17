from email import message
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from db.api import *
from keyboard.index import *
from bot_connections import bot

class reg_data(StatesGroup):
    ph_num = State()
    name = State()
    second_name = State()


def create_handlers(dp: Dispatcher):
    dp.register_message_handler(choose_lang, commands=['start', 'help'])
    dp.register_message_handler(register_user, Text(equals="register_user"), state=None)
    dp.register_message_handler(register_user_ph_num, state=reg_data.ph_num)
    dp.register_message_handler(register_user_name, state=reg_data.name)
    dp.register_message_handler(register_user_second_name, state=reg_data.second_name)
    dp.register_message_handler(catalog, Text(equals="catalog"))


async def choose_lang(msg: types.Message):
    await msg.reply("Виберіть мову\nВыберите язык\nChoose language", reply_markup=kb_start_lang)
    await bot.send_message(msg.from_user.id,'hehe-haha', reply_markup=kb_client)
    
#вызов регистрации и переход в Машинное состояние - await reg_data.ph_num.set()
async def register_user(msg: types.Message):
    await reg_data.ph_num.set()
    await bot.send_message(msg.from_user.id,'phone number')
#перехват номера телефона
async def register_user_ph_num(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ph_num'] = msg.text
    await reg_data.next()
    await bot.send_message(msg.from_user.id, 'name')

#перехват имени
async def register_user_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await reg_data.next()
    await bot.send_message(msg.from_user.id, 'second_name')
    
#перехват фамилии и вывод словаря в чат с последующим выходом с машинного состояния - await state.finish()
async def register_user_second_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['second_name'] = msg.text
    async with state.proxy() as data:
        await bot.send_message(msg.from_user.id, str(data))
    await state.finish()

async def catalog(msg: types.Message):
    await msg.reply("ТЫ гейская скотина")