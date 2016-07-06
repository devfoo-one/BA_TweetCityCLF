from Utils import happyfuntokenizing


class Tokenizer:
    __remove_urls = False
    __remove_user_mentions = False
    __preserve_case = True
    __remove_hashtags = False

    def __init__(self, remove_urls=False, remove_user_mentions=False, remove_hashtags=False, preserve_case=True):
        self.__remove_urls = remove_urls
        self.__remove_user_mentions = remove_user_mentions
        self.__preserve_case = preserve_case
        self.__remove_hashtags = remove_hashtags
        # self.__hft__ = happyfuntokenizing.Tokenizer(preserve_case=self.__preserve_case__)

    def tokenize(self, tweet):
        tweet_text = tweet['text']

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

        if self.__remove_user_mentions:
            for mention in tweet['entities']['user_mentions']:
                tweet_text = tweet_text.replace('@' + mention['screen_name'], '')

        if self.__remove_hashtags:
            for hashtag in tweet['entities']['hashtags']:
                tweet_text = tweet_text.replace('#' + hashtag['text'], '')

        tokens = tweet_text.split()

        if not self.__preserve_case:
            pass

        return tokens
