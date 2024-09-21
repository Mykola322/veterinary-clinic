import json

from app.data import list_files


def open_file(path: str = list_files.ANIMALS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        animals = json.load(file)

    return animals