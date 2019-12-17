def liczbyTrojkatne(n):
    suma = 0
    for i in range(n + 1):
        suma += i
    return suma

def liczbyTrojkatneGenerator():
    suma = 0
    for i in range(10):
        suma += i
        yield suma
    return

assert liczbyTrojkatne(1) == 1
assert liczbyTrojkatne(3) == 6
assert liczbyTrojkatne(4) == 10
gen1 = liczbyTrojkatneGenerator()
for i in range(20):
    print(next(gen1, -1))

#gen2 = liczbyTrojkatneGenerator()
#lista = list(gen2)
#print (lista)
for i in liczbyTrojkatneGenerator():
    print (i)