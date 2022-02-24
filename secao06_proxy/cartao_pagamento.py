from abc import ABC, abstractmethod


class Carteira(ABC):
    @abstractmethod
    def pagar(self):
        pass


class CarteiraDigital(Carteira):
    def __init__(self):
        self.cartao = None
        self.conta = None

    def __get_conta(self):
        self.conta = self.cartao
        return self.conta

    @property
    def tem_saldo(self):
        print(f'CarteiraDigital:: Checando se a conta {self.__get_conta()} tem saldo')
        return True

    def set_cartao(self, cartao):
        self.cartao = cartao

    def pagar(self):
        if self.tem_saldo:
            print('CarteiraDigital:: Pagando o bar...')
            return True
        else:
            print('CarteiraDigital:: Desculpe, você não tem saldo suficiente')
            return False


class CartaoDebito(Carteira):

    def __init__(self):
        self.carteira_digital = CarteiraDigital()

    def pagar(self):
        cartao = input('insira os dados do cartão')
        self.carteira_digital.set_cartao(cartao)
        return self.carteira_digital.pagar()


class Cliente:
    def __init__(self):
        print('Cliente:: Quero COmprar uma Cerveja!')
        self.cartao_debito = CartaoDebito()
        self.comprei = None

    def fazer_pagamento(self):
        self.comprei = self.cartao_debito.pagar()

    def __del__(self):
        if self.comprei:
            print('Cliente:: Comprei uma cerveja')
        else:
            print('CLiente:: Não comprei uma cerveja')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.fazer_pagamento()
    del cliente
