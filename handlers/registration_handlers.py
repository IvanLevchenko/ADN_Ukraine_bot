import re
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from bot_connection import bot, dp
from keyboard.index import *

registration_valid_keyboard_edit_state = False

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
        if registration_valid_keyboard_edit_state == False:
            await Registration_Form.next()
            await bot.send_message(msg.from_user.id, 'second_name')
        await msg.answer(
        "Name: %s \nSurname: %s \nPhone: %s \nEmail: %s"
        % (data['name'], data['surname'], data['phone'], data['email']), 
        reply_markup=registration_valid_keyboard
        )
        registration_valid_keyboard_edit_state = False
        await state.finish()
    

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
        await msg.answer(
            "Name: %s \nSurname: %s \nPhone: %s \nEmail: %s"
            % (data['name'], data['surname'], data['phone'], data['email']), 
            reply_markup=registration_valid_keyboard
        )
    await state.finish()

@dp.callback_query_handler(text='registration_valid_keyboard_confirm')
async def registration_valid_keyboard_confirm(callback: types.CallbackQuery):
    await callback.message.answer(
        'registration successfully completed'
    )

@dp.callback_query_handler(text='registration_valid_keyboard_edit')
async def registration_valid_keyboard_edit(callback: types.CallbackQuery):
    registration_valid_keyboard_edit_state = True
    await callback.message.answer(
        'choose what you need',
        reply_markup=registration_edit_keyboard
    )
    
    
@dp.callback_query_handler(text='registration_edit_keyboard_name')
async def registration_edit_keyboard_name(callback: types.CallbackQuery):
    await Registration_Form.name.set()
    
    
# @dp.callback_query_handler(text='registration_edit_keyboard_surname')
# async def registration_edit_keyboard_surname(callback: types.CallbackQuery):
#     await callback.message.answer("",reply_markup=)
    
    
# @dp.callback_query_handler(text='registration_edit_keyboard_phone')
# async def registration_edit_keyboard_phone(callback: types.CallbackQuery):
#     await callback.message.answer("",reply_markup=)


# @dp.callback_query_handler(text='registration_edit_keyboard_email')
# async def registration_edit_keyboard_email(callback: types.CallbackQuery):
#     await callback.message.answer("",reply_markup=)


# @dp.callback_query_handler(text='registration_edit_keyboard_all')
# async def registration_edit_keyboard_all(callback: types.CallbackQuery):
