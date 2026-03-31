a = int(input('scrivi numero iniziale '))
b = int(input('scrivi numero finale '))
lista_numeri = []
for i in range(a, b):
    if i % 2 == 0:
        lista_numeri.append(i)
print(lista_numeri)