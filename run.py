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
raw_train_data_nlt, train_targets_nlt = dataset.getData(n=len(dataset) * 0.8,
                                                        cut_long_tail=True)  # get 80% of data for training
raw_test_data_nlt, test_targets_nlt = dataset.getData(offset=len(dataset) * 0.8, n=len(dataset) * 0.1,
                                                      cut_long_tail=True)  # get another 10% for testing

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
print('Training classifier...', end='', flush=True)
clf_e1 = Pipeline([('vect', CountVectorizer(preprocessor=e1_preproc_text, tokenizer=tok, lowercase=False, binary=True)),
                   ('clf', MultinomialNB()),
                   ])
clf_e1.fit(raw_train_data_nlt, train_targets_nlt)
print('done.')
print('Predicting test data...', end='', flush=True)
e1_predicted = clf_e1.predict(raw_test_data_nlt)
print('done.')
labels = list(set(test_targets_nlt))  # take only labels that have support
target_names = [dataset.getTargetName(x) for x in labels]
print(metrics.classification_report(test_targets_nlt, e1_predicted, labels=labels, target_names=target_names, digits=4))
print('---------- e1: BINARY BOW BASELINE END ----------')
