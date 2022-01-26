from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4


class Pessoa(ABC):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__nascimento = datetime.now()

    def __str__(self) -> str:
        return self.__nome

    def __repr__(self) -> str:
        return self.__nome

    @abstractmethod
    def ganhar_dinheiro(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome: str):
        super().__init__(nome=nome)
        self.__matricula = str(uuid4()).split('-')[0].upper()

    def ganhar_dinheiro(self):
        print('como ganhar dinheiro?')


if __name__ == '__main__':
    aluno = Aluno('lucas')
    aluno.ganhar_dinheiro()