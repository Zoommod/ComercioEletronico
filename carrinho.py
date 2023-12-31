from cor import CorTexto


class Carrinho:
    def __init__(self):
        self.lista_produtos = []
        self.lista_codigos_carrinho = []
        self.total = 0

    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)
        self.lista_codigos_carrinho.append(produto.get_codigo())
        self.total += produto.get_valor()
        print(f"\n'{CorTexto.VERDE}{produto.get_nome()}' adicionado ao carrinho.")

    def mostrar_carrinho(self):
        print("CARRINHO DE COMPRAS:\n")
        for produto in self.lista_produtos:
            print(f"{CorTexto.CIANO}Nome: {CorTexto.BRANCO}{produto.get_nome()}")
            print(f"{CorTexto.CIANO}Valor: {CorTexto.BRANCO}R${produto.get_valor()}\n")
        print(f"{CorTexto.CIANO}Total: {CorTexto.BRANCO}R${self.total:.2f}\n")

    def concluir_compra(self):
        if not self.lista_produtos:
            print(f"\n{CorTexto.VERMELHO}O carrinho está vazio. Adicione produtos antes de concluir a compra.")
            return

        print("\nCUPOM FISCAL:\n")
        for produto in self.lista_produtos:
            print(f"{CorTexto.CIANO}Nome: {CorTexto.BRANCO}{produto.get_nome()}")
            print(f"{CorTexto.CIANO}Valor: {CorTexto.BRANCO}R${produto.get_valor()}\n")
        print(f"{CorTexto.CIANO}Total: {CorTexto.BRANCO}R${self.total:.2f}")

    def retirar_item(self, produto):
        if produto.get_codigo() in self.lista_codigos_carrinho:
            self.lista_codigos_carrinho.remove(produto.get_codigo())
            self.lista_produtos.remove(produto)
            self.total -= produto.get_valor()
            print(f"\n{CorTexto.VERDE}{produto.get_nome()} foi removido do carrinho.")
        else:
            print(f"\n{CorTexto.VERMELHO}O código digitado não é de um produto inserido no carrinho. Tente novamente!")




