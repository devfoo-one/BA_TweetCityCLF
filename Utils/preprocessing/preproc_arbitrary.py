class ArbitraryFeatureProcessor:
    config = {
        'extract_profile_location': False,
    }

    def __init__(self, extract_profile_location=False):
        self.config['extract_profile_location'] = extract_profile_location

    def digest(self, tweet):
        features = []
        """Processes a tweet object (as given from the streaming api) and returns a string."""  # TODO UPDATE ME
        tweet_text = tweet['text']

        """remove URLs"""
        if self.config['extract_profile_location']:
            # do something
            pass

        return ' '.join(features)

    def __call__(self, tweet):
        return self.digest(tweet)

    def __str__(self):
        return ', '.join([attr + '=' + str(val) for attr, val in self.config.items()])
