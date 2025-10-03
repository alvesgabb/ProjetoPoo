# produto.py
class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor >= 0:
            self.__quantidade = valor

    def adicionar_estoque(self, quantidade):
        if isinstance(quantidade, (int, float)) and quantidade >= 0:
            self.__quantidade += quantidade

    def remover_estoque(self, quantidade):
        if isinstance(quantidade, (int, float)) and 0 <= quantidade <= self.__quantidade:
            self.__quantidade -= quantidade

    def __str__(self):
        return f"Produto: {self.__nome} | Preço: R$ {self.__preco:.2f} | Quantidade: {self.__quantidade}"
    