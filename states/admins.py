from aiogram.dispatcher.filters.state import State, StatesGroup


class AddingAdmin(StatesGroup):
    ENTERING_USER_ID = State()


class RemovingAdmin(StatesGroup):
    ENTERING_USER_ID = State()