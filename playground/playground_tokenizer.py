import json

from Utils.tokenization import Tokenize

tok = Tokenize.TweetTokenizer()

with open('../../data/Germany_filtered_shuffled.json') as dataset:
    for line in dataset:
        tweet = json.loads(line)
        print('TWEET: "', tweet['text'], '"', sep='')
        tokens = tok(tweet['text'])
        for t in tokens:
            print('\tTOKEN: "',t,'"', sep='')
            if len(t) == 1:
                print('\t\tFOUND SINGLE CHAR TOKEN "', t, '" ', ord(t), sep='')
