class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def adicionar_produto(self,  *produtos):
        for produto in produtos:
            self._produtos.append(produto)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('bola', 20), Produto('Caderno', 10)
carrinho.adicionar_produto(p1, p2)
carrinho.listar_produtos()

print(p1.__dict__)
