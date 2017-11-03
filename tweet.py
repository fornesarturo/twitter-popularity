from twitter import *
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

def getTweets(AT,AT_S,CON,CON_S, mentioned="@lopezobrador_"):
    
    t = Twitter(auth=OAuth(AT,AT_S,CON,CON_S))

    tweets = t.search.tweets(q=mentioned)

    tweet = tweets['statuses'][4]
    #for tweet in tweets['statuses']:
    text = tweet['text']
    print(str(text))
    print(len(text))
    for word in text.split():
        print(word)

AT = "880668541-hAfZ3IqqTgc1aJNjJzEojfjX0tD9rHF9Q6zNQ3BZ"
AT_S = "tl98z1tdnCPRWx8YY4HkZVxbbEoaXfJv4XTmNazFvBb8y"
CON = "kgFzF4dC6jJC1bynLhOSvWFrV"
CON_S = "gKX4yAWrSamlGrh9iatOjcfUsrenjqyl4QnfmvvDQMocds0XHv" 

getTweets(AT,AT_S,CON,CON_S, mentioned="@lopezobrador_")
