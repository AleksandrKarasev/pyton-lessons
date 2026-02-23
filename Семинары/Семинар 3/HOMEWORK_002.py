"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент 
к заданному числу Х. Пользователь в первой строке вводит натуральное число 
N - количество элементов в массиве. В последующих строках записаны N целых чисел А. 
Последняя строка содержит число Х
"""

# Ввод данных
N = int(input("Введите количество элементов: "))
arr = []
for i in range(N):
    arr.append(int(input("Введите элемент: ")))

X = int(input("Введите число X: "))

# Поиск ближайшего элемента
best_element = arr[0]
min_diff = abs(arr[0] - X)

for i in range(1, N):
    current_diff = abs(arr[i] - X)
    if current_diff < min_diff:
        min_diff = current_diff
        best_element = arr[i]

# Вывод результата
print("Самый близкий элемент:", best_element)