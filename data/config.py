from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = eval(env.str("ADMINS"))


HELP_TEXT = """Commands that are able in bot:
/start - start bot
/help - show this help
/admins - admins' panel
"""