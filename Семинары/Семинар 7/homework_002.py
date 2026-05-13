"""
Задача 36: Напишите функцию print_operation_table(operation, 
num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк 
и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у
 которой ровно два аргумента, как, например, у операции умножения.
"""

def print_operation_table(operation, num_rows=6, num_columns=6):
    """
    Печатает таблицу из num_rows строк и num_columns столбцов,
    где элемент на позиции (i, j) вычисляется как operation(i, j).
    Нумерация строк и столбцов начинается с 1.
    """
    # Собираем все элементы таблицы, чтобы определить нужную ширину столбца
    table = []
    for row in range(1, num_rows + 1):
        row_values = []
        for col in range(1, num_columns + 1):
            row_values.append(operation(row, col))
        table.append(row_values)

    # Максимальная длина строкового представления элемента
    max_width = max(len(str(val)) for row in table for val in row) if table else 0

    # Печать таблицы с выравниванием по правому краю
    for row in table:
        for val in row:
            print(f"{val:>{max_width}}", end=" ")
        print()  # переход на новую строку

# Пример использования:
print_operation_table(lambda x, y: x + y)