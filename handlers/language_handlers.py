from aiogram import types
from keyboard.index import *

async def ask_language(msg: types.Message):
    await msg.answer("Виберіть мову\nВыберите язык\nChoose language", reply_markup=language_pick_keyboard)

async def set_language(callback: types.CallbackQuery):
    lang = callback.data.split("=")[1]
    output_msg = ""
    if lang == "UA":
        output_msg = "мова встановлена"
    elif lang == "RU":
        output_msg = "язык установлен"
    else:
        output_msg = "language has been set"

    await callback.message.answer(output_msg, reply_markup=initial_keyboard)
