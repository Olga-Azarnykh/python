"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = 'num_1 + num_2 * j'

    def __add__(self, other):
        return f'Сумма комплексных чисел >> {self.num_1 + other.num_1} + {self.num_2 + other.num_2} * j'

    def __mul__(self, other):
        return f'Произведение комплексных чисел >> {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + {self.num_2 * other.num_1} * j'

    def __str__(self):
        return f'complex_1 >> {self.num_1} + {self.num_2} * j'


complex_1 = ComplexNumber(7, 9)
complex_2 = ComplexNumber(-5, 3)
print(complex_1)
print(complex_1 + complex_2)
print(complex_1 * complex_2)