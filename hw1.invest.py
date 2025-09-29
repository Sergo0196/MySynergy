a = float(input('Введите сумму Майкла: '))
b = float(input('Введите сумму Ивана: '))
min_invest = float(input('Минимальная сумма инвестиций: '))

if b >= min_invest or a >= min_invest:
    if  b >= min_invest and a >= min_invest:
        print(2)
    elif a >= min_invest:
        print('Mike')
    elif b >= min_invest:
        print('Ivan')
elif a < min_invest and b < min_invest:
    if a + b >= min_invest:
        print(1)
    else:
        print(0)        
elif a >= min_invest:
    print('Mike')
elif b >= min_invest:
    print('Ivan')

