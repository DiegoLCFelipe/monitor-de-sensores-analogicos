from dataclasses import dataclass
from tratamentodesinal import Strategy
import numpy as np


@dataclass
class Steinhart(Strategy):
    TEMPERATURA_MINIMA = -40
    TEMPERATURA_MAXIMA = 125
    resistencia: float = 10000
    unidade: str = 'Celcius'

    COEF_STEINHART_1 = 1.009249522e-03
    COEF_STEINHART_2 = 2.378405444e-04
    COEF_STEINHART_3 = 2.019202697e-07

    def converte_sinal(self, registro_arduino):
        if registro_arduino is not None:
            temperatura = 1.0 / (
                    self.COEF_STEINHART_1 + self.COEF_STEINHART_2 *
                    np.log(self.resistencia * (1023 / registro_arduino - 1)) +
                    self.COEF_STEINHART_3 * np.log(self.resistencia * (1023 / registro_arduino - 1)) ** 3)
            if self.unidade == 'Kelvin':
                return temperatura
            elif self.unidade == 'Celcius':
                return temperatura - 273.15
