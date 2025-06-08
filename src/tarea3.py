import numpy as np
import matplotlib.pyplot as plt

def senal_parametros(amp, fhz, fase):
    rAmp = 1
    rfrec = 1        #referencia
    rtiempo = np.linspace(-1, 5, 1000)
    rfase = 0
    rts = 0.01
    rn = np.arange(-1, 5, rts)
    rxc = rAmp * np.sin(2 * np.pi * rfrec * rtiempo + rfase)
    rxd = rAmp * np.sin(2 * np.pi * rfrec * rn + rfase)
    Amp = float(amp)
    frec = float(fhz)
    tiempo = np.linspace(-1, 5, 1000)  #modificable
    fase = float(fase)
    ts = 0.01
    n = np.arange(-1, 5, ts)
    xc = Amp * np.sin(2 * np.pi * frec * tiempo + fase)
    xd = Amp * np.sin(2 * np.pi * frec * n + fase)


    plt.figure(figsize=(10, 10))
    plt.suptitle(f'Referencia:   A=F=1         Phi=0\n' +
                 f'Modificada:   A={amp} F={fhz} Phi={fase} rad')

    plt.subplot(3, 1, 1)#grafica1
    plt.plot(rtiempo, rxc, 'b--')
    plt.plot(tiempo, xc, 'r')
    plt.title('Señales continuas')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.subplot(3, 1, 2)#grafica2
    plt.stem(rn, rxd, linefmt='c--', markerfmt='bo', basefmt='b--')
    plt.stem(n, xd, linefmt='m-', markerfmt='ro', basefmt='r-')
    plt.title('Señales discretas')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.subplot(3, 1, 3)#grafica3
    plt.plot(rtiempo, rxc, 'b--')
    plt.stem(rn, rxd, linefmt='c--', markerfmt='bo', basefmt='b--')
    plt.plot(tiempo, xc, 'r')
    plt.stem(n, xd, linefmt='m-', markerfmt='ro', basefmt='r-')
    plt.title('Sobreposicion')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
