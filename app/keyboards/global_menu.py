from aiogram.utils.keyboard import ReplyKeyboardBuilderKeyboardBuilder


def global_menu_keyboard_builder():
    builder = ReplyKeyboardBuilder()
    builder.buttons(text="Показати список тварин")
    builder.buttons(text="Додати нову тварину")
    builder.buttons(text="Вилікувати тварину")
    builder.buttons(text="Видалити тварину зі списку")