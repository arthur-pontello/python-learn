import json

try:
    with open('agenda_contatos.json', 'r') as f:
        contatos = json.load(f)
except FileNotFoundError:
    contatos = []

def buscar_contatos():
    nome = input('busca: ')
    return [c for c in contatos if nome.lower() in c['nome'].lower()]

def selecao_itens(lista):
    for i, item in enumerate(lista):
        print(f'{i}) {item['nome']} - {item['telefone']} - {item['email']}')


print('---Funções---')
print('1- adicionar contato')
print('2- buscar contato')
print('3- editar contato existente')
print('4- remover contato')
print('5- listar contatos existentes')
print('6- Salvar')

while True:
    funcao = input('selecione uma funcao: ')
    print()
    match funcao:
        case '1':
            nome = input('nome: ') #possiveis erros
            telefone = input('telefone: ') #formatar
            email = input('e-mail: ')
            contatos.append({'nome': nome, 'telefone': telefone, 'email': email})
            contatos.sort(key=lambda contato: contato['nome'])
            print()

        case '2':
            opcoes = buscar_contatos()
            for contato in opcoes:
                print(f'{contato['nome']} - {contato['telefone']} - {contato['email']}')
            print()

        case '3':
            opcoes = buscar_contatos()
            selecao_itens(opcoes)
            editar = input('Selecione o numero do contato a editar: ')
            try: editar = int(editar) 
            except ValueError: 
                print('Valor inválido') 
                continue
            for i, ctt in enumerate(contatos):
                if ctt is opcoes[editar]:
                    contatos[i]['nome'] = input('novo nome: ')
                    contatos[i]['telefone'] = input('novo telefone: ')
                    contatos[i]['email'] = input('novo email: ')
                    break
            print()

        case '4':
            busca = buscar_contatos()
            selecao_itens(busca)
            remover = input('Selecione o item a remover: ')
            try: remover = int(remover) 
            except ValueError: 
                print('Valor inválido') 
            for i, ctt in enumerate(contatos):
                if ctt is busca[remover]:
                    contatos.pop(i)
                    break
            print()
        
        case '5':
            print('nome - telefone - email')
            for contato in contatos:
                print(f'{contato['nome']} - {contato['telefone']} - {contato['email']}')
            print()
        
        case '6':
                with open('agenda_contatos.json', 'w') as f:
                    json.dump(contatos, f)