"""Printing module
"""
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

DATE_FORMAT = "%Y-%m-%d"

def user_to_name(argument):
    """Switch functionality
    """
    switcher = {
        "lopezobrador_": "A. López Obrador",
        "RicardoAnayaC": "R. Anaya Cortés",
        "luisederbez": "L. Dervez Bautista",
        "RafaMorenoValle": "R. Moreno Valle",
        "JCRomeroHicks": "J. Romero Hicks",
        "eruviel_avila": "E. Ávila Villegas",
        "MFBeltrones": "M. Beltrones Rivera",
        "JoseAMeadeK": "J. Meade Kuribreña",
        "aurelionuno": "A. Nuño Mayer",
        "IvonneOP": "I. Ortega Pacheco",
        "osoriochong": "M. Osorio Chong",
        "LVidegaray": "L. Videgaray Caso",
        "Silvano_A": "S. Aureoles Conejo",
        "ManceraMiguelMX": "M. Mancera Espinosa",
        "Mzavalagc": "M. Zavala Gómez",
        "RiosPiterJaguar": "A. Ríos Piter",
        "JaimeRdzNL": "J. Rodríguez 'El Bronco'",
        "PedroFerriz": "P. Ferriz de Con"
    }
    return switcher.get(argument, "nothing")

def print_popularity(candidates_list, party=None):
    """Plots candidates popularity
    """

    """
    candidates_list = {
        "A":[("2017-10-01",10),("2017-10-02",12)],
        "B":[("2017-10-01",8),("2017-10-02",15)]
    }
    """

    plt.clf()
    plt.xlabel("Days")
    plt.ylabel("Popularity")
    if party != None:
        plt.title("Last 11 days (" + party + ")")
    else:
        plt.title("Last 11 days")
    plt.grid(True)

    cmap = plt.get_cmap('jet')
    colors = cmap(np.linspace(0, 1.0, len(candidates_list.items())))

    for i, (candidate, items_list) in enumerate(candidates_list.items()):
        y = []
        dates = []
        print(candidate)
        for date, value in items_list:
            dates.append(date)
            y.append(value)
        x = [dt.datetime.strptime(d, DATE_FORMAT).date() for d in dates]
        print(x)
        print(y)

        to_sort = zip(x, y)
        z = sorted(to_sort, key=lambda x: x[0])
        x, y = zip(*z)

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(DATE_FORMAT))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.plot(x, y, label=user_to_name(candidate), color=colors[i])
        plt.gcf().autofmt_xdate()
        #plt.plot_date(x, y, fmt=DATE_FORMAT, xdate=True, label=str(candidate))
    plt.legend()
    plt.show()

def pretty_print(data):
    """Pretty print interface.
    """
    import pprint
    pretty_printer = pprint.PrettyPrinter(indent=4)
    pretty_printer.pprint(data)

def main():
    """Main function
    """
    #print_popularity(None)

if __name__ == '__main__':
    main()
