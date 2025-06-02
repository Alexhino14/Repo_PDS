import matplotlib.pyplot as plt

def plot_signal_subplot(t_cont, t_disc, x_cont, x_disc, title):
    plt.figure(figsize=(8, 8))
    plt.suptitle(title)

    #continua
    plt.subplot(3, 1, 1)
    plt.plot(t_cont, x_cont, 'r')
    plt.title('Continua')
    plt.ylabel('Amplitud')
    plt.grid(True)

    #discreta
    plt.subplot(3, 1, 2)
    plt.stem(t_disc, x_disc, linefmt='b-', markerfmt='go', basefmt='k-')
    plt.title('Discreta')
    plt.ylabel('Amplitud')
    plt.grid(True)

    #sobreponer
    plt.subplot(3, 1, 3)
    plt.plot(t_cont, x_cont, 'r', label='Continua')
    plt.stem(t_disc, x_disc, linefmt='b-', markerfmt='go', basefmt='k-', label='Discreta')
    plt.title('Ambas')
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(True)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
