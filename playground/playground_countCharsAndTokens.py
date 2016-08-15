import html.parser
import json
import pickle

count_chars = {}
count_tokens = {}
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
            chars = len(text)
            tokens = len(text.split())
            if chars not in count_chars.keys():
                count_chars[chars] = 0
            if tokens not in count_tokens.keys():
                count_tokens[tokens] = 0
            count_chars[chars] += 1
            count_tokens[tokens] += 1

        if n % 10000 == 0:
            print(n)

with open('count_chars.pickle', mode='wb') as count_chars_f:
    with open('count_tokens.pickle', mode='wb') as count_tokens_f:
        pickle.dump(count_chars, count_chars_f)
        pickle.dump(count_tokens, count_tokens_f)
