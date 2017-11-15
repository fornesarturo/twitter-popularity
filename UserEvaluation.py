"""
This is the main module.
"""
import datetime as dt

from BuildRedis import set_client
from RedisClient import RedisClient

def main():
    """Main procedure.
    """
    twitter_client = set_client()
    redis_client = RedisClient()

    username = "pkumamoto"  # input("¿Qué usuario quieres investigar? ")
    date = "2017-11-14" # input("Fecha en formato yyyy-mm-dd: ")

    twitter_client.get_tweets(username, date, range_date=1)
    cleaned_data = twitter_client.clean_data(path="rawtweets.csv")

    twitter_client.save_tweets_csv(
        [tweet[0] for tweet in cleaned_data.values() if len(tweet[0]) > 0])
    popularity = redis_client.calculate_popularity(path_to_csv="rawtweets.csv")

    if popularity != None:
        print("{user} - {date}: {popularity}".format(
            user=username,
            date=date,
            popularity=popularity))
        redis_client.save_popularity(username, date, popularity)
    else:
        print("No tweets available for this date.")

if __name__ == '__main__':
    # main()
    REDIS_CLIENT = RedisClient()

    result = REDIS_CLIENT.get_popularity_history("pkumamoto")

    TWITTER_CLIENT = set_client()

    for key in result.keys():
        print(key.decode())
