def fact(a):
    ls = []
    if a == 1:
        return print('!1 = 1')
    else:
        result = 1
        for i in range(1, a + 1):
            result *= i
            ls.append(result)
            sorted_ls = sorted(ls, reverse=True)
        return print(sorted_ls)
fact(1)