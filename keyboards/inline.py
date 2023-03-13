from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


ikb = InlineKeyboardMarkup(row_width=3)
cb = CallbackData("ikb", "action")

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("plus", callback_data=cb.new("plus"))],
    [InlineKeyboardButton("minus", callback_data=cb.new("minus"))],
    [InlineKeyboardButton("random", callback_data=cb.new("random"))],
    [InlineKeyboardButton("close", callback_data=cb.new("close"))],
])
