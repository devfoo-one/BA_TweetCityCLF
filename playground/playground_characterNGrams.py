from sklearn.feature_extraction.text import CountVectorizer

from Utils.tokenization import Tokenize

tok = Tokenize.TweetTokenizer()
cv = CountVectorizer(tokenizer=tok, lowercase=False, binary=True, analyzer='char', ngram_range=(1, 3))
docs = ['AAA BBB']
tdm = cv.fit_transform(docs)
for idx, a in enumerate(tdm.getrow(0).toarray()[0]):
    if a != 0:
        print(idx, '-', cv.get_feature_names()[idx], '-', a)
