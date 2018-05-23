import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict


def temperature_graphics(dictionery):
    temperature = []
    for d in dictionery['list']:
        temperature.append(d["main"]['temp'])
    k = np.arange(0, len(temperature), 1)
    plt.plot(k, temperature, "b:")
    plt.title('График температуры', fontweight='normal', color='r', fontsize=20)
    plt.xlabel('Час', fontweight='normal', fontsize=14)
    plt.ylabel('Температура', fontweight='normal', fontsize=14)
    plt.show()



def pie_chart(dictionery):
    weather = defaultdict(lambda: 0)
    for d in dictionery["list"]:
        weather[d["weather"][0]["description"]] += 1
    k = []
    l = []
    for w in weather:
        l.append(w)
        k.append(weather[w])
    plt.title('Распространенность типа погоды', fontweight='normal', color='r', fontsize=20)
    plt.pie(k, autopct='%.1f', radius=1.0, explode=[0.2] + [0 for _ in range(len(l) - 1)])
    plt.legend(bbox_to_anchor=(-0.16, 0.45, 0.25, 0.25), loc='lower left', labels=l)
    plt.show()


s = ''
corpus = 'json_dictionery'
with open(corpus, 'r',  encoding="utf-8") as fout:
    for line in fout:
        s = line

dictionery = json.loads(s)
temperature_graphics(dictionery)
pie_chart(dictionery)
