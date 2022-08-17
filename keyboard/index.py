from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.row(
    InlineKeyboardButton(text="Register", callback_data="/register"),
    InlineKeyboardButton(text="Goods", callback_data="/goods"),
)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)   
kb_client.row(KeyboardButton('register_user'), 
              KeyboardButton('catalog')
)


kb_start_lang = InlineKeyboardMarkup(row_width=3)
kb_start_lang.row(InlineKeyboardButton(text='UA🇺🇦', callback_data="sss"), 
             InlineKeyboardButton(text='RU🇷🇺', callback_data="sss"), 
             InlineKeyboardButton(text='EN🇺🇸', callback_data="sss")
)