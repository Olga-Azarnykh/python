"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Поехали'

    def stop(self):
        return f'Остановились'

    def turn(self, direction):
        result = ''
        if direction == 'right':
            result = 'Включи правый поворотник, направо едем!'
        elif direction == 'left':
            result = 'Включи левый поворотник, да не тот левый, другой левый! Налево едем!'
        else:
            result = 'Эй, я туда не умею ездить!'
        return result

    def show_speed(self):
        return 'Скорость равна ' + self.speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        # self.is_police = not self.is_police

    def show_speed(self):
        if int(self.speed) > 60:
            return (f'Приедем, сходи на госуслуги, там тебя ждет письмо счастья!')
        else:
            return ''


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        # self.is_police = not self.is_police

    def show_speed(self):
        if int(self.speed) < 200:
            return (f'Я медленнее не умею!')
        else:
            return ''


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        # self.is_police = not self.is_police

    def show_speed(self):
        if int(self.speed) > 40:
            return (f'Приедем, сходи на госуслуги, там тебя ждет письмо счастья!')
        else:
            return ''


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return 'Как хочу, так и еду у меня сирена, и мигалка, и свисток!'


mycar1 = TownCar('80', 'Зеленая', 'Рено', False)

mycar2 = PoliceCar('80', 'Белая', 'Шкода', True)

mycar3 = SportCar('100', 'Желтая', 'Ламборджини', False)

mycar4 = WorkCar('45', 'Синий', 'Автобус', False)

print(mycar1.go())
print(mycar1.stop())
print(mycar1.turn('left'))
print(mycar1.turn('right'))
print(mycar1.show_speed())

print(mycar2.show_speed())
print(mycar3.show_speed())
print(mycar4.show_speed())