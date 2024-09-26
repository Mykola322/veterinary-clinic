import json
import os
from app.data import list_files



def open_file(path: str = list_files.ANIMALS) -> list:
    if not os.path.exists(path):
        with open(path, "w") as fh:
            json.dump([], fh)

    with open(path, "r", encoding="utf-8") as file:
        animals = json.load(file)

    return animals


def save_file(file: list, path: str = list_files.ANIMALS):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(file, fh, indent=4, ensure_ascii=False)


def del_animal(animal, path: str = list_files):
    animals = open_file()
    animals.remove(animal)
    save_file(animals)
    return f"Тварину '{animal}' було успішно видалено!"


def curve_animal(animal, path: str = list_files.CURVE_ANIMALS)-> str:
    del_animal(animal)

    curve_animals = open_file(path)
    curve_animals.append(animal)
    save_file(curve_animals, path)

    return f"Тварину '{animal}' було успішно вилікувано!"


def add_animal(animal, path: str = list_files.ANIMALS) -> str:
    animals = open_file()

    if animal not in animals:
        animals.append(animal)
        save_file(animals)
        msg = f"Тварину '{animal}' було успішно додано!"
    else:
        msg = f"Тварина '{animal}' уже є у списку."

    return msg