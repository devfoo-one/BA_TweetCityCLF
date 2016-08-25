import json

hashtag_collection = {}
hashtag_count_yes = 0
hashtag_count_no = 0
key_errors = 0
n = 0

with open('../../data/Germany_filtered_shuffled.json') as dataset:
    for line in dataset:
        try:
            tweet = json.loads(line)
        except ValueError:
            continue
        try:
            hashtags = tweet['entities']['hashtags']
        except KeyError:
            key_errors += 1
            continue

        has_hashtag = len(hashtags) == 0
        if has_hashtag:
            hashtag_count_yes += 1
            for tag in hashtags:
                hashtag_text = tag['text']
                if hashtag_text not in hashtag_collection.keys():
                    hashtag_collection[hashtag_text] = 0
                hashtag_collection[hashtag_text] += 1

        if not has_hashtag:
            hashtag_count_no += 1

        n += 1

        if n % 10000 == 0:
            print('n = {}, tweets with hashtag = {}, tweets without hashtag = {}, key_errors = {}, sum check = {}, unique hashtags = {}'.format(
                n,
                hashtag_count_yes,
                hashtag_count_no,
                key_errors,
                (hashtag_count_yes + hashtag_count_no + key_errors) == n,
                len(hashtag_collection.keys())
            ))
            print(hashtag_collection)
