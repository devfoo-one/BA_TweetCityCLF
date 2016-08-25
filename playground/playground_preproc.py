import json

from Utils.preprocessing.preproc_meta import MetaFeatureProcessor

meta_preproc = MetaFeatureProcessor(extract_profile_location=True)
with open('../../data/Germany_filtered_shuffled.json') as dataset:
    for line in dataset:
        try:
            tweet = json.loads(line)
        except ValueError:
            continue
        print(meta_preproc.digest(tweet))

# text_preproc = MetaFeatureProcessor(extract_profile_location=True)
# with open('../../data/Germany_filtered_shuffled.json') as dataset:
#     for line in dataset:
#         try:
#             tweet = json.loads(line)
#         except ValueError:
#             continue
#         print(meta_preproc.digest(tweet))
