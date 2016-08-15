import json, langid

count_tweetDE = 0
count_lang_id_de = 0
# with open('../../data/Germany_filtered.json') as dataset:
with open('../../data/Germany.json') as dataset:
    for line in dataset:
        try:
            tweet = json.loads(line)
        except ValueError:
            continue
        text = tweet['text']
        lang_tweet = tweet['lang']
        if lang_tweet == 'de':
            count_tweetDE += 1
            lang, score = langid.classify(text)
            if lang == 'de':
                count_lang_id_de += 1
            if count_tweetDE % 1000 == 0:
                print(count_tweetDE, count_lang_id_de, (count_lang_id_de / count_tweetDE) * 100)

