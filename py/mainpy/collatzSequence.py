import time
import math
    
def collatz():
    x = 2
    n = input('n: ')
    n = int(n)
    nList = []

    nList.append('1. {0}'.format(n))

    if n != 1:
        while True:
            if n % 2 != 0:
                n *= 3
                n += 1
    
            else:
                n /= 2
    
            time.sleep(.003)
            n = int(n)
            nList.append('{0}. {1}'.format(x, n))
    
            x += 1
    
            if n == 1 or n == -1:
                nList = '\n'.join(nList)
                return nList
                break
                return nList

        if n == 1:
            return nList

for x in range(0, 3):
    print(collatz(), '\n')
