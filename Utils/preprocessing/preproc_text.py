import re


class TextProcessor:
    __remove_urls__ = False
    __remove_user_mentions__ = False
    __transform_lowercase__ = True
    __remove_hashtags__ = False
    __blind_urls__ = False
    __expand_urls__ = True

    def __init__(self, blind_urls=False, remove_urls=False, remove_user_mentions=False, remove_hashtags=False,
                 transform_lowercase=True, expand_urls=True):
        self.__remove_urls__ = remove_urls
        self.__remove_user_mentions__ = remove_user_mentions
        self.__transform_lowercase__ = transform_lowercase
        self.__remove_hashtags__ = remove_hashtags
        self.__blind_urls__ = blind_urls
        self.__expand_urls__ = expand_urls

    def digest(self, tweet):
        """Processes a tweet object (as given from the streaming api) and returns a string."""
        tweet_text = tweet['text']

        """remove URLs"""
        if self.__remove_urls__:
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
        if self.__blind_urls__:
            for url in tweet['entities']['urls']:
                tweet_text = tweet_text.replace(url['url'], '[URL]')
            try:
                for url in tweet['entities']['media']:
                    tweet_text = tweet_text.replace(url['url'], '[MEDIA_URL]')
            except KeyError:
                pass

        """remove user mentions"""
        if self.__remove_user_mentions__:
            for mention in tweet['entities']['user_mentions']:
                tweet_text = tweet_text.replace('@' + mention['screen_name'], '')

        """remove hashtags"""
        if self.__remove_hashtags__:
            for hashtag in tweet['entities']['hashtags']:
                tweet_text = tweet_text.replace('#' + hashtag['text'], '')

        """transform to lowercase"""
        if self.__transform_lowercase__:
            tweet_text = tweet_text.lower()

        """expand urls"""
        if self.__expand_urls__:
            urls = []
            for url in tweet['entities']['urls']:
                urls.append((url['url'], url['expanded_url']))
            try:
                for url in tweet['entities']['media']:
                    urls.append((url['url'], url['expanded_url']))
            except KeyError:
                pass
            for url, expanded_url in urls:
                tweet_text = tweet_text.replace(url, expanded_url)

        return tweet_text

    def __call__(self, tweet):
        return self.digest(tweet)