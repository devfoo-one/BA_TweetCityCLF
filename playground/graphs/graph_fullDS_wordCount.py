import pickle
import matplotlib.pyplot as plt
from playground.graphs.colors import Colors
c = Colors()

count_tokens = pickle.load(open('../count_tokens.pickle', 'rb'))

tokens = [x[0] for x in count_tokens.items()]
counts = [x[1] for x in count_tokens.items()]

plt.rcParams['font.size'] = 18.0
plt.bar(tokens, counts, color=c.qualitative[0], width=0.6)
plt.gca().set_ylabel("Anzahl der Tweets")
plt.gca().set_xlabel("Wörter pro Tweet")
plt.savefig('fullDS_filteredDE_wordCount.png', bbox_inches='tight', dpi=300)
plt.show()
