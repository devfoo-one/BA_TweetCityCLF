import sys

from sklearn import metrics, cross_validation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

import Preprocessing
import Preprocessing as tp
import PrintingScorer
import Tokenization
from Dataset import Dataset

dataset_path = sys.argv[1]

""" read from json """
dataset = Dataset(dataset=dataset_path)

""" Initialise default tokenizer """
tok = Tokenization.TweetTokenizer()


def e1():
    """
    E1 - Binary BagOfWords
    Full text gets tokenized and transformed into a binary term-document-matrix.
    Dataset with long tail
    """
    print('========== e1: BINARY BOW WITH LONG TAIL BEGIN ==========')
    raw_data, targets = dataset.getData(cut_long_tail=False)
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    pipeline = Pipeline(
        [('vect', CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True)),
         ('clf', MultinomialNB()),
         ])

    print('Cross Validation all classes...')
    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()
    cross_validation.cross_val_score(pipeline, raw_data, targets, cv=5, n_jobs=1, scoring=scorer)
    print('done.')

    print('--- CLASSIFICATION REPORT FOR LAST 10% (LONG-TAIL) CLASSES ---')
    targets_nlt_90 = dataset.getData(cut_long_tail=True)[1]
    labels_longtail = list(set(targets).difference(set(targets_nlt_90)))  # take only labels that have support
    target_names_longtail = [dataset.getTargetName(x) for x in labels_longtail]
    predicted = cross_validation.cross_val_predict(pipeline, raw_data, targets, cv=5, n_jobs=1)
    print(metrics.classification_report(targets, predicted, labels=labels_longtail,
                                        target_names=target_names_longtail, digits=4))

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

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)
    dataset_50percent = Dataset(dataset_path, long_tail_cutoff=0.5)
    raw_data_nlt_50, targets_nlt_50 = dataset_50percent.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    print('Cross Validation with 90% long-tail-cutoff...', end='', flush=True)
    pipeline = Pipeline(
        [('vect', CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True)),
         ('clf', MultinomialNB()),
         ])
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=5, scoring=scorer)
    print('done.')

    print('Cross Validation with 50% long-tail-cutoff...', end='', flush=True)
    cross_validation.cross_val_score(pipeline, raw_data_nlt_50, targets_nlt_50, cv=5, n_jobs=5, scoring=scorer)
    print('done.')
    print('--- CLASSIFICATION REPORT FOR LONG-TAIL-CUTOFF 50% CLASSES ---')
    predicted = cross_validation.cross_val_predict(pipeline, raw_data_nlt_50, targets_nlt_50, cv=5, n_jobs=5)
    labels = list(set(targets_nlt_50))  # take only labels that have support
    target_names = [dataset.getTargetName(x) for x in labels]
    print(metrics.classification_report(targets_nlt_50, predicted, labels=labels,
                                        target_names=target_names, digits=4))
    print('========== e2: BINARY BOW WITHOUT LONG-TAIL END ==========')


def e3():
    """
        E3 - TF/IDF BagOfWords without long-tail
        Full text gets tokenized and transformed into a tf/idf weighted term-document-matrix.
        Dataset without long tail
        """
    print('========== e3: TF/IDF BOW WITHOUT LONG-TAIL (0.9 CutOff) BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    pipeline = Pipeline(
        [('vect', TfidfVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, use_idf=True)),
         ('clf', MultinomialNB()),
         ])

    print('Grid Search...', end='', flush=True)
    # http://stackoverflow.com/questions/27697766/understanding-min-df-and-max-df-in-scikit-countvectorizer
    min_df_range = [x / 1000 for x in range(2, 12, 2)]
    min_df_range.append(1)  # test documents with minimal df of 1(one) document
    min_df_range.append(0.001)  # test documents with minimal df of 1(one) document
    max_df_range = [x / 10 for x in range(2, 12, 2)]
    max_df_range.append(0.1)
    print('min_df:', min_df_range)
    print('max_df:', max_df_range)
    parameters = {'vect__min_df': min_df_range,  # test 0.001, 0.002, ... , 0.01
                  'vect__max_df': max_df_range  # test 0.1, 0.2, 0.4, 0.6, ... , 1.0
                  }
    gs = GridSearchCV(pipeline, parameters, n_jobs=10)
    gs = gs.fit(raw_data_nlt_90, targets_nlt_90)
    gs_winner = gs.best_estimator_
    for score in gs.grid_scores_:
        print(score)
    print('done.')

    print('--- GridSearch WINNER ---')
    print(gs_winner)
    print('-------------------------')

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    print('Cross Validation...', end='', flush=True)
    cross_validation.cross_val_score(gs_winner, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=5, scoring=scorer)
    print('done.')
    print('========== e3: TF/IDF BOW WITHOUT LONG-TAIL END ==========')


