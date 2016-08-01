import sys

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
PERCENT_TRAIN = 0.8
PERCENT_TEST = 0.1
PERCENT_EVAL = 0.1

raw_train_data, train_targets = dataset.getData(n=len(dataset) * PERCENT_TRAIN,
                                                cut_long_tail=False)  # get 80% of data for training
raw_train_data_nlt, train_targets_nlt = dataset.getData(n=len(dataset) * PERCENT_TRAIN,
                                                        cut_long_tail=True)  # get 80% of data for training
raw_test_data, test_targets = dataset.getData(offset=len(dataset) * PERCENT_TRAIN, n=len(dataset) * PERCENT_TEST,
                                              cut_long_tail=False)  # get another 10% for testing
raw_test_data_nlt, test_targets_nlt = dataset.getData(offset=len(dataset) * PERCENT_TRAIN,
                                                      n=len(dataset) * PERCENT_TEST,
                                                      cut_long_tail=True)  # get another 10% for testing


def e1():
    """
    E1 - Binary BagOfWords
    Full text gets tokenized and transformed into a binary term-document-matrix.
    Dataset with long tail
    """
    print('========== e1: BINARY BOW BASELINE WITH LONG TAIL BEGIN ==========')
    e1_preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                       remove_hashtags=False,
                                       transform_lowercase=False, expand_urls=False)
    print('** preproc config:', e1_preproc_text, '**')
    print('Training classifier...', end='', flush=True)
    pipeline_e1 = Pipeline(
        [('vect', CountVectorizer(preprocessor=e1_preproc_text, tokenizer=tok, lowercase=False, binary=True)),
         ('clf', MultinomialNB()),
         ])
    pipeline_e1.fit(raw_train_data, train_targets)
    print('done.')
    print('Predicting test data...', end='', flush=True)
    e1_predicted = pipeline_e1.predict(raw_test_data)
    print('done.')
    print('--- FULL CLASSIFICATION REPORT WITH ALL CLASSES ---')
    labels = list(set(test_targets))  # take only labels that have support
    target_names = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(test_targets, e1_predicted, labels=labels, target_names=target_names, digits=4))
    print('--- CLASSIFICATION REPORT FOR LONG-TAIL CLASSES ---')
    labels_longtail = list(set(test_targets).difference(set(test_targets_nlt)))  # take only labels that have support
    target_names_longtail = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(test_targets, e1_predicted, labels=labels_longtail,
                                        target_names=target_names_longtail, digits=4))
    print('========== e1: BINARY BOW BASELINE END ==========')


def e2():
    """
    E2 - Binary BagOfWords without long-tail
    Full text gets tokenized and transformed into a binary term-document-matrix.
    Dataset with long tail
    """
    print('========== e2: BINARY BOW BASELINE WITHOUT LONG-TAIL BEGIN ==========')
    e2_preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                       remove_hashtags=False,
                                       transform_lowercase=False, expand_urls=False)
    print('** preproc config:', e2_preproc_text, '**')
    print('Training classifier...', end='', flush=True)
    pipeline_e2 = Pipeline(
        [('vect', CountVectorizer(preprocessor=e2_preproc_text, tokenizer=tok, lowercase=False, binary=True)),
         ('clf', MultinomialNB()),
         ])
    pipeline_e2.fit(raw_train_data_nlt, train_targets_nlt)
    print('done.')
    print('Predicting test data...', end='', flush=True)
    e2_predicted = pipeline_e2.predict(raw_test_data_nlt)
    print('done.')
    print('--- FULL CLASSIFICATION REPORT WITH ALL CLASSES ---')
    labels = list(set(test_targets_nlt))  # take only labels that have support
    target_names = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(test_targets_nlt, e2_predicted, labels=labels, target_names=target_names,
                                        digits=4))
    print('========== e2: BINARY BOW BASELINE WITHOUT LONG-TAIL END ==========')


"""Run experiments"""
e1()
e2()
