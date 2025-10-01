n = int(input())
cnt = 0
for i in range(n):
    num = int(input(f'Введите число {i + 1}: '))
    if num == 0:
        cnt += 1
print (f'Чисел равных нулю: {cnt}')
