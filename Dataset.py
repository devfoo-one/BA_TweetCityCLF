"""
Reads the Germany.json dataset and filters for "lang"=="de" and "place.type" == "city"
"""

import json, pickle

"""Extracts a place object out of a tweet and returns (id, place)"""


def extractPlace(jsonObj):
    id = jsonObj['place']['id']
    place = jsonObj['place']
    return id, place


"""Checks if dict[key] is present and increment by one, if not set dict[key] = 1"""


def incrementCounterDict(key, dict):
    try:
        dict[key] += 1
    except KeyError:
        dict[key] = 1


"""Checks if dict[key] is a set and add 'value', if not create new set and add 'value'"""


def add2ListDict(key, value, dict):
    try:
        dict[key].add(value)
    except KeyError:
        dict[key] = set()
        dict[key].add(value)


"""Takes a tweet object and removes unnecessary parts (to save memory)"""


def cleanTweetObj(tweet):
    return {'text': tweet['text']}


class Dataset:
    def __init__(self, dataset):

        self.__target_names__ = {}
        self.__target_counter__ = {}
        self.data = []
        self.targets = []
        DEBUGCOUNTER = 0
        for line in open(dataset):

            """DEBUG"""
            DEBUGCOUNTER += 1
            if DEBUGCOUNTER % 10000 == 0:
                print(DEBUGCOUNTER)
            # if DEBUGCOUNTER > 2000:
            #     break
            """END DEBUG"""
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
        return self.__target_names__[targetID]