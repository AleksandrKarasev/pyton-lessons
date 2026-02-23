# Списки
# Как создать список

# list_1=[]
# list_1=list()
# list_1=[1,2,3,8]
# print(list_1)
# print(*list_1)# вывод без скобок и запятых

# Работа через списки
# for i in list_1:
#     print(i)

# Размер списка
# print(len(list_1))

# Вывод конкертного элемента
# print(list_1[0])

# Добавление в конец списка
# list_1=[1,5]
# print(list_1)
# list_1.append(8)
# print(list_1)

# Добавление в пустой список значения
# list_1=[]
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# Удаление последнего элемента в списке 
# list_1=[1,2,3,4,5,6,7,8,9,10]
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())

# Удаление конкретного элемента
# list_1=[1,2,3,4,5]
# print(list_1.pop(0))
# print(list_1)

# Добавление на элемента на нужную позицию
# list_1=[1,2,3,4,5]
# print(list_1.insert(0,0))
# print(list_1)

# Срезы списка
# list_1=[1,2,3,4,5,6,7,8,9,10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # 1,2,3,4,5,6,7,8,9,10
# print(list_1[:2]) # 1,2 
# print(list_1[len(list_1)-2:]) # 9,10
# print(list_1[2:9])
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6])
# print(list_1[::6])

# Кортежа
## Создание кортежа
# t=()
# print(type(t))
# print(t)

# t=(1,2,3)
# print(type(t))
# print(t)

# Преобразование списка в кортеж

# v=[1,2,3]
# print(v)
# print(type(v))
# v=tuple(v)
# print(v)
# print(type(v))

# a,b,c=v
# print(a,b,c)

# Словари
## Создание пустого словаря
# d={}
# d=dict()
## Заполнение словаря
# d['q']='qwerty'
# print(d)

# d['w']='werty'

## Вывод значения ключа
# print(d['q'])

# Пример

# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)
# dictionary['left']='<='
# print(dictionary)
# # Удаление элемента
# del dictionary['left']
# print(dictionary)
# # Работа с циклом
# for item in dictionary:
#     print('{} : {}'.format(item, dictionary[item]))

# # Второй способ
# for (k,v) in dictionary.items():
#     print(k,v)

# Множество 
# colors={'red', 'green', 'blue'}
# print(colors)
# Добавление элемента в множество
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# # Удаление
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# Операции над множествами

# a={1,2,3,5,8}
# b={2,5,8,13,21}
# c=a.copy()
# print(c)
# u=a.union(b)
# print(u)
# i=a.intersection(b)
# print(i)
# d1=a.difference(b)
# print(d1)
# dr=b.difference(a)
# print(dr)
# q=a.union(b).difference(a.intersection(b))
# print(q)

# Замороженное множество
# a={1,2,3}
# b=frozenset(a)
# print(b)

# Генератор списков
list_1=[i for i in range(1,101)]
print(list_1)
list_2= [i  for i in range (1,101) if i%2==0 ]
print(list_2)