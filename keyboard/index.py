from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.row(
    InlineKeyboardButton(text="Register", callback_data="/register"),
    InlineKeyboardButton(text="Goods", callback_data="/goods"),
)