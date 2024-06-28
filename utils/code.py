import json
import os
from datetime import datetime


def load_operations():
    """Загружает список операций клиента из файла .json"""
    # абсолютный путь /home/cheandrey/PycharmProjects/Banking_Project/operations.json
    filename = "operations.json"
    path = os.path.join(filename)
    with open(path, 'r') as file:
        data = json.load(file)
        return data


def execute_sort(listing):
    # отсортированные executed-транзакции"
    new_list = []
    for item in listing:
        if "state" in item:
            if item["state"] == "EXECUTED":
                new_list.append(item)
    return new_list


list_actions = load_operations()
new_lising = execute_sort(list_actions)


def sort_last_five(operlist):
    """виборка пяти последних операций"""

    def get_date(item):
        """проверка наличия данных по ключу date в словаре"""
        return item.get('date', '')

    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
            return True
        except ValueError:
            return False

    sorted_operations = sorted(operlist, key=lambda x: validate_date(get_date(x)), reverse=True)
    return sorted_operations



listing = sort_last_five(new_lising)
# Повторная сортировка полученного списка по дате в убывающем порядке
sorted_data = sorted(listing, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

def date_reform(listing):
    # преобразование даты в формат "21.01.2018"
    for item in listing:
        date_str = item["date"]
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        new_date = date_obj.strftime('%d.%m.%Y')
        item["date"] = new_date
    return listing


def from_reform(listing):
    # разделение счета 'from' пробелами и добавление звездочек"
    for item in listing:
        if 'from' in item:
            s = item["from"]
            # Находим индекс последнего пробела с конца
            space_index = s.rfind(" ")
            # Извлекаем правую часть после последнего пробела
            right_part = s[space_index + 1:]
            # Форматируем правую часть
            input_str = " ".join([right_part[i:i + 4] for i in range(0, len(right_part), 4)])
            output_str = ""
            # Разбиваем строку на блоки
            blocks = input_str.split()
            if "Счет" in item["from"]:
                blocks[1] = blocks[1][:-2]
                blocks[2] = blocks[2][2:]
            blocks[-2] = "**" * (len(blocks[-2]) // 2)
            blocks[-3] = blocks[-3][:-2] + "**"
            output_str = " ".join(blocks)
            # Соединяем части обратно
            result = f"{s[:space_index]} {output_str}"
            item["from"] = result
    return listing


def to_reform(listing):
    # преобразовавние счета 'to'"
    for item in listing:
        if 'to' in item:
            s = item["to"]
            # Находим индекс последнего пробела с конца
            space_index = s.rfind(" ")
            # Извлекаем правую часть после последнего пробела
            right_part = s[space_index + 1:]
            # Получаем последние шесть символов
            input_str = right_part[-6:]
            output_str = "**" + input_str[1:]
            result = f"{s[:space_index]} {output_str}"
            item["to"] = result
    return listing



last_list = date_reform(sorted_data[:5])
last_list = from_reform(last_list)
last_list = to_reform(last_list)