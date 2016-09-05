class TextProcessor:
    config = {
        'remove_urls': False,
        'remove_user_mentions': False,
        'transform_lowercase': True,
        'remove_hashtags': False,
        'blind_urls': False,
        'expand_urls': True
    }

    def __init__(self, blind_urls=False, remove_urls=False, remove_user_mentions=False, remove_hashtags=False,
                 transform_lowercase=True, expand_urls=True, only_hashtags=False):
        """
        Initialises a TextPreprocessor with given configuration
        :param blind_urls: replace urls with [URL] or [MEDIA]
        :param remove_urls: remove urls
        :param remove_user_mentions: remove user mentions
        :param remove_hashtags: remove hashtags
        :param transform_lowercase: transform everything to lowercase
        :param expand_urls: transform twitter short urls to real urls
        :param only_hashtags: return only hashtags
        """
        self.config['remove_urls'] = remove_urls
        self.config['remove_user_mentions'] = remove_user_mentions
        self.config['transform_lowercase'] = transform_lowercase
        self.config['remove_hashtags'] = remove_hashtags
        self.config['only_hashtags'] = only_hashtags
        self.config['blind_urls'] = blind_urls
        self.config['expand_urls'] = expand_urls

    def digest(self, tweet):
        """
        Processes a Tweet object (as given from the streaming api) and returns a string.
        Processing is done according to initial configuration.
        :param tweet: Tweet, as given from the streaming api
        :return: processed tweet as String
        """
        tweet_text = tweet['text']

        """only hashtags"""
        if self.config['only_hashtags']:
            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['text'])
            return ' '.join(hashtags)

        """remove URLs"""
        if self.config['remove_urls']:
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
        if self.config['blind_urls']:
            for url in tweet['entities']['urls']:
                tweet_text = tweet_text.replace(url['url'], '[URL]')
            try:
                for url in tweet['entities']['media']:
                    tweet_text = tweet_text.replace(url['url'], '[MEDIA_URL]')
            except KeyError:
                pass

        """remove user mentions"""
        if self.config['remove_user_mentions']:
            for mention in tweet['entities']['user_mentions']:
                tweet_text = tweet_text.replace('@' + mention['screen_name'], '')

        """remove hashtags"""
        if self.config['remove_hashtags']:
            for hashtag in tweet['entities']['hashtags']:
                tweet_text = tweet_text.replace('#' + hashtag['text'], '')

        """transform to lowercase"""
        if self.config['transform_lowercase']:
            tweet_text = tweet_text.lower()

        """expand urls"""
        if self.config['expand_urls']:
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
        """
        Calls digest(tweet)
        :param tweet: Tweet, as given from the streaming api
        :return: String
        """
        return self.digest(tweet)

    def __str__(self):
        return ', '.join([attr + '=' + str(val) for attr, val in self.config.items()])


class MetaFeatureProcessor:
    config = {
        'extract_profile_location': False,
        'extract_user_id': False
    }

    def __init__(self, extract_profile_location=False, extract_user_id=False):
        """
        Initialises a TextPreprocessor with given configuration
        :param extract_profile_location: extract profile location field (user object)
        :param extract_user_id: extract id of user object
        """
        self.config['extract_profile_location'] = extract_profile_location
        self.config['extract_user_id'] = extract_user_id

    def digest(self, tweet):
        """
        Processes a Tweet object (as given from the streaming api) and returns a string.
        Processing is done according to initial configuration.
        :param tweet: Tweet, as given from the streaming api
        :return: processed tweet as String
        """
        features = []

        """extract user location"""
        if self.config['extract_profile_location']:
            try:
                user_location = tweet['user']['location']
            except KeyError:
                user_location = None
            if user_location is None or len(user_location) == 0:
                user_location = ''
            features.append(user_location)

        if self.config['extract_user_id']:
            user_id = str(tweet['user']['id'])
            features.append(user_id)

        return ' '.join(features)

    def __call__(self, tweet):
        """
       Calls digest(tweet)
       :param tweet: Tweet, as given from the streaming api
       :return: String
       """
        return self.digest(tweet)

    def __str__(self):
        return ', '.join([attr + '=' + str(val) for attr, val in self.config.items()])
