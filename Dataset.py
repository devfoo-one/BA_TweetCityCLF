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
        """
        Reads json file with one tweet per line
        :param dataset: Path to data file
        :param cut_long_tail: If True, long-tail target classes will be merged to class 'other'
        """
        self.__data_count__ = 0
        self.__target_names__ = {}  # k: target id, v: {name: count of name string}
        self.__target_names_noLongTail__ = {}  # k: target id, v: {name: count of name string}
        self.__target_counter__ = {}  # k: target id, v: count
        self.__target_counter_noLongTail__ = {}  # k: target id, v: count
        self.__data__ = []  # filtered tweet objects
        self.__targets__ = []  # targets
        self.__targets_noLongTail__ = []  # targets with 'other' class
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
        self.__targets_noLongTail__ = list(self.__targets__)
        self.__target_counter_noLongTail__ = dict(self.__target_counter__)
        self.__target_names_noLongTail__ = dict(self.__target_names__)
        self.__target_names_noLongTail__['other'] = ['other']
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
                self.__target_counter_noLongTail__.pop(target_id)
                self.__target_names_noLongTail__.pop(target_id)
        self.__target_counter_noLongTail__['other'] = class_other_n
        for t in enumerate(self.__targets_noLongTail__):
            if t[1] in other_ids:
                self.__targets_noLongTail__[t[0]] = 'other'

    def __addTargetName__(self, key, name):
        """Adds a target name to the target name collection"""
        if key not in self.__target_names__.keys():
            self.__target_names__[key] = {}
        if name not in self.__target_names__[key].keys():
            self.__target_names__[key][name] = 0
        self.__target_names__[key][name] += 1

    def getTargetName(self, target_id):
        """Returns the top name for one target id"""
        if target_id == 'other':  # if someone asks for 'other' then use this dict
            return sorted(self.__target_names_noLongTail__[target_id], key=lambda x: x[1], reverse=True)[0]
        else:  # superset of noLongTail dict,  so no problems with general inquiries
            return sorted(self.__target_names__[target_id], key=lambda x: x[1], reverse=True)[0]

    def getData(self, offset=0, n=None, cut_long_tail=False):
        """Returns a tuple of (data, target)"""
        offset = int(offset)
        if cut_long_tail:
            if n is None:
                return self.__data__[offset:], self.__targets_noLongTail__[offset:]
            else:
                n = int(n)
                return self.__data__[offset:offset + n], self.__targets_noLongTail__[offset:offset + n]
        else:
            if n is None:
                return self.__data__[offset:], self.__targets__[offset:]
            else:
                n = int(n)
                return self.__data__[offset:offset + n], self.__targets__[offset:offset + n]

    def __len__(self):
        return self.__data_count__
