import json
import matplotlib.pyplot as plt
import numpy as np


s = ''
corpus = 'json_dictionery'
with open(corpus, 'r',  encoding="utf-8") as fout:
    for line in fout:
        s = line

dictionery = json.loads(s)
l = []
for d in dictionery['list']:
    l.append(d["main"]['temp'])
k = np.arange(0, len(l), 1)
plt.plot(k, l, "b:")
plt.show()