def soma(*args):
    return sum(args)

print(soma(1,2,3,4))

lista = [
    {'p': 'mamao', 'preco': 20},
    {'p': 'banana', 'preco': 50}
]

lista2 = list(map(
    lambda p: p['preco'] * 3,
    lista
))

lista3 = list(filter(
    lambda p: p['preco'] > 20,
    lista
))
print(lista2)
print(lista3)