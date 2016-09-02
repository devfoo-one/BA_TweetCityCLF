import numpy as np
import matplotlib.pyplot as plt
from playground.graphs.colors import Colors

c = Colors()

data = [  # label, macro, weighted
    ('E 2', 0.034, 0.262),
    ('E 3.1', 0.015, 0.220),
    ('E 3.2', 0.027, 0.239),
    ('E 3.3', 0.028, 0.240),
    ('E 3.4', 0.015, 0.215),
    ('E 4', 0.031, 0.260),
    ('E 5.1', 0.143, 0.326),
    ('E 5.2', 0.141, 0.323),
    ('E 6.1', 0.023, 0.261),
    ('E 6.2', 0.024, 0.268),
    ('E 7.1', 0.141, 0.318),
    ('E 7.2', 0.097, 0.305),
    ('E 7.3', 0.100, 0.306),
    ('E 7.4', 0.089, 0.300),
    ('E 8', 0.294, 0.573),
]

labels = [x[0] for x in data]
macro_scores = [x[1] for x in data]
weighted_scores = [x[2] for x in data]

bar_width = 0.35
index = np.arange(len(data))
size = macro_scores

fig, ax = plt.subplots()
rects1 = ax.bar(index, macro_scores, bar_width, color=c.qualitative[1])
rects2 = ax.bar(index+bar_width, weighted_scores, bar_width, color=c.qualitative[0])

ax.set_ylabel('F1-Maß')
ax.set_xlabel('Experiment')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(labels)
ax.yaxis.grid(True)

ax.legend((rects1[0], rects2[0]), ('macro', 'weighted'), loc='best')

plt.rcParams['font.size'] = 18.0
plt.show()