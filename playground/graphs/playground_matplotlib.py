# Spielwiese für matplotlib
# TODO: Balkenbeschriftungen


import numpy as np
import matplotlib.pyplot as plt
from playground.graphs.colors import Colors

c = Colors()


labels = ['place','geo+place']
sizes = [11851804, 2379056]
colors = c.qualitative
plt.pie(sizes, labels=labels, startangle=90, colors=colors, autopct='%1.1f%%')
# n = len(data)
# X = np.arange(n)
# plt.bar(data, X)
plt.axis('equal')
plt.show()
