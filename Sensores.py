from pyfirmata import Arduino, util
from datetime import datetime
import numpy as np


class Sensores:

    def __init__(self, porta_serial='/dev/ttyACM0', pino='a:0:i', resistencia=10000):
        self.placa = Arduino(porta_serial)
        self.resistencia = resistencia
        iterador = util.Iterator(self.placa)
        iterador.start()
        self.registro = self.placa.get_pin(pino)

    def __iter__(self):
        return self

    def sinal_padrao_arduino(self):
        return 1023 * self.registro.read()


class NTC(Sensores):
    COEF_STEINHART_1 = 1.009249522e-03
    COEF_STEINHART_2 = 2.378405444e-04
    COEF_STEINHART_3 = 2.019202697e-07

    def __next__(self):
        if self.registro.read() is not None:
            return self.calcula_temperatura()


    def calcula_resistencia_thermistor(self):
        return self.resistencia * (1023 / self.sinal_padrao_arduino() - 1)

    @staticmethod
    def transforma_de_kelvin_para_celcius(temperatura_em_kelvin):
        return temperatura_em_kelvin - 273.15

    def calcula_temperatura(self, unidade="Celcius"):
        temperatura = 1.0 / (
                self.COEF_STEINHART_1 + self.COEF_STEINHART_2 * np.log(self.calcula_resistencia_thermistor())
                + self.COEF_STEINHART_3 * np.log(self.calcula_resistencia_thermistor()) ** 3)
        if unidade == 'Kelvin':
            return temperatura
        elif unidade == 'Celcius':
            return self.transforma_de_kelvin_para_celcius(temperatura)
