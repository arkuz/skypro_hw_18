import json


def _load_json_file(filename: str) -> list[dict]:
    """ Загрузить JSON файл """
    with open(filename, encoding='utf8') as file:
        return json.load(file)
