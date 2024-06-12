import json
import datetime


def load_operations():

    """Загружает список операций клиента из файла .json"""
    with open("/home/cheandrey/PycharmProjects/Banking_Project/operations.json", 'r') as file:
        data = json.load(file)
        return data


list_line = load_operations()
print(list_line)
