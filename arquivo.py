

# arquivo.py
import os
from produto import Produto

ARQUIVO = "produtos.txt"

def salvar_produtos(produtos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for p in produtos:
            f.write(f"{p.nome};{p.preco};{p.quantidade}\n")

def carregar_produtos():
    lista = []
    if not os.path.exists(ARQUIVO):
        return lista
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            nome, preco, quantidade = linha.strip().split(";")
            lista.append(Produto(nome, float(preco), int(quantidade)))
    return lista