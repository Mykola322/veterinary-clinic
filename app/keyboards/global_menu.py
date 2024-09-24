from aiogram.utils.keyboard import ReplyKeyboardBuilder

def global_menu_keyboard_builder():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Показати список тварин")
    builder.button(text="Додати нову тварину")
    builder.button(text="Вилікувати тварину")
    builder.button(text="Видалити тварину зі списку")
    builder.adjust(1)
    return builder.as_markup()
