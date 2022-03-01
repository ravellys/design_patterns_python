from abc import ABC, abstractmethod


class Seguidor(ABC):
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def notify(self, *args, **kwargs):
        pass

    @abstractmethod
    def seguir(self, *args, **kwargs):
        pass

    @abstractmethod
    def desseguir(self, *args, **kwargs):
        pass


class Influencer(ABC):
    def __init__(self):
        self.__seguidores = set()  # 1:N

    @property
    def seguidores(self):
        return self.__seguidores

    @seguidores.setter
    def seguidores(self, value):
        if not isinstance(value, set):
            value = {value}
        self.__seguidores.update(value)

    @abstractmethod
    def add_seguidor(self, pessoa_virtual: Seguidor):
        pass

    def remove_seguidor(self, pessoa_virtual: Seguidor):
        self.__seguidores.discard(pessoa_virtual)

    @abstractmethod
    def postar(self, conteudo: str):
        pass


class PessoaVirtual(Seguidor, Influencer):
    def __init__(self, name: str):
        Seguidor.__init__(self, name)
        Influencer.__init__(self)

    def add_seguidor(self, pessoa_virtual):
        self.seguidores = pessoa_virtual
        print(f'olá {self.name}, {pessoa_virtual.name} seguiu você')

    def remove_seguidor(self, pessoa_virtual):
        super(PessoaVirtual, self).remove_seguidor(pessoa_virtual)
        print(f'olá {self.name}, {pessoa_virtual.name} deixou de seguir você')

    def seguir(self, pessoa_virtual):
        print(f'>>> olá {self.name}! você seguiu {pessoa_virtual.name}!')
        pessoa_virtual.add_seguidor(self)

    def desseguir(self, pessoa_virtual):
        print(f'>>> olá {self.name}! você desseguiu {pessoa_virtual.name}!')
        pessoa_virtual.remove_seguidor(self)

    def notify(self, pessoa_virtual, conteudo: str):
        print(f'olá {self.name}! {pessoa_virtual.name}, Postou: {conteudo}')

    def postar(self, conteudo: str):
        for seguidor in self.seguidores:
            seguidor.notify(self, conteudo)


if __name__ == '__main__':
    lucas = PessoaVirtual('lucas')
    abraao = PessoaVirtual('abraão')
    ailtinho = PessoaVirtual('ailtinho')

    lucas.seguir(ailtinho)
    abraao.seguir(ailtinho)

    ailtinho.postar('Por que choras Brad Pitty?')
    abraao.desseguir(ailtinho)
    ailtinho.postar('@abraao, Meteu essa?')
