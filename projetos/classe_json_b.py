import json
from classe_json_a import Pessoa, CAMINHO_ARQUIVO

with open(CAMINHO_ARQUIVO, 'r') as dados:
    pessoas = json.load(dados)

# print(pessoas)