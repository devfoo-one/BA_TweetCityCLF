import sys

from Dataset import Dataset
from Utils import tweet_preprocessor as tp

dataset_path = sys.argv[1]

"""read from json"""
dataset = Dataset(dataset=dataset_path)

t1 = tp.Processor(blind_urls=False, remove_urls=False, remove_user_mentions=False, remove_hashtags=False,
                  transform_lowercase=False)

raw_train_data, train_targets = dataset.getData(n=900)
train_data = [t1.digest(tweet) for tweet in raw_train_data]
raw_test_data, test_targets = dataset.getData(offset=900, n=100)
test_data = [t1.digest(tweet) for tweet in raw_test_data]

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

baseline = Pipeline([('vect', CountVectorizer()),
                     ('clf', MultinomialNB()),
                     ])
baseline.fit(train_data, train_targets)
predicted = baseline.predict(test_data)
for tweet, target, predict in zip(train_data, train_targets, predicted):
    print(dataset.getTargetName(target), dataset.getTargetName(predict))

import numpy as np

print(np.mean(predicted == test_targets))

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
