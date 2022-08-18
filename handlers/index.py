from email import message
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from db.api import *
from keyboard.index import *
from bot_connection import bot, dp

class user_registration_data(StatesGroup):
    phone_number = State()
    name = State()
    second_name = State()


def create_handlers(dp: Dispatcher):
    dp.register_message_handler(choose_lang, commands=['start', 'help'])
    # dp.callback_query_handler(set_localisation_ua, text='set_localisation_ua') 
    # dp.callback_query_handler(set_localisation_ru, text='set_localisation_ru')
    # dp.callback_query_handler(set_localisation_en, text='set_localisation_en')
    dp.register_message_handler(register_user, Text(equals="register_user"), state=None)
    dp.register_message_handler(register_user_phone_number, state=user_registration_data.phone_number)
    dp.register_message_handler(register_user_name, state=user_registration_data.name)
    dp.register_message_handler(register_user_second_name, state=user_registration_data.second_name)
    dp.register_message_handler(catalog, Text(equals="catalog"))


async def choose_lang(msg: types.Message):
    await msg.reply("Виберіть мову\nВыберите язык\nChoose language", reply_markup=language_pick_keyboard)
    
    
@dp.callback_query_handler(text='set_localisation_ua')
async def set_localisation_ua(callback: types.CallbackQuery):
    await callback.message.answer('мова встановлена', reply_markup=context_menu_keyboard) #In the future, connect keyboards of different localizations, or adapt one for multilingualism
    await callback.answer()


@dp.callback_query_handler(text='set_localisation_ru')    
async def set_localisation_ru(callback: types.CallbackQuery):
    await callback.message.answer('язык установлен', reply_markup=context_menu_keyboard) #In the future, connect keyboards of different localizations, or adapt one for multilingualism
    await callback.answer()


@dp.callback_query_handler(text='set_localisation_en')
async def set_localisation_en(callback: types.CallbackQuery):
    await callback.message.answer('language set', reply_markup=context_menu_keyboard) #In the future, connect keyboards of different localizations, or adapt one for multilingualism
    await callback.answer()
    
    
#call register and go to FSM state - await user_registration_data.phone_number.set()
async def register_user(msg: types.Message):
    await user_registration_data.phone_number.set()
    await bot.send_message(msg.from_user.id,'phone number')
    
    
#getting a phone number
async def register_user_phone_number(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = msg.text
    await user_registration_data.next()
    await bot.send_message(msg.from_user.id, 'name')


#getting a name
async def register_user_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await user_registration_data.next()
    await bot.send_message(msg.from_user.id, 'second_name')

    
#receiving a surname with subsequent exit from the FSM state - await state.finish()
async def register_user_second_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['second_name'] = msg.text
    async with state.proxy() as data:
        await bot.send_message(msg.from_user.id, str(data))
    await state.finish()


async def catalog(msg: types.Message):
    await msg.reply("testovik")