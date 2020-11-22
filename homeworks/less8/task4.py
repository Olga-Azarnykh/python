"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    def __init__(self, name):
        self.adress = name


class Off_equp:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def delivery_good(whouse, goods, brand, value):
        # print(f'{whouse}  {goods} {brand} {value}')
        return [whouse], [goods], [brand], [value]


class Printer(Off_equp):
    def __init__(self, brand, value, name):
        super().__init__(name)
        self.brand = brand
      #  self.color_value = color_value
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
