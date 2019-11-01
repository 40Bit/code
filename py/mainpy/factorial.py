import math

a = 1
y = 1
z = 1
nList = []

global a
global y
global z
global nList

n = input('what is your number? ')
n = int(n)

print('computing factorial...')

for x in range(0, n):
    nList.append(a)
    a += 1

while True:
    if y in nList:
        z *= y
        y += 1

    else:
        print(z)
        break
