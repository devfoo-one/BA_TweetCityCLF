import json

places = [
    'c589d9d6ed38927c', '582f38b2762fb9a2',  # Frankfurt am Main
    '75ea2e4bcf0b7a4d', 'e385d4d639c6a423',  # Stuttgart
    'eeb57bfe49fa0831', 'e363ae8f809220c6',  # Neunkirchen
    '2d1e776f896ad2a2', '5eefdd08491a1c89',  # Leipzig
    '3078869807f9dd36', '31518521a29847bc',  # Berlin
]

counter = {}
one_sample_per_id = {}
for p in places:
    counter[p] = 0

i = 0
with open('../../data/Germany_filtered_shuffled.json') as jsonfile:
    for line in jsonfile:
        tweet = json.loads(line)
        place_obj = tweet['place']
        place_id = place_obj['id']
        if place_id in places:
            if counter[place_id] == 0:
                one_sample_per_id[place_id] = place_obj
            counter[place_id] += 1

            # print(place_id, json.dumps(place_obj))
        i += 1
        if i % 100000 == 0:
            print(counter)
            print(i)

print(counter)
for k,v in one_sample_per_id.items():
    print(k, v)