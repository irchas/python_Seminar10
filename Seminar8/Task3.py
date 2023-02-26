"""
3) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
new_Text3 = []
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('Seminar8/Text3.txt', 'r') as my_f:
    nums = my_f.read().split('\n')
    print(nums)
    for i in nums:
        i = i.split(' ', 1)
        new_Text3.append(rus[i[0]] + i[1])
    print(new_Text3)

with open('Seminar8/new_Text3.txt', 'w') as my_f2:
    my_f2.writelines(f'{new_Text3}\n')


