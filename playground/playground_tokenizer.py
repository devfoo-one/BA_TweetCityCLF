import json

from Utils.preprocessing import preproc_text

# tok = tokenizer.Tokenizer(remove_urls=True, remove_user_mentions=True, remove_hashtags=True, preserve_case=True)
tok = preproc_text.TextProcessor(blind_urls=True, remove_user_mentions=True, remove_hashtags=False, transform_lowercase=True)
with open('../../data/Germany_filtered_shuffled.json') as dataset:
    for line in dataset:
        tweet = json.loads(line)
        print('---', tweet['text'], '---')
        tokens = tok.digest(tweet)
        print(tokens)
