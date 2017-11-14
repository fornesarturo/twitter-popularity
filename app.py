"""
This is the main module.
"""
import datetime as dt

from BuildRedis import setClient
from RedisClient import RedisClient

def main():
    twitterClient = setClient()
    redisClient = RedisClient()

    username = "lopezobrador_" #input("¿Qué usuario quieres investigar? ")
    date = "2017-11-13" #input("Fecha en formato yyyy-mm-dd: ")
    twitterClient.getTweets(username, dt.datetime.now().strftime("%Y-%m-%d"))
    cleanedData = twitterClient.cleanData(path="rawtweets.csv")
    twitterClient.prettyP(cleanedData)
    twitterClient.saveTweetsCSV([tweet[0] for tweet in cleanedData.values() if len(tweet[0]) > 0])
    popularity = redisClient.calculatePopularity(pathToCSV="rawtweets.csv", data=None)
    print("{user} - {date}: {popularity}".format(user=username, date=date, popularity=popularity))

if __name__ == '__main__':
    main()