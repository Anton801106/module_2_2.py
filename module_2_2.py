# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = int(10)
second = int(10)
third = int(10)

if first == second == third:
    print(int(3))
elif first == second or first == third or second == third:
    print(int(2))
else:
    print(int(0))