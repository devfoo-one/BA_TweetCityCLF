import pickle
import matplotlib.pyplot as plt
from playground.graphs.colors import Colors
c = Colors()

count_chars = pickle.load(open('../count_chars.pickle', 'rb'))

chars = [x[0] for x in count_chars.items()]
counts = [x[1] for x in count_chars.items()]

plt.rcParams['font.size'] = 18.0
plt.bar(chars, counts, color=c.qualitative[0], width=0.6)
plt.gca().set_ylabel("Anzahl der Tweets")
plt.gca().set_xlabel("Zeichen pro Tweet")
# plt.gca().set_yscale('log')

plt.savefig('fullDS_filteredDE_charCount.png', bbox_inches='tight', dpi=600)
plt.show()
