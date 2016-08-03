import json

count_all = 0
count_geo = 0
count_place = 0
count_geo_place = 0
with open('../../data/Germany.json') as dataset:
    for line in dataset:
        try:
            jsonObj = json.loads(line)
        except ValueError:
            continue  # could not decode json line, skipping.
        hasPlace = jsonObj['place'] is not None
        hasGeo = jsonObj['geo'] is not None
        if hasGeo and hasPlace:
            count_geo_place += 1
        else:
            if hasGeo:
                count_geo += 1
            if hasPlace:
                count_place += 1
        count_all += 1
        # if not hasPlace and not hasGeo:
        #     print(json.dumps(jsonObj))
        if count_all % 100000 == 0:
            print(
                'all: {}, only_place: {}, only_geo: {}, both: {}, nothing: {}'.format(count_all, count_place, count_geo,
                                                                                      count_geo_place, (
                                                                                      count_all - count_geo_place - count_geo - count_place)))
print(
                'all: {}, only_place: {}, only_geo: {}, both: {}, nothing: {}'.format(count_all, count_place, count_geo,
                                                                                      count_geo_place, (
                                                                                      count_all - count_geo_place - count_geo - count_place)))