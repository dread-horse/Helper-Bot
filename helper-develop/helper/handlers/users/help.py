from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Commads list: ",
            "/start - Start dialog",
            "/help - Get help",
            "/language - Select programming language")
    
    await message.answer("\n".join(text))
