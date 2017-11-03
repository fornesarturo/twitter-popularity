import twitter

class TwitterClient:
    def __init__(self, AT, AT_S, CON, CON_S):
        import twitter

        self.t = twitter.api.Api(consumer_key=CON, consumer_secret=CON_S, access_token_key=AT, access_token_secret=AT_S, tweet_mode='extended')
