""" Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

my_list = ['разработка', 'администрирование', 'protocol', 'standard']

for el in my_list:
    el_BYTES = el.encode('utf-8')
    print(el_BYTES)
    el_STR = el_BYTES.decode('utf-8')
    print(el_STR)
    