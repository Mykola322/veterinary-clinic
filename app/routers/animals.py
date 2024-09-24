from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from app.data import files_actions
from app.keyboards.animals import anims_keyboard_builder, anim_actions_keyboards

anims_router = Router()


@anims_router.message(F.text == "Показати список тварин")
async def show_animals(message: Message, state: FSMContext):
    animals = files_actions.open_file()
    keyboard = anims_keyboard_builder(animals)
    await message.answer(
        text="Виберіть тварину",
        reply_markup=keyboard
    )

@anims_router.callback_query(F.data.startswith("anim_"))
async def animal_actions(callback: CallbackQuery, state: FSMContext):
    animal = callback.message.data.split("_")[-1]
    keyboard = anim_actions_keyboards(animal)
    await callback.message.answer(
        text=animal,
        reply_markup=keyboard
        )