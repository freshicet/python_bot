import tweepy
from decouple import config

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config('consumer_key'), 
    config('consumer_secret'))
auth.set_access_token(config('key'), 
    config('secret'))

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")