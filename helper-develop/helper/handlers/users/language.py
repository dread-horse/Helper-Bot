from aiogram import types

from data.messages import language_theme_message

from utils.engine.mydb_help import get_theme

from loader import dp, bot

from keyboards.inline.language import inline_language_menu
from keyboards.inline.theme import inline_theme_menu


@dp.message_handler(commands=['language'])
async def lan(message: types.Message):
    await bot.send_message(message.chat.id, "Programming Languages", reply_markup=inline_language_menu())


@dp.callback_query_handler()
async def language_call(call: types.CallbackQuery):
    calldata = call.data.split(' ')
    if calldata[0] == "language":
        await bot.send_message(call.message.chat.id, "Article by: ", reply_markup=inline_theme_menu(calldata[1]))

    elif calldata[0] == "theme":
        theme = get_theme(language=calldata[2], theme=calldata[1])
        await bot.send_message(call.message.chat.id, language_theme_message.format(theme[0], theme[1]))