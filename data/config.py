from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

HELP_TEXT = """Команди, які підтримуються ботом

/start - почати роботу
/help - допомога
/admins - панель адміністраторів
"""
