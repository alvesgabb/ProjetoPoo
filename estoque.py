# estoque.py
from arquivo import salvar_produtos, carregar_produtos

class Estoque:
    def __init__(self):
        self.produtos = carregar_produtos()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        salvar_produtos(self.produtos)

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        for p in self.produtos:
            print(p)

    def remover_produto(self, nome_produto):
        self.produtos = [p for p in self.produtos if p.nome != nome_produto]
        salvar_produtos(self.produtos)

    def adicionar_quantidade(self, nome_produto, quantidade):
        for p in self.produtos:
            if p.nome == nome_produto:
                p.adicionar_estoque(quantidade)
                salvar_produtos(self.produtos)
                return
        print("Produto não encontrado.")

    def remover_quantidade(self, nome_produto, quantidade):
        for p in self.produtos:
            if p.nome == nome_produto:
                p.remover_estoque(quantidade)
                salvar_produtos(self.produtos)
                return
        print("Produto não encontrado.")