import json
CAMINHO_ARQUIVO = 'classe_json.json'
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('arthur', 18)
p2 = Pessoa('maria', 30)
p3 = Pessoa('clovis', 62)
dados = [vars(p1), vars(p2), vars(p3)]
# print(dados)

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(dados, arquivo)
