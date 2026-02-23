"""
Дан массив, состоящий из целых чисел. 
Напишите программу, которая подсчитает количество элементов массива, 
больших предыдущего (элемента с предыдущим номером)
"""

list_1=list()

k=int(input("Сколько элементов "))

for i in range(k):
    list_1.append(int(input()))

print(list_1)
count=0
for i in range(1, len(list_1)):
    if list_1[i] > list_1[i-1]:
        count += 1

print(count)