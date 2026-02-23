"""
Напишите программу для печати всех уникальных значений в словаре.
"""

a=dict()

k=int(input("Кол-во элементов в массиве "))
for i in range(k):
    a[input()]=input()

print(a)

key=list()

attribute=list()

for item in a :
    key.append(item)
    attribute.append(a[item])

b=set(attribute)
print(b)