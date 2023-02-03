import math
n = int(input("Enter number:"))
i = 0
result = int(math.pow(2, i))
while result <= n:
    print(f'{result} ', end='')
    i += 1
    result = int(math.pow(2, i))
