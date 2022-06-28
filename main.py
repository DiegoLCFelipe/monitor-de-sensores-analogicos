import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from Sensores import NTC

x = []
y = []


def valor_slider(slider, val=3):
    fig.canvas.draw_idle()
    return slider.val


def plota_temperatura(i, x, y):
    leitura = next(termistor)
    x.append(leitura[0])
    y.append(leitura[1])

    x = x[-valor_slider(slider_de_amostras):]
    y = y[-valor_slider(slider_de_amostras):]

    ax.cla()
    ax.plot(x, y)

    ax.set_title('Registro de Temperatura TNC 103')
    ax.set_ylabel('Temperatura °C')


termistor = NTC()

fig, ax = plt.subplots(figsize=(12, 8))
ax_slider_n = plt.axes([0.15, 0.1, 0.75, 0.03])

slider_de_amostras = Slider(ax=ax_slider_n, label='N',
                            valmin=0, valmax=30, valinit=3, valstep=1)
ax.xaxis.set_tick_params(rotation=45)

ani = animation.FuncAnimation(fig, plota_temperatura, fargs=(x, y), interval=1000)
fig.subplots_adjust(bottom=0.25, left=0.15)
plt.show()
