from twitter import *
import pprint
pp = pprint.PrettyPrinter(indent=4)

np.set_printoptions(threshold=sys.maxsize)

def getTweets(AT,AT_S,CON,CON_S, mentioned="@lopezobrador_"):
    
    t = Twitter(auth=OAuth(AT,AT_S,CON,CON_S))

    print("Busqueda sobre EPN")
    tweets = t.search.tweets(q="@EPN")
    for tweet in tweets['statuses']:
        if not(tweet['text'][0] == 'R' and tweet['text'][1] == 'T'):
            print(tweet['text'])

    print()
    print("Tweets de EPN")
    tweets2 = t.statuses.user_timeline(screen_name="EPN")
    for tweet in tweets2:
        if not(tweet['text'][0] == 'R' and tweet['text'][1] == 'T'):
            print(tweet['text'])
    
    #pp.pprint(tweets2)
    

AT = "880668541-hAfZ3IqqTgc1aJNjJzEojfjX0tD9rHF9Q6zNQ3BZ"
AT_S = "tl98z1tdnCPRWx8YY4HkZVxbbEoaXfJv4XTmNazFvBb8y"
CON = "kgFzF4dC6jJC1bynLhOSvWFrV"
CON_S = "gKX4yAWrSamlGrh9iatOjcfUsrenjqyl4QnfmvvDQMocds0XHv" 

print(getLastEPNTweet(AT,AT_S,CON,CON_S))


