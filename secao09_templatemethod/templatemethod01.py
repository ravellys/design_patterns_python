from abc import ABC, abstractmethod


class Compilador(ABC):

    @abstractmethod
    def coletar_fonte(self):
        pass

    @abstractmethod
    def compilar_objeto(self):
        pass

    @abstractmethod
    def executar(self):
        pass

    def compilar_e_executar(self):
        self.coletar_fonte()
        self.compilar_objeto()
        self.executar()


class CompiladorIOS(Compilador):
    def compilar_objeto(self):
        print('Compilando código fonte Swift')

    def executar(self):
        print('Programa executando no ambiente de execução')

    def coletar_fonte(self):
        print('Coletando código fonte Swift')


class CompiladorAndroid(Compilador):
    def compilar_objeto(self):
        print('Compilando código fonte Kotlin')

    def executar(self):
        print('Programa executando no ambiente de execução')

    def coletar_fonte(self):
        print('Coletando código fonte Kotlin')


if __name__ == '__main__':
    ios = CompiladorIOS()
    ios.compilar_e_executar()

    android = CompiladorAndroid()
    android.compilar_e_executar()