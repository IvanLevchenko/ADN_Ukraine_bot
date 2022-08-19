import re

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from bot_connection import bot, dp
from db.api import insert_user

# state
class Registration_Form(StatesGroup):
    phone = State()
    name = State()
    surname = State()
    email = State()

# starting a registration
async def register_user(msg: types.Message):
    await Registration_Form.phone.set()
    await bot.send_message(msg.from_user.id, 'phone number')

# getting a phone number
async def register_user_phone(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_regexp = re.match("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$", msg.text)
        if phone_regexp:
            data['phone'] = msg.text
            await Registration_Form.next()
            await bot.send_message(msg.from_user.id, 'name')
        else:
            await bot.send_message(msg.from_user.id, 'enter valid phone number')
            await Registration_Form.phone.set()

# getting a name
async def register_user_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await Registration_Form.next()
    await bot.send_message(msg.from_user.id, 'second_name')

# getting surname
async def register_user_surname(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = msg.text
    await Registration_Form.next()
    await bot.send_message(msg.from_user.id, 'email')

# getting email and finishing state changing
async def register_user_email(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = msg.text
        insert_user({
            'name': data['name'],
            'surname': data['surname'],
            'phone': data['phone'],
            'email': data['email']
        })
        await msg.answer(
            "Name: %s \nSurname: %s \nPhone: %s \nEmail: %s"
            % (data['name'], data['surname'], data['phone'], data['email'])
        )
    await state.finish()
