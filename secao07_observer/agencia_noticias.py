from abc import ABC, abstractmethod
from typing import Set, List


class Inscrito(ABC):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')


class SmsInscito(Inscrito):
    pass


class EmailInscito(Inscrito):
    pass


class PushInscito(Inscrito):
    pass


class AgenciaNoticias:
    def __init__(self):
        self.__inscritos: Set[Inscrito] = set()
        self.__ultima_noticia = None

    def inscrever(self, inscrito: Inscrito):
        self.__inscritos.add(inscrito)

    def desinscrever(self, inscrito: Inscrito = None):
        if not inscrito:
            inscrito = self.__inscritos.pop()
        if inscrito in self.__inscritos:
            self.__inscritos.discard(inscrito)
        print(f'Desinscrevendo o inscrito {type(inscrito).__name__}')
        return inscrito

    def adicionar_noticia(self, noticia):
        self.__ultima_noticia = noticia

    def notificar_todos(self):
        for inscrito in self.__inscritos:
            inscrito.notificar()

    def mostrar_noticia(self):
        return f'URRGENTE: {self.__ultima_noticia}'

    @property
    def inscritos(self):
        print('>>> Inscritos:')
        for inscrito in self.__inscritos:
            print(f'>> {type(inscrito).__name__}')
        return self.__inscritos


if __name__ == '__main__':
    agencia_noticias: AgenciaNoticias = AgenciaNoticias()
    inscrito_sms = SmsInscito(agencia_noticias)
    inscrito_email = EmailInscito(agencia_noticias)
    inscrito_push = PushInscito(agencia_noticias)
    print()
    inscritos = agencia_noticias.inscritos
    print()
    agencia_noticias.adicionar_noticia('Primeira Noticia')
    agencia_noticias.notificar_todos()
    print()
    agencia_noticias.desinscrever(inscrito_push)
    print()
    agencia_noticias.adicionar_noticia('Segunda Noticia')
    agencia_noticias.notificar_todos()
