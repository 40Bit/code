n = 0

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
y = 5

base = [a, b, c, d, e, f]
numBase = [1, 2, 4, 8, 16, 32]
binaryNumber = []

def binary(z):
    global n, a, b, c, d, e, f, base, numBase
    
    if n >= numBase[z]:
        x = n % numBase[z]
        n -= x
        base[z] = n / numBase[z]
        n = x
        base[z] = int(base[z])
        base[z] = str(base[z])
        binaryNumber.append(base[z])

    else:
        base[z] = 0
        base[z] = str(base[z])
        binaryNumber.append(base[z])

for x in range(0, len(base)):
    binary(y)
    y -= 1

binaryNumber = ''.join(binaryNumber)
print(binaryNumber)
