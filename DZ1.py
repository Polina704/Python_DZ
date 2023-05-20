# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# Решение:

n = str(input('Введите трехзначное число: '))
if len(n) != 3:
    print(f'Число {n} не 3-х значное')
else :
    n = int(n)
    summa = 0
    while n > 0:
        x = n % 10
        summa = summa + x
        n = n // 10
        
    print(summa)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
# Петя - x, # Сережа - y, # Катя - Z. # x = y. # z = (x+y)*2 = 4*x. # 4*x + x + x = s. # 6*x = s. # x = s/6

# Решение:

# s = int(input('Введите сколько журавликов сделали вместе ребята: '))
# print('Петя сделал - ', int(s/6), ' , Катя сделала - ', int(4*s/6), ', Сережа сделал - ', int(s/6))

# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# Решение:

# n = str(input('Введите шестизначное число: '))
# if len(n) != 6:
#     print(f'Число {n} не 6-ти значное')
# else :
#     if (int(n[0]) + int(n[1]) + int(n[2])) == (int(n[3]) + int(n[4]) + int(n[5])) :
#         print('yes')
#     else :
#         print('no')



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

# Решение:

# n = int(input('Введите размер шоколадки n: '))
# m = int(input('Введите размер шоколадки m: '))
# k = int(input('Введите кол-во долек, к-рые хотите отломить: '))
# if k < m*n and (k%m==0 or k%n==0):
#     print('yes')
# else:
#     print('no')