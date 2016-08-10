# Zahlen für die Location Types des kompletten Datensatzes
# 7631 nur geo und 1620 keine Angabe wurden weggelassen
"""
total: 14240111 sum counter: 14240111
geo_place_!coord = 0
geo_!place_!coord = 0
geo_place_coord = 2379056
!geo_!place_coord = 0
!geo_!place_!coord = 1620
!geo_place_!coord = 11851804
geo_!place_coord = 7631
!geo_place_coord = 0
"""

import matplotlib.pyplot as plt
from playground.graphs.colors import Colors
c = Colors()

labels = ['place','geo+place+coordinates']
sizes = [11851804, 2379056]
colors = c.qualitative
plt.rcParams['font.size'] = 18.0
plt.pie(sizes, labels=labels, startangle=90, counterclock=False, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
