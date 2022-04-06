class Modelo:
    def __init__(self):
        self.produtos = {
            'ps5': {'id': 1, 'nome': 'Playstation 5', 'preco': 1244},
            'xbox': {'id': 2, 'nome': 'Xnox 360', 'preco': 1445},
            'nii': {'id': 3, 'nome': 'Nintendo WII', 'preco': 1567},
        }


class Controlador:
    def __init__(self):
        self.modelo = Modelo()

    def listar_produtos(self):
        produtos = self.modelo.produtos.items()
        print('------------ Produto -------------')
        for key, produto in produtos:
            print(f'ID: {produto.get("id")}')
            print(f'Nome: {produto.get("nome")}')
            print(f'Preço: {produto.get("preco")}')
            print('')


class Visao:
    def __init__(self):
        self.controlador = Controlador()

    def produtos(self):
        self.controlador.listar_produtos()


if __name__ == '__main__':
    visao = Visao()
    visao.produtos()