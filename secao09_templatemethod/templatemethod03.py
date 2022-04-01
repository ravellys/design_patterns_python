from abc import ABC, abstractmethod


class Viagem(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass

    @abstractmethod
    def retorno(self):
        pass

    def itinerario(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retorno()


class ViagemVeneza(Viagem):

    def ida(self):
        print('Viagem de avião ...')

    def dia1(self):
        print('visita à basílica')

    def dia2(self):
        print('visita ao palácio Doge')

    def dia3(self):
        print('Aproveitar comida...')

    def retorno(self):
        print('Viagem de avião')


class ViagemMalvinas(Viagem):

    def ida(self):
        print('Viagem de onibus ...')

    def dia1(self):
        print('Apreciar a vida marinha')

    def dia2(self):
        print('praticar esportes aquaticos')

    def dia3(self):
        print('relaxar no sol...')

    def retorno(self):
        print('Viagem de avião')


class Travel:
    @classmethod
    def preparar_viagem(cls):
        opcao = input('Qual local de viagem deseja fazer? [Veneza, Malvinas]: ')

        viagem = None
        if opcao == 'Veneza':
            viagem = ViagemVeneza()
        elif opcao == 'Malvinas':
            viagem = ViagemMalvinas()
        else:
            cls.preparar_viagem()
        viagem.itinerario()
        exit()


if __name__ == '__main__':
    Travel.preparar_viagem()
