""" 4) Задание на закрепление знаний по модулю json. Есть файл orders
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
"orders": [
{
"item": "принтер",
"quantity": "10",
"price": "6700",
"buyer": "Ivanov I.I.",
"date": "24.09.2017"
},
{
"item": "scaner",
"quantity": "20",
"price": "10000",
"buyer": "Petrov P.P.",
"date": "11.01.2018"
},
]
}
вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    new_order = {'item': item, 'quantity': quantity,
              'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json', 'r', encoding='utf-8') as json_f:
        orders = json.load(json_f)
        orders['orders'].append(new_order)

    with open('orders.json', 'w', encoding='utf-8') as json_f1:
        json.dump(orders, json_f1, indent=4)


write_order_to_json(input('Введите товар: '),
                    input('Введите количество: '),
                    input('Введите цену: '),
                    input('Введите покупателя: '),
                    input('Введите дату продажи: '))