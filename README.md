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
