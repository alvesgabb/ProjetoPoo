# menu.py
from produto import Produto
from estoque import Estoque

def exibir_menu():
    estoque = Estoque() 
    

    while True:
        print("\n===== Sistema de Gestão de Estoque =====")
        print("1. Cadastrar novo produto")
        print("2. Listar produtos")
        print("3. Adicionar quantidade a um produto")
        print("4. Remover quantidade de um produto")
        print("5. Remover produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            estoque.adicionar_produto(Produto(nome, preco, quantidade))
            print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            estoque.listar_produtos()

        elif opcao == "3":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a adicionar: "))
            estoque.adicionar_quantidade(nome, quantidade)
            print("Quantidade adicionada com sucesso!")

        elif opcao == "4":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a remover: "))
            estoque.remover_quantidade(nome, quantidade)
            print("Quantidade removida com sucesso!")

        elif opcao == "5":
            nome = input("Nome do produto a remover: ")
            estoque.remover_produto(nome)
            print("Produto removido com sucesso!")

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")