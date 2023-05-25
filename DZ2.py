# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# если вверх решкой, то 1
# если вверх гербом, то 0

# Решение:
# n = int(input("Введите число монеток:"))
# countR = 0

# for i in range(n) :
#     status = int(input("Введите положение монет - если вверх решкой, то 1, если вверх гербом, то 0: "))
#     if status == 1 :
#         countR += 1
#     elif status > 1 :
#         print("Ошибка! В положении монеток может быть только 0 или 1")
#         break

# if countR >= n/2 :  
#     print(n - countR) 
# else :
#     print(countR)    


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# X + Y = S; X*Y = P;
# X = S-Y; Y = P/X ; X = S - P/X; X + P/X = S; x^2 + P = Sx

# Решение:
# S = int(input("Введите сумму чисел:"))
# P = int(input("Введите произведение чисел:"))
# y = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
# x = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
# print(x, y)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Решение:
# N = int(input("Input N:"))
# k = 0
# if N<=0 :
#     print("Число N должно быть больше 0")
# else :
#     while 2**k <= N :
#         print(2**k)
#         k += 1
    
