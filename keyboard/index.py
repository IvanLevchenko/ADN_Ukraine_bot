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
    KeyboardButton('products')
)

# Keyboard with languages
language_pick_keyboard = InlineKeyboardMarkup(row_width=3)
language_pick_keyboard.row(
    InlineKeyboardButton(text='UA🇺🇦', callback_data="set_langage=UA"),
    InlineKeyboardButton(text='RU🇷🇺', callback_data="set_langage=RU"),
    InlineKeyboardButton(text='EN🇺🇸', callback_data="set_langage=ENG")
)

# Keyboard with registration info apply/decline
registration_valid_keyboard = InlineKeyboardMarkup(row_width=2)
registration_valid_keyboard.row(
    InlineKeyboardButton(text='confirm☑️', callback_data="registration_valid_keyboard=confirm"),
    InlineKeyboardButton(text='edit📝', callback_data="registration_valid_keyboard=edit")
)

# Keyboard with edit registration info
registration_edit_keyboard = InlineKeyboardMarkup(row_width=4)
registration_edit_keyboard.row(
    InlineKeyboardButton(text='Name', callback_data="registration_edit_keyboard=name"),
    InlineKeyboardButton(text='Surname', callback_data="registration_edit_keyboard=surname"),
).row(
    InlineKeyboardButton(text='Phone', callback_data="registration_edit_keyboard=phone"),
    InlineKeyboardButton(text='Email', callback_data="registration_edit_keyboard=email")
).add(
    InlineKeyboardButton(text='all again', callback_data="registration_edit_keyboard=all"),
)