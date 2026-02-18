# print("Введите первое число")
# a=int(input())
# print(a)
# b=int(input("Введите второе число "))
# print(b)

# print(a, ' + ', b, ' = ', a+b)


# a=5.8888
# b=5.8999999

# print(round(a*b,2))

# iter=2
# print(iter)
# iter +=3
# print(iter)
# iter -=4
# print(iter)
# iter *=5
# print(iter)
# iter /=5
# print(iter)
# iter //=5
# print(iter)
# iter %=5
# print(iter)
# iter **=5
# print(iter)

# n=423
# summa=0
# while n >0 : 
#     x=n%10
#     summa=summa + x
#     n=n//10
# print(summa)

# i=5
# while i < 5 :
#     if i == 3: 
#         break
#     i+=1
# else : 
#     print("Пожалуй хватит")
# print(i)

# n=int(input())
# i=2
# flag=True
# while flag :
#     if n%i==0:
#         flag=False
#         print(i)
#     elif i>n//2:
#         print(n)
#         flag=False
#     i+=1        


# for i in -1,25,40,90,-5:
#     print(i)


# r=range(5)
# for i in r:
#     print(i)
# r=range(2,5)
# for i in r:
#     print(i)
# r=range(100,0,-20)

# for i in r:
#     print(i)

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line +="*"
    print(line)