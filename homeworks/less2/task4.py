# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

usr_inp = input("Введите любую строку из нескольких слов, разделённых пробелами\n>>>")

num_str = 1
i = 0
usr_cond = False
while not usr_cond:
    try:
        pos_space = usr_inp.index(" ", i)
        if pos_space - i <= 10:
            print(usr_inp[i:pos_space])
        else:
            print(usr_inp[i:i + 10])
        num_str = num_str + 1
        if pos_space > i:
            i = pos_space

        i = i + 1
    except ValueError:
        if len(usr_inp) - i <= 10:
            print(usr_inp[i:])
        else:
            print(usr_inp[i:i + 10])
        break