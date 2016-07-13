import json
from Utils import tweet_preprocessor

# tok = tokenizer.Tokenizer(remove_urls=True, remove_user_mentions=True, remove_hashtags=True, preserve_case=True)
tok = tweet_preprocessor.Processor(blind_urls=True, remove_user_mentions=True, remove_hashtags=False, preserve_case=True)
with open('../../data/Germany_filtered_shuffled.json') as dataset:
    for line in dataset:
        tweet = json.loads(line)
        print('---', tweet['text'], '---')
        tokens = tok.digest(tweet)
        print(tokens)
