from aiogram.dispatcher.filters  import Command
from aiogram import types

from loader import dp
from states.navigation import Navigation


@dp.message_handler(text = '/admins', state=Navigation.PICKING_OPTION)
async def start_button_handler(message: types.Message):
    await message.answer("You have pressed button /admins")