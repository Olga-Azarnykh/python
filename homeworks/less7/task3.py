"""
3. Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка. В его конструкторе инициализировать
параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических
операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам
и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.
"""


class Cell:
    def __init__(self, cell_count):
        self.__sell_count = cell_count

    @property
    def cell_count(self):
        return self.__sell_count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        new_cell = self.cell_count - other.cell_count
        if new_cell >0:
            return Cell(new_cell)
        raise ValueError('Err')

    def __truediv__(self, other):
        return self.__floordiv__(other)

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __floordiv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def make_order(self, cell_in_lines: int):
        if not isinstance(cell_in_lines, int):
            raise TypeError('Err')
        temp = self.cell_count // cell_in_lines
        temp2 = self.cell_count % cell_in_lines
        result = '\n'.join(['*' * cell_in_lines + '*' * temp2 if idx +1 == temp and temp2
                            else '*' * cell_in_lines
                            for idx in range(temp)])
        return result


if __name__ == '__main__':
    c1 = Cell(13)
    c2 = Cell(2)
    print(c1.make_order(2))


