# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2

num_monet = int (input ("введите кол-во монет: "))
if 1 <= num_monet <= 100:
    current_mon = 0
    orel = 0
    reshka = 0
    while current_mon < num_monet:
        t = int(input("введите положение монеты 0: если орел или 1: если решка: "))
        current_mon +=1
        if t >= 1:
            orel += 1
        else:
            reshka += 1
if orel > reshka:
    print ("нужно перевернуть решки")
else:
    print ("нужно перевернуть орлы")




