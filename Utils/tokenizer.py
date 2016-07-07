import re

class Tokenizer:
    __remove_urls = False
    __remove_user_mentions = False
    __preserve_case = True
    __remove_hashtags = False
    __blind_urls = False

    def __init__(self, blind_urls=False, remove_urls=False, remove_user_mentions=False, remove_hashtags=False,
                 preserve_case=True):
        self.__remove_urls = remove_urls
        self.__remove_user_mentions = remove_user_mentions
        self.__preserve_case = preserve_case
        self.__remove_hashtags = remove_hashtags
        self.__blind_urls = blind_urls

    def tokenize(self, tweet):
        tweet_text = tweet['text']

        """remove URLs"""
        if self.__remove_urls:
            # collect all url strings (ugly but works)
            urls = []
            for url in tweet['entities']['urls']:
                urls.append(url['url'])
            try:
                for url in tweet['entities']['media']:
                    urls.append(url['url'])
            except KeyError:
                pass
            for url in urls:
                tweet_text = tweet_text.replace(url, '')

        """blind URLs"""
        if self.__blind_urls:
            for url in tweet['entities']['urls']:
                tweet_text = tweet_text.replace(url['url'], '[URL]')
            try:
                for url in tweet['entities']['media']:
                    tweet_text = tweet_text.replace(url['url'], '[MEDIA_URL]')
            except KeyError:
                pass

        """remove user mentions"""
        if self.__remove_user_mentions:
            for mention in tweet['entities']['user_mentions']:
                tweet_text = tweet_text.replace('@' + mention['screen_name'], '')

        """remove hashtags"""
        if self.__remove_hashtags:
            for hashtag in tweet['entities']['hashtags']:
                tweet_text = tweet_text.replace('#' + hashtag['text'], '')

        """tokenization, only whitespace for now..."""
        word_re = re.compile(r'[\s]+')
        tokens = word_re.split(tweet_text)

        if not self.__preserve_case:
            tokens = map(lambda x: str(x).lower(), tokens)

        return tokens
