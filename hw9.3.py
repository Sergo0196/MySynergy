lst = list(map(int, input('Введитие последовательность чисел: ').split()))
se = set()
for i in lst:
    if i in se:
        print("Yes")
    else:
        print("No")
        se.add(i)