x = int(input('please enter a number'))
while x >= 0:
    # sum then digits and print
    digit = 0
    _sum = 0
    while x > 0:
        digit = x % 10
        _sum += digit
        x = x // 10
    print('sum of digits', _sum)
    x = int(input('please enter a number'))
