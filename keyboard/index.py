from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# Initial keyboard
initial_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
initial_keyboard.row(
    KeyboardButton('register_user'), 
    KeyboardButton('catalogue')
)

# Keyboard with languages
language_pick_keyboard = InlineKeyboardMarkup(row_width=3)
language_pick_keyboard.row(
    InlineKeyboardButton(text='UA🇺🇦', callback_data="set_langage=UA"),
    InlineKeyboardButton(text='RU🇷🇺', callback_data="set_langage=RU"),
    InlineKeyboardButton(text='EN🇺🇸', callback_data="set_langage=ENG")
)