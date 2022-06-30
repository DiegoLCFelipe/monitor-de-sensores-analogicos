import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from matplotlib.lines import Line2D

from Sensores import NTC


class Scope:
    def __init__(self, variavel):

        self.controle_deslizante_periodo = None
        self.amplitude_slider = None
        self.y0_slider = None
        self.periodo_slider = None
        self.amp_slider = None
        self.variavel = variavel
        plt.style.context('dark_background')
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.time_data = [0]
        self.sensor_data = [0]
        self.dt = 0
        self.line = Line2D(self.time_data, self.sensor_data)
        self.ax.add_line(self.line)
        self.line.set_linewidth(3)
        self.ax.set_ylim(20, 30)
        self.ax.set_xlim(0, 10)
        plt.subplots_adjust(left=0.3, bottom=0.25)
        self._controle_deslizantes()

    def update(self, data):
        self.ax.figure.canvas.draw()
        self.dt += 1
        self.time_data.append(self.dt)
        self.sensor_data.append(data)

        if len(self.time_data) > 100:
            self.time_data = self.time_data[-600:]
            self.sensor_data = self.sensor_data[-600:]

        self.time_data = self.time_data
        self.sensor_data = self.sensor_data

        self.ax.set_xlim(self.time_data[-1] - self.controle_deslizante_periodo.val, self.time_data[-1])

        self.ax.set_ylim(
            self.controle_deslizante_y_1.val + self.controle_deslizante_y_2.val -
            (self.controle_deslizante_amplitude_1.val + self.controle_deslizante_amplitude_2.val),
            self.controle_deslizante_y_1.val + self.controle_deslizante_y_2.val +
            (self.controle_deslizante_amplitude_1.val + self.controle_deslizante_amplitude_2.val))

        self.line.set_data(self.time_data, self.sensor_data)
        self.ax.grid(True)
        self.ax.set_ylabel('°C')

        return self.line,

    def _cria_controle_deslizante(self, area=None, rotulo='', valor_minimo=0, valor_maximo=10, valor_inical=1, passo=1,
                                  orientacao='vertical'):
        return Slider(ax=plt.axes(area), label=rotulo, valmin=valor_minimo, valmax=valor_maximo, valinit=valor_inical,
                      valstep=passo, orientation=orientacao)

    def _controle_deslizantes(self):
        self.controle_deslizante_periodo = self._cria_controle_deslizante([0.4, 0.1, 0.45, 0.03], 'Período (s)', 1, 600,
                                                                          1, 1, 'horizontal')
        self.controle_deslizante_y_1 = self._cria_controle_deslizante([0.05, 0.25, 0.0225, 0.63], 'Y1', 0, 125, 26,1)
        self.controle_deslizante_y_2 = self._cria_controle_deslizante([0.10, 0.25, 0.0225, 0.63], 'Y2', 0, 0.9, 0, 0.1)
        self.controle_deslizante_amplitude_1 = self._cria_controle_deslizante([0.15, 0.25, 0.0225, 0.63], 'A1', 0, 10, 1,1)
        self.controle_deslizante_amplitude_2 = self._cria_controle_deslizante([0.2, 0.25, 0.0225, 0.63], 'A2', 0, 1, 0.1, 0.1)

    def iniciar_visualizacao(self):

        ani = animation.FuncAnimation(fig=self.fig, func=scope.update,
                                      frames=self.variavel, interval=1000,
                                      blit=True)
        plt.style.context('dark_background')
        plt.show()


termistor = NTC()
scope = Scope(termistor)
scope.iniciar_visualizacao()
