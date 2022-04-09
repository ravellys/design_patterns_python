from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, List


class StateComputer(ABC):
    @property
    @abstractmethod
    def permitido(self) -> List[str]:
        return []

    def mudar(self, state: StateComputer):
        if str(state) in self.permitido:
            print(f'Atual: {self} => mudado para um novo estado: {state}')
            self.__class__ = type(state)
        else:
            print(f'Atual: {self} => não é possível mudar para: {state}')

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return type(self).__name__


class Ligar(StateComputer):
    permitido = ["Desligar", "Suspender", "Hibernar"]


class Desligar(StateComputer):
    permitido = ["Ligar"]


class Suspender(StateComputer):
    permitido = ["Ligar"]


class Hibernar(StateComputer):
    permitido = ["Ligar"]


class Computador:

    def __init__(self, modelo: str):
        self.modelo = modelo
        self.estado = Desligar()

    def alterar(self, state: StateComputer):
        self.estado.mudar(state)


if __name__ == '__main__':
    comp = Computador('Dell')

    comp.alterar(Ligar())
    comp.alterar(Desligar())
    comp.alterar(Ligar())
    comp.alterar(Suspender())
    comp.alterar(Hibernar())
    comp.alterar(Ligar())
    comp.alterar(Desligar())
