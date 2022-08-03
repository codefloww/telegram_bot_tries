from cgitb import text
from aiogram.dispatcher.filters.state import State, StatesGroup

class Navigation(StatesGroup):
    PICKING_OPTION = State()
# states_group = StatesGroup("navigation", on_enter=lambda *args: print("Entering navigation state"))

