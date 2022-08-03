from aiogram import dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types.message import Message

from loader import dp
from keyboards.navigation import navigation_keyboard
from states.navigation import Navigation


@dp.message_handler(
    text="Button 1",
    state=Navigation.PICKING_OPTION
)
async def button_1_handler(message: Message):
    await message.answer("Ти натиснув кнопку 1!")
