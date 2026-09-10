produtos=[
    {'nome': 'mamao', 'preco': 20}
]

novo_produto= [
    {**produto, 'preco': produto['preco'] * 2}
    for produto in produtos
]

print(novo_produto[0]['nome'], novo_produto[0]['preco'], produtos, sep='\n')


iterable = 'Arthur'
iterator = iter(iterable)
for x in iterable:
    print(next(iterator))

print(type(produtos[0]))