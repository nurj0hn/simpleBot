from aiogram import types
from config import dp, bot
from keyboards.reply import ReplyKeyboardRemove, kb
from keyboards.inline import ikb, cb
import random


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="""
<b>/help</b> - <em>show all command with descrition</em>
<b>/start</b> - <em>start bot</em>
<b>/inlines</b> - <em>show inline with plus/minu/random functions</em>

""",
        parse_mode="HTML",
    )
    await message.delete()


@dp.message_handler(commands=["keyboard_off"])
async def help(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Keyboard turned off",
        reply_markup=ReplyKeyboardRemove(),
    )
    await message.delete()


@dp.message_handler(commands=["start"])
async def help(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Hey, Im a bot, and i react to this words on markup keyboard so...",
        reply_markup=kb,
    )
    await message.delete()


# inline kayboards and callback handlers

number = 0


@dp.message_handler(commands=["inlines"])
async def btn(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id, text=f"current number: {number}", reply_markup=ikb
    )


@dp.callback_query_handler(cb.filter(action="plus"))
async def ikb_cd_handler(callback: types.CallbackQuery, callback_data: dict):
    global number
    number += 1
    await callback.message.edit_text(f"current number: {number}", reply_markup=ikb)


@dp.callback_query_handler(cb.filter(action="minus"))
async def ikb_cd_handler(callback: types.CallbackQuery, callback_data: dict):
    global number
    number -= 1
    await callback.message.edit_text(f"current number: {number}", reply_markup=ikb)


@dp.callback_query_handler(cb.filter(action="random"))
async def ikb_cd_handler(callback: types.CallbackQuery, callback_data: dict):
    global number
    number = random.randint(1000, 2000)
    await callback.message.edit_text(f"fcurrent number: {number}", reply_markup=ikb)


@dp.callback_query_handler(cb.filter(action="close"))
async def ikb_cd_handler(callback: types.CallbackQuery, callback_data: dict):
    await callback.message.delete()
