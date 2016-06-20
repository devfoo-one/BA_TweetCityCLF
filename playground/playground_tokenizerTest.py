import pickle
from sklearn.feature_extraction.text import CountVectorizer

"""load persistent dataset"""
with open('../dataset.pickle', 'rb') as f:
    dataset = pickle.load(f)

tweets = []
for i in [603546, 3199841, 3280242]:
    tweets.append(dataset.data[i]['text'])

count_vect = CountVectorizer()
tdm = count_vect.fit_transform(tweets)

for i in range(0, len(tweets)):
    print('"',tweets[i],'" got transformed into...')
    for featureID, count in enumerate(tdm.getrow(i).toarray()[0]): # .toarray()[0] to transform sparse matrix into list
        if count != 0:
            print(count_vect.get_feature_names()[featureID], '(', count, '), ',sep='', end='')
    print('\n-----')

