from aiogram import dispatcher
from aiogram.dispatcher.filters import CommandStart, Command
from aiogram.types.message import Message

from loader import dp


@dp.message_handler(CommandStart())
async def start_handler(message: Message):
    pass


@dp.message_handler(CommandStart(), state=Navigation)
async def help_handler(message: Message):
    pass
