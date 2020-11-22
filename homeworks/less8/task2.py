"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class SomeError(Exception):
    def __init__(self, txt=''):
        self.txt = txt
        print(self.txt)


class Div_zero:
    def __init__(self, divident, devider):
        self.divident = divident
        self.devider = devider

    def except_work(self, divident, devider):
        if divident == 0 or devider == 0:
            raise SomeError('Ошибка деления на букву "O"!')
        else:
            return divident / devider
            # return CodeError


div = 1
dev = 1
usrdivdev = Div_zero(div, dev)
try:
    result = usrdivdev.except_work(div, dev)
except SomeError:
    # print('err')
    pass
