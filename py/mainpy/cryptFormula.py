crypt='Z = A = B + B + B + B'

# translating crypt
lCrypt=crypt.split(' + ')
lCrypt=''.join(lCrypt)
lCrypt=lCrypt.split(' = ')

# the formula
z=len(lCrypt[0])
x=len(lCrypt[2])

y=z*x

q=int(y/x)
w=int(y/z)

qr='%s'%q
wr='%s'%w

for x in range(1, w):
    qr='{0} + {1}'.format(qr, q)

for x in range(1, q):
    wr='{0} + {1}'.format(wr, w)

print('{0} = {1} = {2}'.format(wr, y, qr))
