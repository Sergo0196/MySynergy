while True:
    n = int(input("Параметр множества: "))
    if n >= 1 and n <= 100000:
        for i in range(n):
            a = set(map(int, input().split()))
            print(len(a))
        break
    else:
        print('Параметр указан некорректно')
        continue