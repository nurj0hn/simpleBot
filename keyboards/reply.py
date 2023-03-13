from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(KeyboardButton("/help"))
kb.add(KeyboardButton("/start"))
kb.add(KeyboardButton("/inlines"))
kb.add(KeyboardButton("/keyboard_off"))
