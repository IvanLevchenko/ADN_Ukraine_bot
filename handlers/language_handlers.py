from aiogram import types
from keyboard.index import *
from db.api import check_if_user_exists

async def ask_language(msg: types.Message):
    user_exists = check_if_user_exists(msg.from_user.id)
    if user_exists:
        return
    else:
        await msg.answer("Виберіть мову\nВыберите язык\nChoose language", reply_markup=language_pick_keyboard)


async def set_language(callback: types.CallbackQuery):
    lang = callback.data.split("=")[1]
    if lang == "UA":
        output_msg = "мова встановлена"
    elif lang == "RU":
        output_msg = "язык установлен"
    else:
        output_msg = "language has been set"

    await callback.message.answer(output_msg, reply_markup=initial_keyboard)
    await callback.answer()