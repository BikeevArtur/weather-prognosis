import json
import matplotlib.pyplot as plt
import numpy as np


def temperature_graphics(dictionery):
    l = []
    for d in dictionery['list']:
        l.append(d["main"]['temp'])
    k = np.arange(0, len(l), 1)
    plt.plot(k, l, "b:")
    plt.title('График температуры', fontweight='normal', color='r', fontsize=20)
    plt.xlabel('Час', fontweight='normal', fontsize=14)
    plt.ylabel('Температура', fontweight='normal', fontsize=14)
    plt.show()


s = ''
corpus = 'json_dictionery'
with open(corpus, 'r',  encoding="utf-8") as fout:
    for line in fout:
        s = line

dictionery = json.loads(s)
temperature_graphics(dictionery)
