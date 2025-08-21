
import argparse
import sys
from src.examen_p2 import (
    dft, generate_signal, add_sinusoidal_noise,
    spectral_resolution, top_k_peak_frequencies
)
from utils.grapher import continuous_plotter, discrete_plotter

def parse_args():
    p = argparse.ArgumentParser(description="DFT manual de una señal con y sin ruido.")
    p.add_argument('task', nargs='?', default='examen_p2',
                   help="Argumento dummy para compatibilidad: use 'examen_p2'.")  # compatibilidad con enunciado
    p.add_argument('--fs', type=int, default=256, help='Frecuencia de muestreo [Hz]')
    p.add_argument('--duration', type=float, default=6.0, help='Duración [s]')
    p.add_argument('--f1', type=float, default=8.0, help='Frecuencia seno 1 [Hz]')
    p.add_argument('--f2', type=float, default=20.0, help='Frecuencia seno 2 [Hz]')
    p.add_argument('--fn', type=float, default=50.0, help='Frecuencia del ruido senoidal [Hz]')
    p.add_argument('--noise_amp', type=float, default=0.3, help='Amplitud del ruido senoidal')
    p.add_argument('--no_show', action='store_true', help='No mostrar gráficos (solo cálculos/prints).')
    return p.parse_args()

def main():
    args = parse_args()

    # Señal base
    t, x = generate_signal(fs=args.fs, duration=args.duration, f1=args.f1, f2=args.f2)
    X = dft(x)

    # Señal con ruido
    xr = add_sinusoidal_noise(x, fs=args.fs, fn=args.fn, amplitude=args.noise_amp)
    Xr = dft(xr)

    # Impresiones de apoyo
    N = len(x)
    df = spectral_resolution(args.fs, N)
    print(f"N = {N} muestras, fs = {args.fs} Hz, resolución espectral Δf = {df:.6f} Hz")

    print("Picos señal original (Top 5):")
    for f, val in top_k_peak_frequencies(X, args.fs, k=5):
        print(f"  f ≈ {f:7.3f} Hz  |  |X| = {val:.3f}")
    print("\nPicos señal con ruido (Top 5):")
    for f, val in top_k_peak_frequencies(Xr, args.fs, k=5):
        print(f"  f ≈ {f:7.3f} Hz  |  |X| = {val:.3f}")

    if not args.no_show:
        continuous_plotter(t, x, 'Señal Original (dominio del tiempo)')
        discrete_plotter(X, args.fs, 'Espectro DFT - Señal Original')
        continuous_plotter(t, xr, 'Señal con Ruido Senoidal (dominio del tiempo)')
        discrete_plotter(Xr, args.fs, 'Espectro DFT - Señal con Ruido')

        # Mostrar ventanas
        import matplotlib.pyplot as plt
        plt.show()

if __name__ == '__main__':
    main()
