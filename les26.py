# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень 
# B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def degree(a, b):
    if b == 0:
        return 1
    return a * degree(a, b-1)

a = int(input("Введите число: "))
b = int(input("Введите степень числа(целое неотрицательно число): "))

print('A=',a,';B=',b,'->', degree(a, b))

# p(5, 3) -> 25 * 5 = 125
#            |  
#            5 * 5
#            |
#            1 * 5
#            |
#            1