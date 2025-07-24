from Produto import Produto
from ProdutoAlimenticio import ProdutoAlimenticio

def main():
    produtos = []
    
    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar Produto Comum")
        print("2. Cadastrar Produto Alimentício")
        print("3. Exibir Produtos Cadastrados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            quantidade = int(input("Quantidade do Produto: "))
            produto = Produto(nome, preco, quantidade)
            produtos.append(produto)
        
        elif opcao == '2':
            nome = input("Nome do Produto Alimentício: ")
            preco = float(input("Preço do Produto Alimentício: "))
            quantidade = int(input("Quantidade do Produto Alimentício: "))
            data_validade = input("Data de Validade (DD/MM/AAAA): ")
            produto_alimenticio = ProdutoAlimenticio(nome, preco, quantidade, data_validade)
            produtos.append(produto_alimenticio)
        
        elif opcao == '3':
            print("\nProdutos Cadastrados:")
            for produto in produtos:
                produto.exibir_produtos()
        
        elif opcao == '4':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
