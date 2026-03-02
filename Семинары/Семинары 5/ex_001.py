"""
Последовательностью Фибоначчи
последовательность чисел а
1'.••, a
n' ..., ГДе
a =0, a, = 1, a, = ak1 + 2k2 (k> 1).
Требуется найти N-e число Фибоначчи
"""

def find_fib_index(x):
    if x < 0:
        return None  # или ошибка
    if x == 0:
        return 1
    if x == 1:
        return 2
    a, b = 0, 1
    index = 2  # текущий индекс для b (a1=0, a2=1)
    while b < x:
        a, b = b, a + b
        index += 1
        if b == x:
            return index
    # если вышли из цикла, значит b > x, и число не найдено
    return None  # или можно выбросить исключение

x = int(input("Введите число Фибоначчи: "))
res = find_fib_index(x)
if res is None:
    print("Введённое число не является членом последовательности Фибоначчи (с a1=0, a2=1)")
else:
    print(f"Номер этого члена: {res}")

