
numBase = []
binaryNumber = []
# binaryNumber is where the conversion is stored

s = 1

for x in range(0, 10):
# change number from 10 if n is quite high
    numBase.append(s)
    s *= 2

n = 42
# number to be converted is n

z = len(numBase) - 1

def binary(a):
    global numBase, n
    
    if n >= numBase[a]:
        x = n % numBase[a]
        n -= x
        binaryNumber.append(str(int(n / numBase[a])))
        n = x

    else:
        binaryNumber.append('0')

for x in range(0, len(numBase)):
    binary(z)
    z -= 1

binaryNumber = ''.join(binaryNumber)
print(binaryNumber)
