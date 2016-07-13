from Utils import happyfuntokenizing
from Utils import tweet_preprocessor
import json
twitter_tokenizer = happyfuntokenizing.Tokenizer()
twitter_tokenizer2 = tweet_preprocessor.Processor()
with open('../../data/Germany_filtered.json') as dataset:
    for line in dataset:
        tweet = json.loads(line)
        print('---', tweet['text'], '---')
        for token in twitter_tokenizer2.digest(tweet['text']):
            print(token)