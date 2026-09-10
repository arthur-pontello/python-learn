def zipper(lista1, lista2):
    valor = min(lista1, lista2)
    return [
        (lista1[i], lista2[i]) for i in range(valor)
    ]


a = [1,2,3,4]
b=[5,6,7,8]

print(zipper(a,b))