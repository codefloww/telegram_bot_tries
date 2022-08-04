from aiogram.types import Message
from aiogram.dispatcher.filters import Filter

from utils.db import get_admins


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, message: Message):
        return message.chat.id in get_admins()
