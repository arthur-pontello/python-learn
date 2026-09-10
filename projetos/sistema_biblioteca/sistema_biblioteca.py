# livros: quantidade total e disponível
# movimentações: histórico
# consulta: buscar livro ou pessoa
# armazenar as pessoas e as informações e os livros
import os
import json
ARQUIVO_JSON = 'dados_biblioteca.json'


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def cadastro_livro(self, titulo, autor, total):
        self.livros.append(Livro(titulo, autor, total))

    def cadastro_usuario(self, nome):
        self.usuarios.append(Usuario(nome))

    def salvar(self):
        livros = []
        usuarios = []
        emprestimos = []
        for livro in self.livros:
            livro = vars(livro)
            livros.append(livro)
        for usuario in self.usuarios:
            usuario = vars(usuario)
            usuarios.append(usuario)
        for emprestimo in self.emprestimos:
            emprestimos.append(vars(emprestimo))
        dados = {'livros': livros, 'usuarios': usuarios, 'emprestimos': emprestimos}
        with open(ARQUIVO_JSON, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

        
        


class Livro:
    def __init__(self, titulo, autor, total):
        self.titulo = titulo
        self.autor = autor
        self.total = total
        self.disponiveis = int(total)


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livro = None

class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = None
        self.data_devolucao = None

    def realizar_emprestimo(self, data):
        self.livro.disponiveis -= 1  #verificar se é valido
        self.data_emprestimo = data
        self.usuario.livro = self.livro

    def realizar_devolucao(self, data):
        self.livro.disponiveis += 1  #verificar se é válido
        self.data_devolucao = data
        self.usuario.livros.remove(self.livro)

def usuario_busca(busca):
    for i, usuario in enumerate(biblioteca.usuarios):
        if busca.lower() in usuario.nome.lower():
            print(f'{i}) {usuario.nome}')

def livro_busca(busca):
    for i, livro in enumerate(biblioteca.livros):
        if busca.lower() in livro.titulo.lower():
            print(f'{i}) {livro.titulo}')
    

try:
    with open(ARQUIVO_JSON, 'r') as arquivo:
        biblioteca_dados = json.load(arquivo)

    biblioteca = Biblioteca()
    for i, livro in enumerate(biblioteca_dados['livros']):
        biblioteca.livros.append(Livro(livro['titulo'], livro['autor'], livro['total']))

    for usuario in biblioteca_dados['usuarios']:
        biblioteca.usuarios.append(Usuario(usuario['nome']))

    for emprestimo in biblioteca_dados['emprestimos']:
        biblioteca.emprestimos.append(Emprestimo(emprestimo['usuario'], emprestimo['livro']))
except FileNotFoundError:
    biblioteca = Biblioteca()


while(True):
    print("-----Funcionalidades-----")
    print('1) Cadastrar Livro')
    print('2) Cadastrar Usuário')
    print('3) Realizar empréstimo')
    print('4) Realizar devolução')
    print('5) Consultar Livro ou Usuário')
    print('6) Histórico emprestimos')
    funcionalidade = input('Funcionalidade: ')

    match funcionalidade:
        case '1':
            titulo = input('Titulo: ')
            autor = input('Autor: ')
            total = input('Número de unidades: ')
            biblioteca.cadastro_livro(titulo, autor, total)

        case '2':
            nome = input('Nome: ')
            biblioteca.cadastro_usuario(nome)

        case '3':
            pesquisa_usuario = input('Buscar usuário: ')
            usuario_busca(pesquisa_usuario)
            selecionar_usuario = input('Digite o indice do usuário desejado: ')
            usuario = biblioteca.usuarios[int(selecionar_usuario)]

            pesquisa_livro = input('Busca livro: ')
            livro_busca(pesquisa_livro)
            selecionar_livro = input('Selecione um livro: ')
            livro = biblioteca.livros[int(selecionar_livro)]

            emprestimo = Emprestimo(usuario, livro)
            biblioteca.emprestimos.append(emprestimo)
            data = input('Data: ')
            emprestimo.realizar_emprestimo(data)
            

        case '4':
            pesquisa_usuario = input('Busca usuário: ')
            usuario_busca(pesquisa_usuario)
            selecionar_usuario = input('Digite o indice do usuário desejado: ')
            usuario = biblioteca.usuarios[int(selecionar_usuario)]

            livro = usuario.livro

            emprestimo_ofc = None
            for emprestimo in biblioteca.emprestimos:
                if emprestimo.usuario == usuario and emprestimo.livro == livro and emprestimo.data_devolucao is None:
                    emprestimo_ofc = emprestimo
                    break
            data = input('Data: ')
            emprestimo_ofc.realizar_devolucao(data)

        case '5':
            busca = input('Quer busca um (L)ivro ou um (U)suário: ')
            busca = busca.lower()
            if busca[0] == 'l':
                pesquisa_livro = input('Pesquisa livro: ')
                livro_busca(pesquisa_livro)
                selecionar_livro = input('Digite o indice do livro desejado:')
                livro = biblioteca.livros[int(selecionar_livro)]
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, Total Cópias: {livro.total}, Cópias Disponíveis: {livro.disponiveis}')

            elif busca[0] == 'u':
                pesquisa_usuario = input('Pesquisa usuário: ')
                usuario_busca(pesquisa_usuario)
                selecionar_usuario = input('Digite o índice do usuário desejado: ')
                usuario = biblioteca.usuarios[int(selecionar_usuario)]
                print(f'Nome: {usuario.nome}')
                print(f'Livros:')
                for livro in usuario.livros:
                    print(f'{livro.titulo}, {livro.autor}')

        case '6':
            for emprestimo in biblioteca.emprestimos:
                print(f'Livro {emprestimo.livro.titulo} para usuario {emprestimo.usuario.nome}')

    biblioteca.salvar()