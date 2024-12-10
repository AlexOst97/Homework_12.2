import json
from typing import Any


def transaction(json_file: str) -> Any:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях"""
    empty_list: list[Any] = []
    if json_file is not list and len(json_file) > 0:
        with open(json_file, "r", encoding="utf-8") as file:
            transactions = json.load(file)
            return transactions
    else:
        return empty_list


print(
    transaction(
        r"C:\Users\sanya\PycharmProjects\python_project_dz2\data\operations.json"
    )
)
