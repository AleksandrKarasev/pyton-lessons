"""
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимале. Напишете программу,
заменяет оценки Василия, но наоборот: максимальные - на минимальные.
"""

n=int(input())

list_1=list()
for i in range(n):
    list_1.append(int(input()))

max_n=max(list_1)
min_n=min(list_1)

for i in range(len(list_1)):
    if list_1[i]==max_n:
        list_1[i]=min_n

print(list_1)
