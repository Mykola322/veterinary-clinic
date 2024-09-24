from aiogram.utils.keyboard import InlineKeyboardBuilder


def anim_keyboard_builder(animals: list):
    builder = InlineKeyboardBuilder()

    for animal in animals:
        builder.button(text=animal, callback_data=f"anim_{animal}")

    builder.adjust(3)
    return builder.as_markup()

def anim_actions_keyboards(animal: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Вилікувати тварину", callback_data=f"curve_anim_{animal}")
    builder.button(text="Видалити тварину",callback_data=f"del_anim_{animal}")
    return builder.as_markup()