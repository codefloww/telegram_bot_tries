import aiogram
from aiogram.types import Message
from aiogram.dispatcher.filters import Filter

class IsUsername(Filter):
    key = 'is_username'

    async def check(self, message: Message):
        return message.chat.username and 'B' == message.chat.username[0]