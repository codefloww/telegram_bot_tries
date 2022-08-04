from aiogram import dispatcher
from aiogram.types.message import Message
from aiogram.types.reply_keyboard import ReplyKeyboardRemove

from loader import dp
from keyboards.navigation import navigation_keyboard
from states.channels import AddingChannel, RemovingChannel
from states.navigation import Navigation
from utils.db import get_channels, add_channel, remove_channel


@dp.message_handler(
    text="Add channel",
    state=Navigation.PICKING_OPTION
)
async def adding_channel_start_handler(message: Message):
    await message.answer(
        "Пришли user id канала наступним повідомленням.",
        reply_markup=ReplyKeyboardRemove()
    )
    await AddingChannel.ENTERING_USER_ID.set()


@dp.message_handler(
    state=AddingChannel.ENTERING_USER_ID
)
async def adding_channel_finish_handler(message: Message):
    try:
        user_id = int(message.text)
        try:
            member = await dp.bot.get_chat_member(user_id, dp.bot.id)
        except:
            await message.answer(
                "Треба додати бота до чату!",
                reply_markup=navigation_keyboard
            )
        else:
            if not member.can_change_info:
                await message.answer(
                    "Треба дати права адміна боту!",
                    reply_markup=navigation_keyboard
                )
            else:
                add_channel(user_id)
                await message.answer(
                    "Канал успішно додано!",
                    reply_markup=navigation_keyboard
                )
    except:
        await message.answer(
            "Ти ввів неправильний user id.",
            reply_markup=navigation_keyboard
        )

    await Navigation.PICKING_OPTION.set()


@dp.message_handler(
    text="Remove channel",
    state=Navigation.PICKING_OPTION
)
async def removing_channel_start_handler(message: Message):
    await message.answer(
        "Пришли user id канала наступним повідомленням.",
        reply_markup=ReplyKeyboardRemove()
    )
    await RemovingChannel.ENTERING_USER_ID.set()


@dp.message_handler(
    state=RemovingChannel.ENTERING_USER_ID
)
async def removing_channel_finish_handler(message: Message):
    try:
        user_id = int(message.text)
        remove_channel(user_id)
        await message.answer(
            "Канал успішно видалено!",
            reply_markup=navigation_keyboard
        )
    except:
        await message.answer(
            "Ти ввів неправильний user id.",
            reply_markup=navigation_keyboard
        )

    await Navigation.PICKING_OPTION.set()


@dp.message_handler(
    text="Channels",
    state=Navigation.PICKING_OPTION
)
async def channels_list_handler(message: Message):
    channels = get_channels()
    channels_str = ""
    for channel in channels:
        channels_str = channels_str + str(channel) + "\n"

    await message.answer(
        channels_str,
        reply_markup=navigation_keyboard
    )
