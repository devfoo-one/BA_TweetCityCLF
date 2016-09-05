import html.parser
import json
import pickle

empty_profile_locations = 0
profile_locations = 0
key_errors = 0
locations = set()
n = 0
# with open('../../data/Germany.json', 'r', encoding='utf-8') as dataset:
with open('../../data/Germany_filtered_shuffled.json', 'r', encoding='utf-8') as dataset:
    for line in dataset:
        n += 1
        try:
            tweet = json.loads(line)
        except ValueError:
            continue
        try:
            user_location = tweet['user']['location']
        except KeyError:
            print(json.dumps(tweet))
            key_errors += 1
            continue

        if user_location is None:
            empty_profile_locations += 1
        else:
            user_location = html.parser.HTMLParser().unescape(user_location)
            if len(user_location) == 0:
                empty_profile_locations += 1
            else:
                profile_locations += 1
                user_location = html.parser.HTMLParser().unescape(user_location)
                locations.add(user_location)
        if n % 10000 == 0:
            unique_locs = len(locations)
            print('n = {}, empty profiles = {}, profile locations = {} (unique = {}), key errors = {}'.format(
                n,
                empty_profile_locations,
                profile_locations,
                unique_locs,
                key_errors))

unique_locs = len(locations)
print('n = {}, empty profiles = {}, profile locations = {} (unique = {}), key errors = {}'.format(
    n,
    empty_profile_locations,
    profile_locations,
    unique_locs,
    key_errors))