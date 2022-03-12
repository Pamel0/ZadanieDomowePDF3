from random import randint

lista = []

for i in range(10):
    a = randint(1, 1000)
    lista.append(a)
print(lista)

lista2 = []
for i in lista:
    if i % 2 == 0:
        lista2.append(i)
print(lista2)


