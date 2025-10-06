import pprint
n = int(input())
val_s = {}
for i in range(n):
    val = int(input())
    val_s[val] = {val ** val}
    
print(list(val_s))