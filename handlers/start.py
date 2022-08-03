from aiogram.dispatcher.filters import CommandStart
from aiogram.types.message import Message
from keyboards.navigation import navigation_keyboard
from states.navigation import Navigation
from loader import dp
from filters.is_admin import IsAdmin


@dp.message_handler(CommandStart(), IsAdmin(),state = '*')
async def start_handler(message: Message):
    print(message.chat.first_name)
    await message.answer("Hello, {}!".format(message.chat.first_name), reply_markup=navigation_keyboard)
    await Navigation.PICKING_OPTION.set()



# @dp.message_handler(CommandStart(), state=Navigation)
# async def help_handler(message: Message):
#     pass
