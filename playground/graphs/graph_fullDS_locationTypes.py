# Zahlen für die Location Types des kompletten Datensatzes
# 7631 nur geo und 1620 keine Angabe wurden weggelassen


import matplotlib.pyplot as plt
from playground.graphs.colors import Colors
c = Colors()

labels = ['place','geo+place']
sizes = [11851804, 2379056]
colors = c.qualitative
plt.pie(sizes, labels=labels, startangle=90, counterclock=False, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
