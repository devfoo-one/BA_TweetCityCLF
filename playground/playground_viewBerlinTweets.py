import pickle

"""load persistent dataset"""
with open('../dataset.pickle', 'rb') as f:
    dataset = pickle.load(f)

for i, tweet, target in zip(range(0, len(dataset.data)), dataset.data, dataset.targets):
    targetName = dataset.getTargetName(target)
    username_lowercase = tweet['user']['name'].lower()
    if username_lowercase.count('oberhauser') != 0 or username_lowercase.count('devfoo') != 0:
        print(i, targetName, '-', tweet['user']['name'], '-', tweet['text'])
