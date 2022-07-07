from pyfirmata import Arduino, util
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def converte_sinal(self, registro_arduino):
        pass


class SinalAnalogico:
    def __init__(self, strategy: Strategy, porta_serial: str = '/dev/ttyACM0', pino='a:0:i') -> None:
        self._strategy = strategy
        self.placa = Arduino(porta_serial)
        self.registro_pyfirmata = self.placa.get_pin(pino)
        iterador = util.Iterator(self.placa)
        iterador.start()

    def sinal_padrao_arduino_uno(self):
        if self.registro_pyfirmata.read() is not None:
            return 1023 * self.registro_pyfirmata.read()

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def __iter__(self):
        return self

    def __next__(self) -> None:
        return self._strategy.converte_sinal(self.sinal_padrao_arduino_uno())

    def __str__(self):
        return str(self.__next__())
