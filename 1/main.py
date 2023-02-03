

from random import randint

n = int(input('Enter number of coins :'))
tails = 0
emblems = 0
for _ in range(n):
    curr = randint(0, 1)
    print(f'{curr} ', end='')
    if curr == 0 :
        tails +=1
    else:
        emblems += 1
print()
print(f'Number of coins to turn: {tails if tails < emblems else emblems}')

