import pickle

predictions = pickle.load(open('../../data/e51predictions.pickle', 'rb'))

for y_pred, y in zip(predictions['predicted'], predictions['truth']):
    print('TRUTH: {}, PREDICTED: {}'.format(predictions['target_names'][y], predictions['target_names'][y_pred]))