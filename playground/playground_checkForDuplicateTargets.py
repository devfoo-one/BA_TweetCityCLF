import pickle

target_names_2_id = {}

print('Loading prediction data...', end='', flush=True)
predictions = pickle.load(open('../../data/e51predictions.pickle', 'rb'))
print('done')


for target_id, target_name in predictions['target_names'].items():
    if target_name not in target_names_2_id.keys():
        target_names_2_id[target_name] = set()
    target_names_2_id[target_name].add(target_id)

for target_name, ids in target_names_2_id.items():
    if len(ids) > 1:
        print(target_name, ids)

