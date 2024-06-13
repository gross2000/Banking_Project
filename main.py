from utils.code import last_list


for item in last_list:
    print(f"{item['date']} {item['description']}")
    if 'from' in item and 'to' in item:
        print(f"{item['from']} -> {item['to']}")
    print(f"{item['operationAmount']['amount']} {item['operationAmount']['currency'] ['name']}")
    print()