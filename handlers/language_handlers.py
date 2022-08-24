from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboard.index import *

async def ask_language(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['userid'] =  msg.from_user.id
        await msg.answer("Виберіть мову\nВыберите язык\nChoose language", reply_markup=language_pick_keyboard)

# Start set language
async def set_language(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:    
        lang = callback.data.split("=")[1]
        output_msg = ""
        if lang == "UA":
            data['lang'] = 'ua'
            output_msg = "мова встановлена"
        elif lang == "RU":
            data['lang'] = 'ru'
            output_msg = "язык установлен"
        else:
            data['lang'] = 'en'
            output_msg = "language has been set"

    await callback.message.answer(output_msg, reply_markup=initial_keyboard)
    await callback.answer()