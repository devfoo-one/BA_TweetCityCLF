import sys

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from Dataset import Dataset
from Utils.preprocessing import preproc_text as tp
from Utils.tokenization import Tokenize

dataset_path = sys.argv[1]

""" read from json """
dataset = Dataset(dataset=dataset_path)

""" Initialise default tokenizer """
tok = Tokenize.TweetTokenizer()

"""
    Split data into train, test and validation
     ----------------------------------------------------------
    |               70% TRAIN            | 15% TEST | 15% VALI |
     ----------------------------------------------------------
"""
PERCENT_TRAIN = 0.7
PERCENT_TEST = 0.15
PERCENT_EVAL = 0.15

raw_train_data, train_targets = dataset.getData(n=len(dataset) * PERCENT_TRAIN,
                                                cut_long_tail=False)
raw_train_data_nlt, train_targets_nlt = dataset.getData(n=len(dataset) * PERCENT_TRAIN,
                                                        cut_long_tail=True)

raw_test_data, test_targets = dataset.getData(offset=len(dataset) * PERCENT_TRAIN,
                                              n=len(dataset) * PERCENT_TEST,
                                              cut_long_tail=False)
raw_test_data_nlt, test_targets_nlt = dataset.getData(offset=len(dataset) * PERCENT_TRAIN,
                                                      n=len(dataset) * PERCENT_TEST,
                                                      cut_long_tail=True)

print('SAMPLES = {}, TRAIN = {} ({}%), TEST = {} ({}%)'.format(len(dataset), len(raw_train_data), PERCENT_TRAIN,
                                                               len(raw_test_data), PERCENT_TEST))


def e1():
    """
    E1 - Binary BagOfWords
    Full text gets tokenized and transformed into a binary term-document-matrix.
    Dataset with long tail
    """
    print('========== e1: BINARY BOW WITH LONG TAIL BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')
    print('Training classifier...', end='', flush=True)
    pipeline = Pipeline(
        [('vect', CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True)),
         ('clf', MultinomialNB()),
         ])
    pipeline.fit(raw_train_data, train_targets)
    print('done.')
    print('Predicting test data...', end='', flush=True)
    predicted = pipeline.predict(raw_test_data)

    print('done.')
    print('--- FULL CLASSIFICATION REPORT WITH ALL CLASSES ---')
    labels = list(set(test_targets))  # take only labels that have support
    target_names = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(test_targets, predicted, labels=labels, target_names=target_names, digits=4))
    print('--- CLASSIFICATION REPORT FOR LONG-TAIL CLASSES ---')
    labels_longtail = list(set(test_targets).difference(set(test_targets_nlt)))  # take only labels that have support
    target_names_longtail = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(test_targets, predicted, labels=labels_longtail,
                                        target_names=target_names_longtail, digits=4))

    # print('--- TOP 20 FEATURES BY CHI2 SELECTION---')
    # ch2 = SelectKBest(chi2, k=20)
    # vectorizer_e1 = CountVectorizer(preprocessor=e1_preproc_text, tokenizer=tok, lowercase=False, binary=True)
    # tdm_e1 = vectorizer_e1.fit_transform(raw_train_data)
    # feature_names = vectorizer_e1.get_feature_names()
    # ch2.fit_transform(tdm_e1, train_targets)
    # for i in ch2.get_support(indices=True):  # returns feature indices of original tdm
    #     targets_for_feature = []
    #     for doc, a in enumerate(tdm_e1.getcol(i)):  # get tdm col for feature i
    #         if a != 0:  # check if feature is present in col
    #             target = train_targets[doc]  # get target for document
    #             targets_for_feature.append(target)
    #     print("'", feature_names[i], "' ", [dataset.getTargetName(x) for x in targets_for_feature])

    print('========== e1: BINARY BOW END ==========')


def e2():
    """
    E2 - Binary BagOfWords without long-tail
    Full text gets tokenized and transformed into a binary term-document-matrix.
    Dataset without long tail
    """
    print('========== e2: BINARY BOW WITHOUT LONG-TAIL BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')
    print('Training classifier...', end='', flush=True)
    pipeline = Pipeline(
        [('vect', CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True)),
         ('clf', MultinomialNB()),
         ])
    pipeline.fit(raw_train_data_nlt, train_targets_nlt)
    print('done.')
    print('Predicting test data...', end='', flush=True)
    predicted = pipeline.predict(raw_test_data_nlt)
    print('done.')
    print('--- FULL CLASSIFICATION REPORT WITH ALL CLASSES ---')
    labels = list(set(test_targets_nlt))  # take only labels that have support
    target_names = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(test_targets_nlt, predicted, labels=labels, target_names=target_names,
                                        digits=4))
    print('========== e2: BINARY BOW WITHOUT LONG-TAIL END ==========')


