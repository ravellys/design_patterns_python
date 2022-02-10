from abc import ABC, abstractmethod


# Abstract factory
class PizzaFactory(ABC):

    @abstractmethod
    def criar_pizza(self):
        pass

    @abstractmethod
    def criar_pizza_vegana(self):
        pass


# Concrect Factory
class PizzaBrasileiraFactory(PizzaFactory):
    def criar_pizza(self):
        return PizzaCamarao()

    def criar_pizza_vegana(self):
        return PizzaMandioca()


class PizzaItalianaFactory(PizzaFactory):
    def criar_pizza(self):
        return PizzaBolonha()

    def criar_pizza_vegana(self):
        return PizzaBrocolis()


# Abstract Product
class PizzaVegana(ABC):
    @abstractmethod
    def preparar(self):
        pass


class Pizza(ABC):
    @abstractmethod
    def servir(self, PizzaVeg):
        pass


# Concret Product
class PizzaMandioca(PizzaVegana):
    def preparar(self):
        print(f'Preparando {type(self).__name__}')


class PizzaBrocolis(PizzaVegana):
    def preparar(self):
        print(f'Preparando {type(self).__name__}')


class PizzaCamarao(Pizza):
    def servir(self, pizza_vegana: PizzaVegana):
        print(f'Pizza {type(self).__name__} é servida com camarão na pizza {type(pizza_vegana).__name__}')


class PizzaBolonha(Pizza):
    def servir(self, pizza_vegana: PizzaVegana):
        print(f'Pizza {type(self).__name__} é servida com bolonha na pizza {type(pizza_vegana).__name__}')


# Cliente
class Pizzaria:
    def fazer_pizzas(self):
        for factory in [PizzaBrasileiraFactory(), PizzaItalianaFactory()]:
            self.factory: PizzaFactory = factory
            self.pizza: Pizza = self.factory.criar_pizza()
            self.pizza_vegana: PizzaVegana = self.factory.criar_pizza_vegana()
            self.pizza_vegana.preparar()
            self.pizza.servir(self.pizza_vegana)


if __name__ == '__main__':
    pizzaria = Pizzaria()
    pizzaria.fazer_pizzas()
