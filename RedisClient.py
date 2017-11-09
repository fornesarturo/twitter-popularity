class RedisClient:
    def __init__(self, redisHost='localhost', redisPort='6379', redisDb=0):
        import redis
        pool = redis.ConnectionPool(host=redisHost, port=redisPort, db=redisDb)
        self.redis = redis.Redis(connection_pool=pool)
        self.toAdd = set()

    def cleanRedis(self):
        self.redis.flushdb()

    def populateRedis(self, data):
        """
        data has the following format
            {index: [tweet, value], ...}
        """
        if (self.redis.ping()):
            for i, (tweet, value) in zip(data.keys(), data.values()):
                words = tweet.split(" ")

                for word in words:
                    if self.redis.exists(word):
                        self.redis.hincrby(word, "sum", amount=value)
                        self.redis.hincrby(word, "count", amount=1)
                    else:
                        self.redis.hset(word, "count", 1)
                        self.redis.hset(word, "sum", value)
            return True
        return False

    def getTweetValue(self, phrase):
        phraseValue = 0
        for word in phrase:
            if self.redis.exists(word):
                wordSum = int(self.redis.hget(word, "sum").decode())
                wordCount = int(self.redis.hget(word, "count").decode())
                phraseValue += wordSum / wordCount
            else:
                self.toAdd.add(phrase)
        return phraseValue

    def calculatePopularity(pathToCSV):
        import pandas as pd

        accum = 0
        csvDataFrame = pd.read_csv(pathToCSV)
        for i, row in csvDataFrame.iterrows():
            words = row['Tweet']
            accum += getTweetValue(words)
        return accum / csvDataFrame.size
