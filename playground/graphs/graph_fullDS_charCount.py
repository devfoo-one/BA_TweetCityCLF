import pickle
import matplotlib.pyplot as plt
from playground.graphs.colors import Colors
c = Colors()

# count_items = pickle.load(open('../count_chars.pickle', 'rb'))
# count_items = pickle.load(open('../userLocation_count_tokens.pickle', 'rb'))
count_items = pickle.load(open('../userLocation_count_chars.pickle', 'rb'))

items = [x[0] for x in count_items.items()]
counts = [x[1] for x in count_items.items()]

plt.rcParams['font.size'] = 18.0
plt.bar(items, counts, color=c.qualitative[0], width=0.6)
plt.gca().set_ylabel("Häufigkeit")
# plt.gca().set_xlabel('Wörter pro "location" Attribut des User-Objekts')
plt.gca().set_xlabel('Zeichen pro "location" Attribut des User-Objekts')
# plt.gca().set_xlabel("Zeichen pro Tweet")
# plt.gca().set_yscale('log')

# plt.savefig('fullDS_filteredDE_charCount.png', bbox_inches='tight', dpi=600)
# plt.savefig('fullDS_filteredDE_UserLocation_wordCount.png', bbox_inches='tight', dpi=600)
plt.savefig('fullDS_filteredDE_UserLocation_charCount.png', bbox_inches='tight', dpi=600)
plt.show()
