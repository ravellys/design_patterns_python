class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class SanidadeCheck(metaclass=Singleton):

    def __init__(self):
        self.__servidores = []

    def checar_servidor(self, srv):
        print(f'Checando o {self.__servidores[srv]}')

    def add_servidor(self):
        self.__servidores.append('Servidor 1')
        self.__servidores.append('Servidor 2')
        self.__servidores.append('Servidor 3')
        self.__servidores.append('Servidor 4')

    def mudar_servidor(self):
        self.__servidores.pop()
        self.__servidores.append('Sevidor 5')


if __name__ == '__main__':
    sc1 = SanidadeCheck()
    sc2 = SanidadeCheck()

    sc1.add_servidor()
    print('Cronograma de checagem de sanidade dos servidores A...')
    for srv in range(4):
        sc1.checar_servidor(srv)

    sc2.mudar_servidor()
    print('Cronograma de checagem de sanidade dos servidores B...')
    for srv in range(4):
        sc2.checar_servidor(srv)