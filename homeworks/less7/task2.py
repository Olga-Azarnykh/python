"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""


class Clothes:
    def __init__(self, typecl, sizecl):
        self.typecl = typecl
        self.sizecl = sizecl


class szClothes(Clothes):
    def __add__(self):
        # def countcl(self):
        if self.typecl == 'coat':
            res = self.sizecl / 6.5 + 0.5
        elif self.typecl == 'costume':
            res = 2 * self.sizecl + 0.3

        return res


typeClothes = 'coat'
sizeClothes = 50
consum = szClothes(typeClothes, sizeClothes)
print(f'расход ткани на пальто: {consum.__add__()}')

typeClothes = 'costume'
sizeClothes = 56
consum = szClothes(typeClothes, sizeClothes)
print(f'расход ткани на костюм: {consum.__add__()}')
