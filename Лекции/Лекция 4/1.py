# def math(op, x,y ):
#     print(op(x,y))


# calc2=lambda a,b : a+b

# math(calc2, 4,5)

"""
В списке хранится числа. Нужно выбрать только четные числа и составить список пар
"""

# data = [1, 2, 3,5,8,15, 23,38]
# res = list()
# for i in data:
#     if i%2==0:
#         res.append((i,i**2))
# print(res)

# def select(f,col):
#     return [f(x) for x in col]

# def where (f,col):
#     return[x for x in col if f(x)]

# data = [1, 2, 3,5,8,15, 23,38]

# res=select(int, data)

# res=where(lambda x : x%2==0,res)
# print(res)
# res=list(select(lambda x : (x,x**2), res))
# print(res)

# list_1=[x for x in range(1,28)]
# print(list_1)
# list_1=list(map(lambda x : x+10, list_1))
# print(list_1)

# Задача: С клавиатуры вводится некий набор чисел, 
# в качестве разделителя
# используется пробел. Этот набор чисел будет 
# считан в качестве строки.
# Как превратить list строк в list чисел?

# data='15 156 96 3 5 8 52 5'


# data=list(map(int, data.split()))

# print(data)

# res=map(int,data)

# res=filter(lambda x:x%2 ==0, res)

# res=list(map(lambda x : (x, x**2), res))

# print(res)


# Функция zip

# Пример

# users=['user1', 'user2', 'user3','user4', 'user5']
# ids=[4,5,9,14,7]
# data=list(zip(users, ids))
# print(data)


# Функция zip проходится по минимальному набору данных

# users=['user1', 'user2', 'user3', 'user4', 'user5']
# ids=[4,5,9,14,7]
# salary=[111,222,333]
# data=list(zip(users,ids,salary))
# print(data)

# Функция enumerate 

# Пример 

# users=['user1', 'user2', 'user3']
# data=list(enumerate(users))
# print(data)

# Работа с файлами
## Режим а
# colors=['red', 'green', 'blue']

# data=open('file.txt', 'a', encoding='utf-8')

# data.writelines(colors) # Разделителей не будет

# data.close()

## Режим w

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

## Режим r

# path='file.txt'
# data=open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# Модуль OS
## Смена текущей директории

# import os 

# os.chdir("/Users/aleksandrkarasev/Desktop/GeekBrains(DS)/python знакомство с языком/Лекции/Лекция 4")

## Вывод текущей директории

# import os

# print(os.getcwd())

## модуль os.path

### os.path.basename - базовое имя пути 

# import os

# print(os.path.basename("/Users/aleksandrkarasev/Desktop/GeekBrains(DS)/python знакомство с языком/Лекции/Лекция 4/1.py"))

### os.path.abspath() - возвращает абсолютный путь 

import os

print(os.path.abspath('1.py'))