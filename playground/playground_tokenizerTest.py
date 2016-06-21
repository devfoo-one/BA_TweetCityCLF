import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

"""load persistent dataset"""
with open('../dataset.pickle', 'rb') as f:
    dataset = pickle.load(f)

tweets = []
for i in [603546, 3199841, 3280242]:
    tweets.append(dataset.data[i]['text'])

print("--- BOW n1----")

count_vect = CountVectorizer()
tdm_bow = count_vect.fit_transform(tweets)
for i in range(0, len(tweets)):
    print('"', tweets[i], '" got transformed into...', sep='')
    for featureID, count in enumerate(
            tdm_bow.getrow(i).toarray()[0]):  # .toarray()[0] to transform sparse matrix into list
        if count != 0:
            print(count_vect.get_feature_names()[featureID], '(', count, '), ', sep='', end='')
    print('\n-----')

print("\n\n--- BOW n2----")

count_vect_n2 = CountVectorizer(ngram_range=(2, 2))
tdm_bow_n2 = count_vect_n2.fit_transform(tweets)
for i in range(0, len(tweets)):
    print('"', tweets[i], '" got transformed into...', sep='')
    for featureID, count in enumerate(
            tdm_bow_n2.getrow(i).toarray()[0]):  # .toarray()[0] to transform sparse matrix into list
        if count != 0:
            print(count_vect_n2.get_feature_names()[featureID], ' (', count, '), ', sep='')
    print('\n-----')

print("\n\n--- BOW n1, TF/IDF ----")

tfidf_vect = TfidfVectorizer()
tdm_tfidf = tfidf_vect.fit_transform(tweets)
for i in range(0, len(tweets)):
    print('"', tweets[i], '" got transformed into...')
    for featureID, count in enumerate(
            tdm_tfidf.getrow(i).toarray()[0]):  # .toarray()[0] to transform sparse matrix into list
        if count != 0:
            print(tfidf_vect.get_feature_names()[featureID], ' (', count, ') ', sep='')
    print('\n-----')

print("\n\n--- BOW n1-3, TF/IDF ----")

tfidf_vect_n3 = TfidfVectorizer(ngram_range=(1,3))
tdm_tfidf_n3 = tfidf_vect_n3.fit_transform(tweets)
for i in range(0, len(tweets)):
    print('"', tweets[i], '" got transformed into...')
    for featureID, count in enumerate(
            tdm_tfidf_n3.getrow(i).toarray()[0]):  # .toarray()[0] to transform sparse matrix into list
        if count != 0:
            print(tfidf_vect_n3.get_feature_names()[featureID], ' (', count, ') ', sep='')
    print('\n-----')

print("\n\n--- Tweet Tokenizer (happyfuntokenizing) ----")

from Utils import happyfuntokenizing
twitter_tokenizer = happyfuntokenizing.Tokenizer()

for tweet in tweets:
    print('---',tweet,'---')
    for token in twitter_tokenizer.tokenize(tweet):
        print(token)