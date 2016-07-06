from Utils import happyfuntokenizing
from Utils import tokenizer
import json
twitter_tokenizer = happyfuntokenizing.Tokenizer()
twitter_tokenizer2 = tokenizer.Tokenizer()
with open('../../data/Germany_filtered.json') as dataset:
    for line in dataset:
        tweet = json.loads(line)
        print('---', tweet['text'], '---')
        for token in twitter_tokenizer2.tokenize(tweet['text']):
            print(token)