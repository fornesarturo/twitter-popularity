"""
This will
"""
from BuildRedis import setClient
from RedisClient import RedisClient

def main():
    twitterClient = setClient()
    redisClient = RedisClient()

    username = input("¿Qué usuario quieres investigar?\n")
    date = input("Fecha en ")
    twitterClient.getTweets(username, )
    return

if __name__ == '__main__':
    main()
