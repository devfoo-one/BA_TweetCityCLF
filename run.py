import pickle

from Dataset import Dataset
from Utils import tweet_preprocessor as tp

"""read from json"""
# dataset = Dataset(dataset='../data/Germany_filtered_shuffled.json')
dataset = Dataset(dataset='../data/Germany_filtered_shuffled_n1000.json')
# dataset = Dataset(dataset='../data/Germany_filtered_shuffled_n100000.json')
with open('dataset.pickle', 'wb') as f:
    pickle.dump(dataset, f)
print('Loaded and pickled. Thank you, come again.')
# exit(0)

# """load persistent dataset"""
# with open('dataset.pickle', 'rb') as f:
#     dataset = pickle.load(f)
#     print('dataset loaded.')

t1 = tp.Processor(blind_urls=False, remove_urls=False, remove_user_mentions=False, remove_hashtags=False,
                  preserve_case=True)
t2 = tp.Processor(blind_urls=True, remove_urls=False, remove_user_mentions=False, remove_hashtags=False,
                  preserve_case=True)
t3 = tp.Processor(blind_urls=False, remove_urls=True, remove_user_mentions=False, remove_hashtags=False,
                  preserve_case=True)
t4 = tp.Processor(blind_urls=False, remove_urls=False, remove_user_mentions=True, remove_hashtags=False,
                  preserve_case=True)
t5 = tp.Processor(blind_urls=False, remove_urls=False, remove_user_mentions=True, remove_hashtags=False,
                  preserve_case=False)
t6 = tp.Processor(blind_urls=False, remove_urls=False, remove_user_mentions=True, remove_hashtags=True,
                  preserve_case=True)

data, target = dataset.getData(n=100)
for d in data:
    print('text:\t', d['text'])
    print('t1:\t\t', t1.digest(d))
    print('t2:\t\t', t2.digest(d))
    print('t3:\t\t', t3.digest(d))
    print('t4:\t\t', t4.digest(d))
    print('t5:\t\t', t5.digest(d))
    print('t6:\t\t', t6.digest(d))

# train_data = [x['text'] for x in dataset.data[:1000]]
# train_targets = dataset.targets[:1000]
# test_data = [x['text'] for x in  dataset.data[1001:1100]]
# test_targets = dataset.targets[1001:1100]
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
#
# text_clf = Pipeline([('vect', CountVectorizer()),
#                      ('tfidf', TfidfTransformer()),
#                      ('clf', MultinomialNB()),
# ])
#
# import numpy as np
# text_clf.fit(train_data, train_targets)
# predicted = text_clf.predict(test_data)
# print(np.mean(predicted == test_targets))
