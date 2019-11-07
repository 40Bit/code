# valentineDaySequence.py by Ayush

import time
import math
n = input('n: ')
n = int(n)
x = 0

while True:
    if n % 2 != 0:
        n *= 3
        n += 1

    else:
        n /= 2

    time.sleep(.03)
    n = int(n)
    print(f'{x}. {n}')
    x += 1

    if n == 1:
        break
