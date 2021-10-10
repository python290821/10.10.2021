# print all primes between 1-100
x = 2
while x < 1000:
    i = 2
    while x % i != 0:
        i += 1
    if i == x:
        print(x, ', ', end = '')
    x += 1
