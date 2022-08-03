from aiogram import dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types.message import Message

from loader import dp
from filters.is_admin import IsAdmin
from keyboards.navigation import navigation_keyboard
from states.navigation import Navigation

@dp.message_handler(
    Command("start", "/!"),
    IsAdmin(),
    state="*"
)
async def start_handler(message: Message):
    print(message.chat.first_name)
    await message.answer("Hello, {}!".format(message.chat.first_name), reply_markup=navigation_keyboard)
    await Navigation.PICKING_OPTION.set()
