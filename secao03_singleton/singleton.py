class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Criando o objeto {cls.instance}')
        return cls.instance


if __name__ == '__main__':
    s1 = Singleton()
    print('>>> Intancia 1', id(s1))
    s2 = Singleton()
    print('>>> Intancia 2', id(s2))
