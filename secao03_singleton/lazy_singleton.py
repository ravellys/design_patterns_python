class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('O método __init__ foi chamado...')
        else:
            print(f' A instancia já foi criada: {self.instance()}')

    @classmethod
    def instance(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance


if __name__ == '__main__':
    s1 = Singleton()
    print(f'Objeto criado agora: {Singleton.instance()}')

    s2 = Singleton()
    print('s1 is s2: ', s1 is s2)
