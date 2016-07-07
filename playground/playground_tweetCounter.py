import json

total = 0
rt = 0
nowplaying = 0
with open('../../data/Germany_filtered_shuffled.json') as dataset:
    for line in dataset:
        total += 1
        tweet = json.loads(line)
        # if tweet['retweeted']:
        #     rt += 1
        #     print(json.dumps(tweet))
        # if total % 10000 == 0:
        #     print(total, '/', rt)

        hashtags = tweet['entities']['hashtags']

        for tag in hashtags:
            if tag['text'].lower() == 'nowplaying':
                nowplaying += 1
                print(tweet['text'])
                break

        if total % 10000 == 0:
            print(total, '/', nowplaying, '/', (nowplaying * 100) / total)

    print(total, '/', nowplaying, '/', (nowplaying * 100) / total)