a = 0 
b = 0 
while a <= b:
    a = int(input("Введите число а: "))
    b = int(input("Введите число b: "))
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(list(i, end=' '))
    print('\n')

    