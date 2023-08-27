# 4. Человек загадывает число от 0 до 1000. Программе необходимо угадать число за 10 попыток.
# человек должн подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

num = randint(0, 1000)

low = 0
high = 1000
attempts = 10

print("Загадайте число от 0 до 1000.")

for i in range(1, attempts + 1):
    guess = (low + high) // 2
    print(f"Попытка {i}: Я думаю, что это число {guess}")

    feedback = input("Введите 'больше', 'меньше' или 'верно': ")

    if feedback == "верно":
        print(f"Я угадал число {guess} за {i} попыток.")
    elif feedback == "больше":
        low = guess + 1
    elif feedback == "меньше":
        high = guess - 1
    else:
        print("Пожалуйста, введите 'больше', 'меньше' или 'верно'.")

