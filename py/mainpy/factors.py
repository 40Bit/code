<<<<<<< HEAD
n = 10 # 10: 1, 2, 5
fList = []
i = 0
y = 0

def get_factors(n):
=======
n = 10 # change for different numbers
fList = [] # get fList to see all factors
i = 0 # i is the value of all the factors combined
y = 0

def get_factors(n, fList): # function for getting factors from number (n)
>>>>>>> origin/master
    for x in range(1, n):
        if n % x == 0:
            fList.append(x)
    return fList

<<<<<<< HEAD
def adp(a, z):
=======
def adp(a, z): # function for ADP
>>>>>>> origin/master
    if a > z:
        return 'deficient'

    if a < z:
        return 'abundant'

    if a == z:
        return 'perfect'

<<<<<<< HEAD
fList = get_factors(n)
=======
fList = get_factors(n, fList)
>>>>>>> origin/master
x = 0

for x in range(0, len(fList)):
    i += fList[x]

print(i)
print(adp(n, i))
