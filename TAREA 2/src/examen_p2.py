
import numpy as np

def dft(x):
    """DFT implementada desde cero (O(N^2)).
    Devuelve el arreglo complejo X[k].
    """
    x = np.asarray(x, dtype=complex)
    N = x.size
    n = np.arange(N)
    X = np.zeros(N, dtype=complex)
    # Implementación doble for clara para cumplir el requisito
    for k in range(N):
        s = 0.0j
        for nn in n:
            s += x[nn] * np.exp(-2j * np.pi * k * nn / N)
        X[k] = s
    return X

def generate_signal(fs=256, duration=6.0, f1=8.0, f2=20.0):
    N = int(fs * duration)
    t = np.arange(N) / fs
    x = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)
    return t, x

def add_sinusoidal_noise(x, fs=256, fn=50.0, amplitude=0.3):
    N = len(x)
    t = np.arange(N) / fs
    noise = amplitude * np.sin(2*np.pi*fn*t)
    return x + noise

def spectral_resolution(fs, N):
    return fs / N

def top_k_peak_frequencies(X, fs, k=5):
    """Devuelve las k frecuencias (en Hz) con mayor magnitud, excluyendo DC duplicados.
    """
    mag = np.abs(X)
    # Considerar solo 0..N/2 (espectro positivo)
    N = len(X)
    half = N // 2 + 1
    mag_half = mag[:half]
    idxs = np.argpartition(mag_half, -k)[-k:]
    idxs = idxs[np.argsort(mag_half[idxs])[::-1]]
    freqs = idxs * fs / N
    values = mag_half[idxs]
    return list(zip(freqs, values))
