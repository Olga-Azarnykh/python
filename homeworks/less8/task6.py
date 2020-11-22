"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
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
            chrvalue = int(chrvalue)
        currtype = type(self.chrvalue)

        if (isinstance(chrvalue, int)) or (isinstance(chrvalue, float)):
            pass
            # stop=1
            # return type(chrvalue)
            return chrvalue
        else:
            raise SomeError('Err!')
            # return False


class Warehouse:
    def __init__(self, name):
        self.adress = name


class Off_equp:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def delivery_good(whouse, goods, brand, value):
        return [whouse], [goods], [brand], [value]


class Printer(Off_equp):
    def __init__(self, brand, value, name):
        super().__init__(name)
        self.brand = brand
        self.color_value = self.color_value
        self.value = value

    @staticmethod
    def delivery(whouse, brand, value):
        print(f'{whouse}  {brand} {value}')


class Scanner(Off_equp):
    def __init__(self, brand, hendle, name):
        super().__init__(name)
        self.name = name
        self.brand = brand
        self.hendle = hendle


class Copy_Equp(Off_equp):
    def __init__(self, brand, automatic_feed, name):
        super().__init__(name)
        self.name = name
        self.brand = brand
        self.automatic_feed = automatic_feed


result = []
whouse = Warehouse('')


def receipt():
    usrсh = False
    while usrсh == False:
        usr_whouse = input('Укажите склад, для окончания ввода введите Quit \n>> ')

        if usr_whouse == 'Quit':
            return 'break'

        usr_goods = input('Укажите товар >> ')
        usr_brand = input('Введите производителя >> ')
        usr_value = input('Введите количество >> ')


        chr = Ver_number(usr_value)

        try:
            cur_chr = chr.verifycation(usr_value)
            # result.append(cur_chr)

        except SomeError:
            continue

        if usr_goods == 'Printer':
            usr_colorval = input('введите кол-во цветов >> ')

        elif usr_goods == 'Scanner':
            usr_hendle = input('это ручной сканер или дикий? >> ')

        elif usr_goods == 'Copy_Equp':
            usr_auto = input('подача авто?')

        usr_delivery = Off_equp.delivery_good(usr_whouse, usr_goods, usr_brand, usr_value)
        print(usr_delivery)
        result.append(usr_delivery)


receipt()
print(result)
