from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        print('au au')


class Gato(Animal):
    def falar(self):
        print('Miau')


class Fabrica:
    tipos = ['Gato', 'Cachorro']

    def criar_animal_falante(self, tipo: str) -> Animal:
        if tipo not in self.tipos:
            print(f'tipo {tipo} inválido')
        return eval(tipo)()


if __name__ == '__main__':
    fab = Fabrica()
    animal_str = input('Qual animal você quer que fale? [Cachorro, Gato] ')
    animal: Animal = fab.criar_animal_falante(animal_str)
    animal.falar()
