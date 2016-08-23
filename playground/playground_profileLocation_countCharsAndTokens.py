import html.parser
import json
import pickle

count_chars = {}
count_tokens = {}
n = 0
# with open('../../data/Germany.json', 'r', encoding='utf-8') as dataset:
with open('../../data/Germany_filtered_shuffled.json', 'r', encoding='utf-8') as dataset:
    for line in dataset:
        n += 1
        try:
            tweet = json.loads(line)
        except ValueError:
            continue
        try:
            user_location = tweet['user']['location']
        except KeyError:
            continue

        if user_location is not None:
            user_location = html.parser.HTMLParser().unescape(user_location)
            chars = len(user_location)
            tokens = len(user_location.split())
            if chars not in count_chars.keys():
                count_chars[chars] = 0
            if tokens not in count_tokens.keys():
                count_tokens[tokens] = 0
            count_chars[chars] += 1
            count_tokens[tokens] += 1

        if n % 10000 == 0:
            print(n)

with open('userLocation_count_chars.pickle', mode='wb') as count_chars_f:
    with open('userLocation_count_tokens.pickle', mode='wb') as count_tokens_f:
        pickle.dump(count_chars, count_chars_f)
        pickle.dump(count_tokens, count_tokens_f)

print(count_chars)
print(count_tokens)