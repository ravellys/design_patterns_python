import sqlite3


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class DataBase(metaclass=Singleton):
    connection = None

    def connect(self):
        if self.connection is None:
            print(f'>>> Criando Conexão...')
            self.connection = sqlite3.connect('db')
            self.cursor = self.connection.cursor()
        return self.cursor


if __name__ == '__main__':
    conn1 = DataBase().connect()
    conn2 = DataBase().connect()
