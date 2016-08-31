import json

from Preprocessing import TextProcessor, MetaFeatureProcessor

# meta_preproc = MetaFeatureProcessor(extract_profile_location=True)
# with open('../../data/Germany_filtered_shuffled.json') as dataset:
#     for line in dataset:
#         try:
#             tweet = json.loads(line)
#         except ValueError:
#             continue
#         print(meta_preproc.digest(tweet))

text_preproc = TextProcessor(only_hashtags=True)
# meta_preproc = MetaFeatureProcessor(extract_profile_location=True)
meta_preproc = MetaFeatureProcessor(extract_user_id=True)
with open('../../data/Germany_filtered_shuffled.json') as dataset:
    for line in dataset:
        try:
            tweet = json.loads(line)
        except ValueError:
            continue
        # print(text_preproc.digest(tweet))
        print(meta_preproc.digest(tweet))
