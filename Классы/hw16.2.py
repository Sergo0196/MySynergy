import math

class Turtle:
    
    def __init__(self, x = 0, y = 0, s = 1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f'Текущее положение черепашки: x = {self.x}, y = {self.y}')

    def go_down(self):
        self.y -= self.s
        print(f'Текущее положение черепашки: x = {self.x}, y = {self.y}')

    def go_left(self):
        self.x += self.s
        print(f'Текущее положение черепашки: x = {self.x}, y = {self.y}')


    def go_right(self):
        self.x -= self.s
        print(f'Текущее положение черепашки: x = {self.x}, y = {self.y}')

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 0:
            print('Число клеток не может ровняться или быть меньше 0!')
        else:
            self.s -= 1
    
    
    def count_moves(self, x2, y2):
        mx = abs(x2 - self.x)
        my = abs(y2 - self.y)

        moves_x = math.ceil(mx / self.s)
        moves_y = math.ceil(my / self.s)
        print(f'Количество ходов для достижения x2 = {x2} и y2 = {y2}: {moves_x + moves_y}')


t1 = Turtle(x=0, y=0, s=1)
t1.go_right()
t1.evolve()
print(f'Новый шаг: {t1.s}')
t1.degrade()
print(f"Новый шаг после деградации: {t1.s}")
t1.count_moves(8, 15)


