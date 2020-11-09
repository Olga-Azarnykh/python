# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


import sys
import datetime as dt


_, earndate = sys.argv
def summwork(hwork,pwork,premwork):
    return int(hwork)*int(pwork)+int(premwork)

dearn = earndate.split(',')

zp = summwork(dearn[0],dearn[1],dearn[2])
print(f'зарплата = {zp}')
