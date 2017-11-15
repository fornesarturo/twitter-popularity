"""
This module aims to build the Database of Words.
"""
from TwitterClient import TwitterClient
from RedisClient import RedisClient

def get_keys():
    """Environment variables.
    """
    import os
    access_token = os.environ.get('AT', None)
    access_token_secret = os.environ.get('AT_S', None)
    consumer_key = os.environ.get('CON', None)
    consumer_key_secret = os.environ.get('CON_S', None)
    return (access_token, access_token_secret, consumer_key, consumer_key_secret)

def set_client():
    """Get Twitter Client
    """
    access_token, access_token_secret, consumer_key, consumer_key_secret = get_keys()
    client = TwitterClient(AT=access_token,
                           AT_S=access_token_secret,
                           CON=consumer_key,
                           CON_S=consumer_key_secret)
    return client

def clean_csv_data(client, debug=False, path="alltweets.csv"):
    """Interface to Data Cleaning.
    """
    data = client.clean_data(path, debug)
    do_redis(data)
    return data

def do_redis(cleaned_data):
    """Interface to Redis operations.
    """
    redis_client = RedisClient()
    redis_client.clean_redis()
    if redis_client.populate_redis(cleaned_data):
        print("Done.")
    else:
        print("False.")

def main():
    """Main function
    """
    client = set_client()

    #client.get_tweets("PedroFerriz", "2017-11-01", 14, "ferriztweets.csv")
    #client.getTweets("Mzavalagc", "2017-11-01", 10, "zavalatweets.csv")
    #client.getTweets("JoseAMeadeK", "2017-11-01", 10, "meadetweets.csv")

    ready = input("Ready to clean? (Write yes to proceed)\n")
    if ready.lower() == "yes":
        clean_csv_data(client)

if __name__ == '__main__':
    main()

'''

date = datetime.date(2017, 11, 1)
for i in range(11):
    
    myDate = date + datetime.timedelta(days = i)
    print(myDate.strftime("%d"))
    client.getTweets("lopezobrador_", myDate, "rawtweets"+ myDate.strftime("%d") +".csv")

def getTweets(self, account, date, file = "rawtweets.csv"):
        # Get Tweets and put them somewhere locally in this class or a
        # temp_file.

        import datetime

        if date.strftime("%Y-%m-%d") == datetime.datetime.now().strftime("%Y-%m-%d") or date == 0:
            query = "q=to%3A" + account + " %40" + account +" since%3A" + date.strftime("%Y-%m-%d")
        else:
            endDate = date + datetime.timedelta(days = 1)
            query = "q=to%3A" + account + " %40" + account + " since%3A" + date.strftime("%Y-%m-%d") + " until%3A" + endDate.strftime("%Y-%m-%d")
        
        feed = self.twitter.GetSearch(raw_query=query)
        textArray = []

        for tweet in feed:
            self.prettyP(tweet)
            if(tweet.full_text):
                textArray.append(tweet.full_text)
            else:
                textArray.append(tweet.text)

        self.saveTweetsCSV(textArray, file)
'''
