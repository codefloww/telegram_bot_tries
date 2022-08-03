from aiogram import dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types.message import Message
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from loader import dp
from data.config import HELP_TEXT
from filters.is_admin import IsAdmin

@dp.message_handler(Command('help', '/!'),IsAdmin(),state = '*')
async def help_handler(message: Message,  state = FSMContext):
    await message.answer(HELP_TEXT,
        reply_markup=ReplyKeyboardRemove())
    await state.reset_state()


