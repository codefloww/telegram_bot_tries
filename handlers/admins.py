from aiogram import dispatcher
from aiogram.types.message import Message
from aiogram.types.reply_keyboard import ReplyKeyboardRemove

from loader import dp
from keyboards.navigation import navigation_keyboard
from states.admins import AddingAdmin, RemovingAdmin
from states.navigation import Navigation
from utils.db import get_admins, add_admin, remove_admin


@dp.message_handler(
    text="Add admin",
    state=Navigation.PICKING_OPTION
)
async def adding_admin_start_handler(message: Message):
    await message.answer(
        "Пришли user id адміна наступним повідомленням.",
        reply_markup=ReplyKeyboardRemove()
    )
    await AddingAdmin.ENTERING_USER_ID.set()


@dp.message_handler(
    state=AddingAdmin.ENTERING_USER_ID
)
async def adding_admin_finish_handler(message: Message):
    try:
        user_id = int(message.text)
        add_admin(user_id)
        await message.answer(
            "Адміна успішно додано!",
            reply_markup=navigation_keyboard
        )
    except:
        await message.answer(
            "Ти ввів неправильний user id.",
            reply_markup=navigation_keyboard
        )

    await Navigation.PICKING_OPTION.set()


@dp.message_handler(
    text="Remove admin",
    state=Navigation.PICKING_OPTION
)
async def removing_admin_start_handler(message: Message):
    await message.answer(
        "Пришли user id адміна наступним повідомленням.",
        reply_markup=ReplyKeyboardRemove()
    )
    await RemovingAdmin.ENTERING_USER_ID.set()


@dp.message_handler(
    state=RemovingAdmin.ENTERING_USER_ID
)
async def removing_admin_finish_handler(message: Message):
    try:
        user_id = int(message.text)
        remove_admin(user_id)
        await message.answer(
            "Адміна успішно видалено!",
            reply_markup=navigation_keyboard
        )
    except:
        await message.answer(
            "Ти ввів неправильний user id.",
            reply_markup=navigation_keyboard
        )

    await Navigation.PICKING_OPTION.set()


@dp.message_handler(
    text="Admins",
    state=Navigation.PICKING_OPTION
)
async def admins_list_handler(message: Message):
    admins = get_admins()
    admins_str = ""
    for admin in admins:
        admins_str = admins_str + str(admin) + "\n"

    await message.answer(
        admins_str,
        reply_markup=navigation_keyboard
    )
