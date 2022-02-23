class SalaoFestas:
    def __init__(self):
        print(f'SalaoFestas :: Agendando Salão de festas para o casamento ... ')

    def _esta_disponivel(self):
        print(f'SalaoFestas :: Este salão de festas está disponível?')

    def agendar(self):
        if self._esta_disponivel():
            print(f'SalaoFestas :: Agendamento do salão realizado. \n')
