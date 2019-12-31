import time

a = 0
b = 1
for x in range(999):
    c=a+b
    time.sleep(.2)
    print(c)
    print('/o')
    print('/^')
    a=b
    b=c
    
