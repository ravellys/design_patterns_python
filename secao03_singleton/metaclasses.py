class University(type):
    def __call__(cls, *args, **kwargs):
        print(f'>>> Esses são os args: {args}')
        return type.__call__(cls, *args, **kwargs)


class Geek(metaclass=University):
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2


if __name__ == '__main__':
   obj = Geek(2, 1)
   print(obj)