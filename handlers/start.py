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
    # Присилаємо повідомлення-відповідь з клавіатурою
    await message.answer(
        "Привіт, " + message.chat.first_name,
        reply_markup=navigation_keyboard
    )

    # Задаємо стан вибору опції з клавіатури
    await Navigation.PICKING_OPTION.set()
