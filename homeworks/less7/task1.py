"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, *data):
        self.data = data


class PrintMatrix(Matrix):
    def __init__(self, *data):
        self.data = data
        pass

    def __str__(self, *data):
        result = ''
        for itm in range(len(self.data)):
            for itx in range(len(self.data[itm])):
                result = result + str(self.data[itm][itx]) + ' '
            result = result + '\n'
        return result


print('Переопределение STR')
prn_matr = PrintMatrix([31, 22], [37, 43], [51, 86])
print(prn_matr)

prn_matr = PrintMatrix([3, 5, 32], [2, 4, 6], [-1, 64, -8])
print(prn_matr)

prn_matr = PrintMatrix([3, 5, 8, 3], [8, 3, 7, 1])
print(prn_matr)


class AddMatrix(Matrix):
    def __init__(self, mx32, mx33, mx42):
        self.mx32 = mx32
        self.mx33 = mx33
        self.mx42 = mx42

    def __add__(self):
        res_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        result = ''
        for itm in range(len(self.mx32)):
            for itx in range(len(self.mx33[itm])):
                res_matrix[itm][itx] = self.mx32[itm][itx] + self.mx33[itm][itx] + self.mx42[itm][itx]
        # itm=0
        # itx=0
        for itm in res_matrix:
            st = 1
            for itx in itm:
                # result = result+ str(res_matrix[itx])+' '
                result = result + str(itx) + ' '
            result = result + '\n'
        return result


print('Переопределение ADD')
add_matr = AddMatrix([[31, 22, 0, 0], [37, 43, 0, 0], [51, 86, 0, 0]],
                     [[3, 5, 32, 0], [2, 4, 6, 0], [-1, 64, -8, 0]],
                     [[3, 5, 8, 3], [8, 3, 7, 1], [0, 0, 0, 0]])
print(add_matr.__add__())
