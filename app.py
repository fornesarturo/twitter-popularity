"""
This is the main module.
"""
import datetime as dt

from BuildRedis import set_client
from RedisClient import RedisClient

def main():
    twitter_client = set_client()
    redis_client = RedisClient()

    username = "g_quadri"  # input("¿Qué usuario quieres investigar? ")
    date = "2017-11-13" #input("Fecha en formato yyyy-mm-dd: ")

    twitter_client.get_tweets(username, dt.datetime.now().strftime("%Y-%m-%d"))
    cleaned_data = twitter_client.clean_data(path="rawtweets.csv")
    # twitterClient.prettyP(cleanedData)

    twitter_client.save_tweets_csv(
        [tweet[0] for tweet in cleaned_data.values() if len(tweet[0]) > 0])
    popularity = redis_client.calculate_popularity(path_to_csv="rawtweets.csv")

    print("{user} - {date}: {popularity}".format(user=username, date=date, popularity=popularity))

if __name__ == '__main__':
    main()
