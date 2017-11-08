class TwitterClient:
    def __init__(self, AT, AT_S, CON, CON_S, redisHost='localhost', redisPort='6379', redisDb=0):
        import twitter
        self.twitter = twitter.api.Api(consumer_key=CON, consumer_secret=CON_S, access_token_key=AT, access_token_secret=AT_S, tweet_mode='extended')

    def getTweets(self, queryParam):
        # Get Tweets and put them somewhere locally in this class or a
        # temp_file.
        return

    def cleanData(self, data):
        # Clean the data you got from getTweets, again, store in this class or
        # in a temp_file.
        return

    def toCSV(self):
        # Maybe call this function after getTweets or cleanData to store the
        # output as a CSV.
        return

    def fromCSV(self, pathToCSV):
        # To read from a CSV into methods like cleanData
        return
