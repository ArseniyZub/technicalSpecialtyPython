# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import fractions
import math


def get_franction(value1: str, value2: str) -> str: 
    num1, denom1 = map(int, value1.split("/"))
    num2, denom2 = map(int, value2.split("/"))

    sum_num = num1*denom2 + num2*denom1 
    sum_denom = denom1*denom2
    sum = sum_num, sum_denom
    reduce_fraction(sum[0], sum[1])

    prod_num = num1*num2
    prod_denom = denom1*denom2
    prod = prod_num, prod_denom
    reduce_fraction(prod[0], prod[1])

    return sum, prod


def reduce_fraction(n,m):
    k = math.gcd(n,m)
    return (n//k, m//k)

value1 = input('Введите первую дробь: ')
value2 = input('Введите первую дробь: ')
print('\n')

sum, prod = get_franction(value1, value2)

if sum[0] != sum[1]:
    if sum[0]%sum[1] != 0:
        print(f'Сумма дробей собственной функции: {sum[0]}/{sum[1]}')
    else:
        print(f'Сумма дробей собственной функции: {sum[0]//sum[1]}')
else:
    print(f'Сумма дробей собственной функции: 1')   


if prod[0] != prod[1]:
    if prod[0]%prod[1] != 0:
        print(f'Произведение дробей собственной функции: {prod[0]}/{prod[1]}')
    else:
        print(f'Произведение дробей собственной функции: {prod[0]//prod[1]}')
else:
    print(f'Произведение дробей собственной функции: 1')

print('\n')

frac1 = fractions.Fraction(sum[0], sum[1])
frac2 = fractions.Fraction(prod[0], prod[1])

print(f'Сумма дробей встроенной функции: {frac1}')
print(f'Произведение дробей встроенной функции: {frac2}')
