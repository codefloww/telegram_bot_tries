from aiogram.dispatcher.filters.state import State, StatesGroup


class AddingChannel(StatesGroup):
    ENTERING_USER_ID = State()


class RemovingChannel(StatesGroup):
    ENTERING_USER_ID = State()