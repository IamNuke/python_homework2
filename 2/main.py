
#Т.к. тема была Циклы, то решаем перебором. А так получается квадратное уравнение.
numbers_sum = int(input('Enter summ of numbers :'))
numbers_product = int(input('Enter product of numbers :'))

for x in range(1000):
    if (numbers_sum - x)*x == numbers_product:
        print(f'Numbers: {x}; {numbers_sum - x}')
        break


