"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json


def load_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as origin:
            json_data = json.load(origin)
    except FileNotFoundError:
        json_data = {'orders': []}
    return json_data


def write_to_file(filename, data):
    data_write = load_from_file(filename)
    data_write['orders'].extend(data)
    with open(filename, 'w', encoding='utf-8') as destination:
        json.dump(data_write, destination, indent=4)


orders = [
    {
        'item': 'Carrow',
        'quantity': 10,
        'price': 15.5,
        'buyer': 'Petr Markov',
        'date': '04.04.2023'
    },
    {
        'item': 'Tomato',
        'quantity': 1,
        'price': 10.0,
        'buyer': 'Mark Petrow',
        'date': '03.04.2023'
    },
    {
        'item': 'Potato',
        'quantity': 5,
        'price': 50.0,
        'buyer': 'Petr Vasilev',
        'date': '02.04.2023'
    }
]

write_to_file('orders.json', orders)
