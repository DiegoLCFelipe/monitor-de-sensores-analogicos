from tratamentodesinal import SinalAnalogico
from estrategiadeconversao.thermistorntc103 import Steinhart
from grafico import Animacao
import configuracao

termistor = SinalAnalogico(Steinhart(resistencia=10000, unidade='Celcius'))
scope = Animacao(termistor, 'Temperatura (°C)', **configuracao.CONROLES)
scope.iniciar_visualizacao()
