"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

usr_inp = input("Введите целое положительное число  \n>>>")

cur = 0
chr_seek = usr_inp[cur]

while cur<len(usr_inp):
    if cur>0 and int(usr_inp[cur])>int(chr_seek):
        chr_seek = usr_inp[cur]
    cur+=1

print(chr_seek)