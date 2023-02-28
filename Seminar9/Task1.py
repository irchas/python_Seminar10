""" Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18 """

import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string = ''
        for i in range(len(self.matrix)):
            string = string + ' '.join(map(str, self.matrix[i])) + '\n'
        return string

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        result = copy.deepcopy(self.matrix)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = Matrix(matrix1)
m2 = Matrix(matrix2)
res = m1 + m2
print(f'Первая матрица: \n{m1}')
print(f'Вторая матрица: \n{m2}')
print(f'Сумма матриц: \n{res}')
