from aiogram.dispatcher.filters import Text
from db.api import *
from handlers.language_handlers import *
from handlers.registration_handlers import *
from handlers.registration_handlers import Registration_Form

def create_handlers(dp: Dispatcher):
    # General commands
    dp.register_message_handler(ask_language, commands=['start'])
    # Registration
    dp.register_message_handler(register_user, Text(equals="register_user"), state=None)
    dp.register_message_handler(register_user_phone, state=Registration_Form.phone)
    dp.register_message_handler(register_user_name, state=Registration_Form.name)
    dp.register_message_handler(register_user_surname, state=Registration_Form.surname)
    dp.register_message_handler(register_user_email, state=Registration_Form.email)
    # Registration confirm/edit
    dp.register_callback_query_handler(register_ending, Text(equals=[
    "registration_valid_keyboard=confirm",
    "registration_valid_keyboard=edit"
    ]))
    # Edit register data
    dp.register_callback_query_handler(register_info_edit, Text(equals=[
    "registration_edit_keyboard=name",
    "registration_edit_keyboard=surname",
    "registration_edit_keyboard=all",
    "registration_edit_keyboard=num_phone",
    "registration_edit_keyboard=email"
    ]))
    # Language
    dp.register_callback_query_handler(set_language, Text(equals=[
    "set_langage=UA",
    "set_langage=RU",
    "set_langage=ENG"
    ]))