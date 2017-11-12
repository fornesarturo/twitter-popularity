class TwitterClient:
    
    def __init__(self, AT, AT_S, CON, CON_S, redisHost='localhost', redisPort='6379', redisDb=0):
        import twitter
        self.twitter = twitter.api.Api(consumer_key=CON, consumer_secret=CON_S, access_token_key=AT, access_token_secret=AT_S, tweet_mode='extended')

    def getTweets(self, account, initialDate, rangeD = 0, file = "rawtweets.csv", debug=False):
        # Get Tweets and put them somewhere locally in this class or a
        # temp_file.

        # q=to%3Alopezobrador_ %40lopezobrador_ since%3A2017-11-01 until%3A2017-11-10&count=100
        import datetime
        if initialDate == datetime.datetime.now().strftime("%Y-%m-%d"):
            query = "q=to%3A" + account + " %40" + account + " since%3A" + initialDate + "&count=100"
        else:
            untilD = datetime.datetime.strptime(initialDate, "%Y-%m-%d") + datetime.timedelta(days=rangeD)
            query = "q=to%3A" + account + " %40" + account + " since%3A" + initialDate + " until%3A" + untilD.strftime("%Y-%m-%d") + "&count=100"
        
        feed = self.twitter.GetSearch(raw_query=query)
        
        textArray = []
        if debug:
            print(query)
        for tweet in feed:
            if debug:
                self.prettyP(tweet)
            if(tweet.full_text):
                textArray.append(tweet.full_text)
            else:
                textArray.append(tweet.text)

        self.saveTweetsCSV(textArray, file)

    def cleanData(self, path = "rawtweets.csv", debug=False):
        # Clean the data you got from getTweets, again, store in this class or
        # in a temp_file.
        import unidecode
        symbols = list('''!()-[]{};:+'´"\,<>.=/?@#$%^&*_~''')

        data = self.openTweetsCSV(path)
        jData = self.openStopWords('stopwords.json')

        cleanData = {}
        for i, v in data.items():
            wordsArray = v[0].split(" ")
            cleanWords = []
            for word in wordsArray:
                wordU = unidecode.unidecode(word.lower())
                if wordU and wordU not in jData and word[0] != '@' and word[0] != '#' and wordU.find("http"):
                    for letter in wordU:
                        if letter in symbols:
                            wordU = wordU.replace(letter, '')
                    wordU = wordU.replace('\n', '')
                    if len(wordU) > 0 and cleanData != "":
                        cleanWords.append(wordU)
            cleanData[i] = [" ".join(cleanWords), v[1]]

        if (debug):
            self.prettyP(cleanData)
        return cleanData # Dictionary of cleansed tweets with assigned value

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
