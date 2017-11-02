from twitter import *

def getLastEPNTweet(AT,AT_S,CON,CON_S):
    
    t = Twitter(auth=OAuth(AT,AT_S,CON,CON_S))

    tweets = list(t.statuses.user_timeline(screen_name="EPN",count=1))

    #for tweet in tweets:
        #print(tweet['text'])
    return tweets[0]['text'] + " - EPN" 

AT = "880668541-hAfZ3IqqTgc1aJNjJzEojfjX0tD9rHF9Q6zNQ3BZ"
AT_S = "tl98z1tdnCPRWx8YY4HkZVxbbEoaXfJv4XTmNazFvBb8y"
CON = "kgFzF4dC6jJC1bynLhOSvWFrV"
CON_S = "gKX4yAWrSamlGrh9iatOjcfUsrenjqyl4QnfmvvDQMocds0XHv" 

print(getLastEPNTweet(AT,AT_S,CON,CON_S))
