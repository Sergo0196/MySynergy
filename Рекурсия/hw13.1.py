def recurs(lst, ind):
    if len(lst) == ind:
        return print('Конец списка')
    print(lst[ind])
    recurs(lst, ind + 1)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
recurs(my_list, 0)
