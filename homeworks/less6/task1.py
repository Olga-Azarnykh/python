"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    __color = ['RED', 'YELLOW', 'GREEN']

    def running(self, pozition):
        print(self.__color[pozition])


class Traff(TrafficLight):

    def engine(self):
        i = 0
        stop = False

        super().running(0)
        time.sleep(7)
        super().running(1)
        time.sleep(2)
        super().running(2)
        time.sleep(10)


starttime = time.time()
traff = Traff()
traff.engine()
