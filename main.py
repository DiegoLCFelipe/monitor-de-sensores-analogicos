import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from matplotlib.lines import Line2D

from Sensores import NTC


class Scope:
    def __init__(self, variavel):
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

        self.ax.set_xlim(self.time_data[-1] - self.periodo_slider.val, self.time_data[-1])

        self.ax.set_ylim(self.y1_slider.val + self.y2_slider.val - (self.amplitude1_slider.val + self.amplitude2_slider.val),
                         self.y1_slider.val + self.y2_slider.val + (self.amplitude1_slider.val + self.amplitude2_slider.val))

        self.line.set_data(self.time_data, self.sensor_data)
        self.ax.grid(True)
        self.ax.set_ylabel('°C')

        return self.line,

    def iniciar_visualizacao(self):
        ax_periodo = plt.axes([0.4, 0.1, 0.45, 0.03])
        self.periodo_slider = Slider(ax=ax_periodo,label="Período (s)",valmin=1,valmax=600,valinit=1,valstep=1)

        ax_y1 = plt.axes([0.05, 0.25, 0.0225, 0.63])
        self.y1_slider = Slider(
            ax=ax_y1,
            label="Y1",
            valmin=0,
            valmax=125,
            valinit=26,
            orientation="vertical",
            valstep=1
        )

        ax_y2 = plt.axes([0.10, 0.25, 0.0225, 0.63])
        self.y2_slider = Slider(
            ax=ax_y2,
            label="Y2",
            valmin=0,
            valmax=0.9,
            valinit=0,
            orientation="vertical",
            valstep=0.1
        )

        ax_amplitude1 = plt.axes([0.15, 0.25, 0.0225, 0.63])
        self.amplitude1_slider = Slider(
            ax=ax_amplitude1,
            label="A1",
            valmin=0,
            valmax=10,
            valinit=1,
            orientation="vertical",
            valstep=1
        )

        ax_amplitude2 = plt.axes([0.2, 0.25, 0.0225, 0.63])
        self.amplitude2_slider = Slider(ax=ax_amplitude2,
            label="A2",
            valmin=0,
            valmax=1,
            valinit=0.1,
            orientation="vertical",
            valstep=0.1
        )

        ani = animation.FuncAnimation(fig=self.fig, func=scope.update,
                                      frames=self.variavel, interval=1000,
                                      blit=True)
        plt.style.context('dark_background')
        plt.show()


termistor = NTC()
scope = Scope(termistor)
scope.iniciar_visualizacao()