def e3():
    """
        E3 - TF/IDF BagOfWords without long-tail
        Full text gets tokenized and transformed into a tf/idf weighted term-document-matrix.
        Dataset without long tail
        """
    print('========== e3: TF/IDF BOW WITHOUT LONG-TAIL BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')
    print('Training classifier...', end='', flush=True)
    pipeline = Pipeline(
        [('vect', TfidfVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False)),
         ('clf', MultinomialNB()),
         ])
    pipeline.fit(raw_train_data_nlt, train_targets_nlt)
    print('done.')
    print('Predicting test data...', end='', flush=True)
    predicted = pipeline.predict(raw_test_data_nlt)
    print('done.')
    print('--- FULL CLASSIFICATION REPORT WITH ALL CLASSES ---')
    labels = list(set(test_targets_nlt))  # take only labels that have support
    target_names = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(test_targets_nlt, predicted, labels=labels, target_names=target_names,
                                        digits=4))
    print('========== e3: TF/IDF BOW WITHOUT LONG-TAIL END ==========')


def e4():
    """
        E4 - TF/IDF BagOfWords without long-tail
        Made additional changes in preproc, see printed config
        Full text gets tokenized and transformed into a tf/idf weighted term-document-matrix.
        Dataset without long tail
        """
    print('========== e4: TF/IDF BOW WITHOUT LONG-TAIL CLEANED TWEET 1 BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=True, remove_user_mentions=True,
                                    remove_hashtags=True,
                                    transform_lowercase=True, expand_urls=False)
    print('** preproc config:', preproc_text, '**')
    print('Training classifier...', end='', flush=True)
    pipeline = Pipeline(
        [('vect', TfidfVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False)),
         ('clf', MultinomialNB()),
         ])
    pipeline.fit(raw_train_data_nlt, train_targets_nlt)
    print('done.')
    print('Predicting test data...', end='', flush=True)
    predicted = pipeline.predict(raw_test_data_nlt)
    print('done.')
    print('--- FULL CLASSIFICATION REPORT WITH ALL CLASSES ---')
    labels = list(set(test_targets_nlt))  # take only labels that have support
    target_names = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(test_targets_nlt, predicted, labels=labels, target_names=target_names,
                                        digits=4))

    # print('--- TOP 50 FEATURES BY CHI2 SELECTION---')
    # ch2 = SelectKBest(chi2, k=50)
    # vectorizer = CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True)
    # tdm = vectorizer.fit_transform(raw_train_data_nlt)
    # feature_names = vectorizer.get_feature_names()
    # ch2.fit_transform(tdm, train_targets)
    # for i in ch2.get_support(indices=True):  # returns feature indices of original tdm
    #     targets_for_feature = []
    #     for doc, a in enumerate(tdm.getcol(i)):  # get tdm col for feature i
    #         if a != 0:  # check if feature is present in col
    #             target = train_targets_nlt[doc]  # get target for document
    #             targets_for_feature.append(target)
    #     print("'", feature_names[i], "' -> ", [dataset.getTargetName(x) for x in targets_for_feature], sep='')

    print('========== e4: TF/IDF BOW WITHOUT LONG-TAIL CLEANED TWEET 1 END ==========')


def e5():
    """
        E5 - Character N-Grams
        Made additional changes in preproc, see printed config
        Full text gets tokenized and transformed into a tf/idf weighted term-document-matrix.
        Dataset without long tail
        """
    print('========== e5: CHARACTER N GRAMS (1,3) WITHOUT LONG-TAIL EXPANDED URLS ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=True,
                                    remove_hashtags=False,
                                    transform_lowercase=True, expand_urls=True)
    print('** preproc config:', preproc_text, '**')
    print('Training classifier...', end='', flush=True)
    pipeline = Pipeline(
        [('vect', CountVectorizer(preprocessor=preproc_text, analyzer='char', ngram_range=(1,3))),
         ('clf', MultinomialNB()),
         ])
    pipeline.fit(raw_train_data_nlt, train_targets_nlt)
    print('done.')
    print('Predicting test data...', end='', flush=True)
    predicted = pipeline.predict(raw_test_data_nlt)
    print('done.')
    print('--- FULL CLASSIFICATION REPORT WITH ALL CLASSES ---')
    labels = list(set(test_targets_nlt))  # take only labels that have support
    target_names = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(test_targets_nlt, predicted, labels=labels, target_names=target_names,
                                        digits=4))

    print('========== e5: CHARACTER N GRAMS (1,3) WITHOUT LONG-TAIL EXPANDED URLS END ==========')


"""Run experiments"""
# e1()
# e2()
# e3()
# e4()
e5()
