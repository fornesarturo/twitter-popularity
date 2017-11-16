"""
RedisClient handles interaction with a local Redis Database.
"""
class RedisClient:
    """Handles interaction with a local Redis Database.
    """
    def __init__(self, redisHost='localhost', redisPort='6379', redisDb=0):
        import redis
        pool = redis.ConnectionPool(host=redisHost, port=redisPort, db=redisDb)
        self.redis = redis.Redis(connection_pool=pool)
        self.to_add = set()

    def clean_redis(self):
        """Clean the Database.
        """
        self.redis.flushdb()

    def populate_redis(self, data):
        """
        data has the following format
            {index: [tweet, value], ...}
        """
        if self.redis.ping():
            for (tweet, value) in data.values():
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

    def get_tweet_value(self, phrase):
        """Based on a tweet as string, return its value.
        """
        phrase_value = 0
        for word in phrase:
            if self.redis.exists(word):
                word_sum = float(self.redis.hget(word, "sum").decode())
                word_count = float(self.redis.hget(word, "count").decode())
                phrase_value += word_sum / word_count
            else:
                self.to_add.add(phrase)
        return phrase_value

    def calculate_popularity(self, path_to_csv):
        """Return the popularity of the tweets in a CSV.
        """
        import pandas as pd

        accum = 0
        csv_dataframe = pd.read_csv(path_to_csv)
        if (csv_dataframe.size == 0):
            return None
        iterrows = [row[1] for row in csv_dataframe.iterrows()]
        for row in iterrows:
            words = row['Tweet']
            accum = accum + self.get_tweet_value(words)
        return accum/csv_dataframe.size
    
    def save_popularity(self, username, date, popularity):
        """Save the popularity to a hash of the username
        """
        if self.redis.ping():
            redis_name = username + "_tweets_popularity"
            if self.redis.exists(redis_name):
                if self.redis.hset(redis_name, date, popularity) == 1:
                    print("Register created.")
            else:
                if self.redis.hset(redis_name, date, popularity) == 1:
                    print("New user + register created.")
        else:
            print("Couldn't connect to Redis.")
    
    def get_popularity_history(self, username):
        """
        Get the popularity stored in Redis in the
        username's hash.
        """
        if self.redis.ping():
            redis_name = username + "_tweets_popularity"
            if self.redis.exists(redis_name):
                h_all = self.redis.hgetall(redis_name)
                user_dictionary = {}
                user_dictionary[username] = []
                for key, value in zip(h_all.keys(), h_all.values()):
                    key_string = key.decode()
                    value_float = float(value)
                    user_dictionary[username].append((key_string, value_float))
                return user_dictionary
            else:
                return None
        else:
            return None

    def get_usernames(self):
        """Returns a list of the usernames currently in Redis
        """
        if self.redis.ping():
            users = self.redis.keys("*_tweets_popularity")
            user_list = [user.decode() for user in users]
            for i, user in enumerate(user_list):
                user_list[i] = user.replace("_tweets_popularity", "")
            return user_list
        else:
            return []
