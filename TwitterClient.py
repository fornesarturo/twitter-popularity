class TwitterClient:
    def __init__(self, AT, AT_S, CON, CON_S, redisHost='localhost', redisPort='6379', redisDb=0):
        import twitter
        self.twitter = twitter.api.Api(consumer_key=CON, consumer_secret=CON_S, access_token_key=AT, access_token_secret=AT_S, tweet_mode='extended')
