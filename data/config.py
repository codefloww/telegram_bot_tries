from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

HELP_TEXT = """Commands, supported in bot

/start - start a bot
/help - show this text
"""
