"""
This will
"""
import datetime as dt

from BuildRedis import setClient
from RedisClient import RedisClient

def main():
    twitterClient = setClient()
    redisClient = RedisClient()

    username = input("¿Qué usuario quieres investigar?\n")
    date = input("Fecha en formato Y-m-d")
    twitterClient.getTweets(username, dt.datetime.now().strftime("%Y-%m-%d"))
    return

if __name__ == '__main__':
    main()
