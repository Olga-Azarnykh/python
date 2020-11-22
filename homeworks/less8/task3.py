"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class SomeError(Exception):
    def __init__(self, txt=''):
        self.txt = txt
        print(self.txt)


class Ver_number:
    def __init__(self, chrvalue):
        self.chrvalue = chrvalue

    def verifycation(self, chrvalue):
        if chrvalue.isdigit():
            chrvalue = float(chrvalue)
        if (isinstance(chrvalue, int)) or (isinstance(chrvalue, float)):
            pass
            return chrvalue
        else:
            raise SomeError('Err!')


result = []
usrсh = False

while usrсh == False:
    usr_inp = input('Введите число, для окончания ввода введите Quit \n>>')

    chr = Ver_number(usr_inp)
    if usr_inp == 'Quit':
        break
    try:
        cur_chr = chr.verifycation(usr_inp)
        result.append(cur_chr)

    except SomeError:
        pass

print(result)
