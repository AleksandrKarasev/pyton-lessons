# Нужно создать функцию которая просуммирует все числа 
# от 1 до n

# def sumNumbers(n):
#     summa=0
#     for i in range(1,n+1):
#         summa+=i
    
#     print(summa)

# sumNumbers(5)

# С возратом значения

# def sumNumbers(n):
#     summa=0
#     for i in range(1,n+1):
#         summa+=i
#     return summa

# a=sumNumbers(5)
# print(a)

# Функция с неограниченном кол-во элементов

# def sum_str(*args):
#     res=''
#     for i in args:
#         res+=str(i)
#     return res

# print(sum_str('q','w','e','r','t','y'))
# print(sum_str(1,2,3,4,5))

# import modul

# print(modul.max1(5,9))

# Пользователь вводит число n

# Необходимо вывести n первых членов последовательности фибоначи

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else :
#         return fib(n-1) + fib(n-2)
    
# list_1=list()
# for i in range (1,10):
#     list_1.append(fib(i))

# print(list_1)

# Быстрая сортировка
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3]))

# Сортировка слиянием

def mergesort(nums):
    if len(nums)>1:
        mid=len(nums)//2
        left=nums[mid:]
        right=nums[:mid]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i+=1
            else :
                nums[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1
        
list_1=[1,5,6,9,8,7,2,1,55,2,4]
mergesort(list_1)
print(list_1)
