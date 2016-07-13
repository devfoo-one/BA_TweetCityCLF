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
        },
        'entities': tweet['entities']
    }


class Dataset:
    def __init__(self, dataset):
        self.__data_count__ = 0
        self.__target_names__ = {}  # k: target id, v: {name: count of name string}
        self.__target_counter__ = {}  # k: target id, v: count
        self.__data__ = []
        self.__targets__ = []
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
                    self.__addTargetName__(place_id, place['name'])
                    self.__data__.append(cleanTweetObj(jsonObj))
                    self.__targets__.append(place_id)
                    self.__data_count__ += 1
            except KeyError:
                continue  # Tweet has no lang or place.placetype. skipping.

        """Cut last 10% of targets and point it to class 'other'"""
        self.__target_names__['other'] = ['other']
        sorted_targets = sorted(self.__target_counter__.items(), key=lambda x: x[1], reverse=True)
        percentage_counter = 0
        class_other_n = 0
        other_ids = []
        for target in sorted_targets:
            target_id = target[0]
            target_count = target[1]
            percentage_counter += target_count
            if percentage_counter / self.__data_count__ >= 0.9:
                class_other_n += target_count
                other_ids.append(target_id)
                self.__target_counter__.pop(target_id)
                self.__target_names__.pop(target_id)
        self.__target_counter__['other'] = class_other_n
        for t in enumerate(self.__targets__):
            if t[1] in other_ids:
                self.__targets__[t[0]] = 'other'

    def __addTargetName__(self, key, name):
        """Adds a target name to the target name collection"""
        if key not in self.__target_names__.keys():
            self.__target_names__[key] = {}
        if name not in self.__target_names__[key].keys():
            self.__target_names__[key][name] = 0
        self.__target_names__[key][name] += 1

    def getTargetName(self, target_id):
        """Returns the top name for one target id"""
        return sorted(self.__target_names__[target_id], key=lambda x: x[1], reverse=True)[0]

    def getData(self, n=None):
        """Returns a tuple of (data, target)"""
        if n is None:
            return self.__data__, self.__targets__
        else:
            return self.__data__[:n], self.__targets__[:n]
