class MetaFeatureProcessor:
    config = {
        'extract_profile_location': False,
    }

    def __init__(self, extract_profile_location=False):
        self.config['extract_profile_location'] = extract_profile_location

    def digest(self, tweet):
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

        return ' '.join(features)

    def __call__(self, tweet):
        return self.digest(tweet)

    def __str__(self):
        return ', '.join([attr + '=' + str(val) for attr, val in self.config.items()])
