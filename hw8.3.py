
m = float(input("Максимальный перевозимый вес лодки: "))
if m >= 1 and m <= 10000000:
    fisher = int(input("Количество рыбаков: "))
    if fisher < 1 and fisher > 100:
        print('Количество рыбаков не должно превышать 100 человек!')
    else:
        m_fisher_lst = []
        for i in range(1, fisher + 1):
            m_fisher = float(input(f"вес рыбака {i}:  "))
            print(m_fisher)
            m_fisher_lst.append(m_fisher)
        print(m_fisher_lst)
        m_fisher_lst.sort()
        min = 0
        max = fisher - 1
        boats = 0

        while min <= max:
            if m_fisher_lst[min] + m_fisher_lst[max] <= m:
                min += 1
                max -= 1
                boats += 1
            else:
                max += 1
                boats += 1
print(f'Количество лодок: {boats}')
            

# Количество лодок fisher/2