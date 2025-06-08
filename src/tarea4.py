import numpy as np
import matplotlib.pyplot as plt

def convertidor_da(bits):
    voltaje = 5.0
    n = int(bits)
    niveles = 2 ** n
    paso = voltaje / (niveles - 1)
    resolucionpor = (paso / voltaje) * 100

    datos = (f'Bits: {n}, Niveles: {niveles-1},\n '
                   f'Tamaño de paso: {paso:.4f} Volt/escalon,\n '
                   f'Resolucion: {resolucionpor:.4f} %, '
                   f'Voltaje escala completa: {voltaje} V')

    digin = np.arange(niveles)
    anaout = digin * paso

    plt.figure(figsize=(8, 6))
    plt.suptitle(f'Convertidor Digital-Analogico de {n} bits')

    plt.step(digin, anaout, where='post', color='b', label=datos)
    plt.xlabel('Nivel')
    plt.ylabel('Voltage')
    plt.grid()
    plt.ylim(-0.5, voltaje + 0.5)
    plt.xlim(-1, niveles + 1)
    plt.legend(loc='upper left', fontsize='small', framealpha=0.7)
    plt.show()
