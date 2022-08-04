from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

navigation_keyboard = ReplyKeyboardMarkup([
    [
        KeyboardButton("Add admin"),
        KeyboardButton("Remove admin")
    ],
    [
        KeyboardButton("Admins")
    ],
    [
        KeyboardButton("Add channel"),
        KeyboardButton("Remove channel")
    ],
    [
        KeyboardButton("Channels")
    ]
])
