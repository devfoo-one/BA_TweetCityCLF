import json

# PLACE_TYPE = 'poi'
# PLACE_TYPE = 'neighborhood'
# PLACE_TYPE = 'admin'
# PLACE_TYPE = 'country'
PLACE_TYPE = 'city'

with open('../../data/Germany.json') as dataset:
    for line in dataset:
        try:
            jsonObj = json.loads(line)
        except ValueError:
            continue  # could not decode json line, skipping.
        if jsonObj['place'] is not None:
            if jsonObj['place']['place_type'] == PLACE_TYPE:
                print(json.dumps(jsonObj['place']))
