import sys

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from Dataset import Dataset
from sklearn import cross_validation
from Utils.preprocessing import preproc_text as tp
from Utils.tokenization import Tokenize

raw_train_data, train_targets = Dataset(dataset=sys.argv[1]).getData(cut_long_tail=True)
tok = Tokenize.TweetTokenizer()
preproc_text = tp.TextProcessor(blind_urls=False, remove_urls=False, remove_user_mentions=False,
                                    remove_hashtags=False,
                                    transform_lowercase=False, expand_urls=False)
print('** preproc config:', preproc_text, '**')
print('Training classifier...', end='', flush=True)
pipeline = Pipeline(
    [('vect', CountVectorizer(preprocessor=preproc_text, tokenizer=tok, lowercase=False, binary=True)),
     ('clf', MultinomialNB()),
     ])
print('--- 10-FOLD CV, WEIGHTED F1 ---')
scores = cross_validation.cross_val_score(pipeline, raw_train_data, train_targets, cv=10, n_jobs=-1,
                                          scoring="f1_weighted")
print(scores)