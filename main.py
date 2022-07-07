from Sensores import SinalAnalogico
from Strategy.NTC import NTC
from Grafico import Scope

termistor = SinalAnalogico(NTC(resistencia=10000, unidade='Celcius'))

configuracao_controles = {'Período mínimo': 2,
                          'Período máximo': 100,
                          'Y1 mínimo': 0,
                          'Y1 máximo': 50,
                          'A1 máxima': 20}

scope = Scope(termistor, 'Temperatura (°C)', **configuracao_controles)
scope.iniciar_visualizacao()
