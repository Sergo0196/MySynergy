n = int(input("Введите значение количества строк: "))
lst = []
for i in range(1, n + 1):
    a = int(input(f'Введите значение строки {i}: '))
    if a <= 10000 and a >= 1:
        lst.append(a)
# lst.reverse()
# print(lst)
print(list(reversed(lst))) #Проба разных способов