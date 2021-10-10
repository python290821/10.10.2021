
_sum = 0
x = int(input('please enter a number'))

digit = 0
while x > 0:
    digit = x % 10
    _sum += digit
    x = x // 10

print('sum of digits', _sum)
