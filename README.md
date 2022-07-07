# Monitor de Sensores Analógicos 

<img src="https://github.com/DiegoLCFelipe/monitor-de-sensores-analogicos/blob/master/img/logo.jpeg" align="right"
     alt="Logo pessoal de Diego Felipe" width="130" height="130">
     
O Monitor de Sensores Analógicos é um projeto pessoal para visualizar grandezas físicas convertidas
de sinais analógicos provenienves de microcontroladores Arduino. A ideia é criar uma visualização 
semelhenate a de um osciloscópio, onde é possível controlar, período, amplitude e a posição no eixo y.


# Como funciona

1. A classe `SinalAnalogico` dentro do módulo `tratamentodesinal` faz a comunicação serial com o Arduino 
2. O sinal analógico é convertido para a grandeza física utilizando uma stratégia personalizada salva do diretório `strategiadeconversao` (ver Strategy design pattern) 
3. Após o sinal ser convertido ele é passado para a classe `Animacao`, junto com o nome da grandeza física e as configurações dos controles deslizante 
4. Opcionalmente é possível configurar o design da visualização através do arquivo `design.mplstyle`


<p align="center">
<img src="https://github.com/DiegoLCFelipe/monitor-de-sensores-analogicos/blob/master/img/monitor.gif"
     alt="Gif mostrando o funcionamento do programa" width="578">
</p>

# Configurações 
## Método de Conversão de Sinal

O métdo de conversão do sinal analógico deve ser configurado no `main.py`. Primeiro importe a estratégia (classe) dentro do módulo do sensor, salvo no package `estrategiadeconversao`, conforme mostrado na linha 2. Após isso passe a estratégia como parâmetro da classe `SinalAnalogico`, conforme mostrado na linha 7.

```py
1 from tratamentodesinal import SinalAnalogico
2 from estrategiadeconversao.thermistorntc103 import Steinhart
3 from grafico import Animacao
4 import configuracao
5
6 sinal_convertido = SinalAnalogico(Steinhart(resistencia=10000, unidade='Celcius'))
7 escopo = Animacao(sinal_convertido, 'Temperatura (°C)', **configuracao.CONROLES)
8 escopo.iniciar_visualizacao()
 ```

## Configuração dos Controles

Os controles do "osciloscópio" podem ser configurados dentro do arquivo `configuracao.py`. Por exemplo, temos as configurações do controle deslizante do período. Nota-se que é possível configurar o menor valor do controle, o maior e o passo.

```py
1 CONROLES ={
2     # Controle deslizante período
3     'Período mínimo': 2,
4     'Período máximo': 100,
5     'Escala período': 10
 ```

 ## Design 
 Aspectos de design como cores, estilos de linha e fonte podem ser configurados no arquivo `design.mplstyle`, seguindo o rcParams da biblioteca matplotlib [(https://matplotlib.org/stable/tutorials/introductory/customizing.html)](https://matplotlib.org/stable/tutorials/introductory/customizing.html).

```py
figure.facecolor : (0.91, 0.92, 0.92)
axes.facecolor: (0.95,0.95,0.95)
axes.labelcolor: (0.05, 0.06, 0.07)
axes.titlecolor:  'white'
lines.color: (0.34, 0.15, 0.69)
grid.color: (0.5, 0.53, 0.55, 0.1)
grid.linestyle: -.
patch.facecolor: (0.34, 0.15, 0.69)
xtick.color : (0.05, 0.06, 0.07)
ytick.color : (0.05, 0.06, 0.07)
 ```