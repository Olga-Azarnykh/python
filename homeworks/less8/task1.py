"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import datetime

now = datetime.datetime.now()


class SomeError(Exception):
    def __init__(self, txt=''):
        self.txt = txt
        print(self.txt)


class myData:
    def __init__(self, sdata):
        self.sdata = sdata

    @classmethod
    def convert(cls, sdata):
        # return([int(sdata[0:2:1]),int(sdata[3:5:1]),int(sdata[6:len(sdata):1])])
        return int(sdata[0:2:1]), int(sdata[3:5:1]), int(sdata[6:len(sdata):1])

    @staticmethod
    def validation_data(*data):
        for itm in data:
            val = 0
            for itx in itm:
                if (itx < 1 or itx > 31) and val == 0:
                    raise SomeError('Не верно введен день!')
                elif (itx < 1 or itx > 12) and val == 1:
                    raise SomeError('Не верно введен месяц')
                elif itx > now.year and val == 2:
                    raise SomeError('Не верно введен год')
                val = val + 1
                #    break
        # return '123'


usrData = myData('28-07-2019')
strData = usrData.convert('30-12-2021')
# print(usrData.sdata)

print(strData)

try:
    print(myData.validation_data(strData))
except SomeError:
    pass
