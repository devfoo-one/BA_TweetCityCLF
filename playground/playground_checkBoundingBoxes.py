import pickle, json, geojson

PLACE_NAMES = ['Hamburg', 'Berlin', 'München']

print('Loading stored dataset object...')
with open('dataset.pickle', 'rb') as f:
    dataset = pickle.load(f)
print('done.')

placeIds = []

print('Searching for Hamburg...')
for k, v in dataset.__target_names__.items():
    if 'Hamburg' in v:
        placeIds.append(k)
        print(k, '-', v)
print("done.")

print('Saving all places with found ids...')
with open('places.json', mode='w', encoding='utf8', newline='') as outputfile:
    for line in open('../data/Germany.json'):
        try:
            jsonObj = json.loads(line)
        except ValueError:
            continue  # could not decode json line, skipping.
        try:
            if (jsonObj['lang'] == 'de') and (jsonObj['place'] is not None) and (
                            jsonObj['place']['place_type'] == 'city' and jsonObj['place']['id'] in placeIds):
                print(json.dumps(jsonObj['place']), file=outputfile)
        except KeyError:
            continue  # Tweet has no lang or place.placetype. skipping.
print('done.')

places = {}
for k in placeIds:
    places[k] = []

print('reading places file...')
with open('places.json', encoding='utf8') as file:
    for line in file:
        jsonObj = json.loads(line)
        id = jsonObj['id']
        places[id].append(jsonObj)
print('done.')

lastOne = None
for i in places.keys():
    print("checking", i)
    for p in places[i]:
        bounding_box = geojson.loads(geojson.dumps(p['bounding_box']))
        if lastOne is not None:
            if lastOne != bounding_box:
                print('bounding_box differs!')
                print('lastOne: ', json.dumps(lastOne))
                print('current:', json.dumps(bounding_box))
        lastOne = bounding_box
print("done.")