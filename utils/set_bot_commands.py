from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Open navigation"),
            types.BotCommand("add_channel", "Add channel"),
            types.BotCommand("edit_bio", "Edit bio in all channels"),
        ]
    )
