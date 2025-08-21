
# Análisis de Señales con DFT (Implementación propia)

OBJ
- Generar una señal discreta y agregarle ruido senoidal de una frecuencia específica.
- Analizar el espectro con la **Transformada de Fourier Discreta (DFT)** implementada desde cero (sin `numpy.fft`).
- Identificar picos de la señal en presencia de ruido y estimar la resolución espectral \(\Delta f = f_s/N\).

# ParámetroS
- Frecuencia de muestreo: `f_s = 256 Hz`
- Duración: `6 s` → `N = 1536` muestras
- Frecuencias: `f1 = 8 Hz`, `f2 = 20 Hz`
- Ruido senoidal: por defecto `fn = 50 Hz` (ajustable con `--fn`).


.
├── main.py
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   └── examen_p2.py
└── utils/
    └── grapher.py
```

## Ejecución desde consola
Ejemplo tal como se pide (el argumento `examen_p2` es aceptado pero opcional):
```bash
python main.py examen_p2
```
También puedes ajustar parámetros:
```bash
python main.py --fs 256 --duration 6 --f1 8 --f2 20 --fn 50
```


- La DFT está implementada manualmente en `src/examen_p2.py`.
- Se grafican la señal original y con ruido, junto con sus respectivos espectros.
- En consola se imprime la resolución espectral y las frecuencias pico detectadas (top 5).
