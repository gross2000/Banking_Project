import json
from datetime import datetime


def load_operations():

    """Загружает список операций клиента из файла .json"""
    with open("/home/cheandrey/PycharmProjects/Banking_Project/operations.json", 'r') as file:
        data = json.load(file)
        return data


def sort_last_five(operlist):
    """вибираем пять последних операций"""

    def get_date(item):
        return item.get('date','')

    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
            return True
        except ValueError:
            return False


    sorted_operations = sorted(operlist, key=lambda x: validate_date(get_date(x)), reverse=True)
    return sorted_operations[:5]


list_actions = load_operations()
#print(list_actions)



count = len(list_actions)

print(count)

i = 0
for dict in list_actions:
    for key in dict.keys():
        if key == "date":
            i += 1


print(i)

sort_last_five(list_actions)



list_five = sort_last_five(list_actions)
for operation in list_five:
    print(operation)