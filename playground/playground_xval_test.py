import sys

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from Dataset import Dataset
from sklearn import cross_validation
from Utils.preprocessing import preproc_text as tp
from Utils.tokenization import Tokenize
from Utils.validation import CrossValidation

dataset = Dataset(dataset=sys.argv[1])
raw_train_data, train_targets = dataset.getData(cut_long_tail=True)
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
print('--- 5-FOLD CV, WEIGHTED F1 ---')
scorer = CrossValidation.PrintingScorer()
cross_validation.cross_val_score(pipeline, raw_train_data, train_targets, cv=5, n_jobs=5, scoring=scorer)