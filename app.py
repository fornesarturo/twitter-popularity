if __name__=='__main__':

    import os
    import pprint as pp
    from TwitterClient import TwitterClient
    from RedisClient import RedisClient

    AT = os.environ.get('AT', None)
    AT_S = os.environ.get('AT_S', None)
    CON = os.environ.get('CON', None)
    CON_S = os.environ.get('CON_S', None)

    # Building the database
    client = TwitterClient(AT=AT, AT_S=AT_S, CON=CON, CON_S=CON_S)
    #client.getTweets("@lopezobrador_")

    cleanedData = client.cleanData("rawtweets.csv")
    redisClient = RedisClient()

    redisClient.cleanRedis()
    if redisClient.populateRedis(cleanedData):
        print ("Done.")
    else:
        print ("False.")

    # Get new tweets

    client = TwitterClient(AT=AT, AT_S=AT_S, CON=CON, CON_S=CON_S)
