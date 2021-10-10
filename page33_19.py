a = 1
b = 1
n = int(input('enter fibonacci number'))
while True:
    if b > n:
        break
    c = a + b
    a = b
    b = c
print (b)
    
