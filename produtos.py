produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos2 = [
    {**produto, 'preco': produto['preco'] * 1.1} 
    for produto in produtos
]

for produto in produtos2:
    print(f'nome: {produto["nome"]}, preco: {produto["preco"]:.2f}')

import copy

produtos_por_preco = copy.deepcopy(produtos2)
produtos_por_preco.sort(key=lambda produtos: produtos['preco'])

for produto in produtos_por_preco:
    print(produto)

produtos_ordenados_por_nome = copy.deepcopy(produtos2)
produtos_ordenados_por_nome.sort(key=lambda produto: produto['nome'], reverse=True)

for produto in produtos_ordenados_por_nome:
    print(produto)

