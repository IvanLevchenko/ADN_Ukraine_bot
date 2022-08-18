from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

keyboard = InlineKeyboardMarkup(row_width=2)
# keyboard.row(
#     InlineKeyboardButton(text="Register", callback_data="/register"),
#     InlineKeyboardButton(text="Goods", callback_data="/goods"),
# )

context_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)   
context_menu_keyboard.row( 
    KeyboardButton('register_user'), 
    KeyboardButton('catalog')
)

language_pick_keyboard = InlineKeyboardMarkup(row_width=3)
language_pick_keyboard.row(
    InlineKeyboardButton(text='UA🇺🇦', callback_data="set_localisation_ua"), 
    InlineKeyboardButton(text='RU🇷🇺', callback_data="set_localisation_ru"), 
    InlineKeyboardButton(text='EN🇺🇸', callback_data="set_localisation_en")
)