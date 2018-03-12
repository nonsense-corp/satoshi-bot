import markovify
import tweepy

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    # Get raw text as string.
    with open("input.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    # Setup twitter fallbacks
    cfg = { 
        "consumer_key"        : "???",
        "consumer_secret"     : "???",
        "access_token"        : "???",
        "access_token_secret" : "???" 
    }

    api = get_api(cfg)

    # Generate a setence and find out by the user if they want to tweet it.
    tweet = text_model.make_short_sentence(140)
    print(tweet)
    print('Would you like to tweet this?')
    postTweet = input()
    if postTweet.lower() in ['y', 'yes', 'true']:
        #TODO: Do tweet here
        status = api.update_status(status=tweet) 

main()