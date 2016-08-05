from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

data = [
    {'field1': 'foo     ', 'field2': 'bar'},
    {'field1': 'foo', 'field3': 42},
    {'field2': 'foo', 'field3': 23}
]

targets = [1,2,3]

dv = DictVectorizer()
tdm = dv.fit_transform(data)

print(tdm)
print(dv.get_feature_names())

clf = MultinomialNB()
clf.fit(tdm, targets)
predicted = clf.predict(tdm)

print(metrics.classification_report(targets, predicted))

