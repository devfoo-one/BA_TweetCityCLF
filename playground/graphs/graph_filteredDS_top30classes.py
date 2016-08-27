import numpy as np
import matplotlib.pyplot as plt
from playground.graphs.colors import Colors

c = Colors()

data = [
    ('Berlin', 456701),
    ('Hamburg', 181355),
    ('Frankfurt am Main', 165753),
    ('Köln', 122504),
    ('München', 99697),
    ('Düsseldorf', 90395),
    ('Potsdam', 70149),
    ('Stuttgart', 52548),
    ('Leipzig', 48258),
    ('Hannover', 45051),
    ('Dortmund', 44813),
    ('Bonn', 39449),
    ('Bremen', 23577),
    ('Duisburg', 21555),
    ('Dresden', 21066),
    ('Essen', 20900),
    ('Wiesbaden', 20534),
    ('Nürnberg', 17660),
    ('Göttingen', 17424),
    ('Bielefeld', 16912),
    ('Aachen', 16833),
    ('Mainz', 16575),
    ('Karlsruhe', 15328),
    ('Bochum', 15261),
    ('Karlsdorf-Neuthard', 13893),
    ('Münster', 13853),
    ('Koblenz', 13133),
    ('Fürth', 12209),
    ('Magdeburg', 12161),
    ('Tübingen', 11892),
    # ('Mannheim', 11886),
    # ('Braunschweig', 11351),
    # ('Bremerhaven', 10954),
    # ('Erlangen', 10806),
    # ('Darmstadt', 10756),
    # ('Oldenburg (Oldenburg)', 10508),
    # ('Erfurt', 9916),
    # ('Saarbrücken', 9821),
    # ('Rostock', 9471),
    # ('Wuppertal', 9042),
    # ('Würzburg', 8902),
    # ('Halle (Saale)', 8856),
    # ('Neuss', 8793),
    # ('Kiel', 7990),
    # ('Schifferstadt', 7534),
    # ('Augsburg', 7372),
    # ('Leipzig', 7203),
    # ('Regensburg', 7187),
    # ('Freiburg im Breisgau', 7122)
]

labels = [x[0] for x in data]
index = np.arange(len(data))
size = [(x[1] / 31050.76) for x in data]

plt.bar(index, size, color=c.qualitative[0])
plt.gca().set_ylabel("Anteil in %")
plt.gca().set_xlabel("Position")
plt.gca().set_ylim([0, 20])
plt.axes().set_aspect(0.65, 'box')

for i, label in enumerate(labels):
    plt.text(index[i] + 0.5, size[i] + 0.5, label, {'ha': 'center', 'va': 'bottom'}, rotation=90)
    # plt.annotate(s=label, xy=(index[i], size[i]))
plt.savefig('filteredDS_top30classes.png', bbox_inches='tight', dpi=600)
plt.show()
