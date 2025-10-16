class Cassa:
    def __init__(self, cash = 0):
        self.cash = cash

    def top_up(self, X):
        self.cash += X
        print(f'Пополнение счета на {X}')
    
    def count_1000(self):
        print(self.cash // 1000)
    
    def take_away(self, X):
        if X > self.cash:
            print(f'Недостаточно средств для снятия!\nБаланс счета: {self.cash}')
        else:
            self.cash -= X
            print(f'Выдача наличных на сумму: {X}\nТекущий баланс: {self.cash}')

s1 = Cassa()
print(f'Баланс счета: {s1.cash}')
s1.top_up(5000)
print(f'Баланс счета: {s1.cash}')
s1.take_away(500)


        