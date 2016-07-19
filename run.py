import sys

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from Dataset import Dataset
from Utils.preprocessing import preproc_text as tp
from Utils.tokenization import tweet_tokenizer

dataset_path = sys.argv[1]

""" read from json """
dataset = Dataset(dataset=dataset_path)

""" Initialise default tokenizer """
tok = tweet_tokenizer.Tokenizer()

"""
    Split data into train, test and validation
     ----------------------------------------------------------
    |               80% TRAIN            | 10% TEST | 10% VALI |
     ----------------------------------------------------------
"""
raw_train_data, train_targets = dataset.getData(n=len(dataset) * 0.8,
                                                cut_long_tail=True)  # get 80% of data for training
raw_test_data, test_targets = dataset.getData(offset=len(dataset) * 0.8, n=len(dataset) * 0.1,
                                              cut_long_tail=True)  # get another 10% for testing
test_target_names_noLongTail = dataset.__target_names_list_noLongTail__[int(len(dataset) * 0.8):int(len(dataset) * 0.9)]

"""
    E1 - Binary BagOfWords
    Full text gets tokenized and transformed into a binary term-document-matrix.
    Dataset without long tail
"""
print('---------- e1: BINARY BOW BASELINE BEGIN ----------')

e1_preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                   remove_hashtags=False,
                                   transform_lowercase=False, expand_urls=False)
print('** preproc config:', e1_preproc_text, '**')
test_data_e1 = [e1_preproc_text.digest(tweet) for tweet in raw_test_data]
print('Training classifier...', end='')
clf_e1 = Pipeline([('vect', CountVectorizer(preprocessor=e1_preproc_text, tokenizer=tok, lowercase=False, binary=True)),
                   ('clf', MultinomialNB()),
                   ])
clf_e1.fit(raw_train_data, train_targets)
print('done.')
print('Predicting test data...', end='')
e1_predicted = clf_e1.predict(raw_test_data)
print('done.')
print('MEAN = ', np.mean(e1_predicted == test_targets))
# print(metrics.classification_report(test_targets, predicted, target_names=test_target_names_noLongTail))
# print('PRECISION =',
#       metrics.precision_score(test_targets, predicted, average='macro', labels=dataset.__target_names_list_noLongTail__))
# print('RECALL =', metrics.recall_score(test_targets, predicted, average='macro'))
# print('F1 =', metrics.f1_score(test_targets, predicted, average='macro'))

# for targetId in dataset.__target_names_noLongTail__:
#     print(dataset.getTargetName(targetId))
#     print(metrics.precision_recall_fscore_support(test_targets, predicted, labels=list(targetId)))
# print(metrics.classification_report(test_targets, predicted))

print('---------- e1: BINARY BOW BASELINE END ----------')

# for tweet, target, predict in zip(train_data_e1, train_targets_e1, predicted):
#     print(dataset.getTargetName(target), dataset.getTargetName(predict))
# print(np.mean(predicted == test_targets_e1))

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
