import re

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from bot_connection import bot, dp
from db.api import insert_user
from keyboard.index import *

any_state = {
    'edit_regdat': 0
}

# state
class Registration_Form(StatesGroup):
    phone = State()
    name = State()
    surname = State()
    email = State()

async def get_registration_result(msg ,data ):
    return await msg.answer(
    "Name: %s \nSurname: %s \nPhone: %s \nEmail: %s"
    % (data['name'], data['surname'], data['phone'], data['email']),
    reply_markup=registration_valid_keyboard
) 
                
# starting a registration
async def register_user(msg: types.Message):
    await Registration_Form.phone.set()
    await bot.send_message(msg.from_user.id, 'phone number (example: 0337777777)')

# getting a phone number
async def register_user_phone(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        phone_regexp = re.match("^(?!\($)(?!\)$)(?!\+$)(?!\.$)(?!,$)([0-9]{10})$", msg.text)
        if phone_regexp:
            data['phone'] = msg.text
            if any_state['edit_regdat'] == 1:
                await state.finish()
                await get_registration_result(msg, data)
                any_state['edit_regdat'] = 0
            else: 
                await Registration_Form.next()
                await bot.send_message(msg.from_user.id, 'name')
        else:
            await bot.send_message(msg.from_user.id, 'enter valid phone number')
            await Registration_Form.phone.set()

# getting a name
async def register_user_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
        if any_state['edit_regdat'] == 1:
            await state.finish()
            await get_registration_result(msg, data)
            any_state['edit_regdat'] = 0
        else: 
            await Registration_Form.next()
            await bot.send_message(msg.from_user.id, 'second_name')

# getting surname
async def register_user_surname(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = msg.text
        if any_state['edit_regdat'] == 1:
            await state.finish()
            await get_registration_result(msg, data) 
            any_state['edit_regdat'] = 0
        else: 
            await Registration_Form.next()
            await bot.send_message(msg.from_user.id, 'email (example@gmail.com)')
        

# getting email and finishing state changing
async def register_user_email(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        email_regexp = re.match("((^[a-zA-Z0-9]+)(([_]?)|([.]|[-])?[a-zA-Z0-9]+)*@([a-zA-Z0-9]+)(([_]?)|([.]|[-])?[a-zA-Z0-9]+)*\.[a-zA-Z0-9]{2,}$)", msg.text)
        if email_regexp:
            data['email'] = msg.text
            await get_registration_result(msg, data)
            await state.finish()   
            any_state['edit_regdat'] = 0
        else:
            await bot.send_message(msg.from_user.id, 'enter valid email')
            await Registration_Form.email.set()


# Edit/Confirm registration info
async def register_ending(callback: types.CallbackQuery, state: FSMContext):
    state_valid = callback.data.split("=")[1]
    async with state.proxy() as data:
        if (state_valid == "confirm") & (any_state['edit_regdat'] == 0):
            insert_user({
            'name': data['name'],
            'surname': data['surname'],
            'phone': data['phone'],
            'email': data['email'],
            'lang': data['lang'],
            'userid': data['userid']
        })
            await callback.message.answer("CONGRATULATIONS")
        elif any_state['edit_regdat'] == 1: 
            await callback.message.answer('apply changes?', reply_markup=registration_valid_keyboard)
            any_state['edit_regdat'] = 0
        else:
            await callback.message.answer("What will we edit?", reply_markup=registration_edit_keyboard)
            any_state['edit_regdat'] = 1
      
    await callback.answer()

# Edit options
async def register_info_edit(callback: types.CallbackQuery):
    edit_buton = callback.data.split("=")[1]
    if edit_buton == "name":
        await Registration_Form.name.set()
        await callback.message.answer('enter name')
    elif edit_buton == "surname":
        await callback.message.answer('enter surname')
        await Registration_Form.surname.set()
    elif edit_buton == "num_phone":
        await Registration_Form.phone.set()
        await callback.message.answer('enter phone (example: 0337777777)')
    elif edit_buton == "email":
        await Registration_Form.email.set()
        await callback.message.answer('enter email (example@gmail.com)')
    else:
        await Registration_Form.phone.set()
        any_state['edit_regdat'] = 0
        await callback.message.answer('enter phone (example: 0337777777)')

    await callback.answer()