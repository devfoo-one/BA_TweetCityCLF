import json

from Utils.preprocessing.preproc_meta import MetaFeatureProcessor
from Utils.preprocessing.preproc_text import TextProcessor

# meta_preproc = MetaFeatureProcessor(extract_profile_location=True)
# with open('../../data/Germany_filtered_shuffled.json') as dataset:
#     for line in dataset:
#         try:
#             tweet = json.loads(line)
#         except ValueError:
#             continue
#         print(meta_preproc.digest(tweet))

text_preproc = TextProcessor(only_hashtags=True)
with open('../../data/Germany_filtered_shuffled.json') as dataset:
    for line in dataset:
        try:
            tweet = json.loads(line)
        except ValueError:
            continue
        print(text_preproc.digest(tweet))
