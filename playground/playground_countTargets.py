import json

target_counter = {}
i = 0
with open('../../data/Germany_filtered_shuffled.json') as jsonfile:
    for line in jsonfile:
        tweet = json.loads(line)
        target_id = tweet['place']['id']
        if target_id not in target_counter.keys():
            target_counter[target_id] = 0
        target_counter[target_id] += 1
        i += 1
        if i % 100000 == 0:
            print(i)

print(len(target_counter))
