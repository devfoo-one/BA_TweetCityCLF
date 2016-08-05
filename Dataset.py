"""
Reads the Germany.json dataset and filters for "lang"=="de" and "place.type" == "city"
"""

import json


def extractPlace(json_obj):
    """
    Extracts a place object out of a tweet and returns (id, place)
    :param json_obj: twitter place object
    :return: (id, place)
    """
    place_id = json_obj['place']['id']
    place = json_obj['place']
    return place_id, place


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


def add2ListDict(key, value, dictionary):
    """
    Checks if dictionary[key] is a set and add 'value', if not create new set and add 'value'
    :param key: dictionary key
    :param value: value to add to list
    :param dictionary: dictionary to work with
    """
    try:
        dictionary[key].add(value)
    except KeyError:
        dictionary[key] = set()
        dictionary[key].add(value)


def cleanTweetObj(tweet):
    """
    Takes a tweet object and removes unnecessary parts (to save memory)
    :param tweet: tweet object from streaming api
    :return: filtered twitter object with same structure
    """
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
        """
        self.__data_count__ = 0
        self.__target_names_dict__ = {}  # k: target id, v: {name: count of name string}
        self.__target_names_dict_noLongTail__ = {}  # k: target id, v: {name: count of name string}
        self.__target_counter__ = {}  # k: target id, v: count
        self.__target_counter_noLongTail__ = {}  # k: target id, v: count

        """data lists"""
        self.__data__ = []  # filtered tweet objects
        self.__targets__ = []  # targets
        self.__targets_noLongTail__ = []  # targets with 'other' class

        print('DATASET: Initialising with file', dataset)
        print('DATASET: Reading JSON... ', end='', flush=True)
        for line in open(dataset):
            try:
                jsonObj = json.loads(line)
            except ValueError:
                continue  # could not decode json line, skipping.
            try:
                if (jsonObj['lang'] == 'de') and (jsonObj['place'] is not None) and (
                            jsonObj['place']['place_type'] == 'city' and jsonObj['place']['country_code'] == 'DE'):
                    place_id, place = extractPlace(jsonObj)
                    incrementCounterDict(place_id, self.__target_counter__)  # increment place counter
                    self.__addTargetName__(place_id, place['name'])
                    self.__data__.append(cleanTweetObj(jsonObj))
                    self.__targets__.append(place_id)
                    self.__data_count__ += 1
            except KeyError:
                continue  # Tweet has no lang or place.placetype. skipping.
        print('done.')

        print("DATASET: Generating 'other' class for last 10% (long tail) target classes... ", end='', flush=True)
        """Cut last 10% of targets and point it to class 'other'"""
        self.__targets_noLongTail__ = list(self.__targets__)
        self.__target_counter_noLongTail__ = dict(self.__target_counter__)
        self.__target_names_dict_noLongTail__ = dict(self.__target_names_dict__)
        self.__target_names_dict_noLongTail__['other'] = {'other': 1}
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
                self.__target_names_dict_noLongTail__.pop(target_id)
        self.__target_counter_noLongTail__['other'] = class_other_n
        for t in enumerate(self.__targets_noLongTail__):
            if t[1] in other_ids:
                self.__targets_noLongTail__[t[0]] = 'other'
        print('done.')

    def __addTargetName__(self, key, name):
        """
        Adds a target name to the target name collection and increment name counter
        :param key: target id
        :param name: target name
        """
        if key not in self.__target_names_dict__.keys():
            self.__target_names_dict__[key] = {}
        if name not in self.__target_names_dict__[key].keys():
            self.__target_names_dict__[key][name] = 0
        self.__target_names_dict__[key][name] += 1

    def getTargetName(self, target_id):
        """
        Returns the top name for one target id
        :param target_id: target id
        :return: str, most frequent name for this target id
        """
        if target_id == 'other':  # if someone asks for 'other' then use this dict
            return sorted(self.__target_names_dict_noLongTail__[target_id].items(), key=lambda x: x[1], reverse=True)[0][0]
        else:  # superset of noLongTail dict,  so no problems with general inquiries
            return sorted(self.__target_names_dict__[target_id].items(), key=lambda x: x[1], reverse=True)[0][0]

    def getData(self, offset=0, n=None, cut_long_tail=False):
        """
        Returns a tuple of (data, target)
        :param offset: data offset
        :param n: number of data to return
        :param cut_long_tail: use 'other' class for long tail targets
        :return: (data, target)
        """
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
