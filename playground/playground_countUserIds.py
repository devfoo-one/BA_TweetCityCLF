import html.parser
import json
import pickle

user_counts = {}
n = 0
with open('../../data/Germany_filtered_shuffled.json', 'r', encoding='utf-8') as dataset:
    for line in dataset:
        n += 1
        try:
            tweet = json.loads(line)
        except ValueError:
            continue

        user_id = tweet['user']['id']
        if user_id not in user_counts.keys():
            user_counts[user_id] = 0
        user_counts[user_id] += 1

        if n % 10000 == 0:
            print('n={}, unique user ids={}'.format(n, len(user_counts)))

print('n={}, unique user ids={}'.format(n, len(user_counts)))

with open('user_ids_de_filtered.pickle', mode='wb') as user_counts_f:
    pickle.dump(user_counts, user_counts_f)
