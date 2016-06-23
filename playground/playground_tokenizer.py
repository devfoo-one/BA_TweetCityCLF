import json
with open('../../data/Germany_filtered.json') as dataset:
    for line in dataset:
        tweet = json.loads(line)