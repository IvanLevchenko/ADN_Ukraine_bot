from aiogram import types
from bot_connection import dp
from keyboard.index import *

async def choose_lang(msg: types.Message):
    await msg.answer("Виберіть мову\nВыберите язык\nChoose language", reply_markup=language_pick_keyboard)


@dp.callback_query_handler(text='set_localisation_ua')
async def set_localisation_ua(callback: types.CallbackQuery):
    await callback.message.answer(
        'мова встановлена',
        reply_markup=context_menu_keyboard
    )  # In the future, connect keyboards of different localizations, or adapt one for multilingualism
    await callback.answer()


@dp.callback_query_handler(text='set_localisation_ru')
async def set_localisation_ru(callback: types.CallbackQuery):
    await callback.message.answer(
        'язык установлен',
        reply_markup=context_menu_keyboard
    )  # In the future, connect keyboards of different localizations, or adapt one for multilingualism
    await callback.answer()


@dp.callback_query_handler(text='set_localisation_en')
async def set_localisation_en(callback: types.CallbackQuery):
    await callback.message.answer(
        'language set',
        reply_markup=context_menu_keyboard
    )  # In the future, connect keyboards of different localizations, or adapt one for multilingualism
    await callback.answer()