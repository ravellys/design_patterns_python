from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class State(ABC):
    @abstractmethod
    def manipular(self): pass


class StateConcretoA(State):
    def manipular(self):
        print(type(self).__name__)


class StateConcretoB(State):
    def manipular(self):
        print(type(self).__name__)


class Context(State):
    def manipular(self):
        if not self.state:
            return
        self.state.manipular()

    def __init__(self):
        self.__state: Optional[State] = None

    @property
    def state(self) -> State:
        return self.__state

    @state.setter
    def state(self, val: State):
        self.__state = val


if __name__ == '__main__':
    contexto = Context()
    statea = StateConcretoA()
    stateb = StateConcretoB()

    contexto.state = statea
    contexto.manipular()

    contexto.state = stateb
    contexto.manipular()
