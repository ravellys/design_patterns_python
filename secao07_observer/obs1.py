"""
>> Cada OBSERVADOR tem um OBJETO e um OBJETO pode ter vários OBSERVADOR (OBJETO 1:N OBSERVADOR)
>> OBJETO tem um método notificar_todos
>> OBSERVADOR tem um metodo notificar
>> notificar_todos executa o notificar de cada OBSERVADOR
"""

from abc import ABC


class Objeto:

    def __init__(self):
        self.__observadores = []

    def __repr__(self):
        return ':: Objeto ::'

    def registrar(self, observador):
        self.__observadores.append(observador)

    def notificar_todos(self, *args, **kwargs):
        for observador in self.__observadores:
            observador.notificar(self, *args, **kwargs)


class Observador(ABC):
    def __init__(self, objeto):
        objeto.registrar(self)

    def notificar(self, objeto, *args):
        print(f'O {type(self).__name__} recebeu uma {args[0]} de {objeto}')


class ObservadorA(Observador):
    pass


class ObservadorB(Observador):
    pass


if __name__ == '__main__':
    obj = Objeto()

    obsA = ObservadorA(obj)
    obsB = ObservadorB(obj)

    obj.notificar_todos('notificacao')