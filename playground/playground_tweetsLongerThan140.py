import html.parser
import json

n = 0
with open('../../data/Germany.json', 'r', encoding='utf-8') as dataset:
    for line in dataset:
        n += 1
        try:
            tweet = json.loads(line)
        except ValueError:
            continue
        try:
            lang = tweet['lang']
        except KeyError:
            continue
        if lang == 'de':
            text = html.parser.HTMLParser().unescape(tweet['text'])
            if len(text) > 140:
                print(n,' - ', tweet['created_at'], ': "', text, '", len:',len(text), sep='')