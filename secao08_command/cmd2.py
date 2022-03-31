from abc import ABC, abstractmethod


class Receiver:
    def acao(self):
        print('Ação Receiver')


class Command(ABC):
    def __init__(self, recv: Receiver):
        self.recv = recv

    @abstractmethod
    def executar(self):
        pass


class CommandConcreto(Command):

    def executar(self):
        self.recv.acao()


class Invoker:
    def comando(self, cmd: Command):
        self.cmd = cmd

    def executar(self):
        self.cmd.executar()


if __name__ == '__main__':
    rcv = Receiver()
    cmd = CommandConcreto(rcv)

    invoker = Invoker()
    invoker.comando(cmd)
    invoker.executar()
