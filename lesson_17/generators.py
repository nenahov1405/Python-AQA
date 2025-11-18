# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def pair_sequency_generator(n):
    current = 0
    while current <= n:
        yield current
        current += 2

N = 17

sequence = pair_sequency_generator(N)

print(f"Парні числа в діапазоні від 0 до {N}:")

for number in sequence:
    print(number, end=" ")


#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator(n):
    a, b = 0, 1
    if n < 0:
        return
    if a <= n:
        yield a

    while b <= n:
        yield b
        a, b = b, a + b

N = 100
fib_sequence = fibonacci_generator(N)
print(f'\nПослідовність Фібоначчі до {N}:')
result = list(fib_sequence)
print(result)