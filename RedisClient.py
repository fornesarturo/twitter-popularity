class RedisClient:
    def __init__(self, redisHost='localhost', redisPort='6379', redisDb=0):
        import redis
        pool = redis.ConnectionPool(host=redisHost, port=redisPort, db=redisDb)
        self.redis = redis.Redis(connection_pool=pool)
        self.toAdd = set()

    def cleanRedis(self):
        self.redis.flushdb()

    def populateRedis(self, pathToCSV):
        if (self.redis.ping()):
            import pandas as pd
            csvNodes = pd.read_csv(pathToCSV)
            for i, row in csvNodes.iterrows():
                words = row['palabras'].split(" ")
                value = row['valor']

                for word in words:
                    if self.redis.exists(word):
                        self.redis.hincrby(word, "sum", amount=value)
                        self.redis.hincrby(word, "count", amount=1)
                    else:
                        self.redis.hset(word, "count", amount=1)
                        self.redis.hset(word, "sum", value)

            return True
        return False

    def getPhraseValue(self, phrase):
        phraseValue = 0
        for word in phrase:
            if self.redis.exists(word):
                wordSum = int(self.redis.hget(word, "sum").decode())
                wordCount = int(self.redis.hget(word, "count").decode())
                phraseValue += wordSum / wordCount
            else:
                self.toAdd.add(phrase)
        return phraseValue