def e4():
    """
       E4 - Binary BagOfWords lowercase without long-tail
       Full text gets tokenized, lowercased and transformed into a binary term-document-matrix.
       Dataset without long tail
       """
    print('========== e4: BINARY BOW LOWERCASE WITHOUT LONG-TAIL BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=True, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    print('Cross Validation with 90% long-tail-cutoff...', end='', flush=True)
    pipeline = Pipeline(
        [('vect', CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=True, binary=True)),
         ('clf', MultinomialNB()),
         ])
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=5, scoring=scorer)
    print('done.')

    print('Cross Validation with 50% long-tail-cutoff...', end='', flush=True)
    dataset_50percent = Dataset(dataset_path, long_tail_cutoff=0.5)
    raw_data_nlt_50, targets_nlt_50 = dataset_50percent.getData(cut_long_tail=True)
    cross_validation.cross_val_score(pipeline, raw_data_nlt_50, targets_nlt_50, cv=5, n_jobs=5, scoring=scorer)
    print('done.')

    print('========== e4: BINARY BOW LOWERCASE WITHOUT LONG-TAIL BEGIN END ==========')


def e5_1():
    """
        E5_1 - TOKEN N-GRAMS
        Dataset without long tail
    """
    print('========== e5_1: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True, analyzer='word',
                          ngram_range=(1, 3))),
         ('clf', MultinomialNB()),
         ])
    print(pipeline)
    print('Cross Validation with 90% long-tail-cutoff...', end='', flush=True)
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1, scoring=scorer)
    print('done.')
    print('========== e5_1: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL END ==========')


def e5_2():
    """
        E5_2 - TOKEN N-GRAMS lowercase
        Dataset without long tail
    """
    print('========== e5_2: TOKEN-NGRAMS (1,3) LOWERCASE WITHOUT LONG-TAIL BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=True, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=True, binary=True, analyzer='word',
                          ngram_range=(1, 3))),
         ('clf', MultinomialNB()),
         ])
    print(pipeline)
    print('Cross Validation with 90% long-tail-cutoff...', end='', flush=True)
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1, scoring=scorer)
    print('done.')
    print('========== e5_2: TOKEN-NGRAMS (1,3) LOWERCASE WITHOUT LONG-TAIL END ==========')


def e5_1_storePrediction():
    """
        E5_1 - TOKEN N-GRAMS lowercase
        Dataset without long tail
    """
    print('========== e5_1: TOKEN-NGRAMS (1,3) LOWERCASE WITHOUT LONG-TAIL BEGIN ==========')
    export = {
        'target_names': {},
        'predicted': [],
        'truth': []
    }
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True, analyzer='word',
                          ngram_range=(1, 3))),
         ('clf', MultinomialNB()),
         ])
    print(pipeline)
    print('Predicting...')
    export['predicted'] = cross_validation.cross_val_predict(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1)
    export['truth'] = targets_nlt_90
    export['predicted'] = list(export['predicted'])
    for target_id in set(targets_nlt_90):
        export['target_names'][target_id] = dataset.getTargetName(target_id)
    print('done.')

    import pickle
    with open('../data/e51predictions.pickle', mode='wb') as export_f:
        pickle.dump(export, export_f)

    print('========== e5_1: TOKEN-NGRAMS (1,3) LOWERCASE WITHOUT LONG-TAIL END ==========')


def e6():
    """
        E6 - Char N-Grams
        Dataset without long tail
    """
    print('========== e6: CHARACTER N GRAMS (2,4) WITHOUT LONG-TAIL BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True, analyzer='char',
                          ngram_range=(2, 4))),
         ('clf', MultinomialNB()),
         ])
    print(pipeline)
    print('Cross Validation with 90% long-tail-cutoff...', end='', flush=True)
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1, scoring=scorer)
    print('done.')

    print('========== e6: CHARACTER N GRAMS (2,4) WITHOUT LONG-TAIL END ==========')


def e6_l():
    """
        E6 - Char N-Grams lowercase
        Dataset without long tail
    """
    print('========== e6_l: CHARACTER N GRAMS (2,4) LOWERCASE WITHOUT LONG-TAIL BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=True, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=True, binary=True, analyzer='char',
                          ngram_range=(2, 4))),
         ('clf', MultinomialNB()),
         ])
    print(pipeline)
    print('Cross Validation with 90% long-tail-cutoff...', end='', flush=True)
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1, scoring=scorer)
    print('done.')

    print('========== e6_l: CHARACTER N GRAMS (2,4) LOWERCASE WITHOUT LONG-TAIL END ==========')


def e7_1():
    """
            E5 - TOKEN N-GRAMS
            Dataset without long tail
        """
    print('========== e7_1: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL NO USER MENTIONS BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=True,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True, analyzer='word',
                          ngram_range=(1, 3))),
         ('clf', MultinomialNB()),
         ])
    print('Cross Validation with 90% long-tail-cutoff...')
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1, scoring=scorer)
    print('done.')
    print('========== e7_1: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL NO USER MENTIONS END ==========')


