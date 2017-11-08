class RedisClient:
    def __init__(self, redisHost='localhost', redisPort='6379', redisDb=0):
        import redis
        pool = redis.ConnectionPool(host=redisHost, port=redisPort, db=redisDb)
        self.redis = redis.Redis(connection_pool=pool)

    def populateRedis(self, pathToCSV):
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
