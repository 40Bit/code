n = 10 # 10: 1, 2, 5
fList = []
i = 0
y = 0

def get_factors(n):
    for x in range(1, n):
        if n % x == 0:
            fList.append(x)
    return fList

def adp(a, z):
    if a > z:
        return 'deficient'

    if a < z:
        return 'abundant'

    if a == z:
        return 'perfect'

fList = get_factors(n)
x = 0

for x in range(0, len(fList)):
    i += fList[x]

print(i)
print(adp(n, i))
