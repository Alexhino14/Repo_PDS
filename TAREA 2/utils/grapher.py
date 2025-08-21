
import numpy as np
import matplotlib.pyplot as plt

def continuous_plotter(t, x, title):
    plt.figure()
    plt.plot(t, x)
    plt.title(title)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.tight_layout()

def discrete_plotter(X, fs, title):
    N = len(X)
    # LADO POSITIVO (frecuencias reales 0..fs)
    freqs = np.arange(N) * fs / N
    magnitudes = np.abs(X)
    plt.figure()
    markerline, stemlines, baseline = plt.stem(freqs, magnitudes, basefmt=" ")
    plt.title(title)
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud')
    plt.grid(True)
    plt.xlim(0, fs/2)  
    plt.tight_layout()
