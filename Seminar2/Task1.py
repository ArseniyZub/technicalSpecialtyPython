# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


def number_hex(number: int):
    result = ''
    DIV_HEX = 16
    hex_letters = list('0123456789abcdef')

    while number > 0:
        result = hex_letters[number % DIV_HEX] + result
        number //= DIV_HEX
    return result

number = int(input('Введите число: '))
print('Встренная функция: ' + hex(number)[-2::])
print('Собственная функция: ' + number_hex(number))

