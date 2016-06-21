"""Takes the main dataset and filters out all lines wich are not necessary"""

import json

with open('../../data/Germany_filtered.json', mode='w', encoding='utf8', newline='') as outputfile:
    for line in open('../../data/Germany.json'):
        try:
            jsonObj = json.loads(line)
        except ValueError:
            continue  # could not decode json line, skipping.
        try:
            if (jsonObj['lang'] == 'de') and (jsonObj['place'] is not None) and (
                        jsonObj['place']['place_type'] == 'city'):
                outputfile.write(line)
        except KeyError:
            continue  # Tweet has no lang or place.placetype. skipping.
