# listar
# desfazer 
# refazer
import os
import json
with open('lista_tarefas.json', 'r') as arquivo:
    lista = json.load(arquivo)

print('Comandos: listar, desfazer, refazer')

cache = None

while True:
    tarefa_comando = input('Digite uma tarefa ou comando: ')
    if tarefa_comando == 'listar':
        for item in lista:
            print(item)
        with open('lista_tarefas.json', 'w') as arquivo:
            json.dump(lista, arquivo)
        print()
    
    elif tarefa_comando == 'desfazer':
        try:    
            cache = lista[-1]
            lista.pop()
        except IndexError: print('Ação Inválida')
        for item in lista:
            print(item)
        print()


    elif tarefa_comando == 'refazer':
        if cache is None:
            print('Ação Inválida')
            continue
        lista.append(cache)
        for item in lista:
            print(item)
        cache = None
        print()
    
    elif tarefa_comando == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Comandos: listar, desfazer, refazer')

    else:
        lista.append(tarefa_comando)
        for item in lista:
            print(item)
        print()
