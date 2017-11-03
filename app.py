if __name__=='__main__':
    
    import os
    from TwitterClient import TwitterClient
    AT = os.environ.get('AT', None)
    AT_S = os.environ.get('AT_S', None)
    CON = os.environ.get('CON', None)
    CON_S = os.environ.get('CON_S', None)
    
    client = TwitterClient(AT=AT, AT_S=AT_S, CON=CON, CON_S=CON_S)
    print(client.t)
