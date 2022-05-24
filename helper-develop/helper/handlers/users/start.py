from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from data.messages import start_message
from keyboards.default import menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    await message.answer(
        text=start_message.format(message.from_user.full_name))
