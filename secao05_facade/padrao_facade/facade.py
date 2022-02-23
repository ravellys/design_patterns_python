from banda import Banda
from floristas import Florista
from restaurante import Restaurante
from salao_festas import SalaoFestas


class GerenciamentoEventos:
    def __init__(self):
        self.salao = SalaoFestas()
        self.florista = Florista()
        self.restaurante = Restaurante()
        self.banda = Banda()
        print('GerenciamentoEventos :: Vou Organizar com todo mundo| \n\n')

    def organizar(self):
        self.salao.agendar()
        self.florista.arranjar_flores()
        self.restaurante.preparar_comida()
        self.banda.montar_palco()


class CLiente:

    def __init__(self):
        print('Preparação de casamento!')

    def contratar_gerente_eventos(self):
        print('VOu COntratar um gerente de eventos')
        facade = GerenciamentoEventos()
        facade.organizar()

    def __del__(self):
        print('Cliente :: foi muito simples organizar com facade')


if __name__ == '__main__':
    cliente = CLiente()
    cliente.contratar_gerente_eventos()