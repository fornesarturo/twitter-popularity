"""
TwitterClient handles interaction with Twitter API.
"""

class TwitterClient:
    """
    TwitterClient handles interaction with Twitter API.
    """
    def __init__(self, AT, AT_S, CON, CON_S):
        import twitter
        self.twitter = twitter.api.Api(consumer_key=CON,
                                       consumer_secret=CON_S,
                                       access_token_key=AT,
                                       access_token_secret=AT_S,
                                       tweet_mode='extended')

    def get_tweets(self, account, initial_date=None, range_date=0, file="rawtweets.csv"):
        """
        Get Tweets and put them in a temp_file.
        """
        import datetime as dt

        if initial_date == dt.datetime.now().strftime("%Y-%m-%d"):
            query = "q=to%3A" + account + " %40" + account +\
                    " since%3A" + initial_date +\
                    "&count=100"
        else:
            until = dt.datetime.strptime(initial_date, "%Y-%m-%d") + dt.timedelta(days=range_date)
            query = "q=to%3A" + account + " %40" + account +\
                    " since%3A" + initial_date+\
                    " until%3A" + until.strftime("%Y-%m-%d")+"&count=100"

        feed = self.twitter.GetSearch(raw_query=query)
        text_array = []
        for tweet in feed:
            if tweet.full_text:
                text_array.append(tweet.full_text)
            else:
                text_array.append(tweet.text)

        self.save_tweets_csv(text_array, file)

    def clean_data(self, path="alltweets.csv", debug=False):
        """Clean the data you got from getTweets.
        Return a dictionary of cleansed tweets with assigned value
        """
        import unidecode
        symbols = list('''!()-[]{};:+'´"\\,<>.=/?@#$%^&*_~''')

        data = self.open_tweets_csv(path)
        json_data = self.open_stop_words('stopwords.json')

        clean_data = {}
        for i, value in data.items():
            words_array = value[0].split(" ")
            clean_words = []
            for word in words_array:
                word_uni = unidecode.unidecode(word.lower())
                if word_uni and word_uni not in json_data and \
                word[0] != '@' and word[0] != '#' and word_uni.find("http"):
                    for letter in word_uni:
                        if letter in symbols:
                            word_uni = word_uni.replace(letter, '')
                    word_uni = word_uni.replace('\n', '')
                    word_length = len(word_uni)
                    if word_length > 0 and clean_data != "":
                        clean_words.append(word_uni)
            clean_data[i] = [" ".join(clean_words), value[1]]

        if debug:
            self.pretty_print(clean_data)
        return clean_data

    def open_stop_words(self, path):
        """Returns stop words as a json dictionary.
        """
        import json
        with open(path) as json_file:
            json_data = json.load(json_file)
        return json_data

    def save_tweets_csv(self, data, path="rawtweets.csv"):
        """Save Tweets as CSV file.
        """
        import pandas as pd
        dataframe = pd.DataFrame(data, columns=["Tweet"])
        dataframe["Value"] = 'Undef'
        dataframe.to_csv(path, index=False, encoding='utf-8')

    def open_tweets_csv(self, path):
        """Open tweets and return them as a dictionary
        """
        import csv
        graded_tweets = {}
        with open(path) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')
            next(read_csv, None)
            for i, row in enumerate(read_csv):
                if len(row) == 2:
                    graded_tweets[i] = [row[0], row[1]]

        return graded_tweets

    def pretty_print(self, data):
        """Pretty print interface.
        """
        import pprint

        pretty_printer = pprint.PrettyPrinter(indent=4)
        pretty_printer.pprint(data)
