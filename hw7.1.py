tmp = input("Введите слово: ")
if tmp[::] == tmp[-1::-1]:
    print('yes')
else:
    print('no')