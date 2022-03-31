from abc import ABC, abstractmethod
from typing import List


# Receiver
class Acao:
    def comprar(self):
        print('você irá comprar ações')

    def vender(self):
        print('você irá vender ações')


# Command
class Ordem(ABC):
    @abstractmethod
    def executar(self):
        pass


# Comamand Concreto
class OrdemCompra(Ordem):
    def __init__(self, acao: Acao):
        self.acao: Acao = acao

    def executar(self):
        self.acao.comprar()


class OrdemVenda(Ordem):
    def __init__(self, acao: Acao):
        self.acao: Acao = acao

    def executar(self):
        self.acao.vender()


# Invoker
class Agente:
    def __init__(self):
        self.__fila_ordens: List[Ordem] = []

    def adicionar_ordem_na_fila(self, ordem: Ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()


if __name__ == '__main__':
    # cliente
    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    ordem_venda = OrdemVenda(acao)

    # Invoker
    agente = Agente()
    agente.adicionar_ordem_na_fila(ordem_venda)
    agente.adicionar_ordem_na_fila(ordem_compra)
