
class TwitterClient:
    def __init__(self, AT, AT_S, CON, CON_S, redisHost='localhost', redisPort='6379', redisDb=0):
        import twitter
        self.twitter = twitter.api.Api(consumer_key=CON, consumer_secret=CON_S, access_token_key=AT, access_token_secret=AT_S, tweet_mode='extended')

    def getTweets(self, queryParam):
        # Get Tweets and put them somewhere locally in this class or a
        # temp_file.

        feed = self.twitter.GetSearch(term=queryParam)
        textArray = []

        for tweet in feed:
            if(tweet.full_text):
                textArray.append(tweet.full_text)
            else:
                textArray.append(tweet.text)

        self.saveTweetsCSV(textArray, "rawtweets.csv")

    def cleanData(self, path = "rawtweets.csv", debug=False):
        # Clean the data you got from getTweets, again, store in this class or
        # in a temp_file.
        import unidecode

        data = self.openTweetsCSV(path)
        jData = self.openStopWords('stopwords.json')

        cleanData = {}
        for i, v in data.items():
            wordsArray = v[0].split(" ")
            cleanWords = []
            for word in wordsArray:
                wordU = unidecode.unidecode(word)
                if wordU not in jData:
                    cleanWords.append(wordU)
            cleanData[i] = [" ".join(cleanWords), v[1]]

        if (debug):
            self.prettyP(cleanData)
        return cleanData # Dictionary of cleansed tweets with assigned value

    def toCSV(self):
        # Maybe call this function after getTweets or cleanData to store the
        # output as a CSV.
        return

    def fromCSV(self, pathToCSV):
        # To read from a CSV into methods like cleanData
        return

    def openStopWords(self, path):
        import json
        with open(path) as jFile:
            jData = json.load(jFile)
        return jData

    def saveTweetsCSV(self, data, path = "rawtweets.csv"):
        import pandas as pd
        df = pd.DataFrame(data, columns=["Tweet"])
        df["Value"] = 'Undef'
        df.to_csv(path, index=False, encoding='utf-8')
        print(df)

    def openTweetsCSV(self, path):
        gradedTweets = {}
        import csv
        with open(path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            next(readCSV, None)
            for i, row in enumerate(readCSV):
                gradedTweets[i] = [row[0], row[1]]

        return gradedTweets # Dictionary of tweets with assigned value

    def prettyP(self, data):
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(data)
