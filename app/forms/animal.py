from aiogram.fsm.state import State, StatesGroup


class AnimalsForm(StatesGroup):
    name = State()