from aiogram.types import Message
from aiogram.dispatcher.filters import Filter
from data.config import ADMINS

class IsAdmin(Filter):
    key = 'is_admin'

    async def check(self, message: Message):
        return message.chat.id in ADMINS
