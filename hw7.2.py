tmp = input('Введите строку: ')
if len(tmp) <= 1000:
    print(" ".join(tmp.split()))
else:
    print('Количество символов не должно превышать 1000')