def e7_2():
    """
            E5 - TOKEN N-GRAMS
            Dataset without long tail
        """
    print('========== e7_2: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL NO URLS BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=True, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True, analyzer='word',
                          ngram_range=(1, 3))),
         ('clf', MultinomialNB()),
         ])
    print('Cross Validation with 90% long-tail-cutoff...')
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1, scoring=scorer)
    print('done.')
    print('========== e7_2: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL NO URLS END ==========')


def e7_3():
    """
            E5 - TOKEN N-GRAMS
            Dataset without long tail
        """
    print('========== e7_3: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL BLIND URLS BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=True, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True, analyzer='word',
                          ngram_range=(1, 3))),
         ('clf', MultinomialNB()),
         ])
    print('Cross Validation with 90% long-tail-cutoff...')
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1, scoring=scorer)
    print('done.')
    print('========== e7_3: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL NO HASHTAGS END ==========')


def e7_4():
    """
            E5 - TOKEN N-GRAMS
            Dataset without long tail
        """
    print('========== e7_4: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL NO HASHTAGS BEGIN ==========')
    preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=True,
                                    transform_lowercase=False, expand_urls=False)
    print('** preproc config:', preproc_text, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True, analyzer='word',
                          ngram_range=(1, 3))),
         ('clf', MultinomialNB()),
         ])
    print('Cross Validation with 90% long-tail-cutoff...')
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1, scoring=scorer)
    print('done.')
    print('========== e7_4: TOKEN-NGRAMS (1,3) WITHOUT LONG-TAIL NO HASHTAGS END ==========')


def e8_1():
    """
        E8 - TOKEN-NGRAMS ON USER PROFILE LOCATION
        Dataset without long tail
    """
    print(
        '========== e8_1: TOKEN-NGRAMS (1,3) TOKEN-NGRAMS ON USER PROFILE LOCATION WITHOUT LONG-TAIL BEGIN ==========')
    # preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=True, remove_user_mentions=False,
    #                                 remove_hashtags=True,
    #                                 transform_lowercase=False, expand_urls=False)
    preproc_meta = Preprocessing.MetaFeatureProcessor(extract_profile_location=True)
    print('** preproc config:', preproc_meta, '**')

    raw_data_nlt_90, targets_nlt_90 = dataset.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_meta, tokenizer=tok, lowercase=False, binary=True, analyzer='word',
                          ngram_range=(1, 3))),
         ('clf', MultinomialNB()),
         ])
    print('Cross Validation with 90% long-tail-cutoff...')
    cross_validation.cross_val_score(pipeline, raw_data_nlt_90, targets_nlt_90, cv=5, n_jobs=1, scoring=scorer)
    print('done.')
    print('========== e8_1: TOKEN-NGRAMS (1,3) TOKEN-NGRAMS ON USER PROFILE LOCATION WITHOUT LONG-TAIL END ==========')


def e8_2():
    """
        E8 - TOKEN-NGRAMS ON USER PROFILE LOCATION
        Dataset without long tail
    """
    print('========== e8_2: TOKEN-NGRAMS (1,3) TOKEN-NGRAMS ON USER PROFILE LOCATION LTCUTOFF 0.5 BEGIN ==========')
    preproc_meta = Preprocessing.MetaFeatureProcessor(extract_profile_location=True)
    print('** preproc config:', preproc_meta, '**')

    dataset_50percent = Dataset(dataset_path, long_tail_cutoff=0.5)
    raw_data_nlt_50, targets_nlt_50 = dataset_50percent.getData(cut_long_tail=True)

    """ Initialise PrintScorer for cross-validation"""
    scorer = PrintingScorer.PrintingScorer()

    pipeline = Pipeline(
        [('vect',
          CountVectorizer(preprocessor=preproc_meta, tokenizer=tok, lowercase=False, binary=True, analyzer='word',
                          ngram_range=(1, 3))),
         ('clf', MultinomialNB()),
         ])
    print('Cross Validation with 50% long-tail-cutoff...')
    cross_validation.cross_val_score(pipeline, raw_data_nlt_50, targets_nlt_50, cv=5, n_jobs=5, scoring=scorer)
    print('done.')
    print('--- CLASSIFICATION REPORT FOR LONG-TAIL-CUTOFF 50% CLASSES ---')
    predicted = cross_validation.cross_val_predict(pipeline, raw_data_nlt_50, targets_nlt_50, cv=5, n_jobs=5)
    labels = list(set(targets_nlt_50))  # take only labels that have support
    target_names = [dataset_50percent.getTargetName(x) for x in labels]
    print(metrics.classification_report(targets_nlt_50, predicted, labels=labels,
                                        target_names=target_names, digits=4))
    print('========== e8_2: TOKEN-NGRAMS (1,3) TOKEN-NGRAMS ON USER PROFILE LOCATION LTCUTOFF 0.5 END ==========')


"""Run experiments"""
e1()
# e2()
# e3()
# e4()
# e5()
# e5_1() # TODO BINARY
# e5_1_storePrediction()
# e6()
# e6_l()
# e7_1()
# e7_2()
# e7_3()
# e7_4()
# e8_1()
# e8_2()
# e8_3() # TODO USERID
