"""
Известно кол-во учащихся в кажом классе (всего их 3).
Минимальное кол-во парт которые нужны
"""
first_class=int(input("Введите кол-во учащихся в первом классе"))
second_class=int(input("Введите кол-во учащихся в втором классе "))
third_class=int(input("Введите кол-во учащихся в третьем классе"))

desks_a = (first_class + 1) // 2
desks_b = (second_class + 1) // 2
desks_c = (third_class + 1) // 2

print(desks_a+desks_b+desks_c)