# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

num = 10 
fib_gen = fibonacci_generator()
fibonacci_sequence = [next(fib_gen) for _ in range(num)]
print(fibonacci_sequence)