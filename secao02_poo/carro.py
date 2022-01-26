from typing import Optional

from pessoa import Pessoa


class Carro:
    def __init__(self, is_sedan: bool = False):
        self.__is_sedan: bool = is_sedan
        self.__velocidade: int = 0
        self.__motorista: Optional[Pessoa] = None

    def __str__(self) -> str:
        if self.__motorista:
            return f'Carro do(a) {self.__motorista}'
        return 'Carro sem motorista'

    def dirigir(self, motorista: Pessoa):
        self.__motorista = motorista
        self.acelerar(1)

    def acelerar(self, velocidade: int):
        self.__velocidade += velocidade

    def parar(self):
        self.__velocidade = 0


if __name__ == '__main__':
    angelina = Pessoa('angelina')
    fusca = Carro()
    fusca.dirigir(angelina)
    print(fusca.__dict__)
    print(fusca)
