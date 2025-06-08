import numpy as np
from src.utils.grapher import plot_signal_subplot

def frec_senal(fhz):
    Amp = 1
    frec = float(fhz)
    tiempo = np.linspace(-1, 5, 1000)
    xc = Amp * np.sin(2 * np.pi * frec * tiempo)
    ts = 0.01
    tn = np.arange(-1, 5, ts)
    xd = Amp * np.sin(2 * np.pi * frec * tn)
    print(fhz)
    print('Hz')
    plot_signal_subplot(tiempo, tn, xc, xd, f' Frecuencia {frec} Hz')
    
