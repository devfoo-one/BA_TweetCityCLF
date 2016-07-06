import json
from Utils import tokenizer

tok = tokenizer.Tokenizer(remove_urls=True, remove_user_mentions=True, remove_hashtags=True, preserve_case=False)
with open('../../data/Germany_filtered_shuffled.json') as dataset:
    for line in dataset:
        tweet = json.loads(line)
        print('---', tweet['text'], '---')
        for token in tok.tokenize(tweet):
            print(token)
            pass
