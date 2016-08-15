"""
city 11867110
country 1343691
admin 652058
neighborhood 361192
poi 6809
NOPLACE:  9251

"""
import matplotlib.pyplot as plt
from playground.graphs.colors import Colors
c = Colors()

labels = ['city','country', 'andere']
sizes = [11867110, 1343691, 652058 + 361192 + 6809]
colors = c.qualitative
plt.rcParams['font.size'] = 18.0
plt.pie(sizes, labels=labels, startangle=0, counterclock=False, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
