import matplotlib.pyplot as plt

def continuous_plotter(x, y, title=""):
    plt.figure()
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")

def discrete_plotter(x, y, title="", stem=False):
    plt.figure()
    if stem:
        plt.stem(x, y, use_line_collection=True)
    else:
        plt.plot(x, y)
    plt.title(title)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
