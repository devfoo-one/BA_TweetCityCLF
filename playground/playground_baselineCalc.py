import pickle

"""load persistent dataset"""
with open('../dataset.pickle', 'rb') as f:
    dataset = pickle.load(f)

