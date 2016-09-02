import pickle
import matplotlib.pyplot as plt
from playground.graphs.colors import Colors
c = Colors()

tweet_histo = {}
count_users = pickle.load(open('../user_ids_de_filtered.pickle', 'rb'))
print(len(count_users))
for userid, count in count_users.items():
    if count not in tweet_histo.keys():
        tweet_histo[count] = 0
    tweet_histo[count] += 1

# items = [x[0] for x in tweet_histo.items()]
# counts = [x[1] for x in tweet_histo.items()]

count_sum = 0
users = 0
print(tweet_histo.items())
for number, count in tweet_histo.items():
    count_sum += number * count
    users += count

print(count_sum, users)


# plt.rcParams['font.size'] = 18.0
# plt.bar(items, counts, color=c.qualitative[0])
# plt.gca().set_ylabel("Häufigkeit")
# plt.gca().set_xlabel('Tweets pro User')
# plt.gca().set_yscale('log')
# #
# # # plt.savefig('fullDS_filteredDE_charCount.png', bbox_inches='tight', dpi=600)
# # # plt.savefig('fullDS_filteredDE_UserLocation_wordCount.png', bbox_inches='tight', dpi=600)
# # plt.savefig('fullDS_filteredDE_UserLocation_charCount.png', bbox_inches='tight', dpi=600)
# plt.show()
