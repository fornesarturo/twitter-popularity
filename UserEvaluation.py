"""
This is the main module.
"""
import datetime as dt
from BuildRedis import set_client
from RedisClient import RedisClient
from PlotPopularity import print_popularity

MORENA = ["lopezobrador_"]
PAN = ["RicardoAnayaC", "luisederbez", "RafaMorenoValle", "JCRomeroHicks"]
PRI = ["eruviel_avila", "MFBeltrones", "JoseAMeadeK", "aurelionuno", "IvonneOP", "osoriochong",
       "LVidegaray"]
PRD = ["Silvano_A", "ManceraMiguelMX"]
INDEPENDENT = ["Mzavalagc", "RiosPiterJaguar", "JaimeRdzNL", "PedroFerriz"]

def do_evaluation(username, date):
    '''Do twitter evaluation
    '''
    twitter_client = set_client()
    redis_client = RedisClient()

    #username = "pkumamoto"  # input("¿Qué usuario quieres investigar? ")
    #date = "2017-11-14" # input("Fecha en formato yyyy-mm-dd: ")

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

def string_to_list(argument):
    '''Switch functionality
    '''
    switcher = {
        "PRD": PRD,
        "MORENA": MORENA,
        "PRI": PRI,
        "PAN": PAN,
        "INDEPENDENT": INDEPENDENT
    }
    
    if len(argument.split("+")) > 1:
        final_parties = []
        for party in argument.split("+"):
            final_parties += switcher.get(party, "nothing")
        return final_parties
    else:
        return switcher.get(argument, "nothing")

def plot_evaluations(party=None):
    '''Plot all available results
    '''
    redis_client = RedisClient()

    user_list = []
    if party is None:
        user_list = redis_client.get_usernames()
    else:
        user_list = string_to_list(party)

    print(user_list)
    results = {}
    for user in user_list:
        result = redis_client.get_popularity_history(user)
        results.update(result)
    #pretty_print(results)
    print_popularity(results, party)

def pretty_print(data):
    """Pretty print interface.
    """
    import pprint
    pretty_printer = pprint.PrettyPrinter(indent=4)
    pretty_printer.pprint(data)

def main():
    """Main procedure.
    """

    candidates1 = PRI + INDEPENDENT
    candidates2 = MORENA + PAN + PRD

    # Uncomment following fors (Execute first for and wait 15 minutes, then execute second for)
    '''
    for candidate in candidates1:
        for i in range(5, 16):
            my_date = dt.date(2017, 11, i)
            do_evaluation(candidate, my_date.strftime("%Y-%m-%d"))
    '''
    '''
    for candidate in candidates2:
        for i in range(5, 16):
            my_date = dt.date(2017, 11, i)
            do_evaluation(candidate, my_date.strftime("%Y-%m-%d"))S
    '''
    while True:
        # Write PAN, PRD, PRI, MORENA, INDEPENDENT or leave empty for all available
        party = input(
            "Partido (PAN, PRD, PRI, MORENA, INDEPENDENT," +\
            " exit, para todos sólo enter, para varios concatenar con '+'): \n")
        if party == "exit" or party == "Exit":
            break
        plot_evaluations(party)

if __name__ == '__main__':
    main()
    #REDIS_CLIENT = RedisClient()

    #RESULT = REDIS_CLIENT.get_popularity_history("pkumamoto")

    #print(REDIS_CLIENT.get_usernames())
