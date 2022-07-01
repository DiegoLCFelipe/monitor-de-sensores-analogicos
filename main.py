import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from matplotlib.lines import Line2D

from Sensores import NTC


class Scope:
    def __init__(self, variavel, nome_variavel):
        self.variavel = variavel
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        plt.subplots_adjust(left=0.3, bottom=0.2)
        self.time_data = [0]
        self.sensor_data = [0]
        self.dt = 0

        self.nome_variavel = nome_variavel
        self._numero_de_registros_armazenados = 600

        self.line = Line2D(self.time_data, self.sensor_data)
        self.ax.add_line(self.line)
        self.line.set_linewidth(3)

        # Localização dos controles deslizantes
        self.__AX_CONTROLE_PERIODO = [0.4, 0.1, 0.45, 0.03]
        self.__AX_CONTROLE_Y1 = [0.05, 0.25, 0.0225, 0.63]
        self.__AX_CONTROLE_Y2 = [0.10, 0.25, 0.0225, 0.63]
        self.__AX_CONTROLE_AMPLITUDE1 = [0.15, 0.25, 0.0225, 0.63]
        self.__AX_CONTROLE_AMPLITUDE2 = [0.2, 0.25, 0.0225, 0.63]

        # Configuração dos controles deslizantes
        self._conf_controle_periodo = ['Período (s)', 1, 600, 1, 1]
        self._conf_controle_y1 = ['Y1', 0, 125, 26, 1]
        self._conf_controle_y2 = ['Y2', 0, 0.9, 0, 0.1]
        self._conf_controle_amplitude1 = ['A1', 0, 10, 1, 1]
        self._conf_controle_amplitude2 = ['A2', 0, 1, 0.1, 0.1]

        self._controles_deslizantes()

    @property
    def _numero_de_registros_armazenados(self):
        return self._numero_de_registros_armazenados

    @_numero_de_registros_armazenados.setter
    def _numero_de_registros_armazenados(self, value):
        self._numero_de_registros_armazenados = value

    @property
    def _conf_controle_y1(self):
        return self._conf_controle_y1

    @_conf_controle_y1.setter
    def _conf_controle_y1(self, value):
        self._conf_controle_y1 = value

    @property
    def _conf_controle_y2(self):
        return self._conf_controle_y2

    @_conf_controle_y2.setter
    def _conf_controle_y2(self, value):
        self._conf_controle_y2 = value

    @property
    def _conf_controle_amplitude1(self):
        return self._conf_controle_amplitude1

    @_conf_controle_amplitude1.setter
    def _conf_controle_amplitude1(self, value):
        self._conf_controle_amplitude1 = value

    @property
    def _conf_controle_amplitude2(self):
        return self._conf_controle_amplitude1

    @_conf_controle_amplitude2.setter
    def _conf_controle_amplitude2(self, value):
        self._conf_controle_amplitude1 = value


    def update(self, data):
        self.ax.figure.canvas.draw()
        self.dt += 1
        self.time_data.append(self.dt)
        self.sensor_data.append(data)

        if len(self.time_data) > self._numero_de_registros_armazenados:
            self.time_data = self.time_data[-self._numero_de_registros_armazenados:]
            self.sensor_data = self.sensor_data[-self._numero_de_registros_armazenados:]

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
        self.ax.set_ylabel(self.nome_variavel)

        return self.line,

    def _cria_controle_deslizante(self, area=None, configuracao=None, orientacao='vertical'):
        if configuracao is None:
            configuracao = []
        return Slider(ax=plt.axes(area), label=configuracao[0], valmin=configuracao[1], valmax=configuracao[2],
                      valinit=configuracao[3], valstep=configuracao[4], orientation=orientacao)

    def _controles_deslizantes(self):
        self.controle_deslizante_periodo = self._cria_controle_deslizante(self.__AX_CONTROLE_PERIODO,
                                                                          self._conf_controle_periodo, 'horizontal')
        self.controle_deslizante_y_1 = self._cria_controle_deslizante(self.__AX_CONTROLE_Y1,
                                                                      self._conf_controle_y1)
        self.controle_deslizante_y_2 = self._cria_controle_deslizante(self.__AX_CONTROLE_Y2,
                                                                      self._conf_controle_y2)
        self.controle_deslizante_amplitude_1 = self._cria_controle_deslizante(self.__AX_CONTROLE_AMPLITUDE1,
                                                                              self._conf_controle_amplitude1)
        self.controle_deslizante_amplitude_2 = self._cria_controle_deslizante(self.__AX_CONTROLE_AMPLITUDE2,
                                                                              self._conf_controle_amplitude2)

    def iniciar_visualizacao(self):
        ani = animation.FuncAnimation(fig=self.fig, func=scope.update,
                                      frames=self.variavel, interval=1000,
                                      blit=True)
        plt.show()




termistor = NTC()
scope = Scope(termistor, 'Temperatura (°C)')
scope.iniciar_visualizacao()
