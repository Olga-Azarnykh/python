"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    # _income = {}
    __income = {}

    def __init__(self, name, surname, position, dictwage):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = dictwage


class Position(Worker):
    def __init__(self, name, surname, position, dictwage):
        super().__init__(name, surname, position, dictwage)
        self.dictwage = dictwage

    def get_full_name(self):
        result = self.name + ' ' + self.surname
        return result

    def get_total_income(self):
        result = self.dictwage['wage'] + self.dictwage['bonus']
        return result


"""
wk = Worker('Name1','Surname1','pos1',{'wage':'100','bonus':'10'})
wk.print_vd()
"""
employe = Position('Иван', 'Петров', 'оператор лопаты', {'wage': 10000, 'bonus': 4500})
print(f'Полное имя сотрудника: {employe.get_full_name()} его заработок {employe.get_total_income()}')

# print(wk._Worker__income)
