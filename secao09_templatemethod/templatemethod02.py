from abc import ABC, abstractmethod


class ClasseAbs(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

    def template_method(self):
        print('executando method1 depois method2')
        self.method1()
        self.method2()


class ClassConc1(ClasseAbs):
    def method1(self):
        print(f'mehod1 {type(self).__name__}')

    def method2(self):
        print(f'method2 {type(self).__name__}')


class ClassConc2(ClasseAbs):
    def method1(self):
        print(f'mehod1 {type(self).__name__}')

    def method2(self):
        print(f'method2 {type(self).__name__}')


class Cliente:
    @classmethod
    def main(cls):
        ClassConc1().template_method()
        ClassConc2().template_method()


if __name__ == '__main__':
    Cliente.main()
