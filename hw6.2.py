x = 0 
cnt = 0
while x <= 2000000000:
    x = int(input('Введите число: '))
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    print(cnt)