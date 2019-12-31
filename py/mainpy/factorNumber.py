import re

y = 0
i = []

z = input('')
z = re.sub(',', '', z)
z = z.split()

for x in range(0, len(z)):
    z[y] = int(z[y])
    y += 1

y = 1

def get_factors(n):
    fList = []
    
    for x in range(1, n + 1):
        if n % x == 0:
            fList.append(x)
            
    return fList

while i != z:
    i = get_factors(y)
    y += 1

print(y - 1)
