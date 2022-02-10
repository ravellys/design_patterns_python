from abc import abstractmethod, ABC


class Secao(ABC):

    @abstractmethod
    def __repr__(self):
        pass


class SecaoPessoal(Secao):
    def __repr__(self):
        return 'Seção Pessoal'


class SecaoProfissional(Secao):
    def __repr__(self):
        return 'Seção Profissional'


class SecaoPublicacao(Secao):
    def __repr__(self):
        return 'Seção Publicação'


class SecaoAlbum(Secao):
    def __repr__(self):
        return 'Seção Álbum'


class SecaoPublica(Secao):
    def __repr__(self):
        return 'Seção Pública'


class Perfil(ABC):
    def __init__(self):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes

    def add_secao(self, secao):
        self.secoes.append(secao)


class Linkedin(Perfil):
    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoProfissional())
        self.add_secao(SecaoPublicacao())


class Facebook(Perfil):
    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoAlbum())


if __name__ == '__main__':
    rede_social = 'Facebook'

    perfil = eval(rede_social)()

    print(f'Criando o perfil no(a) {type(perfil).__name__}')
    print(f'O perfil tem as secoes: {perfil.get_secoes()}')