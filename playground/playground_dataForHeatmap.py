"""
Takes the data set and exports a csv file with the following columns:
- PlaceID
- PlaceName
- BoundingBox (geojson)
- center
- count
"""
import json, numpy, csv

target_names_dict = {}  # k: target id, v: {name: count of name string}
target_counter = {}  # k: target id, v: occurrence count
places = {}  # k: target id, v: (bounding_box, center)


def addTargetName(key, name, dict):
    """
    Adds a target name to the target name collection and increment name counter

    :param key: target id
    :param name: target name
    :param dict: target name dictionary
    """
    if key not in dict.keys():
        dict[key] = {}
    if name not in dict[key].keys():
        dict[key][name] = 0
    dict[key][name] += 1


def getTargetName(target_id):
    """
    Returns the top name for one target id

    :param target_id: target id
    :return: str, most frequent name for this target id
    """
    return sorted(target_names_dict[target_id].items(), key=lambda x: x[1], reverse=True)[0][0]


def incrementCounterDict(key, dictionary):
    """
    Checks if dictionary[key] is present and increment by one, if not set dict[key] = 1

    :param key: dictionary key
    :param dictionary: dictionary
    """
    try:
        dictionary[key] += 1
    except KeyError:
        dictionary[key] = 1

with open('../../data/Germany_filtered_shuffled.json') as jsonfile:
    for line in jsonfile:
        tweet = json.loads(line)
        place_id = tweet['place']['id']
        place_name = tweet['place']['name']
        addTargetName(place_id, place_name, target_names_dict)
        if place_id not in places.keys():
            bounding_box = tweet['place']['bounding_box']
            center = numpy.mean(bounding_box['coordinates'], axis=1)
            places[place_id] = {'bounding_box': bounding_box, 'center': (center[0,1], center[0,0])}
        incrementCounterDict(place_id, target_counter)  # increment place counter

with open('../../data/places.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(('place_id', 'name', 'count', 'bounding_box','center_lat', 'center_long'))
    for place in sorted(target_counter.items(), key=lambda x: x[1], reverse=True):
        place_id = place[0]
        place_count = place[1]
        csvwriter.writerow(
            (
                place_id,
                getTargetName(place_id),
                place_count,
                json.dumps(places[place_id]['bounding_box']),
                str.replace(str(places[place_id]['center'][0]),'.',','),  # replace period for better number handling in external tools
                str.replace(str(places[place_id]['center'][1]),'.',',')
            )
        )
