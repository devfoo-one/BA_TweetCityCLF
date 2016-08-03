from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.naive_bayes import MultinomialNB

data = ['i am am classA', 'classB i am', 'am i classC?']
targets = ['a', 'b', 'c']
vectorizer = CountVectorizer(lowercase=False)
tdm = vectorizer.fit_transform(data)
feature_names = vectorizer.get_feature_names()

print('FEATURE NAMES:')
print(feature_names)
print('TDM:')
print(tdm)

"""BEST FEATURE EXTRACTION"""
ch2 = SelectKBest(chi2, k=3)
best_features = ch2.fit_transform(tdm, targets)
print('BEST 3 FEATURES TDM:')
print(best_features)
for i in ch2.get_support(indices=True):  # returns feature indices of original tdm
    targets_for_feature = []
    for doc, a in enumerate(tdm.getcol(i)):  # get tdm col for feature i
        if a != 0:  # check if feature is present in
            target = targets[doc]  # get target for document
            targets_for_feature.append(target)
    print(feature_names[i], targets_for_feature)

# clf = MultinomialNB()
# clf.fit(tdm, targets)
