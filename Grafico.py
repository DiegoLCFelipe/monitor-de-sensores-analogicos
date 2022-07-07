import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from matplotlib.lines import Line2D


class Scope:
    plt.style.use('apresentacao.mplstyle')

    def __init__(self, variavel, nome_variavel, **kwargs):
        self.variavel = variavel
        self.time_data = [0]
        self.sensor_data = [0]
        self.dt = 0

        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.fig.subplots_adjust(left=0.3, bottom=0.2)
        self.line = Line2D(self.time_data, self.sensor_data)
        self.ax.add_line(self.line)

        self.nome_variavel = nome_variavel
        self._numero_de_registros_armazenados = 600

        # Localização dos controles deslizantes

        self.__AX_CONTROLE_PERIODO = self.fig.add_axes([0.4, 0.1, 0.45, 0.03])
        self.__AX_CONTROLE_Y1 = self.fig.add_axes([0.05, 0.25, 0.0225, 0.63])
        self.__AX_CONTROLE_Y2 = self.fig.add_axes([0.10, 0.25, 0.0225, 0.63])
        self.__AX_CONTROLE_AMPLITUDE1 = self.fig.add_axes([0.15, 0.25, 0.0225, 0.63])
        self.__AX_CONTROLE_AMPLITUDE2 = self.fig.add_axes([0.2, 0.25, 0.0225, 0.63])

        self._minimo_controle_periodo = kwargs.get('Período mínimo', 0)
        self._minimo_controle_y_1 = kwargs.get('Y1 mínimo', 0)
        self._minimo_controle_y_2 = kwargs.get('Y2 mínimo', 0)
        self._minimo_controle_amplitude_1 = kwargs.get('A1 mínima', 0)
        self._minimo_controle_amplitude_2 = kwargs.get('A2 mínima', 0)

        self._maximo_controle_periodo = kwargs.get('Período máximo', 100)
        self._maximo_controle_y_1 = kwargs.get('Y1 máximo', 125)
        self._maximo_controle_y_2 = kwargs.get('Y2 máximo', 0.9)
        self._maximo_controle_amplitude_1 = kwargs.get('A1 máxima', 10)
        self._maximo_controle_amplitude_2 = kwargs.get('A2 máxima', 1)

        self._passo_controle_periodo = kwargs.get('Escala período', 10)
        self._passo_controle_y_1 = kwargs.get('Escala Y1', 1)
        self._passo_controle_y_2 = kwargs.get('Escala Y2', 0.1)
        self._passo_controle_amplitude_1 = kwargs.get('Escala A1', 1)
        self._passo_controle_amplitude_2 = kwargs.get('Escala A2', 0.1)

        self._controles_deslizantes()

    @staticmethod
    def _cria_controle_deslizante(area=None, titulo: str = '', minimo: float = 0.0,
                                  maximo: float = 100.0, passo: float = 1, orientacao: str = 'vertical'):
        return Slider(ax=area, label=titulo, valmin=minimo, valmax=maximo,
                      valinit=(maximo - minimo) / 2, valstep=passo, orientation=orientacao)

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
            (self.controle_deslizante_amplitude_1.val + self.controle_deslizante_amplitude_2.val) / 2,
            self.controle_deslizante_y_1.val + self.controle_deslizante_y_2.val +
            (self.controle_deslizante_amplitude_1.val + self.controle_deslizante_amplitude_2.val) / 2)

        self.line.set_data(self.time_data, self.sensor_data)
        self.ax.grid(True)
        self.ax.set_ylabel(self.nome_variavel)
        return self.line,

    def _controles_deslizantes(self):
        self.controle_deslizante_periodo = \
            self._cria_controle_deslizante(self.__AX_CONTROLE_PERIODO,
                                           titulo='Período (s)',
                                           minimo=self._minimo_controle_periodo,
                                           maximo=self._maximo_controle_periodo,
                                           passo=self._passo_controle_periodo,
                                           orientacao='horizontal')

        self.controle_deslizante_y_1 = \
            self._cria_controle_deslizante(self.__AX_CONTROLE_Y1,
                                           titulo='Y1',
                                           minimo=self._minimo_controle_y_1,
                                           maximo=self._maximo_controle_y_1,
                                           passo=self._passo_controle_y_1)

        self.controle_deslizante_y_2 = \
            self._cria_controle_deslizante(self.__AX_CONTROLE_Y2,
                                           titulo='Y2',
                                           minimo=self._minimo_controle_y_2,
                                           maximo=self._maximo_controle_y_2,
                                           passo=self._passo_controle_y_2)

        self.controle_deslizante_amplitude_1 = \
            self._cria_controle_deslizante(self.__AX_CONTROLE_AMPLITUDE1,
                                           titulo='A1',
                                           minimo=self._minimo_controle_amplitude_1,
                                           maximo=self._maximo_controle_amplitude_1,
                                           passo=self._passo_controle_amplitude_1)

        self.controle_deslizante_amplitude_2 \
            = self._cria_controle_deslizante(self.__AX_CONTROLE_AMPLITUDE2,
                                             titulo='A2',
                                             minimo=self._minimo_controle_amplitude_2,
                                             maximo=self._maximo_controle_amplitude_2,
                                             passo=self._passo_controle_amplitude_2)

    def iniciar_visualizacao(self):
        ani = animation.FuncAnimation(fig=self.fig, func=self.update,
                                      frames=self.variavel, interval=1000,
                                      blit=True)

        plt.show()
