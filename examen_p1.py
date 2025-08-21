import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import continuous_plotter, discrete_plotter

def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        suma = 0
        for n in range(N):
            suma += x[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(suma)
    return np.array(X)

def run():
    fm = 0.5
    fc = 8
    m = 0.5
    fs = 64
    T = 4
    t = np.arange(0, T, 1/fs)

    x_t = (1 + m*np.cos(2*np.pi*fm*t)) * np.sin(2*np.pi*fc*t)

    X = dft(x_t)
    N = len(X)
    freqs = np.arange(0, fs, fs/N)
    mag = np.abs(X) / N

    continuous_plotter(t, x_t, "Señal en el tiempo")
    discrete_plotter(freqs, mag, "Espectro (DFT)", stem=True)

    plt.show()
