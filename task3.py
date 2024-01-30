'''
Создайте функцию генератор чисел Фибоначчи
'''


def gen_fib(counter: int) -> iter.__class__:
    yield 0
    yield 1
    first = 0
    second = 1
    for _ in range(counter - 2):
        first, second = second, first + second
        yield second


print(*gen_fib(10))
