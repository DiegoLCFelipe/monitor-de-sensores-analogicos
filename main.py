from tratamentodesinal import SinalAnalogico
from estrategiadeconversao.thermistorntc103 import Steinhart
from grafico import Animacao
import configuracao

sinal_convertido = SinalAnalogico(Steinhart(resistencia=10000, unidade='Celcius'))
escope = Animacao(sinal_convertido, 'Temperatura (°C)', **configuracao.CONROLES)
escope.iniciar_visualizacao()
