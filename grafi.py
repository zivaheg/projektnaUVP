import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#def float_v_int(stolpec: int):
#    """spremeni vrsto stolpca iz tabele """
#    v_stevilkah = pd.to_numeric(podana_zivljenska_doba[f"{stolpec}"], downcast='signed')
#    return v_stevilkah


def komet_graf_za_informiranost(a, b):
    plt.style.use('_mpl-gallery-nogrid')
    
    x = a
    y = b

    # plot:
    fig, ax = plt.subplots()
    ax.hist2d(x, y, bins=(np.arange(-1400, 2200, 20), np.arange(-1400, 2200, 20)))
    ax.set(xlim=(1600, 2050), ylim=(1700, 2050))
    return plt.show()



#x = pd.to_numeric(podana_zivljenska_doba["Rojstvo"], downcast='signed')
#y = pd.to_numeric(podana_zivljenska_doba["Smrt"], downcast='signed')
    #x = float_v_int(a)
    #y = float_v_int(b)

#def kometu_podobn_graf(a, b, x_od, x_do, y_od, y_do):
    # plt.style.use('_mpl-gallery-nogrid')
    
    # x = a
    # y = b

    # # plot:
    # fig, ax = plt.subplots()
    # ax.hist2d(x, y, bins=(np.arange(-1400, 2200, 20), np.arange(-1400, 2200, 20)))
    # ax.set(xlim=(f"{x_od}", f"{x_do}"), ylim=(1700, 2050))
    # return plt.show()