from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import files_actions, list_files
from app.keyboards.animals import anims_keyboard_builder, anim_actions_keyboards
from app.forms.animal import AnimalsForm


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
    animal = callback.data.split("_")[-1]
    keyboard = anim_actions_keyboards(animal)
    await callback.message.answer(
        text=animal,
        reply_markup=keyboard
        )

@anims_router.callback_query(F.data.startswith("curve_anim_"))
async def curve_animal(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    msg = files_actions.curve_animal(animal)
    await callback.message.answer(text=msg)


@anims_router.callback_query(F.data.startswith("del_anim_"))
async def del_animal(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    msg = files_actions.del_animal(animal)
    await callback.message.answer(text=msg)

@anims_router.message(F.text == "Додати нову тварину")
async def add_animal(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(AnimalsForm.name)
    await message.answer(text="Введіть кличку тварини")

@anims_router.message(AnimalsForm.name)
async def save_new_animal(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = files_actions.add_animal(data.get("name"))
    await message.answer(text=msg)

@anims_router.message(F.text == "Показати список вилікуваних тварин")
async def show_curved_anims(message: Message, state: FSMContext):
    curve_animals = files_actions.open_file(list_files.CURVE_ANIMALS)

    msg = ""
    for anim in enumerate(curve_animals, start=1):
        msg += f"{i}. {anim}\n"

    await message.answer(text=msg)