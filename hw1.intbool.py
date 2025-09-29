value = int(input())

if value < 0 and value % 2 == 0:
    print('Четное отрицательное число')
elif value == 0:
    print('Число равное нулю')
elif value > 0 and value % 2 != 0:
    print("Число положительное и не является четным")