from aiogram.dispatcher.filters import Text
from db.api import *
from handlers.catalogue_handlers import *
from handlers.language_handlers import *
from handlers.registration_handlers import *
from handlers.registration_handlers import Registration_Form

def create_handlers(dp: Dispatcher):
    dp.register_message_handler(choose_lang, commands=['start', 'help'])
    # dp.callback_query_handler(set_localisation_ua, text='set_localisation_ua') 
    # dp.callback_query_handler(set_localisation_ru, text='set_localisation_ru')
    # dp.callback_query_handler(set_localisation_en, text='set_localisation_en')
    dp.register_message_handler(register_user, Text(equals="register_user"), state=None)
    dp.register_message_handler(register_user_phone, state=Registration_Form.phone)
    dp.register_message_handler(register_user_name, state=Registration_Form.name)
    dp.register_message_handler(register_user_surname, state=Registration_Form.surname)
    dp.register_message_handler(register_user_email, state=Registration_Form.email)
    dp.register_message_handler(catalogue, Text(equals="catalog"))

