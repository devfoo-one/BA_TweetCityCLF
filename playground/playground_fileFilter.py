"""Takes the main dataset and filters out all lines wich are not necessary"""

import json

# with open('../../data/Germany_filtered.json', mode='w', encoding='utf8', newline='') as outputfile:
#     for line in open('../../data/Germany.json'):
#         try:
#             jsonObj = json.loads(line)
#         except ValueError:
#             continue  # could not decode json line, skipping.
#         try:
#             if (jsonObj['lang'] == 'de') and (jsonObj['place'] is not None) and (
#                         jsonObj['place']['place_type'] == 'city'):
#                 outputfile.write(line)
#         except KeyError:
#             continue  # Tweet has no lang or place.placetype. skipping.


# with open('../../data/Germany_filtered_shuffled_v2.json', mode='w', encoding='utf8', newline='') as outputfile:
#     for line in open('../../data/Germany_filtered_shuffled.json'):
#         try:
#             jsonObj = json.loads(line)
#         except ValueError:
#             continue  # could not decode json line, skipping.
#         try:
#             if (jsonObj['lang'] == 'de') and (jsonObj['place'] is not None) and (
#                         jsonObj['place']['place_type'] == 'city') and jsonObj['place']['country_code'] == 'DE':
#                 outputfile.write(line)
#         except KeyError:
#             continue  # Tweet has no lang or place.placetype. skipping.

# TOP 10 CLASSES ONLY
top_10_class_ids = [
    '3078869807f9dd36',
    '5bcd72da50f0ee77',
    'c589d9d6ed38927c',
    '8abc99434d4f5d28',
    '37439688c6302728',
    'b7d3c12268abd20e',
    '659395aaea6aa724',
    'e385d4d639c6a423',
    '5eefdd08491a1c89',
    '48504653e183c91c'
]
with open('../../data/Germany_filtered_shuffled_top10classes.json', mode='w', encoding='utf8',
          newline='') as outputfile:
    for line in open('../../data/Germany_filtered_shuffled.json'):
        try:
            jsonObj = json.loads(line)
        except ValueError:
            continue  # could not decode json line, skipping.
        try:
            if jsonObj['place']['id'] in top_10_class_ids:
                outputfile.write(line)
        except KeyError:
            continue  # Tweet has no lang or place.placetype. skipping.
