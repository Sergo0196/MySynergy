import random

def pr_m(t):
    for i in t:
        print(i)

x = int(input('Число значений в строке: '))
y = int(input('Число строк в матрице: '))

manrix_1 = [[random.randint(1, 10) for i in range(x)] for i in range(y)]
matrix_2 = [[random.randint(1, 10) for i in range(x)] for i in range(y)]
matrix_3 = [[0 for i in range (x)] for i in range(y)]

for i in range(len(manrix_1)):
    for j in range(len(manrix_1)):
        matrix_3[i][j] = manrix_1[i][j] + matrix_2[i][j]
print('Матрица 1:')
pr_m(manrix_1)
print('Матрица 2:')
pr_m(matrix_2)
print('Результат сложения матриц:')
pr_m(matrix_3)
