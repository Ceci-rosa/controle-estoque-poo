class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_produtos(self):
        print(f'Nome: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}')
