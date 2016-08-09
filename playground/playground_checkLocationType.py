import json

count_all = 0
counter = {
    'geo_place_coord': 0,
    'geo_place_!coord': 0,
    'geo_!place_coord': 0,
    'geo_!place_!coord': 0,
    '!geo_place_coord': 0,
    '!geo_place_!coord': 0,
    '!geo_!place_coord': 0,
    '!geo_!place_!coord': 0,
}

with open('../../data/Germany.json') as dataset:
    for line in dataset:
        try:
            jsonObj = json.loads(line)
        except ValueError:
            continue  # could not decode json line, skipping.
        hasPlace = jsonObj['place'] is not None
        hasGeo = jsonObj['geo'] is not None
        hasCoord = jsonObj['coordinates'] is not None

        if hasGeo and hasPlace and hasCoord:
            counter['geo_place_coord'] += 1
        if hasGeo and hasPlace and not hasCoord:
            counter['geo_place_!coord'] += 1
        if hasGeo and not hasPlace and hasCoord:
            counter['geo_!place_coord'] += 1
        if hasGeo and not hasPlace and not hasCoord:
            counter['geo_!place_!coord'] += 1
        if not hasGeo and hasPlace and hasCoord:
            counter['!geo_place_coord'] += 1
        if not hasGeo and hasPlace and not hasCoord:
            counter['!geo_place_!coord'] += 1
        if not hasGeo and not hasPlace and hasCoord:
            counter['!geo_!place_coord'] += 1
        if not hasGeo and not hasPlace and not hasCoord:
            counter['!geo_!place_!coord'] += 1

        count_all += 1

        if count_all % 100000 == 0:
            print(count_all)

print('done. total:', count_all, 'sum counter:', sum(counter.values()))
for key, value in counter.items():
    print(key,'=', value)

