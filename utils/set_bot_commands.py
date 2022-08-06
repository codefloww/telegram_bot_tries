from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Open navigation"),
            types.BotCommand("help", "Open help"),
            types.BotCommand("edit_bio", "Edit bio in all channels"),
        ]
    )
