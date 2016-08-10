# Zahlen language codes des kompletten Datensatzes (TOP 4)
#


import matplotlib.pyplot as plt
from playground.graphs.colors import Colors

c = Colors()

data = [
    ('de', 3730991),
    ('en', 3169944),
    ('fr', 2413405),
    ('und', 1308943),
    ('nl', 1111669),
    ('tr', 398758),
    ('es', 349800),
    ('pl', 304292),
    ('ar', 224088),
    ('cs', 167118),
    ('ru', 157981),
    ('pt', 128301),
    ('ja', 118874),
    ('in', 106315),
    ('it', 92376),
    ('tl', 74254),
    ('da', 43100),
    ('et', 30720),
    ('ht', 28658),
    ('sv', 28075),
    ('no', 26046),
    ('fa', 21421),
    ('sk', 19808),
    ('th', 17879),
    ('ro', 15454),
    ('fi', 14243),
    ('hu', 11960),
    ('sl', 11502),
    ('lv', 9768),
    ('hi', 8950),
    ('ko', 8654),
    ('lt', 8549),
    ('bs', 8063),
    ('uk', 7632),
    ('el', 7623),
    ('cy', 6946),
    ('is', 5939),
    ('bg', 5573),
    ('eu', 5023),
    ('zh', 4746),
    ('hr', 4015),
    ('iw', 3109),
    ('sr', 2511),
    ('ur', 2439),
    ('vi', 2254),
    ('ne', 1313),
    ('ta', 635),
    ('ps', 254),
    ('ml', 208),
    ('ckb', 203),
    ('bn', 135),
    ('si', 99),
    ('ka', 93),
    ('hy', 70),
    ('mr', 30),
    ('kn', 11),
    ('am', 9),
    ('pa', 5),
    ('lo', 3),
    ('or', 3),
    ('sd', 2),
    ('ug', 2),
    ('iu', 2),
    ('gu', 2),
    ('chr', 2),
    ('km', 2),
    ('te', 1),
    ('bo', 1)
]

print(data)
sizes = [x[1] for x in data[0:3]]
sizes.append(sum([x[1] for x in data[3:]]))
print(sizes)
labels = [x[0] for x in data[0:3]]
labels.append('andere')
print(labels)
colors = c.qualitative
explode = [0.1,0,0,0]
plt.rcParams['font.size'] = 18.0
plt.pie(sizes, labels=labels, startangle=90, counterclock=False, explode=explode, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
