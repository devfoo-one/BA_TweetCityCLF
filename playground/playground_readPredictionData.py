import pickle

print('Loading prediction data...', end='', flush=True)
predictions = pickle.load(open('../../data/e51predictions.pickle', 'rb'))
target_names = predictions['target_names']
print('done')

targets = [
    # 'b470fb5cf49810b9',  # Tübingen
    # '3078869807f9dd36',  # Berlin
    # '48504653e183c91c',  # Hannover
    '6002284889d67fa1',  # Bielefeld
]

# for k,v in target_names.items():
#     if v == 'Bielefeld':
#         print(k,v)
# exit(0)

wrong_predictions = {}
for k in targets:
    wrong_predictions[k] = {}

for y_pred, y in zip(predictions['predicted'], predictions['truth']):
    if y in targets:
        if y_pred not in wrong_predictions[y].keys():
            wrong_predictions[y][y_pred] = 0
        wrong_predictions[y][y_pred] += 1

for target_id, wrong_y in wrong_predictions.items():
    print("Wrong predictions for target id {} ({})".format(target_id, target_names[target_id]))
    for place_id,count in sorted(wrong_y.items(), key=lambda x: x[1], reverse=True):
        print("{} - {} ({})".format(count, target_names[place_id], place_id))