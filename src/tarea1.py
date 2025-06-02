import numpy as np
from scipy import signal
from src.utils.grapher import plot_signal_subplot

def generar_senales():
    f = 2
    t = np.linspace(-1, 7, 1000)
    Ts = 0.05
    tn = np.arange(-1, 7, Ts)

    x1_cont = np.sin(2 * np.pi * f * t)
    x1_disc = np.sin(2 * np.pi * f * tn)

    u = np.heaviside(t, 1)
    x2_cont = np.exp(-2 * t) * u
    u_disc = np.heaviside(tn, 1)
    x2_disc = np.exp(-2 * tn) * u_disc

    x3_cont = signal.sawtooth(2 * np.pi * f * t, width=0.5)
    x3_disc = signal.sawtooth(2 * np.pi * f * tn, width=0.5)

    x4_cont = signal.square(2 * np.pi * f * t)
    x4_disc = signal.square(2 * np.pi * f * tn)

    plot_signal_subplot(t, tn, x1_cont, x1_disc, 'Sinusoidal')
    plot_signal_subplot(t, tn, x2_cont, x2_disc, 'Exponencial')
    plot_signal_subplot(t, tn, x3_cont, x3_disc, 'Triangular')
    plot_signal_subplot(t, tn, x4_cont, x4_disc, 'Cuadrada)')
