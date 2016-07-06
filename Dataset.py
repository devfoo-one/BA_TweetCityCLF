"""
Reads the Germany.json dataset and filters for "lang"=="de" and "place.type" == "city"
"""

import json


def extractPlace(jsonObj):
    """Extracts a place object out of a tweet and returns (id, place)"""
    id = jsonObj['place']['id']
    place = jsonObj['place']
    return id, place


def incrementCounterDict(key, dict):
    """Checks if dict[key] is present and increment by one, if not set dict[key] = 1"""
    try:
        dict[key] += 1
    except KeyError:
        dict[key] = 1


def add2ListDict(key, value, dict):
    """Checks if dict[key] is a set and add 'value', if not create new set and add 'value'"""
    try:
        dict[key].add(value)
    except KeyError:
        dict[key] = set()
        dict[key].add(value)


def cleanTweetObj(tweet):
    """Takes a tweet object and removes unnecessary parts (to save memory)"""
    return {
        'text': tweet['text'],
        'timestamp_ms': tweet['timestamp_ms'],
        'user': {
            'name': tweet['user']['name']
        }
    }


class Dataset:
    def __init__(self, dataset):
        self.__target_names__ = {}
        self.__target_counter__ = {}
        self.data = []
        self.targets = []
        for line in open(dataset):
            try:
                jsonObj = json.loads(line)
            except ValueError:
                continue  # could not decode json line, skipping.
            try:
                if (jsonObj['lang'] == 'de') and (jsonObj['place'] is not None) and (
                            jsonObj['place']['place_type'] == 'city'):
                    place_id, place = extractPlace(jsonObj)
                    incrementCounterDict(place_id, self.__target_counter__)  # increment place counter
                    add2ListDict(place_id, place['name'], self.__target_names__)
                    self.data.append(cleanTweetObj(jsonObj))
                    self.targets.append(place_id)
            except KeyError:
                continue  # Tweet has no lang or place.placetype. skipping.

    """Returns the names for one target id"""

    def getTargetName(self, targetID):
        return list(self.__target_names__[targetID])
