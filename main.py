from tratamentodesinal import SinalAnalogico
from estrategiadeconversao.thermistorntc103 import Steinhart
from grafico import Animacao

termistor = SinalAnalogico(Steinhart(resistencia=10000, unidade='Celcius'))

configuracao_controles = {'Período mínimo': 2,
                          'Período máximo': 100,
                          'Y1 mínimo': 0,
                          'Y1 máximo': 50,
                          'A1 máxima': 20}

scope = Animacao(termistor, 'Temperatura (°C)', **configuracao_controles)
scope.iniciar_visualizacao()
