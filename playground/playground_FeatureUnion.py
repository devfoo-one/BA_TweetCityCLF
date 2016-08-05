from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from scipy.sparse import hstack

data1 = [
    {'field1': 'foo     ', 'field2': 'bar'},
    {'field1': 'foo', 'field3': 42},
    {'field2': 'foo', 'field3': 23}
]
data2 = ['oans', 'zwoa', 'drü']

targets = [1, 2, 3]

dictVect = DictVectorizer()
tdm_dictVect = dictVect.fit_transform(data1)
print(dictVect.get_feature_names())
print('tdm_dictVect shape:', tdm_dictVect.shape)
print(tdm_dictVect)

countVect = CountVectorizer()
tdm_countVect = countVect.fit_transform(data2)
print(countVect.get_feature_names())
print('tdm_countVect shape:',tdm_countVect.shape)
print(tdm_countVect)

tdm_combined = hstack([tdm_dictVect, tdm_countVect])
combined_features = dictVect.get_feature_names() + countVect.get_feature_names()
print(combined_features)
print('tdm_combined shape:', tdm_combined.shape)
print(tdm_combined)        # TODO DIESE MAL NACHPRÜFEN

clf = MultinomialNB()
clf.fit(tdm_combined, targets)
predicted = clf.predict(tdm_combined)
print(metrics.classification_report(targets, predicted))
