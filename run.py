import pickle

from Dataset import Dataset

"""read from json"""
dataset = Dataset(dataset='../data/Germany.json')
with open('dataset.pickle', 'wb') as f:
    pickle.dump(dataset, f)

# """load persistent dataset"""
# with open('dataset.pickle', 'rb') as f:
#     dataset = pickle.load(f)


train_data = [x['text'] for x in dataset.data[:1000]]
train_targets = dataset.targets[:1000]
test_data = [x['text'] for x in  dataset.data[1001:1100]]
test_targets = dataset.targets[1001:1100]



for i in train_data:
    if len(i) == 0:
        print(i, "foo")

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
])

import numpy as np
text_clf.fit(train_data, train_targets)
predicted = text_clf.predict(test_data)
print(np.mean(predicted == test_targets))
