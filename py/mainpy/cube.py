import random

colors = []
sideOne = ''

for x in range(1, 10):
    colors.append("r{0}".format(x))
    colors.append("o{0}".format(x))
    colors.append("y{0}".format(x))
    colors.append("g{0}".format(x))
    colors.append("b{0}".format(x))
    colors.append("w{0}".format(x))

for x in range(0, 3):
    i = random.choice(colors)
    colors.remove(i)

    j = random.choice(colors)
    colors.remove(j)

    k = random.choice(colors)
    colors.remove(k)

    i = i[:-1]
    j = j[:-1]
    k = k[:-1]

    sideOne += '{0} {1} {2} \n'.format(i, j, k)

print(sideOne)
