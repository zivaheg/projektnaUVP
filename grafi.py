import matplotlib.pyplot as plt
import numpy as np



def komet_graf_za_informiranost(a, b):
    """Graf za informiranost z že določenimi parametri"""
    x = a
    y = b

    fig, ax = plt.subplots()
    
    ax.hist2d(x, y, bins=(np.arange(-1400, 2200, 20), np.arange(-1400, 2200, 20)))
    ax.set(xlim=(1600, 2050), ylim=(1700, 2050))

    fig.suptitle("Količina podatkov rojstva in smrti") 
    ax.set_xlabel("Letnice rojstva")
    ax.set_ylabel("Letnice smrti")
    return plt.show()

