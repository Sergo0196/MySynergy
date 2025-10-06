val_s = {}
for i in range(10,-6, -1): # например от числа 10, до -5 (включительно)
    val_s[i] = {i ** i}
print(val_s)