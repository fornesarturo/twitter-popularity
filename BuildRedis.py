"""
This module aims to build the Database of Words.
"""
from TwitterClient import TwitterClient
from RedisClient import RedisClient

def getKeys():
    import os
    AT = os.environ.get('AT', None)
    AT_S = os.environ.get('AT_S', None)
    CON = os.environ.get('CON', None)
    CON_S = os.environ.get('CON_S', None)
    return (AT, AT_S, CON, CON_S)

def setClient():
    AT, AT_S, CON, CON_S = getKeys()
    client = TwitterClient(AT=AT, AT_S=AT_S, CON=CON, CON_S=CON_S)
    return client

def cleanCSVData(client, debug = False, path = "alltweets.csv"):
    data = client.cleanData(path, debug)
    doREDIS(data)
    return data

def doREDIS(cleanedData):
    redisClient = RedisClient()
    redisClient.cleanRedis()
    if redisClient.populateRedis(cleanedData):
        print ("Done.")
    else:
        print ("False.")

def main():
    
    client = setClient()

    client.getTweets("JorgeGCastaneda", "2017-11-01", 10, "castanedatweets.csv")
    client.getTweets("Mzavalagc", "2017-11-01", 10, "zavalatweets.csv")
    client.getTweets("JoseAMeadeK", "2017-11-01", 10, "meadetweets.csv")

    ready = input("Ready to clean? (Write yes to proceed)\n")
    if ready.lower() == "yes":
        cleanCSVData(client)

if __name__=='__main__':
    
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

