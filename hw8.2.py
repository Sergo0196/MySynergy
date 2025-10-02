while True:
    n = int(input('Введите параметр массива: '))
    if n < 1 or n > 100000:
        print('Введено недопустимое значене параметра массива')
        continue
    else: 
        a = list(map(int, input("Введите значения массива: ").split()))
        if len(a) != n:
            print('Введено некорректное количество значений массива')
            continue    
        else:
            a.insert(0, a.pop(-1))
            for i in a:
                if i < 1 or i > 1000000000:
                    a.remove(i)
            print(a)
            break
                 
        
    