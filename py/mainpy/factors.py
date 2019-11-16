n = 10 # change for different numbers
fList = [] # get fList to see all factors
i = 0 # i is the value of all the factors combined
y = 0

def get_factors(n, fList): # function for getting factors from number (n)
    for x in range(1, n):
        if n % x == 0:
            fList.append(x)
    return fList

def adp(a, z): # function for ADP
    if a > z:
        return 'deficient'

    if a < z:
        return 'abundant'

    if a == z:
        return 'perfect'

fList = get_factors(n, fList)
x = 0

for x in range(0, len(fList)):
    i += fList[x]

print(i)
print(adp(n, i))
